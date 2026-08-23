# ==============================================================================
# IOTEC EXECUTIVE PRESENTATION ENGINE
# APRESENTAÇÃO EXECUTIVA PARA INSTITUIÇÕES FINANCEIRAS
# ==============================================================================

Clear-Host

$CorTitulo="Cyan"
$CorTexto="White"
$CorDestaque="Green"

function Titulo($Texto){
    Write-Host ""
    Write-Host "==============================================================" -ForegroundColor DarkCyan
    Write-Host $Texto -ForegroundColor $CorTitulo
    Write-Host "==============================================================" -ForegroundColor DarkCyan
    Write-Host ""
}

function Espera{
    Write-Host ""
    Read-Host "Pressione ENTER para continuar"
}

Titulo "BEM-VINDO À IOTEC"

Write-Host "Prezado(a) Gerente." -ForegroundColor $CorTexto
Write-Host ""
Write-Host "Agradecemos sua visita." -ForegroundColor $CorTexto
Write-Host ""
Write-Host "Esta apresentação foi preparada para permitir uma avaliação" -ForegroundColor $CorTexto
Write-Host "institucional, tecnológica e econômica da IOTEC." -ForegroundColor $CorTexto

Espera

Titulo "QUEM SOMOS"

Write-Host "A IOTEC desenvolve tecnologia proprietária." -ForegroundColor $CorTexto
Write-Host ""
Write-Host "Nossa atuação envolve:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  • Engenharia de Software"
Write-Host "  • Inteligência Artificial"
Write-Host "  • Arquitetura de Sistemas"
Write-Host "  • Plataformas Digitais"
Write-Host "  • Pesquisa e Desenvolvimento"
Write-Host "  • Ativos Intelectuais"

Espera

Titulo "PATRIMÔNIO TECNOLÓGICO"

Write-Host "Os principais ativos incluem:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  • Arquitetura Proprietária"
Write-Host "  • Frameworks"
Write-Host "  • Algoritmos"
Write-Host "  • Documentação Técnica"
Write-Host "  • Modelos de Negócio"
Write-Host "  • Sistemas Especializados"
Write-Host "  • Plataformas"

Espera

Titulo "MODELO DE NEGÓCIO"

Write-Host "A empresa foi estruturada para transformar tecnologia" -ForegroundColor White
Write-Host "em produtos e serviços capazes de gerar receitas." -ForegroundColor White

Write-Host ""
Write-Host "Fluxo simplificado:" -ForegroundColor Yellow
Write-Host ""
Write-Host "Cliente" -ForegroundColor Cyan
Write-Host "   |"
Write-Host "Portal" -ForegroundColor Cyan
Write-Host "   |"
Write-Host "Processamento (Esteira B2B)" -ForegroundColor Cyan
Write-Host "   |"
Write-Host "Entrega" -ForegroundColor Cyan
Write-Host "   |"
Write-Host "Receita" -ForegroundColor Green

Espera

Titulo "OBJETIVO DESTA APRESENTAÇÃO"

Write-Host "Esta apresentação NÃO solicita aprovação automática." -ForegroundColor Yellow
Write-Host ""
Write-Host "Seu objetivo é disponibilizar informações para análise" -ForegroundColor White
Write-Host "da instituição financeira, respeitando seus critérios" -ForegroundColor White
Write-Host "de crédito, risco e conformidade." -ForegroundColor White

Espera

Titulo "ENCERRAMENTO"

Write-Host "A IOTEC agradece a oportunidade." -ForegroundColor Green
Write-Host ""
Write-Host "Toda documentação complementar poderá ser apresentada" -ForegroundColor White
Write-Host "durante o processo de análise, quando solicitada." -ForegroundColor White

Write-Host ""
Write-Host "Fim da apresentação." -ForegroundColor Green