Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC JSON STANDARDIZER"
Write-Host "==============================================="
Write-Host ""

Get-ChildItem C:\IOTEC -Filter *.py | ForEach-Object {

    $arquivo = $_.FullName

    Write-Host "Analisando $($_.Name)..."

    $codigo = Get-Content $arquivo -Raw

    # Corrige oportunidade = banco
    $codigo = $codigo -replace `
    'oportunidades\s*=\s*banco',
    'oportunidades = banco.get("oportunidades", [])'

    # Corrige empresas = banco
    $codigo = $codigo -replace `
    'empresas\s*=\s*banco',
    'empresas = banco.get("empresas", [])'

    # Corrige missoes = banco
    $codigo = $codigo -replace `
    'missoes\s*=\s*banco',
    'missoes = banco.get("missoes", [])'

    # Corrige agentes = banco
    $codigo = $codigo -replace `
    'agentes\s*=\s*banco',
    'agentes = banco.get("agentes", [])'

    # Corrige clientes = banco
    $codigo = $codigo -replace `
    'clientes\s*=\s*banco',
    'clientes = banco.get("clientes", [])'

    Set-Content `
        -Encoding UTF8 `
        $arquivo `
        $codigo

}

Write-Host ""
Write-Host "==============================================="
Write-Host " PADRONIZAÇÃO CONCLUÍDA"
Write-Host "==============================================="