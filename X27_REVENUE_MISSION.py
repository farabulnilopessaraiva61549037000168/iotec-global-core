import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path

BASE = Path(r"C:\IOTEC")

print("=" * 60)
print("X27 REVENUE MISSION")
print("=" * 60)

tot_leads = 0
tot_opps = 0
tot_props = 0
tot_contracts = 0
valor_pipeline = 0.0
valor_contratos = 0.0

DBS = [
    "enterprise.db",
    "IOTEC_OPPORTUNITY.db",
    "IOTEC_PROPOSALS.db",
    "IOTEC_CONTRACTS.db"
]

for db_name in DBS:

    db = BASE / db_name

    if not db.exists():
        continue

    try:

        conn = sqlite3.connect(db)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table'"
        )

        tabelas = [x[0] for x in cur.fetchall()]

        if "leads" in tabelas:

            cur.execute("SELECT COUNT(*) FROM leads")
            tot_leads += cur.fetchone()[0]

        if "opportunities" in tabelas:

            cur.execute(
                "SELECT COUNT(*), "
                "COALESCE(SUM(value),0) "
                "FROM opportunities"
            )

            qtd, valor = cur.fetchone()

            tot_opps += qtd
            valor_pipeline += valor

        if "proposals" in tabelas:

            cur.execute(
                "SELECT COUNT(*), "
                "COALESCE(SUM(value),0) "
                "FROM proposals"
            )

            qtd, valor = cur.fetchone()

            tot_props += qtd
            valor_pipeline += valor

        if "contracts" in tabelas:

            cur.execute(
                "SELECT COUNT(*), "
                "COALESCE(SUM(value),0) "
                "FROM contracts"
            )

            qtd, valor = cur.fetchone()

            tot_contracts += qtd
            valor_contratos += valor

        conn.close()

    except Exception as erro:

        print("ERRO:", db_name)
        print(erro)

print()
print("=" * 60)
print("MISSAO COMERCIAL")
print("=" * 60)

print(f"LEADS................ {tot_leads}")
print(f"OPORTUNIDADES........ {tot_opps}")
print(f"PROPOSTAS............ {tot_props}")
print(f"CONTRATOS............ {tot_contracts}")

print()
print(f"PIPELINE............. R$ {valor_pipeline:,.2f}")
print(f"CONTRATADO........... R$ {valor_contratos:,.2f}")

print()
print("=" * 60)

if valor_contratos > 0:
    print("EXISTEM CONTRATOS CADASTRADOS")
else:
    print("NAO EXISTEM CONTRATOS REGISTRADOS")

if tot_leads == 0:
    print("SEM LEADS")
else:
    print("EXISTEM LEADS PARA TRABALHAR")

print("=" * 60)



