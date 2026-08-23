$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 FORÇANDO CORREÇÃO TOTAL DE FORMULÁRIOS" -ForegroundColor Cyan

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # Remove QUALQUER action existente
    $c = $c -replace 'action=".*?"', ''

    # Força action correta
    $c = $c -replace '<form', '<form action="/enviar" method="post"'

    # Remove method GET se existir
    $c = $c -replace 'method="get"', 'method="post"'

    Set-Content $_.FullName $c

    Write-Host "✔ FORÇADO:" $_.Name
}

Write-Host "✅ TODOS OS FORMULÁRIOS AGORA APONTAM PARA /enviar" -ForegroundColor Green
