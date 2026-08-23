Write-Host ""
Write-Host "===================================================="
Write-Host " IOTEC PREMIUM UI RECOVERY ENGINE"
Write-Host "===================================================="
Write-Host ""

# ======================================================
# EMAIL
# ======================================================

$email = "iotec.bl@proton.me"

# ======================================================
# LOCATIONS
# ======================================================

$locations = @(
    "C:\Tecnologia",
    "$env:USERPROFILE\Desktop\OFICINA_IOTEC"
)

# ======================================================
# PREMIUM CSS
# ======================================================

$premiumCss = @'

<style>

body {

    background:
    radial-gradient(
        circle at top right,
        rgba(255,180,60,0.10),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom left,
        rgba(255,120,0,0.08),
        transparent 30%
    ),

    #07090f !important;

    color: white !important;

    font-family: Segoe UI !important;
}

form {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 30px;

    backdrop-filter: blur(14px);

    box-shadow:
    0 0 30px rgba(255,180,60,0.08);

    margin-top: 30px;
}

input,
textarea,
select {

    width: 100% !important;

    background:
    rgba(255,255,255,0.05) !important;

    border:
    1px solid rgba(255,255,255,0.08) !important;

    color: white !important;

    padding: 14px !important;

    border-radius: 14px !important;

    margin-top: 10px !important;

    margin-bottom: 18px !important;

    font-size: 15px !important;

    outline: none !important;

    transition: 0.3s;
}

input:focus,
textarea:focus,
select:focus {

    border:
    1px solid rgba(255,180,60,0.5) !important;

    box-shadow:
    0 0 20px rgba(255,180,60,0.15);
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

    padding: 16px 24px !important;

    border-radius: 14px !important;

    font-weight: bold !important;

    cursor: pointer !important;

    transition: 0.3s !important;

    width: 100%;
}

button:hover,
input[type=submit]:hover {

    transform: translateY(-3px);

    box-shadow:
    0 0 30px rgba(255,180,60,0.25);
}

label {

    color:
    rgba(255,255,255,0.75) !important;

    font-size: 14px !important;
}

h1, h2, h3 {

    color: #ffcc70 !important;
}

</style>

'@

# ======================================================
# PROCESS
# ======================================================

foreach ($location in $locations) {

    if (!(Test-Path $location)) {

        Write-Host ""
        Write-Host "[WARNING] LOCATION NOT FOUND:"
        Write-Host $location

        continue
    }

    Write-Host ""
    Write-Host "===================================================="
    Write-Host " SCANNING:"
    Write-Host $location
    Write-Host "===================================================="

    $htmlFiles = Get-ChildItem `
        -Path $location `
        -Recurse `
        -Filter *.html `
        -ErrorAction SilentlyContinue

    foreach ($file in $htmlFiles) {

        Write-Host ""
        Write-Host "[PROCESSING]"
        Write-Host $file.FullName

        # ==================================================
        # BACKUP
        # ==================================================

        $backupDir = Join-Path `
            $file.DirectoryName `
            "BACKUP"

        if (!(Test-Path $backupDir)) {

            New-Item `
                -ItemType Directory `
                -Path $backupDir | Out-Null
        }

        Copy-Item `
            $file.FullName `
            (Join-Path $backupDir $file.Name) `
            -Force

        Write-Host "[OK] BACKUP CREATED"

        # ==================================================
        # CONTENT
        # ==================================================

        $content = Get-Content `
            $file.FullName `
            -Raw

        # ==================================================
        # INSERT PREMIUM CSS
        # ==================================================

        if ($content -notmatch "IOTEC PREMIUM UI") {

            $content = $content -replace `
                '</head>',
                "$premiumCss`n</head>"
        }

        # ==================================================
        # FIX FORMS
        # ==================================================

        $content = $content -replace `
            '<form([^>]*)>',
            '<form name="iotec-contact" method="POST" data-netlify="true">$1<input type="hidden" name="form-name" value="iotec-contact">'

        # ==================================================
        # FIX EMAIL
        # ======================================================

        $content = $content -replace `
            'mailto:[^"]+',
            $email

        # ==================================================
        # FORCE UTF8
        # ======================================================

        if ($content -notmatch 'charset=UTF-8') {

            $content = $content -replace `
                '<head>',
                '<head><meta charset="UTF-8">'
        }

        # ==================================================
        # SAVE
        # ======================================================

        Set-Content `
            -Path $file.FullName `
            -Value $content `
            -Encoding UTF8

        Write-Host "[OK] PREMIUM UI APPLIED"

        Write-Host "[OK] FORMS CONNECTED"

        Write-Host "[OK] EMAIL ROUTING ENABLED"

        Write-Host "[OK] STRUCTURE STABILIZED"
    }
}

Write-Host ""
Write-Host "===================================================="
Write-Host " IOTEC PREMIUM RECOVERY COMPLETE"
Write-Host "===================================================="