$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 LIMPEZA PROFISSIONAL DE NOMES" -ForegroundColor Cyan

Get-ChildItem $base -Recurse | ForEach-Object {

    $novoNome = $_.Name

    $novoNome = $novoNome -replace " ", "_"
    $novoNome = $novoNome -replace "—", "_"
    $novoNome = $novoNome -replace "·", "_"

    if ($novoNome -ne $_.Name) {
        Rename-Item $_.FullName $novoNome -Force
        Write-Host "✔ Renomeado: $($_.Name)"
    }
}

Write-Host "🔧 Corrigindo HTML..." -ForegroundColor Yellow

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    $c = $c -replace " ", "_"
    $c = $c -replace "—", "_"
    $c = $c -replace "·", "_"

    Set-Content $_.FullName $c
}

Write-Host "✅ FINALIZADO" -ForegroundColor Green
