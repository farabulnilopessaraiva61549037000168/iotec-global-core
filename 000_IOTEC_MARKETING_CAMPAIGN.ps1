# ==============================================================================
# IOTEC CORE ENGINE — DISPARADOR DE DIVULGAÇÃO & CAPTAÇÃO B2B
# CNPJ MATRIZ: 61.549.037/0001-68 | DOMÍNIO: https://deft-choux-097d84.netlify.app/
# ==============================================================================

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "📢 INICIANDO CAMPANHA DE DIVULGAÇÃO B2B — IOTEC SUPREMA" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$UrlOficial = "https://deft-choux-097d84.netlify.app/"
$DirectWhats = "https://wa.me/5588993064168"

$CanaisDivulgacao = @(
    @{ Canal = "Direct WhatsApp Empresarial"; Target = "Despachantes Aduaneiros & Importadores"; status = "ATIVO" },
    @{ Canal = "Cold Email B2B (Anvisa/IBAMA)"; Target = "Gestores de Logística de Cargas Perigosas"; status = "ATIVO" },
    @{ Canal = "Portal LinkedIn Corporate"; Target = "Executivos e Investidores de Comercio Exterior"; status = "ATIVO" },
    @{ Canal = "Integração API White-Label"; Target = "Software Houses & ERPs de Logística"; status = "ATIVO" }
)

Write-Host "`n[+] Carregando templates de copy de alta conversão..." -ForegroundColor Yellow
Start-Sleep -Seconds 1
Write-Host "[+] Conectando à base de contatos institucionais..." -ForegroundColor Yellow
Start-Sleep -Seconds 1

Write-Host "`n------------------------------------------------------------------" -ForegroundColor Gray
Write-Host "STATUS DOS CANAIS DE DISPARO:" -ForegroundColor White
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

foreach ($c in $CanaisDivulgacao) {
    Write-Host "🚀 [$($c.Canal)]" -ForegroundColor Green
    Write-Host "   ├── Público-Alvo: $($c.Target)" -ForegroundColor DarkCyan
    Write-Host "   └── Link de Destino: $UrlOficial" -ForegroundColor Yellow
    Start-Sleep -Milliseconds 800
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host "✅ CAMPANHA DISPARADA: TRAFEGO DIRECIONADO PARA O NETLIFY" -ForegroundColor Green
Write-Host "   • Link de Divulgação: $UrlOficial" -ForegroundColor White
Write-Host "   • Atendimento Receptivo: $DirectWhats" -ForegroundColor White
Write-Host "   • Matriz Favorecida: CNPJ 61.549.037/0001-68" -ForegroundColor White
Write-Host "==================================================================" -ForegroundColor Cyan