Write-Host ""
Write-Host "========================================="
Write-Host " MISSION 05 - RENDER TRUTH"
Write-Host "========================================="
Write-Host ""

Write-Host "[LOCAL PROOF]"
try {

    $r = Invoke-WebRequest `
    http://127.0.0.1:3000/iotec-proof `
    -UseBasicParsing

    Write-Host $r.Content

}
catch {

    Write-Host "LOCAL OFFLINE"

}

Write-Host ""
Write-Host "[RENDER ROOT]"
try {

    $r = Invoke-WebRequest `
    https://iotec-platform-1.onrender.com `
    -UseBasicParsing

    Write-Host ("SIZE: " + $r.Content.Length)

    if($r.Content -match "GLOBAL ENTERPRISE INTELLIGENCE"){
        Write-Host "ENTERPRISE FOUND"
    }

    if($r.Content -match "IOTEC PORTAL WEBFLASK"){
        Write-Host "OLD PORTAL FOUND"
    }

}
catch {

    Write-Host "RENDER OFFLINE"

}

Write-Host ""
Write-Host "[RENDER PROOF]"
try {

    $r = Invoke-WebRequest `
    https://iotec-platform-1.onrender.com/iotec-proof `
    -UseBasicParsing

    Write-Host $r.Content

}
catch {

    Write-Host "ROUTE NOT FOUND"

}

Write-Host ""
Write-Host "[RENDER NEW LEAD]"
try {

    Invoke-WebRequest `
    https://iotec-platform-1.onrender.com/new-lead `
    -Method POST `
    -UseBasicParsing

}
catch {

    Write-Host $_.Exception.Message

}

Write-Host ""
Write-Host "[PROCFILE]"
Get-Content Procfile

Write-Host ""
Write-Host "[CURRENT FILE HASH]"

(Get-FileHash ENTERPRISE_RENDER_READY.py).Hash

Write-Host ""
Write-Host "========================================="
Write-Host " FINAL DIAGNOSIS GENERATED"
Write-Host "========================================="