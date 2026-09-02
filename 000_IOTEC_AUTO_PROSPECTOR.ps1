# ==============================================================================
# IOTEC CORE ENGINE — MOTOR AUTÔNOMO DE DIVULGAÇÃO & MENSAGENS HUMANIZADAS
# CNPJ MATRIZ: 61.549.037/0001-68 | DOMÍNIO: https://deft-choux-097d84.netlify.app/
# ==============================================================================

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🤖 IOTEC AGENTE DE DIVULGAÇÃO CONTINUA & PROSPEÇÃO B2B" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$UrlOficial = "https://deft-choux-097d84.netlify.app/"
$DirectWhats = "https://wa.me/5588993064168"

$TemplatesHumanizados = @(
    @{
        Canal = "WhatsApp / Direct (Despachantes)";
        Copy = "Olá! Tudo bem? Vi que vocês atuam fortemente com desembaraço aduaneiro. Lançamos uma plataforma que emite certidões DTA, DUIMP e licenças Anvisa com chancela ICP-Brasil instantânea. Dá para testar direto no navegador: $UrlOficial — Se precisar de algo em lote, fico à disposição!"
    },
    @{
        Canal = "LinkedIn (Gestores de TI & ERPs)";
        Copy = "Boa tarde! Estamos disponibilizando a API REST da IOTEC para automação de certidões operacionais. Dá para embutir no ERP de vocês e gerar nova receita recorrente. Confere a estrutura: $UrlOficial"
    },
    @{
        Canal = "Cold Email (Importadoras & Logística)";
        Copy = "Prezados, simplificamos o processo de emissão e verificação de licenças IBAMA e Anvisa para transporte de cargas. Sistema 100% online com verificação por QR Code: $UrlOficial. Atendimento direto: $DirectWhats"
    }
)

$horaAtual = (Get-Date).ToString("HH:mm:ss")
Write-Host "`n[+] Hora Atual: $horaAtual | Motor de Prospecção Ativo em Segundo Plano" -ForegroundColor Green
Write-Host "------------------------------------------------------------------" -ForegroundColor Gray

foreach ($msg in $TemplatesHumanizados) {
    Write-Host "📌 [$($msg.Canal)]" -ForegroundColor Yellow
    Write-Host "   └── Mensagem Gerada:" -ForegroundColor White
    Write-Host "   '$($msg.Copy)'`n" -ForegroundColor DarkCyan
    Start-Sleep -Milliseconds 600
}

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "✅ AGENTE PRONTO PARA COPIAR E DISPARAR NAS JANELAS ESTRATÉGICAS" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Cyan