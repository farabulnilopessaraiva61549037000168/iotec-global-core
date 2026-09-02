# ==============================================================================
# IOTEC CORE ENGINE — RADAR MULTI-CLOUD (NETLIFY, RENDER, GITHUB)
# CNPJ MATRIZ: 61.549.037/0001-68 | FOCO: CAPTAÇÃO & VENDAS URGENTES
# ==============================================================================

$PathCaixa = "C:\IOTEC\caixa_real.json"

Clear-Host
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🚨 IOTEC RADAR MULTI-CLOUD — MONITORAMENTO DE VENDAS EM TEMPO REAL" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🌐 FRONT-END : Netlify (https://deft-choux-097d84.netlify.app/)" -ForegroundColor White
Write-Host "⚙️ BACK-END  : Render / Flask Server (Porta 5000 / Webhook)" -ForegroundColor White
Write-Host "💻 CODE & API: GitHub Repository & Developer Hub" -ForegroundColor White
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

$lastTransactionCount = 0
$lastSaldo = 0.0

if (Test-Path $PathCaixa) {
    $inicial = Get-Content $PathCaixa -Raw -Encoding UTF8 | ConvertFrom-Json
    $lastTransactionCount = $inicial.transacoes.Count
    $lastSaldo = [double]$inicial.saldo_real
}

Write-Host "💰 CAIXA CONSOLIDADO: R$ $($lastSaldo.ToString('N2'))" -ForegroundColor Green
Write-Host "------------------------------------------------------------------`n" -ForegroundColor Gray

while ($true) {
    if (Test-Path $PathCaixa) {
        $dados = Get-Content $PathCaixa -Raw -Encoding UTF8 | ConvertFrom-Json
        $currentCount = $dados.transacoes.Count
        $currentSaldo = [double]$dados.saldo_real

        if ($currentCount -gt $lastTransactionCount) {
            $venda = $dados.transacoes[-1]

            # Bip de Confirmação de Caixa Real
            [Console]::Beep(1200, 250)
            [Console]::Beep(1800, 350)

            Write-Host "`n💰 [NOVA VENDA DETECTADA NAS INFRAESTRUTURAS!]" -ForegroundColor Yellow -BackgroundColor DarkRed
            Write-Host "=================================================" -ForegroundColor Yellow
            Write-Host "📦 Certidão / Documento : $($venda.produto)" -ForegroundColor White
            Write-Host "💵 Valor Convertido     : R$ ($([double]$venda.valor).ToString('N2'))" -ForegroundColor Green
            Write-Host "💳 Gateway de Origem    : $($venda.gateway)" -ForegroundColor Cyan
            Write-Host "🌐 Servidor de Captura  : Netlify / Render API" -ForegroundColor White
            Write-Host "🕒 Data/Hora            : $($venda.data)" -ForegroundColor White
            Write-Host "📈 Saldo Total IOTEC    : R$ $($currentSaldo.ToString('N2'))" -ForegroundColor Green
            Write-Host "=================================================`n" -ForegroundColor Yellow

            $lastTransactionCount = $currentCount
            $lastSaldo = $currentSaldo
        }
        else {
            $agora = (Get-Date).ToString("HH:mm:ss")
            Write-Host "📡 [$agora] RADAR ATIVO: Escutando Netlify (Front) + Render (APIs) + GitHub (Devs)..." -ForegroundColor DarkGray
        }
    }
    Start-Sleep -Seconds 4
}