import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime
import sqlite3
import os

print("=" * 70)
print("X27 MISSION BOARD")
print("=" * 70)
print()

print("DATA:", datetime.now())
print()

ROOT = r"C:\IOTEC"

pipeline = 0
propostas = 0
contratos = 0
oportunidades = 0

# =====================================================
# OPORTUNIDADES
# =====================================================

try:

    db = os.path.join(ROOT, "IOTEC_OPPORTUNITY.db")

    conn = sqlite3.connect(db)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    cur.execute("""
        SELECT COUNT(*),
               COALESCE(SUM(estimated_value),0)
        FROM opportunities
    """)

    oportunidades, valor = cur.fetchone()

    pipeline += valor

    conn.close()

except:
    pass

# =====================================================
# PROPOSTAS
# =====================================================

try:

    db = os.path.join(ROOT, "IOTEC_PROPOSALS.db")

    conn = sqlite3.connect(db)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    cur.execute("""
        SELECT COUNT(*),
               COALESCE(SUM(value),0)
        FROM proposals
    """)

    propostas, valor = cur.fetchone()

    pipeline += valor

    conn.close()

except:
    pass

# =====================================================
# CONTRATOS
# =====================================================

try:

    db = os.path.join(ROOT, "IOTEC_CONTRACTS.db")

    conn = sqlite3.connect(db)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    cur.execute("""
        SELECT COUNT(*),
               COALESCE(SUM(contract_value),0)
        FROM contracts
    """)

    contratos, valor = cur.fetchone()

    contratado = valor

    conn.close()

except:

    contratado = 0

# =====================================================
# PAINEL
# =====================================================

print("=" * 70)
print("MISSAO DO DIA")
print("=" * 70)
print()

print("[ ] Localizar 10 empresas reais")
print("[ ] Encontrar telefone")
print("[ ] Encontrar email")
print("[ ] Registrar no CRM")
print("[ ] Enviar proposta")
print("[ ] Registrar retorno")
print("[ ] Agendar reuniao")
print("[ ] Fechar contrato")
print()

print("=" * 70)
print("FUNIL COMERCIAL")
print("=" * 70)
print()

print(f"OPORTUNIDADES ......... {oportunidades}")
print(f"PROPOSTAS ............. {propostas}")
print(f"CONTRATOS ............. {contratos}")
print()

print(f"PIPELINE .............. R$ {pipeline:,.2f}")
print(f"CONTRATADO ............ R$ {contratado:,.2f}")
print()

print("=" * 70)
print("META DA SEMANA")
print("=" * 70)
print()

print("1 CLIENTE REAL")
print("1 CONTRATO REAL")
print("1 PAGAMENTO REAL")
print()

print("=" * 70)
print("PRIORIDADE")
print("=" * 70)
print()

print("1 - PREFEITURAS")
print("2 - ESCOLAS")
print("3 - INDUSTRIAS")
print("4 - COMERCIO")
print()

print("=" * 70)
print("STATUS")
print("=" * 70)

if contratado > 0:
    print("EXISTEM CONTRATOS REGISTRADOS")
else:
    print("BUSCAR PRIMEIRO CONTRATO")

print()
print("MISSAO LIBERADA")
print("=" * 70)



