Write-Host ""
Write-Host "====================================="
Write-Host " IOTEC AUTO REPAIR ENGINE"
Write-Host "====================================="
Write-Host ""

$arquivo = "C:\IOTEC\Iotec_Spine.py"

if (!(Test-Path $arquivo)) {

    Write-Host "Arquivo nao encontrado."
    exit
}

$backup = "C:\IOTEC\BACKUP_Iotec_Spine.py"

Copy-Item $arquivo $backup -Force

Write-Host "[OK] Backup criado."

$conteudo = Get-Content $arquivo -Raw

$conteudo = $conteudo -replace "`t", "    "

Write-Host "[OK] Tabs convertidas."

$conteudo = $conteudo -replace 'print\("`r?`n', 'print("\n'

Write-Host "[OK] Prints corrigidos."

$conteudo = $conteudo -replace '""', '"'

Write-Host "[OK] Aspas revisadas."

Set-Content -Path $arquivo -Value $conteudo -Encoding UTF8

Write-Host "[OK] Arquivo reestruturado."

Write-Host ""
Write-Host "====================================="
Write-Host " TESTANDO NUCLEO"
Write-Host "====================================="
Write-Host ""

python $arquivo

Write-Host ""
Write-Host "====================================="
Write-Host " REPARO FINALIZADO"
Write-Host "====================================="