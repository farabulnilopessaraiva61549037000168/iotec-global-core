Write-Host ""
Write-Host "==================================="
Write-Host "IOTEC AUTO BACKUP"
Write-Host "==================================="

$origem = "C:\IOTEC"
$backup = "C:\IOTEC\BACKUP"

if (-not (Test-Path $backup))
{
    New-Item `
    -ItemType Directory `
    -Path $backup `
    | Out-Null
}

$data =
Get-Date -Format "yyyyMMdd_HHmmss"

Get-ChildItem `
$origem `
-Filter "*.py" `
| ForEach-Object {

    $destino =
    Join-Path `
    $backup `
    ($_.BaseName + "_" + $data + ".py")

    Copy-Item `
    $_.FullName `
    $destino

    Write-Host "BACKUP ->" $_.Name
}

Write-Host ""
Write-Host "BACKUP FINALIZADO"