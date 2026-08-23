Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC UTF8 RECOVERY ENGINE"
Write-Host "======================================================="
Write-Host ""

# =======================================================
# SHOWROOM
# =======================================================

$file = "C:\Tecnologia\showroom\index.html"

# =======================================================
# CHECK
# =======================================================

if (!(Test-Path $file)) {

    Write-Host "[ERROR] SHOWROOM NOT FOUND"
    exit
}

Write-Host "[OK] SHOWROOM FOUND"

# =======================================================
# READ RAW
# =======================================================

$content = Get-Content `
    -Path $file `
    -Raw

# =======================================================
# FIX COMMON UTF ISSUES
# =======================================================

$content = $content.Replace("â€”", "—")
$content = $content.Replace("â€œ", """")
$content = $content.Replace("â€", """")
$content = $content.Replace("Ã§", "ç")
$content = $content.Replace("Ã£", "ã")
$content = $content.Replace("Ã¡", "á")
$content = $content.Replace("Ã©", "é")
$content = $content.Replace("Ãª", "ê")
$content = $content.Replace("Ã­", "í")
$content = $content.Replace("Ã³", "ó")
$content = $content.Replace("Ãµ", "õ")
$content = $content.Replace("Ãº", "ú")

# =======================================================
# FORCE UTF8 META
# =======================================================

if ($content -notmatch "charset=UTF-8") {

    $content = $content -replace `
        "<head>",
        "<head><meta charset=`"UTF-8`">"
}

# =======================================================
# SAVE UTF8
# =======================================================

Set-Content `
    -Path $file `
    -Value $content `
    -Encoding UTF8

Write-Host "[OK] UTF8 RESTORED"

# =======================================================
# OPEN
# =======================================================

Start-Process $file

Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC UTF8 RECOVERY COMPLETE"
Write-Host "======================================================="