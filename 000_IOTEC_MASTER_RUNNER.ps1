# ==============================================================================
# IOTEC ENTERPRISE - ORQUESTRADOR DE INICIALIZAÇÃO TOTAL
# CNPJ: 61.549.037/0001-68
# ==============================================================================

Write-Host "[IOTEC] Iniciando orquestracao total do ecossistema..." -ForegroundColor Green

Set-Location -Path "C:\IOTEC"

# 1. Nucleo e Governanca Central
Write-Host "[1/5] Subindo Kernel, Governanca e Central de Operacoes..." -ForegroundColor Cyan
Start-Process python -ArgumentList "001_IOTEC_KERNEL.py" -WindowStyle Hidden
Start-Process python -ArgumentList "000_IOTEC_GOVERNANCA_FINAL.py" -WindowStyle Hidden
Start-Process python -ArgumentList "000_WEB_CENTRAL_OPERACOES.py" -WindowStyle Hidden

# 2. Watch Tower e Nucleo Adaptativo
Write-Host "[2/5] Ativando Watch Tower e Nucleo Adaptativo de RAM..." -ForegroundColor Cyan
Start-Process python -ArgumentList "001_IOTEC_WATCH_TOWER.py" -WindowStyle Hidden
Start-Process python -ArgumentList "000_IOTEC_NUCLEO_ADAPTATIVO.py" -WindowStyle Hidden

# 3. Motores Financeiros e Gateways (Asaas / Webhooks)
Write-Host "[3/5] Conectando Gateways Financeiros e Webhooks..." -ForegroundColor Cyan
Start-Process python -ArgumentList "015_PAYMENT_GATEWAY_ENGINE.py" -WindowStyle Hidden
Start-Process python -ArgumentList "071_IOTEC_WEBHOOK.py" -WindowStyle Hidden
Start-Process python -ArgumentList "000_IOTEC_TELEMETRIA_ROTATIVIDADE.py" -WindowStyle Hidden

# 4. Automacao de Vendas e Prospeccao
Write-Host "[4/5] Ligando Motores de Prospeccao e Disparos..." -ForegroundColor Cyan
Start-Process python -ArgumentList "000_IOTEC_MAPA_OPERACAO_247.py" -WindowStyle Hidden
if (Test-Path ".\000_IOTEC_AUTO_PROSPECTOR.ps1") { Start-Process powershell -ArgumentList "-File .\000_IOTEC_AUTO_PROSPECTOR.ps1" -WindowStyle Hidden }
if (Test-Path ".\000_IOTEC_MONITOR_VENDAS_REAIS.ps1") { Start-Process powershell -ArgumentList "-File .\000_IOTEC_MONITOR_VENDAS_REAIS.ps1" -WindowStyle Hidden }

# 5. Gateways de Comunicacao
Write-Host "[5/5] Subindo Servicos de E-mail e WhatsApp..." -ForegroundColor Cyan
Start-Process python -ArgumentList "018_EMAIL_ENGINE.py" -WindowStyle Hidden
Start-Process python -ArgumentList "052_WHATSAPP_BUSINESS_MANAGER.py" -WindowStyle Hidden

Write-Host "==================================================================" -ForegroundColor Green
Write-Host "[IOTEC] Todos os modulos foram inicializados em segundo plano!" -ForegroundColor Green
Write-Host "[IOTEC] Painel Web ativo em: http://localhost:8080" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Green
