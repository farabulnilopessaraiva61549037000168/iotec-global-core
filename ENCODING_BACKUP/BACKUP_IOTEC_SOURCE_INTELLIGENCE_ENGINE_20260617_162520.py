import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
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
    pass

    print("-", fonte)

print("")
print("NUCLEO DE FONTES ATIVO")


