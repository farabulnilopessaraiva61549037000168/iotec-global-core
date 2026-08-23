Write-Host ""
Write-Host "=================================================="
Write-Host " IOTEC INTERFACE RECOVERY ENGINE"
Write-Host "=================================================="
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
    Write-Host "=================================================="
    Write-Host " SCANNING:"
    Write-Host $location
    Write-Host "=================================================="

    # ==================================================
    # HTML FILES
    # ==================================================

    $htmlFiles = Get-ChildItem `
        -Path $location `
        -Recurse `
        -Filter *.html `
        -ErrorAction SilentlyContinue

    foreach ($file in $htmlFiles) {

        Write-Host ""
        Write-Host "[PROCESSING]"
        Write-Host $file.FullName

        # ==============================================
        # BACKUP
        # ==============================================

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

        # ==============================================
        # CONTENT
        # ==============================================

        $content = Get-Content `
            $file.FullName `
            -Raw

        # ==============================================
        # REMOVE BROKEN MAILTO
        # ==============================================

        $content = $content -replace `
            'mailto:[^"]+', `
            $email

        # ==============================================
        # NETLIFY FORM INTEGRATION
        # ==============================================

        $content = $content -replace `
            '<form([^>]*)>', `
            '<form name="iotec-contact" method="POST" data-netlify="true">$1<input type="hidden" name="form-name" value="iotec-contact">'

        # ==============================================
        # FIX PATHS
        # ==============================================

        $content = $content -replace '\\', '/'

        # ==============================================
        # FORCE UTF8
        # ==============================================

        if ($content -notmatch 'charset=UTF-8') {

            $content = $content -replace `
                '<head>', `
                '<head><meta charset="UTF-8">'
        }

        # ==============================================
        # SAVE
        # ==============================================

        Set-Content `
            -Path $file.FullName `
            -Value $content `
            -Encoding UTF8

        Write-Host "[OK] INTERFACE RESTORED"

        Write-Host "[OK] FORMS CONNECTED"

        Write-Host "[OK] UTF8 STANDARDIZED"

        Write-Host "[OK] PATHS NORMALIZED"
    }
}

Write-Host ""
Write-Host "=================================================="
Write-Host " IOTEC RECOVERY COMPLETE"
Write-Host "=================================================="