Write-Host ""
Write-Host "====================================="
Write-Host "IOTEC RESERVOIR AUTO FIX"
Write-Host "====================================="
Write-Host ""

$File = "C:\IOTEC\IOTEC_RESERVOIR_MANAGER.py"

if (!(Test-Path $File))
{
    Write-Host "ARQUIVO NAO ENCONTRADO:"
    Write-Host $File
    exit
}

$code = Get-Content $File -Raw

# =====================================================
# warehouse_id -> item_id
# =====================================================

$code = $code -replace "warehouse_id", "item_id"

# =====================================================
# remove campo title do INSERT
# =====================================================

$code = $code -replace ",\s*title\s*,", ","

# remove title da lista VALUES caso exista
$code = $code -replace "\(\s*str\(datetime\.now\(\)\),\s*reservoir,\s*source,\s*item_id,\s*title,\s*value\s*\)",
"(
        str(datetime.now()),
        reservoir,
        source,
        item_id,
        value
    )"

Set-Content `
    -Path $File `
    -Value $code `
    -Encoding UTF8

Write-Host ""
Write-Host "[OK] CORRECOES APLICADAS"
Write-Host ""

Write-Host "EXECUTANDO TESTE..."
Write-Host ""

python $File

Write-Host ""
Write-Host "CONCLUIDO"
Write-Host ""