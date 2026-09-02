[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host

Set-Location -Path "C:\IOTEC"

# Injeção de Variáveis na Memória
[System.Environment]::SetEnvironmentVariable("EVOLUTION_API_URL", "https://iotec-global-core.onrender.com", "Process")
[System.Environment]::SetEnvironmentVariable("EVOLUTION_API_KEY", "SUA_CHAVE_DEFINIDA", "Process")

Write-Host "`n[1/2] Disparando Motores da Sonda e da Central de Operações..." -ForegroundColor Cyan

$ScriptsCore = @(
    "001_IOTEC_KERNEL.py",
    "000_IOTEC_GOVERNANCA_FINAL.py",
    "000_IOTEC_BRAIN_ENGINE.py",
    "000_IOTEC_ROVER_SENSOR.py",
    "071_IOTEC_WEBHOOK.py",
    "052_WHATSAPP_EVOLUTION_ENGINE.py",
    "000_WEB_CENTRAL_OPERACOES.py"
)

foreach ($Script in $ScriptsCore) {
    if (Test-Path ".\$Script") {
        Start-Process python -ArgumentList $Script -WindowStyle Hidden
        Write-Host " -> Engine '$Script' operacional." -ForegroundColor Green
    }
}

Write-Host "`n[2/2] Sonda Operacional em Modo 24/7 (Zero Simulação)" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Green
Write-Host "  Painel de Telemetria Web: http://localhost:8080" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Green

while ($true) {
    $Hora = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    [System.GC]::Collect()
    $ProcessosPython = Get-Process python -ErrorAction SilentlyContinue
    $Total = ($ProcessosPython | Measure-Object).Count
    
    Write-Host "[$Hora] [SONDA ROVER ONLINE] $Total motores ativos captando dados..." -ForegroundColor DarkGray
    Start-Sleep -Seconds 30
}
