$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 RECONFIGURANDO ROTAS" -ForegroundColor Cyan

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # remover links da replit
    $c = $c -replace 'https://.*?replit\.dev', ''

    # mapear rotas novas
    $c = $c -replace 'href="/servicos"', 'href="/servicos.html"'
    $c = $c -replace 'href="/diagnostico"', 'href="/diagnostico.html"'
    $c = $c -replace 'href="/portais"', 'href="/portais.html"'

    Set-Content $_.FullName $c
}

Write-Host "✅ ROTAS LOCAIS ATIVADAS" -ForegroundColor Green
