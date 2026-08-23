param(
    [int]$Cycles = 1,
    [switch]$Describe
)

$ErrorActionPreference = "Stop"

$Base = Split-Path $PSScriptRoot -Parent
$PyFile = Join-Path $Base "CORE\nucleus\iotec_nucleus.py"

if (-not (Test-Path $PyFile)) {
    throw "Núcleo Python não encontrado em: $PyFile"
}

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    throw "Python não encontrado no PATH."
}

if ($Describe) {
    python $PyFile --describe
    exit $LASTEXITCODE
}

python $PyFile --cycles $Cycles
exit $LASTEXITCODE
