Param(
    [Parameter(Mandatory=$true)]
    [string]$UrlGithub
)

Set-Location C:\IOTEC

if (-not (Test-Path ".git")) {
    git init
}

# 1. Adiciona alterações de subpastas e submódulos se existirem
git add --all

# 2. Faz o commit incluindo tudo
git commit -m "Sincronizacao IOTEC Total - Consolidação de Módulos e Subpastas"

# 3. Garante branch main
git branch -M main

# 4. Ajusta a URL remota e envia com força total
git remote remove origin 2>$null
git remote add origin $UrlGithub
git push -u origin main --force

Write-Host "`n✅ CÓDIGO E ESTRUTURA INTEGRAL ENVIADOS AO GITHUB COM SUCESSO!" -ForegroundColor Green
