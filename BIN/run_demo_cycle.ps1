$ErrorActionPreference = "Stop"
$Base = Split-Path $PSScriptRoot -Parent
$Py = Join-Path $Base "CORE\runtime\run_demo_cycle.py"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python não encontrado no PATH." }
python $Py
exit $LASTEXITCODE
