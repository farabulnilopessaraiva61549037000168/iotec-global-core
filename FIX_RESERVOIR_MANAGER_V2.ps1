Write-Host ""
Write-Host "====================================="
Write-Host "IOTEC RESERVOIR AUTO FIX V2"
Write-Host "====================================="
Write-Host ""

$file = "C:\IOTEC\IOTEC_RESERVOIR_MANAGER.py"

if (!(Test-Path $file))
{
    Write-Host "ARQUIVO NAO ENCONTRADO"
    exit
}

$code = Get-Content $file -Raw

# --------------------------------------------------
# CORRIGE row[4]
# --------------------------------------------------

$code = $code.Replace(
@"
    item_id = row[0]
    source = row[1]
    category = row[2]
    title = row[3]
    value = row[4]
"@,
@"
    item_id = row[0]
    source = row[1]
    category = row[2]
    value = row[3]
"@
)

# --------------------------------------------------
# CORRIGE PLACEHOLDERS SQL
# --------------------------------------------------

$code = $code.Replace(
"?,?,?,?,?,?",
"?,?,?,?,?"
)

Set-Content `
    -Path $file `
    -Value $code `
    -Encoding UTF8

Write-Host ""
Write-Host "[OK] CORRECOES APLICADAS"
Write-Host ""

Write-Host "EXECUTANDO TESTE..."
Write-Host ""

python $file

Write-Host ""
Write-Host "FIM"
Write-Host ""