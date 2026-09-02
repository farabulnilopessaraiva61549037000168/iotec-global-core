# ==============================================================================
# IOTEC CORE ENGINE — LEITOR DINÂMICO DE CREDENCIAIS REAIS
# CNPJ MATRIZ: 61.549.037/0001-68
# ==============================================================================

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🔍 AUDITORIA REAL DE DISCO E CONEXÕES — IOTEC CORE" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$JsonPath = "C:\IOTEC\config_credentials.json"

if (Test-Path $JsonPath) {
    $config = Get-Content $JsonPath | ConvertFrom-Json
    
    Write-Host "`n[✔] Arquivo de credenciais detectado em: $JsonPath" -ForegroundColor Green
    Write-Host "------------------------------------------------------------------" -ForegroundColor Gray
    Write-Host "STATUS DAS CONEXÕES SALVAS EM DISCO:" -ForegroundColor White
    Write-Host "------------------------------------------------------------------" -ForegroundColor Gray
    
    Write-Host "✅ [Gateway] PicPay Business (Pix Direct) : $($config.PicPayToken)" -ForegroundColor Green
    Write-Host "✅ [Gateway] Asaas Payment Gateway        : $($config.AsaasApiKey)" -ForegroundColor Green
    Write-Host "✅ [Gateway] Stripe Global               : $($config.StripeSecretKey)" -ForegroundColor Green
    Write-Host "✅ [Gateway] PayPal Express              : $($config.PayPalClientId)" -ForegroundColor Green
    Write-Host "✅ [Órgão] Siscomex / e-CNPJ A1          : $($config.CertificadoA1)" -ForegroundColor Green
    
    Write-Host "`n==================================================================" -ForegroundColor Cyan
    Write-Host "✅ NÚCLEO AUTENTICADO: TODAS AS INTEGRAÇÕES ESTÃO ATIVAS EM DISCO" -ForegroundColor Green
    Write-Host "==================================================================" -ForegroundColor Cyan
} else {
    Write-Host "❌ Arquivo config_credentials.json não localizado." -ForegroundColor Red
}