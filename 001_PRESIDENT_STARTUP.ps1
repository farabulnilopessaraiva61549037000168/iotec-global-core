# =====================================================================
# IOTEC PRESIDENT STARTUP
# Primeira Rotina da Presidência
# =====================================================================

Clear-Host

$ROOT="C:\IOTEC"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "               IOTEC PRESIDENT STARTUP"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

if(!(Test-Path $ROOT))
{
    Write-Host "Pasta C:\IOTEC não encontrada." -ForegroundColor Red
    exit
}

Set-Location $ROOT

Write-Host "Data............. $(Get-Date)"
Write-Host ""

# ===========================================================
# CONTAGEM
# ===========================================================

$python=Get-ChildItem $ROOT -Recurse -Filter *.py -ErrorAction SilentlyContinue

$ps=Get-ChildItem $ROOT -Recurse -Filter *.ps1 -ErrorAction SilentlyContinue

$db=Get-ChildItem $ROOT -Recurse -Filter *.db -ErrorAction SilentlyContinue

$json=Get-ChildItem $ROOT -Recurse -Filter *.json -ErrorAction SilentlyContinue

$html=Get-ChildItem $ROOT -Recurse -Filter *.html -ErrorAction SilentlyContinue

Write-Host "============================================================"
Write-Host "PATRIMÔNIO DIGITAL"
Write-Host "============================================================"
Write-Host ""

Write-Host ("Arquivos Python....... {0}" -f $python.Count)

Write-Host ("PowerShell............ {0}" -f $ps.Count)

Write-Host ("Banco de Dados........ {0}" -f $db.Count)

Write-Host ("JSON.................. {0}" -f $json.Count)

Write-Host ("HTML.................. {0}" -f $html.Count)

Write-Host ""

# ===========================================================
# TAMANHO
# ===========================================================

$total=(Get-ChildItem $ROOT -Recurse -File -ErrorAction SilentlyContinue |
Measure-Object Length -Sum).Sum

$gb=[Math]::Round($total/1GB,2)

Write-Host "Espaço utilizado...... $gb GB"

Write-Host ""

# ===========================================================
# MAIORES ARQUIVOS
# ===========================================================

Write-Host "============================================================"
Write-Host "10 MAIORES ARQUIVOS"
Write-Host "============================================================"
Write-Host ""

Get-ChildItem $ROOT -Recurse -File -ErrorAction SilentlyContinue |
Sort-Object Length -Descending |
Select-Object -First 10 |
ForEach-Object{

"{0,-60} {1,10:N2} MB" -f $_.Name,($_.Length/1MB)

}

Write-Host ""

# ===========================================================
# BANCOS
# ===========================================================

Write-Host "============================================================"
Write-Host "BANCOS DE DADOS"
Write-Host "============================================================"
Write-Host ""

$db | ForEach-Object{

Write-Host $_.FullName

}

Write-Host ""

# ===========================================================
# RELATÓRIO
# ===========================================================

$relatorio=@"

============================================================
PARECER DA PRESIDÊNCIA
============================================================

A plataforma foi localizada.

Nenhuma alteração foi realizada.

Esta rotina apenas identificou
o patrimônio existente.

Próxima missão:

Conhecer profundamente
cada ativo encontrado.

============================================================

"@

$relatorio | Out-File PRESIDENT_REPORT.txt -Encoding UTF8

Write-Host ""
Write-Host "Relatório salvo em PRESIDENT_REPORT.txt" -ForegroundColor Green

Write-Host ""
Write-Host "============================================================"
Write-Host "MISSÃO CONCLUÍDA"
Write-Host "============================================================"
Write-Host ""