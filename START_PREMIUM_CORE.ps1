Write-Host ''
Write-Host '====================================='
Write-Host ' PREMIUM ECOSYSTEM CORE'
Write-Host '====================================='
Write-Host ''

Set-Location 'C:\IOTEC'

Write-Host '[1/3] Starting Global Agent...'
Start-Process powershell -ArgumentList 'python AGENTS\orchestrator.py'

Write-Host '[2/3] Starting Portal Main...'
Start-Process powershell -ArgumentList 'cd PORTALS\portal_main; .\START_PORTAL.ps1'

Write-Host '[3/3] Premium Core Online'
