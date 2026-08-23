$origem = "$env:USERPROFILE\Desktop\OFICINA_IOTEC"
$destino = "C:\IOTEC\IOTEC_RENDER_READY"
$static = "$destino\static"

Write-Host "🚀 DEPLOY SEGURO" -ForegroundColor Cyan

if (Test-Path $destino) {
    Remove-Item $destino -Recurse -Force
}

New-Item -ItemType Directory -Path $static | Out-Null

# Copia tudo sem alterar nada
Copy-Item "$origem\*" $static -Recurse -Force

# Converte apenas extensão .htm -> .html (SEM mexer no conteúdo)
Get-ChildItem $static -Recurse -Filter *.htm | ForEach-Object {
    $novo = $_.FullName -replace "\.htm$", ".html"
    Copy-Item $_.FullName $novo
}

# cria index
$primeiro = Get-ChildItem $static -Filter *.html | Select-Object -First 1
Copy-Item $primeiro.FullName "$static\index.html" -Force

"flask" | Out-File "$destino\requirements.txt"

Write-Host "✅ RESTAURADO COM SEGURANÇA" -ForegroundColor Green