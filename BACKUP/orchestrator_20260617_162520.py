import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
Write-Host ""
Write-Host "====================================="
Write-Host " PREMIUM ECOSYSTEM CORE"
Write-Host "====================================="
Write-Host ""

Set-Location "C:\IOTEC"

Write-Host "[1/4] Starting Global Agent..."
python AGENTS\orchestrator.py

Write-Host "[2/4] Starting Portal Main..."
Start-Process powershell -ArgumentList "cd PORTALS\portal_main; npm run dev -- --port 5173"

Write-Host "[3/4] Starting Ecosystem..."
Start-Process powershell -ArgumentList "cd PORTALS\ecosystem; npm run dev -- --port 5174"

Write-Host "[4/4] Premium Core Online"


