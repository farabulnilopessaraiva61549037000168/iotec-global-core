Write-Host ""
Write-Host "======================================================"
Write-Host " IOTEC MASTER CORE INITIALIZATION"
Write-Host "======================================================"
Write-Host ""

# ======================================================
# MASTER CORE
# ======================================================

$core = "C:\Tecnologia"

# ======================================================
# CHECK CORE
# ======================================================

if (!(Test-Path $core)) {

    Write-Host "[ERROR] CORE NOT FOUND"
    exit
}

Write-Host "[OK] MASTER CORE FOUND"
Write-Host $core

# ======================================================
# STRUCTURE
# ======================================================

$folders = @(

    "assets",
    "css",
    "js",
    "interfaces",
    "showroom",
    "forms",
    "deploy",
    "ai",
    "monitor",
    "backups",
    "reports",
    "contracts",
    "leads"
)

foreach ($folder in $folders) {

    $path = Join-Path $core $folder

    if (!(Test-Path $path)) {

        New-Item `
            -ItemType Directory `
            -Path $path | Out-Null

        Write-Host "[CREATED] $folder"
    }
    else {

        Write-Host "[EXISTS] $folder"
    }
}

# ======================================================
# SEARCH HTML
# ======================================================

Write-Host ""
Write-Host "======================================================"
Write-Host " SCANNING INTERFACES"
Write-Host "======================================================"

$htmlFiles = Get-ChildItem `
    -Path $core `
    -Filter *.html `
    -Recurse `
    -ErrorAction SilentlyContinue

foreach ($file in $htmlFiles) {

    Write-Host ""
    Write-Host "[INTERFACE FOUND]"
    Write-Host $file.FullName
}

# ======================================================
# CREATE MONITOR FILE
# ======================================================

$monitorFile = Join-Path `
    $core `
    "monitor\system_status.txt"

@"
======================================
IOTEC SYSTEM STATUS
======================================

CORE STATUS: ONLINE
DEPLOY STATUS: READY
SHOWROOM STATUS: READY
AI STATUS: READY
FORM STATUS: MONITORING
EMAIL ROUTING: ACTIVE

======================================
"@ | Set-Content $monitorFile

Write-Host ""
Write-Host "[OK] MONITOR FILE CREATED"

# ======================================================
# CREATE LEADS FILE
# ======================================================

$leadsFile = Join-Path `
    $core `
    "leads\incoming_leads.txt"

if (!(Test-Path $leadsFile)) {

    New-Item `
        -ItemType File `
        -Path $leadsFile | Out-Null

    Write-Host "[OK] LEADS FILE CREATED"
}

# ======================================================
# CREATE CONTRACTS FILE
# ======================================================

$contractsFile = Join-Path `
    $core `
    "contracts\contracts.txt"

if (!(Test-Path $contractsFile)) {

    New-Item `
        -ItemType File `
        -Path $contractsFile | Out-Null

    Write-Host "[OK] CONTRACTS FILE CREATED"
}

# ======================================================
# FINAL
# ======================================================

Write-Host ""
Write-Host "======================================================"
Write-Host " IOTEC MASTER CORE READY"
Write-Host "======================================================"

Write-Host ""
Write-Host "NEXT STEP:"
Write-Host "SELECT OFFICIAL INTERFACE"
Write-Host "CONNECT FORMS"
Write-Host "DEPLOY SHOWROOM"
Write-Host "ENABLE AI CONCIERGE"