# ==============================================================================
#            IOTEC ECOSYSTEM — GUARDIÃO UNIFICADO E SENTINELA AUTOMÁTICA
# ==============================================================================

$Global:IOTEC_PATH = "C:\IOTEC"
$Global:DB_PATH    = "C:\IOTEC\iotec.db"
$Global:WPP_PATH   = "C:\IOTEC\wppconnect-server"

function Write-GuardianLog {
    param ([string]$Origem, [string]$Mensagem, [string]$Tipo = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $cor = switch ($Tipo) {
        "SUCCESS" { "Green" }
        "WARN"    { "Yellow" }
        "ERROR"   { "Red" }
        default   { "Cyan" }
    }
    Write-Host "[$timestamp] [$Tipo] [$Origem] $Mensagem" -ForegroundColor $cor

    try {
        $conn = New-Object System.Data.SQLite.SQLiteConnection("Data Source=$Global:DB_PATH;Version=3;")
        $conn.Open()
        $cmd = $conn.CreateCommand()
        $cmd.CommandText = "CREATE TABLE IF NOT EXISTS guardian_events (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, origem TEXT, mensagem TEXT, tipo TEXT)"
        $cmd.ExecuteNonQuery() | Out-Null
        
        $cmd.CommandText = "INSERT INTO guardian_events (timestamp, origem, mensagem, tipo) VALUES (@ts, @ori, @msg, @tp)"
        $cmd.Parameters.AddWithValue("@ts", $timestamp) | Out-Null
        $cmd.Parameters.AddWithValue("@ori", $Origem) | Out-Null
        $cmd.Parameters.AddWithValue("@msg", $Mensagem) | Out-Null
        $cmd.Parameters.AddWithValue("@tp", $Tipo) | Out-Null
        $cmd.ExecuteNonQuery() | Out-Null
        $conn.Close()
    } catch {
        # Se o SQLite falhar, ignora para manter a sentinela operante
    }
}

function Repair-DiskSpace {
    Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Iniciando limpeza preventiva de cache e arquivos temporarios..." -Tipo "WARN"
    try {
        Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
        npm cache clean --force 2>&1 | Out-Null
        Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Espaco temporario liberado com sucesso." -Tipo "SUCCESS"
        return $true
    } catch {
        Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Falha na limpeza de disco: $_" -Tipo "ERROR"
        return $false
    }
}

function Repair-WppServer {
    Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Restaurando servico WPPConnect na porta 21465..." -Tipo "WARN"
    try {
        Get-Process -Name "node" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 2
        Start-Process -FilePath "node" -ArgumentList "index.js" -WorkingDirectory $Global:WPP_PATH -WindowStyle Hidden
        Start-Sleep -Seconds 5
        Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Servico WPPConnect reiniciado em segundo plano." -Tipo "SUCCESS"
        return $true
    } catch {
        Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Erro ao reiniciar WPPConnect: $_" -Tipo "ERROR"
        return $false
    }
}

function Invoke-IotecSafeExecution {
    param ([scriptblock]$ScriptBlock, [string]$Contexto = "ESTEIRA_B2B")
    
    try {
        & $ScriptBlock
    } catch {
        $erro = $_.Exception.Message
        Write-GuardianLog -Origem $Contexto -Mensagem "Excecao interceptada: $erro" -Tipo "ERROR"

        if ($erro -like "*ENOSPC*" -or $erro -like "*no space left*") {
            Repair-DiskSpace
        }
        elseif ($erro -like "*21465*" -or $erro -like "*ECONNREFUSED*" -or $erro -like "*503*") {
            Repair-WppServer
        }
        elseif ($erro -like "*locked*" -or $erro -like "*busy*") {
            Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Banco de dados bloqueado. Aplicando pausa tactica de 3s..." -Tipo "WARN"
            Start-Sleep -Seconds 3
        }
        else {
            Write-GuardianLog -Origem "SELF-HEALING" -Mensagem "Isolando falha nao mapeada para manter a esteira viva." -Tipo "WARN"
        }
    }
}

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "         IOTEC GUARDIAN SENTINEL — INTERCEPTACAO E AUTO-CURA ATIVAS          " -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

while ($true) {
    Invoke-IotecSafeExecution -Contexto "WATCHDOG_INFRA" -ScriptBlock {
        $disk = Get-PSDrive C
        $freeGB = [math]::round($disk.Free / 1GB, 2)
        if ($freeGB -lt 0.5) {
            $msgErro = "ENOSPC: Espaco critico em disco C: " + $freeGB + " GB restantes"
            throw $msgErro
        }

        $portCheck = Test-NetConnection -ComputerName "localhost" -Port 21465 -WarningAction SilentlyContinue
        if (-not $portCheck.TcpTestSucceeded) {
            throw "ECONNREFUSED: Porta 21465 do WhatsApp desconectada."
        }

        $statusMsg = "Sistema Operacional e Servicos OK (Disco C: " + $freeGB + " GB | WPPConnect: ONLINE)"
        Write-GuardianLog -Origem "SENTINELA" -Mensagem $statusMsg -Tipo "SUCCESS"
    }

    Start-Sleep -Seconds 30
}
