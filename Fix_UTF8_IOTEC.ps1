Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC UTF8 SAFE RECOVERY"
Write-Host "==============================================="
Write-Host ""

$file = "C:\Tecnologia\showroom\index.html"

if (!(Test-Path $file)) {

    Write-Host "[ERROR] FILE NOT FOUND"
    exit
}

Write-Host "[OK] FILE FOUND"

$content = Get-Content $file -Raw

# FORCE UTF8 META

if ($content -notmatch "charset") {

    $content = $content -replace `
        "<head>",
        "<head><meta charset='UTF-8'>"
}

# REMOVE MOST COMMON BROKEN SEQUENCES

$content = $content -replace "â€œ", ""
$content = $content -replace "â€", ""
$content = $content -replace "â€”", "-"
$content = $content -replace "Ã", ""

# SAVE CLEAN UTF8

Set-Content `
    -Path $file `
    -Value $content `
    -Encoding UTF8

Write-Host "[OK] UTF8 NORMALIZED"

Start-Process $file

Write-Host ""
Write-Host "==============================================="
Write-Host " RECOVERY COMPLETE"
Write-Host "==============================================="