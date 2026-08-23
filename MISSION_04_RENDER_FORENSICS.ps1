Write-Host ""
Write-Host "====================================="
Write-Host " RENDER FORENSICS"
Write-Host "====================================="
Write-Host ""

Write-Host "[1] GIT REMOTE"
git remote -v

Write-Host ""
Write-Host "[2] PROCFILE"
if(Test-Path ".\Procfile"){
    Get-Content Procfile
}

Write-Host ""
Write-Host "[3] IOTEC PROOF"
Select-String `
-Path ENTERPRISE_RENDER_READY.py `
-Pattern "iotec-proof"

Write-Host ""
Write-Host "[4] LOCAL TEST"

try {

    $r = Invoke-WebRequest `
    http://127.0.0.1:3000/iotec-proof `
    -UseBasicParsing

    Write-Host $r.Content

}
catch {

    Write-Host "LOCAL SERVER OFFLINE"

}

Write-Host ""
Write-Host "[5] RENDER TEST"

try {

    $r = Invoke-WebRequest `
    https://iotec-platform-1.onrender.com/iotec-proof `
    -UseBasicParsing

    Write-Host $r.Content

}
catch {

    Write-Host "RENDER DOES NOT HAVE ROUTE"

}

Write-Host ""
Write-Host "====================================="
Write-Host " FORENSICS COMPLETE"
Write-Host "====================================="