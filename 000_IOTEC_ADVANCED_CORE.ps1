# ==============================================================================
# IOTEC ENTERPRISE - NÚCLEO AUTÔNOMO DE OPERAÇÃO E MONETIZAÇÃO AVANÇADA
# CNPJ: 61.549.037/0001-68
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host

Write-Host "==================================================================" -ForegroundColor Green
Write-Host "     IOTEC SYSTEM CORE - AUTONOMOUS MONETIZATION & CONTROL ENGINE  " -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Green

Set-Location -Path "C:\IOTEC"

# 1. DIAGNÓSTICO DOS BANCOS
Write-Host "`n[1/5] Auditando bases de dados SQLite..." -ForegroundColor Cyan
$Databases = @("iotec.db", "iotec_financial.db", "iotec_kernel.db", "data_store.db")
foreach ($Db in $Databases) {
    if (Test-Path ".\$Db") {
        $Size = (Get-Item ".\$Db").Length / 1KB
        Write-Host " -> [OK] Base '$Db' ativa - Tamanho: $([math]::Round($Size, 2)) KB" -ForegroundColor Green
    }
}

# 2. CARREGAMENTO DE CHAVES EM MEMÓRIA
Write-Host "`n[2/5] Mapeando cofre de credenciais..." -ForegroundColor Cyan
$RequiredKeys = @("ASAAS_API_KEY", "RENDER_API_KEY", "NETLIFY_AUTH_TOKEN", "PAYPAL_CLIENT_ID", "PICPAY_TOKEN")
$KeysLoaded = 0
foreach ($Key in $RequiredKeys) {
    $Val = [System.Environment]::GetEnvironmentVariable($Key)
    if (-not [string]::IsNullOrEmpty($Val)) { $KeysLoaded++ }
}
Write-Host " -> Status: $KeysLoaded de $($RequiredKeys.Count) chaves ativas na memoria." -ForegroundColor Green

# 3. START DOS MOTORES PYTHON
Write-Host "`n[3/5] Disparando motores do Kernel e Central de Vendas..." -ForegroundColor Cyan
$CorePythonScripts = @("001_IOTEC_KERNEL.py", "000_IOTEC_GOVERNANCA_FINAL.py", "000_IOTEC_BRAIN_ENGINE.py", "071_IOTEC_WEBHOOK.py", "000_WEB_CENTRAL_OPERACOES.py")
foreach ($Script in $CorePythonScripts) {
    if (Test-Path ".\$Script") {
        Start-Process python -ArgumentList $Script -WindowStyle Hidden
        Write-Host " -> Engine '$Script' rodando em segundo plano." -ForegroundColor Green
    }
}

# 4. MONITORAMENTO E LOOP 24/7
Write-Host "`n[4/5] Entrada em modo autônomo contínuo. O Núcleo está ativo." -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Green
Write-Host "  Painel Web: http://localhost:8080 | CNPJ: 61.549.037/0001-68" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Green

while ($true) {
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    [System.GC]::Collect()
    $PyProcesses = Get-Process python -ErrorAction SilentlyContinue
    $Count = ($PyProcesses | Measure-Object).Count
    Write-Host "[$Timestamp] [NÚCLEO ATIVO] $Count motores Python operando | Memoria otimizada." -ForegroundColor DarkGray
    Start-Sleep -Seconds 45
}
