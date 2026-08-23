$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 PADRONIZANDO CAMPOS DOS FORMULÁRIOS" -ForegroundColor Cyan

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # Nome
    $c = $c -replace 'name="[^"]*nome[^"]*"', 'name="nome"'
    $c = $c -replace 'name="name"', 'name="nome"'

    # Email
    $c = $c -replace 'name="[^"]*mail[^"]*"', 'name="email"'
    $c = $c -replace 'name="emailAddress"', 'name="email"'

    # Mensagem
    $c = $c -replace 'name="[^"]*msg[^"]*"', 'name="mensagem"'
    $c = $c -replace 'name="message"', 'name="mensagem"'

    Set-Content $_.FullName $c

    Write-Host "✔ Ajustado:" $_.Name
}

Write-Host "✅ FORMULÁRIOS PADRONIZADOS" -ForegroundColor Green
