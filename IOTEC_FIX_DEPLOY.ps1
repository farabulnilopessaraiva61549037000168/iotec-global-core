# =========================
# IOTEC FIX DEPLOY
# =========================

$origem = "$env:USERPROFILE\Desktop\OFICINA_IOTEC"
$destino = "C:\IOTEC\IOTEC_RENDER_READY"
$static = "$destino\static"

Write-Host "🚀 INICIANDO" -ForegroundColor Cyan

if (Test-Path $destino) {
    Remove-Item $destino -Recurse -Force
}

New-Item -ItemType Directory -Path $static | Out-Null

Copy-Item "$origem\*" $static -Recurse -Force

Get-ChildItem $static -Recurse -Include *.htm, *.html | ForEach-Object {
    $c = Get-Content $_.FullName -Raw
    $c = $c -replace "_files/", ""
    $novo = $_.FullName -replace "\.htm$", ".html"
    Set-Content $novo $c -Encoding UTF8
    if ($_.FullName -like "*.htm") { Remove-Item $_.FullName }
}

Get-ChildItem $static -Recurse -Directory | Where-Object {
    $_.Name -like "*_files"
} | ForEach-Object {
    Copy-Item "$($_.FullName)\*" $static -Recurse -Force
}

$primeiro = Get-ChildItem $static -Filter *.html | Select-Object -First 1
Copy-Item $primeiro.FullName "$static\index.html" -Force

"flask" | Out-File "$destino\requirements.txt"

Write-Host "✅ FINALIZADO" -ForegroundColor Green
