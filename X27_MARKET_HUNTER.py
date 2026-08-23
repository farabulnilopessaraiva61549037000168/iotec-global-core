import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

print("="*70)
print("X27 MARKET HUNTER")
print("="*70)

segmentos = [
    {
        "segmento":"INDUSTRIAS",
        "produto":"Analise de Dados Industriais",
        "ticket":5000
    },
    {
        "segmento":"PREFEITURAS",
        "produto":"Auditoria Operacional",
        "ticket":8000
    },
    {
        "segmento":"ESCOLAS",
        "produto":"Robotica Educacional",
        "ticket":3000
    },
    {
        "segmento":"COMERCIO",
        "produto":"Automacao Comercial",
        "ticket":2500
    }
]

potencial = 0

print()

for s in segmentos:

    valor = s["ticket"] * 10

    potencial += valor

    print(
        f'{s["segmento"]:<15}'
        f' {s["produto"]:<35}'
        f' R$ {valor:,.2f}'
    )

print()
print("="*70)

print("META 10 CLIENTES POR SEGMENTO")

print()

print(f"POTENCIAL TOTAL: R$ {potencial:,.2f}")

print()

print("MISSAO:")
print("1 Localizar empresas reais")
print("2 Encontrar telefone")
print("3 Enviar proposta")
print("4 Registrar retorno")
print("5 Fechar contrato")

print()
print("DATA:", datetime.now())



