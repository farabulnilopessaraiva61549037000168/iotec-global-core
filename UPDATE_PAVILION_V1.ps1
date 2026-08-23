Write-Host ""
Write-Host "========================================="
Write-Host "IOTEC - PRIMEIRO PAVILHÃO"
Write-Host "ATUALIZAÇÃO AUTOMÁTICA"
Write-Host "========================================="
Write-Host ""

$files = Get-ChildItem -Path . -Filter *.py -Recurse

$old = "299.90"
$new = "29.90"

foreach ($file in $files)
{
    $content = Get-Content $file.FullName -Raw

    if ($content.Contains($old))
    {
        $content = $content.Replace($old,$new)

        Set-Content `
            -Path $file.FullName `
            -Value $content `
            -Encoding UTF8

        Write-Host "[ATUALIZADO] $($file.Name)"
    }
}

Write-Host ""
Write-Host "========================================="
Write-Host "ATUALIZAÇÃO CONCLUÍDA"
Write-Host "Novo valor: R$ 29,90"
Write-Host "========================================="