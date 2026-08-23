$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 CORRIGINDO TODOS OS FORMULÁRIOS" -ForegroundColor Cyan

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # Corrige <form> sem action
    $c = $c -replace '<form(?![^>]*action=)', '<form action="/enviar" method="post"'

    # Corrige forms que já existem mas sem method
    $c = $c -replace 'method="get"', 'method="post"'

    Set-Content $_.FullName $c

    Write-Host "✔ Corrigido:" $_.Name
}

Write-Host "✅ TODOS OS FORMULÁRIOS ESTÃO ATIVOS" -ForegroundColor Green
