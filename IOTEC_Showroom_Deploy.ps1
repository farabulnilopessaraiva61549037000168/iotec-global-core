Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC SHOWROOM DEPLOY ENGINE"
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
Write-Host $core

# =======================================================
# SEARCH HTML FILES
# =======================================================

Write-Host ""
Write-Host "======================================================="
Write-Host " SEARCHING INTERFACES"
Write-Host "======================================================="

$htmlFiles = Get-ChildItem `
    -Path $core `
    -Filter *.html `
    -Recurse `
    -ErrorAction SilentlyContinue

if ($htmlFiles.Count -eq 0) {

    Write-Host "[ERROR] NO HTML FOUND"
    exit
}

$selected = $htmlFiles[0]

Write-Host ""
Write-Host "[OFFICIAL INTERFACE]"
Write-Host $selected.FullName

# =======================================================
# COPY TO SHOWROOM
# =======================================================

$destination = Join-Path `
    $showroom `
    "index.html"

Copy-Item `
    $selected.FullName `
    $destination `
    -Force

Write-Host ""
Write-Host "[OK] INTERFACE COPIED TO SHOWROOM"

# =======================================================
# CONTENT
# =======================================================

$content = Get-Content `
    $destination `
    -Raw

# =======================================================
# UTF8
# =======================================================

if ($content -notmatch 'charset=UTF-8') {

    $content = $content -replace `
        '<head>',
        '<head><meta charset="UTF-8">'
}

# =======================================================
# FORM REPAIR
# =======================================================

$content = $content -replace `
    '<form([^>]*)>',
    '<form name="iotec-contact" method="POST" data-netlify="true">$1<input type="hidden" name="form-name" value="iotec-contact">'

# =======================================================
# EMAIL ROUTING
# =======================================================

$content = $content -replace `
    'mailto:[^"]+',
    $email

# =======================================================
# PREMIUM OVERLAY
# =======================================================

$premium = @'

<style>

body {

    background:
    radial-gradient(
        circle at top right,
        rgba(255,180,60,0.10),
        transparent 25%
    ),

    #07090f !important;
}

form {

    background:
    rgba(255,255,255,0.04);

    border-radius: 24px;

    padding: 30px;

    backdrop-filter: blur(14px);

    border:
    1px solid rgba(255,255,255,0.08);
}

input,
textarea,
select {

    width: 100% !important;

    padding: 14px !important;

    border-radius: 14px !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    background:
    rgba(255,255,255,0.05) !important;

    color: white !important;

    margin-top: 10px !important;

    margin-bottom: 18px !important;
}

button,
input[type=submit] {

    background:
    linear-gradient(
        145deg,
        #ffcc70,
        #ff9f1a
    ) !important;

    color: black !important;

    border: none !important;

    padding: 16px !important;

    border-radius: 14px !important;

    font-weight: bold !important;

    width: 100%;
}

</style>

'@

if ($content -notmatch 'ffcc70') {

    $content = $content -replace `
        '</head>',
        "$premium`n</head>"
}

# =======================================================
# SAVE
# =======================================================

Set-Content `
    -Path $destination `
    -Value $content `
    -Encoding UTF8

Write-Host "[OK] PREMIUM SYSTEM APPLIED"

Write-Host "[OK] FORM SYSTEM CONNECTED"

Write-Host "[OK] EMAIL ROUTING ACTIVE"

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

Write-Host ""
Write-Host "SHOWROOM:"
Write-Host $destination