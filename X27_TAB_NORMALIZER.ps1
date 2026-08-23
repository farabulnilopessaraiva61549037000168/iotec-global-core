Write-Host ""
Write-Host "====================================="
Write-Host "X27 INDENTATION AUDITOR"
Write-Host "====================================="
Write-Host ""

$root = "C:\IOTEC"

$erros = @()

Get-ChildItem $root -Filter *.py -Recurse | ForEach-Object {

    try {

        python -m py_compile $_.FullName 2>$null

        if ($LASTEXITCODE -ne 0) {

            $erros += $_.FullName

        }

    }
    catch {

        $erros += $_.FullName

    }

}

Write-Host ""
Write-Host "Arquivos com erro:" $erros.Count
Write-Host ""

$erros | Out-File "C:\IOTEC\X27_INDENTATION_ERRORS.txt"

Write-Host "Relatorio salvo:"
Write-Host "C:\IOTEC\X27_INDENTATION_ERRORS.txt"