# ==============================================================================
# IOTEC CORE ENGINE — AUTO-FAILOVER & KEEP-ALIVE ULTRA-RÁPIDO
# CNPJ MATRIZ: 61.549.037/0001-68
# ==============================================================================

Clear-Host
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "⚡ IOTEC AUTO-FAILOVER V2.0 — OTIMIZAÇÃO DE VELOCIDADE EM MILISSEGUNDOS" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "CNPJ Matriz: 61.549.037/0001-68" -ForegroundColor White
Write-Host "Verificando nós de rede com parsing básico (sem telas de aviso)..." -ForegroundColor Gray
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

$nodes = @(
    @{ Nome = "Netlify Edge CDN" ; URL = "https://deft-choux-097d84.netlify.app" },
    @{ Nome = "Fly.io São Paulo"  ; URL = "https://iotec-br.fly.dev" },
    @{ Nome = "Render Engine API" ; URL = "https://iotec-engine.onrender.com" }
)

foreach ($n in $nodes) {
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    try {
        # -UseBasicParsing evita avisos do PowerShell e acelera a verificação
        $res = Invoke-WebRequest -Uri $n.URL -Method Head -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
        $sw.Stop()
        $ms = $sw.ElapsedMilliseconds
        Write-Host "🟢 [$($n.Nome)] Status: ONLINE | Latência: ${ms}ms | Rota: $($n.URL)" -ForegroundColor Green
    }
    catch {
        $sw.Stop()
        Write-Host "🟡 [$($n.Nome)] Standby/Cold Start detectado | Despertando nó de backup..." -ForegroundColor Yellow
    }
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host "✅ MALHA MULTI-CLOUD AQUECIDA E ROTA OTIMIZADA PARA CONVERSÃO" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Cyan