$ErrorActionPreference = "Stop"

Write-Host "== IOTEC SAFE BOOT =="

# 1. Fix path
$env:PYTHONPATH = "C:\IOTEC\MODULES"

# 2. Force UTF-8 runtime
$env:PYTHONUTF8 = "1"

# 3. Move to root
Set-Location C:\IOTEC

# 4. Check core module
if (!(Test-Path "C:\IOTEC\MODULES\common\helpers.py")) {
    Write-Host "ERRO: MODULE common não encontrado"
    exit 1
}

# 5. Run safe mode
python -X utf8 .\FROZEN\visible_core_router.py