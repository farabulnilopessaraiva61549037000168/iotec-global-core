param($action, $module)

if ($action -eq "iotech" -and $module -eq "up") {

  Write-Host ">> IOTEC AUTO-DEPLOY INICIADO" -ForegroundColor Cyan

  # LOG
  $log = "C:\IOTEC\logs\boot.log"
  "BOOT: $(Get-Date)" | Add-Content $log

  # SCAN REAL DO SISTEMA
  Get-ComputerInfo | Out-File C:\IOTEC\core\scanner\system_scan.txt

  # PORTAS HTTP
  netsh advfirewall firewall add rule name="IOTEC_HTTP_8080" dir=in action=allow protocol=TCP localport=8080
  netsh advfirewall firewall add rule name="IOTEC_API_5000" dir=in action=allow protocol=TCP localport=5000

  # NODE / ELECTRON CHECK
  if (!(Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "Node não encontrado (instale depois)" -ForegroundColor Yellow
  }

  # SERVIÇO WINDOWS
  $svc = Get-Service -Name IOTEC_SUPERVISOR -ErrorAction SilentlyContinue
  if (!$svc) {
    sc.exe create IOTEC_SUPERVISOR binPath= "powershell.exe -ExecutionPolicy Bypass -File C:\IOTEC\services\supervisor.ps1" start= auto
  }

  Write-Host ">> IOTEC ONLINE" -ForegroundColor Green
}
