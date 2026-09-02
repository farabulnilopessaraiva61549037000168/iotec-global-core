# =========================================================================================
#           USINA IOTEC — MASTER DISPATCH & RELATIONAL ENGINE (24/7)
# =========================================================================================

$dbPath = "C:\IOTEC\iotec_kernel.db"

Write-Host "`n=========================================================================================" -ForegroundColor Cyan
Write-Host "     USINA IOTEC — ACTIVATING CENTRAL DISPATCH & EXECUTIVE RELATIONSHIP ENGINE     " -ForegroundColor Cyan
Write-Host "=========================================================================================`n" -ForegroundColor Cyan

# 1. Auditoria e Resgate de Chamadas / Leads em Espera
$auditQuery = @"
import sqlite3
conn = sqlite3.connect(r'$dbPath')
c = conn.cursor()
c.execute("SELECT id, empresa, pais_codigo, telefone, score_match, status FROM iotec_corporate_leads ORDER BY score_match DESC")
leads = c.fetchall()
conn.close()
for l in leads:
    print(f"{l[0]}|{l[1]}|{l[2]}|{l[3]}|{l[4]}|{l[5]}")
"@

$leadsData = python -c $auditQuery

Write-Host "[AUDITORIA] Mapeando fila de espera e leads qualificados no iotec_kernel.db..." -ForegroundColor Yellow
Write-Host "-----------------------------------------------------------------------------------------" -ForegroundColor Gray

foreach ($line in $leadsData) {
    if (-not $line) { continue }
    $parts = $line.Split('|')
    $lId = $parts[0]
    $empresa = $parts[1]
    $pais = $parts[2]
    $telefone = $parts[3]
    $score = $parts[4]
    $status = $parts[5]

    $tzMap = @{
        "BR" = "SA Eastern Standard Time"
        "US" = "Eastern Standard Time"
        "DE" = "W. Europe Standard Time"
        "AE" = "Arabian Standard Time"
        "JP" = "Tokyo Standard Time"
        "AU" = "AUS Eastern Standard Time"
    }

    $tzId = $tzMap[$pais]
    if (-not $tzId) { $tzId = "Eastern Standard Time" }

    $tz = [TimeZoneInfo]::FindSystemTimeZoneById($tzId)
    $horaLocal = [TimeZoneInfo]::ConvertTimeFromUtc([DateTime]::UtcNow, $tz)
    $horaInt = $horaLocal.Hour
    $horaStr = $horaLocal.ToString("HH:mm:ss")

    if ($status -eq "CONTATADO") {
        Write-Host "[$horaStr] [JA LANÇADO / EM ACOMPANHAMENTO] $empresa ($pais) -> Status: CONTATADO" -ForegroundColor DarkGray
    }
    elseif ($horaInt -ge 9 -and $horaInt -lt 17) {
        Write-Host "[$horaStr] [JANELA ABERTA] $empresa ($pais) | Match Score: $score% -> Acionando WhatsApp..." -ForegroundColor Green
        
        python C:\IOTEC\029_IOTEC_MULTILANG_DISPATCH.py $telefone

        $updateQuery = "import sqlite3; conn = sqlite3.connect(r'$dbPath'); c = conn.cursor(); c.execute('UPDATE iotec_corporate_leads SET status = ''CONTATADO'', data_atualizacao = datetime(''now'') WHERE id = $lId'); conn.commit(); conn.close()"
        python -c $updateQuery

        Write-Host "[OK] Aproximação executiva registrada com sucesso para $empresa!`n" -ForegroundColor Cyan
    }
    else {
        Write-Host "[$horaStr] [EM ESPERA / FUSO FECHADO] $empresa ($pais) -> Fuso atual fora do expediente comercial local." -ForegroundColor Yellow
    }
}

Write-Host "=========================================================================================" -ForegroundColor Cyan
Write-Host " [USINA IOTEC] Central de Aproximação em Execução Real. Monitorando Vendas 24/7." -ForegroundColor Cyan
Write-Host "=========================================================================================`n" -ForegroundColor Cyan
