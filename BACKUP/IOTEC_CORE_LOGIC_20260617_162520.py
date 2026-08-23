import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

CORE_RULES = {
    "modo_operacao": "REAL",
    "simulacao": False,
    "monitoramento": "24x7",
    "objetivo_principal": "MONETIZACAO",
    "objetivo_secundario": "INTELIGENCIA_DE_MERCADO"
}

CORE_STATES = {
    "captacao": True,
    "analise": True,
    "prospeccao": True,
    "vendas": True,
    "entrega": True
}

MISSIONS = [
    "LOCALIZAR_CLIENTES",
    "IDENTIFICAR_GARGALOS",
    "CRIAR_PRODUTOS",
    "GERAR_RECEITA",
    "ATINGIR_META"
]

SENSORES = {
    "formularios": True,
    "sites": True,
    "render": True,
    "netlify": True,
    "war_room": True,
    "financeiro": True
}

print("")
print("===================================")
print("IOTEC CORE LOGIC")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MODO:")
print(CORE_RULES["modo_operacao"])

print("")
print("OBJETIVO:")
print(CORE_RULES["objetivo_principal"])

print("")
print("MISSOES:")

for item in MISSIONS:
    print("-", item)

print("")
print("SENSORES:")

for sensor, status in SENSORES.items():
    pass

    estado = "ONLINE" if status else "OFFLINE"

    print(
        sensor.upper(),
        "->",
        estado
    )

print("")
print("ESTADOS:")

for estado, ativo in CORE_STATES.items():
    pass

    print(
        estado.upper(),
        "->",
        ativo
    )

print("")
print("NUCLEO OPERACIONAL ATIVO")



