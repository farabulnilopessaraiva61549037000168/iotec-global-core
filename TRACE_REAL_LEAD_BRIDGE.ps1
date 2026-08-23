Write-Host ""
Write-Host "==========================================="
Write-Host " REAL LEAD BRIDGE DIAGNOSTIC"
Write-Host "==========================================="
Write-Host ""

$log = "REAL_LEAD_BRIDGE_TRACE.log"

if (Test-Path $log) {
    Remove-Item $log -Force
}

Write-Host "[1] STARTING SERVER..."
Write-Host ""

$process = Start-Process `
    python `
    -ArgumentList "REAL_LEAD_BRIDGE.py" `
    -RedirectStandardOutput $log `
    -RedirectStandardError $log `
    -PassThru

Start-Sleep 5

Write-Host "[2] SENDING TEST LEAD..."
Write-Host ""

$body = @{
    name = "Bruno"
    email = "bruno@test.com"
    service = "AI Automation"
} | ConvertTo-Json

try {

    Invoke-RestMethod `
        -Uri "http://127.0.0.1:3000/new-lead" `
        -Method Post `
        -ContentType "application/json" `
        -Body $body

}
catch {

    Write-Host ""
    Write-Host "[POST ERROR DETECTED]"
    Write-Host $_.Exception.Message
    Write-Host ""

}

Start-Sleep 3

Write-Host "[3] STOPPING SERVER..."
Write-Host ""

try {
    Stop-Process -Id $process.Id -Force
}
catch {
}

Start-Sleep 2

Write-Host ""
Write-Host "==========================================="
Write-Host " SERVER TRACE"
Write-Host "==========================================="
Write-Host ""

Get-Content $log -Tail 200

Write-Host ""
Write-Host "==========================================="
Write-Host " END OF TRACE"
Write-Host "==========================================="
Write-Host ""