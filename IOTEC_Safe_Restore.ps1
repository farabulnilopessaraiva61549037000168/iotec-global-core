Write-Host ""
Write-Host "=================================================="
Write-Host " IOTEC SAFE RESTORE ENGINE"
Write-Host "=================================================="
Write-Host ""

# ==================================================
# ROOT
# ==================================================

$root = "C:\Tecnologia"

# ==================================================
# SHOWROOM
# ==================================================

$showroom = "C:\Tecnologia\showroom\index.html"

# ==================================================
# CHECK ROOT
# ==================================================

if (!(Test-Path $root)) {

    Write-Host "[ERROR] ROOT NOT FOUND"
    exit
}

Write-Host "[OK] ROOT FOUND"

# ==================================================
# SEARCH BACKUPS
# ==================================================

$backups = Get-ChildItem `
    -Path $root `
    -Recurse `
    -Include *.bak, *.deepbackup, *.restorebackup `
    -ErrorAction SilentlyContinue

if ($backups.Count -eq 0) {

    Write-Host "[ERROR] NO BACKUPS FOUND"
    exit
}

Write-Host ""
Write-Host "=================================================="
Write-Host " BACKUPS FOUND"
Write-Host "=================================================="

$count = 1

foreach ($file in $backups) {

    Write-Host ""
    Write-Host "$count)"
    Write-Host $file.FullName

    $count++
}

# ==================================================
# SELECT FIRST VALID BACKUP
# ==================================================

$selected = $backups[0]

Write-Host ""
Write-Host "=================================================="
Write-Host " SELECTED BACKUP"
Write-Host "=================================================="

Write-Host $selected.FullName

# ==================================================
# RESTORE
# ==================================================

Copy-Item `
    $selected.FullName `
    $showroom `
    -Force

Write-Host ""
Write-Host "[OK] SHOWROOM RESTORED"

# ==================================================
# OPEN
# ==================================================

Start-Process $showroom

# ==================================================
# FINAL
# ==================================================

Write-Host ""
Write-Host "=================================================="
Write-Host " SAFE RESTORE COMPLETE"
Write-Host "=================================================="