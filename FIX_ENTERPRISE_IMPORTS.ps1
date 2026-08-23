$arquivo = "C:\IOTEC\enterprise\source_engine.py"

if (!(Test-Path $arquivo)) {
    Write-Host "Arquivo não encontrado."
    exit
}

$codigo = Get-Content $arquivo -Raw -Encoding UTF8

if ($codigo -notmatch "import sys") {

$imports = @'
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

'@

    $codigo = $imports + $codigo

}

Set-Content $arquivo $codigo -Encoding UTF8

Write-Host ""
Write-Host "====================================="
Write-Host "IMPORTS CORRIGIDOS"
Write-Host "====================================="
Write-Host ""
Write-Host "Execute:"
Write-Host "python C:\IOTEC\enterprise\source_engine.py"