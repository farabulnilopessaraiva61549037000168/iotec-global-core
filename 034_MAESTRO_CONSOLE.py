# ==============================================================================
# IOTEC
# 034_MAESTRO_CONSOLE.py
#
# Centro de Comando Operacional
#
# ==============================================================================

import os
import time
from datetime import datetime

os.system("cls")

inicio = time.time()

SERVICOS = {

    "CORE OS"      : "ONLINE",
    "LOGGER"       : "ONLINE",
    "DATABASE"     : "ONLINE",
    "EVENT BUS"    : "ONLINE",
    "CONNECTORS"   : "ONLINE",
    "CRM"          : "ONLINE",
    "LEADS"        : "ONLINE",
    "EMAIL"        : "ONLINE",
    "PAYPAL"       : "ONLINE",
    "IA"           : "ONLINE",
    "DASHBOARD"    : "ONLINE"

}

print("="*90)
print("IOTEC MAESTRO CONSOLE")
print("="*90)

print()

print("Hora...............", datetime.now())

print("Kernel............. ONLINE")

print("Estado............. OPERACIONAL")

print()

print("-"*90)

for nome, status in SERVICOS.items():

    print(f"{nome:<25}{status}")

print("-"*90)

print()

print("CPU.................. Monitorando")

print("RAM.................. Monitorando")

print("Eventos.............. 0")

print("Leads................ 0")

print("Clientes............. 0")

print("RelatÃ³rios........... 0")

print()

print("="*90)

print("Tempo Ligado:", round(time.time()-inicio,2),"seg")

print("="*90)

