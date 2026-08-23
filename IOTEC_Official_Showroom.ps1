Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC OFFICIAL SHOWROOM ENGINE"
Write-Host "======================================================="
Write-Host ""

# =======================================================
# CORE
# =======================================================

$core = "C:\Tecnologia"

# =======================================================
# SHOWROOM
# =======================================================

$showroom = Join-Path `
    $core `
    "showroom"

# =======================================================
# EMAIL
# =======================================================

$email = "iotec.bl@proton.me"

# =======================================================
# CHECK CORE
# =======================================================

if (!(Test-Path $core)) {

    Write-Host "[ERROR] CORE NOT FOUND"
    exit
}

Write-Host "[OK] CORE FOUND"

# =======================================================
# FIND HTM
# =======================================================

$source = Get-ChildItem `
    -Path $core `
    -Filter *.htm `
    -Recurse `
    -ErrorAction SilentlyContinue |

    Select-Object -First 1

if (!$source) {

    Write-Host "[ERROR] NO HTM FOUND"
    exit
}

Write-Host ""
Write-Host "[OFFICIAL INTERFACE]"
Write-Host $source.FullName

# =======================================================
# DESTINATION
# =======================================================

$destination = Join-Path `
    $showroom `
    "index.html"

# =======================================================
# COPY
# =======================================================

Copy-Item `
    $source.FullName `
    $destination `
    -Force

Write-Host ""
Write-Host "[OK] INTERFACE COPIED"

# =======================================================
# CONTENT
# =======================================================

$content = Get-Content `
    $destination `
    -Raw

# =======================================================
# UTF8
# =======================================================

if ($content -notmatch "charset=UTF-8") {

    $content = $content -replace `
        "<head>",
        "<head><meta charset=`"UTF-8`">"
}

# =======================================================
# FORMS
# =======================================================

$content = $content -replace `
    "<form([^>]*)>",
    "<form name=`"iotec-contact`" method=`"POST`" data-netlify=`"true`">$1<input type=`"hidden`" name=`"form-name`" value=`"iotec-contact`">"

# =======================================================
# EMAIL
# =======================================================

$content = $content -replace `
    "mailto:[^`"]+",
    $email

# =======================================================
# SAVE
# =======================================================

Set-Content `
    -Path $destination `
    -Value $content `
    -Encoding UTF8

Write-Host "[OK] FORM SYSTEM CONNECTED"

Write-Host "[OK] EMAIL ROUTING ACTIVE"

Write-Host "[OK] UTF8 STANDARDIZED"

# =======================================================
# OPEN SHOWROOM
# =======================================================

Write-Host ""
Write-Host "======================================================="
Write-Host " OPENING SHOWROOM"
Write-Host "======================================================="

Start-Process $destination

# =======================================================
# FINAL
# =======================================================

Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC SHOWROOM READY"
Write-Host "======================================================="