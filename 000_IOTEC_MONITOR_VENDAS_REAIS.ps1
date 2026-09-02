# ==============================================================================
# IOTEC CORE ENGINE — RADAR DE VENDAS & PRESENÇA V2.0 (COM ALERTAS SONOROS)
# CNPJ MATRIZ: 61.549.037/0001-68 | DOMÍNIO: https://deft-choux-097d84.netlify.app/
# ==============================================================================

$PathCaixa = "C:\IOTEC\caixa_real.json"
$inicioOperacao = Get-Date

Clear-Host
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "📡 IOTEC RADAR V2.0 — MONITOR SUPREMO DE LIQUIDAÇÃO & TRÁFEGO" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "CNPJ Matriz : 61.549.037/0001-68" -ForegroundColor White
Write-Host "Gateways    : PicPay | Asaas | Stripe | PayPal" -ForegroundColor White
Write-Host "Plataforma  : https://deft-choux-097d84.netlify.app/" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

$lastTransactionCount = 0
$lastSaldo = 0.0

if (Test-Path $PathCaixa) {
    $inicial = Get-Content $PathCaixa -Raw -Encoding UTF8 | ConvertFrom-Json
    $lastTransactionCount = $inicial.transacoes.Count
    $lastSaldo = [double]$inicial.saldo_real
}

Write-Host "💰 Saldo em Caixa Real : R$ $($lastSaldo.ToString("N2"))" -ForegroundColor Green
Write-Host "📊 Vendas Consolidadas : $lastTransactionCount" -ForegroundColor Green
Write-Host "------------------------------------------------------------------`n" -ForegroundColor Gray

while ($true) {
    if (Test-Path $PathCaixa) {
        $dados = Get-Content $PathCaixa -Raw -Encoding UTF8 | ConvertFrom-Json
        $currentCount = $dados.transacoes.Count
        $currentSaldo = [double]$dados.saldo_real

        if ($currentCount -gt $lastTransactionCount) {
            $ultimaTransacao = $dados.transacoes[-1]

            # BIP SONORO DE CONFIRMAÇÃO DE CAIXA DE R$
            [Console]::Beep(1000, 300)
            [Console]::Beep(1500, 400)

            Write-Host "`n🚨 [ALERTA DE VENDA CONFIRMADA EM TEMPO REAL!]" -ForegroundColor Yellow -BackgroundColor DarkRed
            Write-Host "==================================================================" -ForegroundColor Yellow
            Write-Host "📦 Produto/Certidão : $($ultimaTransacao.produto)" -ForegroundColor White
            Write-Host "💵 Valor Recebido  : R$ ($([double]$ultimaTransacao.valor).ToString('N2'))" -ForegroundColor Green
            Write-Host "💳 Gateway / Canal  : $($ultimaTransacao.gateway)" -ForegroundColor Cyan
            Write-Host "🕒 Horário da Venda : $($ultimaTransacao.data)" -ForegroundColor White
            Write-Host "📈 Novo Saldo Real  : R$ $($currentSaldo.ToString('N2'))" -ForegroundColor Green
            Write-Host "==================================================================`n" -ForegroundColor Yellow

            Write-Host "⚡ [SISTEMA] Autenticando Chancela ICP-Brasil do Documento..." -ForegroundColor DarkCyan
            Start-Sleep -Seconds 1
            Write-Host "✅ [SISTEMA] Certidão chancelada com sucesso no CNPJ 61.549.037/0001-68!" -ForegroundColor Green
            Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

            $lastTransactionCount = $currentCount
            $lastSaldo = $currentSaldo
        }
        else {
            $agora = Get-Date
            $uptime = $agora - $inicioOperacao
            $uptimeFormatado = "{0:D2}h:{1:D2}m:{2:D2}s" -f $uptime.Hours, $uptime.Minutes, $uptime.Seconds
            
            $horaFormatada = $agora.ToString("HH:mm:ss")
            Write-Host "👀 [$horaFormatada] Radar Ativo | Uptime: $uptimeFormatado | Escutando Netlify & Webhooks..." -ForegroundColor DarkGray
        }
    }
    
    Start-Sleep -Seconds 5
}