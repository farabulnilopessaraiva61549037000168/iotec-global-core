import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = r"C:\IOTEC"

print("=" * 70)
print("X27 REAL LEAD MISSION")
print("=" * 70)
print()
print("DATA:", datetime.now())
print()

empresas = {}

BANCOS = [
    "enterprise.db",
    "IOTEC_ACCOUNT_REGISTRY.db",
    "iotec_global.db",
    "IOTEC_OPPORTUNITY.db",
    "IOTEC_PROPOSALS.db",
    "IOTEC_CONTRACTS.db"
]

for banco in BANCOS:

    caminho = Path(ROOT) / banco

    if not caminho.exists():
        continue

    try:

        conn = sqlite3.connect(caminho)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        if banco == "IOTEC_ACCOUNT_REGISTRY.db":

            cur.execute("""
            SELECT company, segment, city, state
            FROM accounts
            """)

            for row in cur.fetchall():

                empresa = row[0]

                empresas[empresa] = {
                    "origem": banco,
                    "segmento": row[1],
                    "cidade": row[2],
                    "estado": row[3]
                }

        elif banco == "iotec_global.db":

            cur.execute("""
            SELECT company, client, email, budget
            FROM leads
            """)

            for row in cur.fetchall():

                empresas[row[0]] = {
                    "origem": banco,
                    "contato": row[1],
                    "email": row[2],
                    "orcamento": row[3]
                }

        elif banco == "IOTEC_OPPORTUNITY.db":

            cur.execute("""
            SELECT organization,
                   product,
                   estimated_value,
                   probability
            FROM opportunities
            """)

            for row in cur.fetchall():

                empresas[row[0]] = {
                    "origem": banco,
                    "produto": row[1],
                    "valor": row[2],
                    "probabilidade": row[3]
                }

        elif banco == "IOTEC_PROPOSALS.db":

            cur.execute("""
            SELECT company,
                   product,
                   value,
                   status
            FROM proposals
            """)

            for row in cur.fetchall():

                empresas[row[0]] = {
                    "origem": banco,
                    "produto": row[1],
                    "valor": row[2],
                    "status": row[3]
                }

        elif banco == "IOTEC_CONTRACTS.db":

            cur.execute("""
            SELECT company,
                   product,
                   contract_value,
                   status
            FROM contracts
            """)

            for row in cur.fetchall():

                empresas[row[0]] = {
                    "origem": banco,
                    "produto": row[1],
                    "valor": row[2],
                    "status": row[3]
                }

        conn.close()

    except Exception as erro:
        print("ERRO:", banco, erro)

print("=" * 70)
print("EMPRESAS IDENTIFICADAS")
print("=" * 70)
print()

for empresa, dados in sorted(empresas.items()):

    print("EMPRESA :", empresa)

    for k, v in dados.items():
        print(f"{k.upper():12}: {v}")

    print("-" * 50)

print()
print("=" * 70)
print("MISSAO COMERCIAL")
print("=" * 70)

print("""
1. Eliminar registros de teste
2. Identificar empresas reais
3. Localizar telefone e email reais
4. Preparar proposta comercial
5. Registrar contato realizado
6. Registrar retorno
7. Converter em contrato
8. Registrar receita real
""")

print()
print("TOTAL EMPRESAS:", len(empresas))
print()
print("MISSAO LIBERADA")



