```powershell
# ============================================================
# IOTEC FORENSIC AUTO ENABLE
# ============================================================

Clear-Host

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " IOTEC FORENSIC AUDIT ACTIVATOR " -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------
# VERIFICA ADMIN
# ------------------------------------------------------------

$currentUser = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())

if (-not $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {

    Write-Host ""
    Write-Host "ERRO: Execute este script como ADMINISTRADOR." -ForegroundColor Red
    Write-Host ""
    Pause
    Exit
}

# ------------------------------------------------------------
# FUNÇÃO SEGURA
# ------------------------------------------------------------

function Safe-Audit {
    param($cmd)

    try {
        Invoke-Expression $cmd | Out-Null
        Write-Host "[OK] $cmd" -ForegroundColor Green
    }
    catch {
        Write-Host "[ERRO] $cmd" -ForegroundColor Red
    }
}

# ------------------------------------------------------------
# ATIVANDO AUDITORIAS
# ------------------------------------------------------------

Write-Host ""
Write-Host "Ativando auditorias..." -ForegroundColor Yellow
Write-Host ""

Safe-Audit 'auditpol /set /subcategory:"Logon" /success:enable /failure:enable'

Safe-Audit 'auditpol /set /subcategory:"Criação de processo" /success:enable'

Safe-Audit 'auditpol /set /subcategory:"Sistema de arquivos" /success:enable /failure:enable'

Safe-Audit 'auditpol /set /subcategory:"Eventos Plug and Play" /success:enable'

Safe-Audit 'auditpol /set /subcategory:"Conexão de Plataforma de Filtragem" /success:enable'

Safe-Audit 'auditpol /set /subcategory:"Armazenamento Removível" /success:enable /failure:enable'

# ------------------------------------------------------------
# AUMENTA TAMANHO DOS LOGS
# ------------------------------------------------------------

Write-Host ""
Write-Host "Expandindo logs..." -ForegroundColor Yellow
Write-Host ""

wevtutil sl Security /ms:104857600
wevtutil sl System /ms:104857600
wevtutil sl Application /ms:104857600

# ------------------------------------------------------------
# HABILITA LOG DE POWERSHELL
# ------------------------------------------------------------

Write-Host ""
Write-Host "Ativando logging PowerShell..." -ForegroundColor Yellow
Write-Host ""

New-Item `
 "HKLM:\Software\Policies\Microsoft\Windows\PowerShell" `
 -Force | Out-Null

New-Item `
 "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" `
 -Force | Out-Null

Set-ItemProperty `
 "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" `
 EnableScriptBlockLogging 1

# ------------------------------------------------------------
# FINAL
# ------------------------------------------------------------

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " AUDITORIA FORENSE ATIVADA COM SUCESSO " -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green
Write-Host ""

Write-Host "Agora o Windows registrará:" -ForegroundColor Cyan
Write-Host "- Logins"
Write-Host "- Processos"
Write-Host "- Arquivos"
Write-Host "- USB"
Write-Host "- Conexões"
Write-Host "- Scripts PowerShell"
Write-Host ""

Pause
```
