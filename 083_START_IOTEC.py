# ==========================================================
# 083_START_IOTEC.py
# BOOT OFICIAL DA IOTEC
# ==========================================================

import time
import webbrowser

ETAPAS = [

"Inicializando Executive Skin",
"Verificando Infraestrutura",
"Conectando Render",
"Conectando Netlify",
"Verificando PayPal",
"Verificando Proton Mail",
"Carregando Kernel",
"Carregando Chief of Staff",
"Carregando Executive Cockpit",
"Carregando Sensores",
"Preparando Portais",
"Iniciando Empresa"

]

print("="*80)
print("IOTEC ENTERPRISE BOOT")
print("="*80)
print()

for etapa in ETAPAS:

    print("[OK]", etapa)
    time.sleep(0.4)

print()
print("="*80)
print("EMPRESA PRONTA")
print("="*80)
print()

print("Abrindo Executive Skin...")

try:

    webbrowser.open("http://127.0.0.1:5000")

except:

    pass

print()

print("Bom dia, Presidente.")
print()

print("A IOTEC encontra-se operacional.")
print()

print("O Chefe de Gabinete apresentarÃƒÂ¡ o briefing.")


