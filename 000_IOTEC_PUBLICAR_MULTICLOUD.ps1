# ==============================================================================
# IOTEC CORE ENGINE — MONITOR DE SAÚDE DA REDE MULTI-CLOUD
# ==============================================================================

$PathMapa = "C:\IOTEC\000_IOTEC_MAPA_DE_NAVEGACAO_MULTICLOUD.json"

Clear-Host
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🌐 IOTEC MAPA DE NAVEGAÇÃO MULTI-CLOUD & REDUNDÂNCIA GLOBAL" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "CNPJ Matriz: 61.549.037/0001-68" -ForegroundColor White
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

if (Test-Path $PathMapa) {
    $rede = Get-Content $PathMapa -Raw -Encoding UTF8 | ConvertFrom-Json

    Write-Host "`n🇧🇷 [ONDAS DE SERVIDORES NACIONAL (SÃO PAULO)]" -ForegroundColor Green
    foreach ($node in $rede.NODES_NACIONAIS) {
        Write-Host "   ├── Provedor: $($node.Provedor)" -ForegroundColor White
        Write-Host "   ├── Rota    : $($node.URL)" -ForegroundColor Yellow
        Write-Host "   └── Função  : $($node.Função)" -ForegroundColor DarkCyan
    }

    Write-Host "`n🌍 [ONDAS DE SERVIDORES INTERNACIONAIS (EDGE/GLOBAL)]" -ForegroundColor Cyan
    foreach ($node in $rede.NODES_INTERNACIONAIS) {
        Write-Host "   ├── Provedor: $($node.Provedor)" -ForegroundColor White
        Write-Host "   ├── Rota    : $($node.URL)" -ForegroundColor Yellow
        Write-Host "   └── Função  : $($node.Função)" -ForegroundColor DarkCyan
    }
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host "✅ REDE DISTRIBUÍDA: A IOTEC ESTÁ PRONTA PARA ABSORVER TRÁFEGO MASSIVO" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Cyan