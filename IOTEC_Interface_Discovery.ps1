Write-Host ""
Write-Host "======================================================="
Write-Host " IOTEC INTERFACE DISCOVERY ENGINE"
Write-Host "======================================================="
Write-Host ""

# =======================================================
# CORE
# =======================================================

$core = "C:\Tecnologia"

# =======================================================
# FILE TYPES
# =======================================================

$extensions = @(
    "*.html",
    "*.htm",
    "*.jsx",
    "*.tsx",
    "*.js",
    "*.php",
    "*.vue"
)

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
# SEARCH
# =======================================================

foreach ($ext in $extensions) {

    Write-Host ""
    Write-Host "======================================================="
    Write-Host " SEARCHING:"
    Write-Host $ext
    Write-Host "======================================================="

    $files = Get-ChildItem `
        -Path $core `
        -Filter $ext `
        -Recurse `
        -ErrorAction SilentlyContinue

    foreach ($file in $files) {

        Write-Host ""
        Write-Host "[FOUND]"
        Write-Host $file.FullName
    }
}

Write-Host ""
Write-Host "======================================================="
Write-Host " DISCOVERY COMPLETE"
Write-Host "======================================================="