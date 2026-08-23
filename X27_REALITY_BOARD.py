import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

TESTES = [
    "CLIENTE_EXEMPLO",
    "EMPRESA_EXEMPLO",
    "ESCOLA ALFA",
    "CLINICA VIDA",
    "PREFEITURA MODELO",
    "MARIA JULIA",
    "CORTEX SYSTEM"
]

print("="*70)
print("X27 REALITY BOARD")
print("="*70)

reais = 0
testes = 0

# CONTRATOS

db = ROOT / "IOTEC_CONTRACTS.db"

if db.exists():

    conn = sqlite3.connect(db)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    cur.execute("""
        SELECT company,
               product,
               contract_value,
               status
        FROM contracts
    """)

    contratos = cur.fetchall()

    print()
    print("CONTRATOS")
    print("-"*70)

    for c in contratos:

        nome = str(c[0]).upper()

        eh_teste = any(x in nome for x in TESTES)

        if eh_teste:
            testes += 1
            tipo = "TESTE"
        else:
            reais += 1
            tipo = "REAL"

        print(
            f"{tipo:8}"
            f"{c[0]:25}"
            f"R$ {c[2]:,.2f}"
        )

    conn.close()

print()
print("="*70)
print("VERDADE OPERACIONAL")
print("="*70)

print(f"CONTRATOS REAIS ...... {reais}")
print(f"CONTRATOS TESTE ...... {testes}")

print()

if reais == 0:

    print("ALERTA:")
    print("NAO EXISTEM CLIENTES REAIS")

    print()
    print("MISSAO:")
    print("CONQUISTAR O PRIMEIRO CLIENTE PAGANTE")

else:

    print("EXISTEM CLIENTES REAIS")
    print("EXPANDIR OPERACAO")

print()
print("="*70)



