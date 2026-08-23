# ============================================================
# FIX_IOTEC_PYTHON_FILES.ps1
# Corrige automaticamente todos os arquivos .py
# ============================================================

$Root = "C:\IOTEC"

Write-Host ""
Write-Host "==============================================="
Write-Host "IOTEC PYTHON FILE REPAIR"
Write-Host "==============================================="
Write-Host ""

$files = Get-ChildItem $Root -Recurse -Filter *.py

$total = 0

foreach($file in $files){

    $text = Get-Content $file.FullName -Raw

    # Remove BOM invisível
    if($text.Length -gt 0 -and $text[0] -eq [char]0xFEFF){
        $text = $text.Substring(1)
    }

    # Corrige \" -> "
    $text = $text.Replace('\"','"')

    # Corrige \' -> '
    $text = $text.Replace("\'","'")

    # Salva novamente em UTF8 sem BOM
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($file.FullName,$text,$utf8)

    Write-Host "[OK] $($file.Name)"

    $total++
}

Write-Host ""
Write-Host "==============================================="
Write-Host "$total arquivos corrigidos."
Write-Host "==============================================="