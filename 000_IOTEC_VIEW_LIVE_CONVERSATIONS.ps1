[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Set-Location -Path "C:\IOTEC"

while ($true) {
    Clear-Host
    Write-Host "==================================================================" -ForegroundColor Green
    Write-Host "  SALAS DE BATE-PAPO DA IOTEC EM TEMPO REAL (CTRL+C para sair)" -ForegroundColor Green
    Write-Host "==================================================================" -ForegroundColor Green
    
    if (Test-Path ".\data_store.db") {
        $Query = "SELECT timestamp, direcao, numero, mensagem FROM live_chat_logs ORDER BY id DESC LIMIT 15;"
        $Logs = python -c "import sqlite3; conn = sqlite3.connect('data_store.db'); c = conn.cursor(); [print(f'[{r[0]}] {r[1]} ({r[2]}): {r[3]}') for r in c.execute('$Query').fetchall()]; conn.close()"
        
        if ($Logs) {
            Write-Host $Logs -ForegroundColor Cyan
        } else {
            Write-Host "Aguardando primeiras interacoes dos agentes com os clientes..." -ForegroundColor DarkGray
        }
    } else {
        Write-Host "Aguardando criacao do banco data_store.db..." -ForegroundColor Yellow
    }

    Start-Sleep -Seconds 2
}
