Write-Host ""
Write-Host "==================================="
Write-Host "IOTEC AUTO RESTORE"
Write-Host "==================================="

$arquivo =
"C:\IOTEC\IOTEC_SOURCE_INTELLIGENCE_ENGINE.py"

if (-not (Test-Path $arquivo))
{
    Write-Host ""
    Write-Host "ARQUIVO AUSENTE"
    Write-Host $arquivo

    @'
from datetime import datetime

print("")
print("===================================")
print("IOTEC SOURCE INTELLIGENCE ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print("CATALOGAR FONTES DE INTELIGENCIA")

fontes = [

    "INMET",
    "FUNCEME",
    "NASA",
    "NOAA",
    "IBGE",
    "IPEA",
    "BACEN",
    "CONAB",
    "EMBRAPA",
    "DATASUS"
]

print("")
print("FONTES:")

for fonte in fontes:

    print("-", fonte)

print("")
print("NUCLEO DE FONTES ATIVO")
'@ |
    Set-Content `
    $arquivo `
    -Encoding UTF8

    Write-Host ""
    Write-Host "ARQUIVO RECRIADO"
}
else
{
    Write-Host ""
    Write-Host "ARQUIVO JA EXISTE"
}

Write-Host ""
Write-Host "FIM"