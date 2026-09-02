# ==============================================================================
# AUTOLIMPEZA AUTOMÁTICA - IOTEC CORE
# ==============================================================================
Get-Process node, python -ErrorAction SilentlyContinue | Where-Object { $_.Id -ne $PID } | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 1

# Garante a existência do diretório de logs
if (-not (Test-Path "C:\IOTEC_CORE\logs")) {
    New-Item -ItemType Directory -Path "C:\IOTEC_CORE\logs" -Force | Out-Null
}

# Executa o Node redirecionando logs de saída e erros para o app.log
node C:\IOTEC\node_jonas_core.js >> C:\IOTEC_CORE\logs\app.log 2>&1


# ------------------------------------------------------------------------------
# ROTINA DO NÚCLEO DE INTELIGÊNCIA & VIRTUAL INVESTOR ROOM
# ------------------------------------------------------------------------------
python C:\IOTEC\023_IOTEC_INVESTOR_HUNTER.py >> C:\IOTEC_CORE\logs\app.log 2>&1
