import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS automation_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    execution_date TEXT,

    analyzed_companies INTEGER,

    opportunities INTEGER,

    proposals INTEGER,

    active_clients INTEGER,

    potential_revenue REAL

)

""")

# empresas

try:
    empresas = cur.execute("""
    SELECT COUNT(*)
    FROM commercial_opportunities
    """).fetchone()[0]
except:
    empresas = 0

# oportunidades

try:
    oportunidades = cur.execute("""
    SELECT COUNT(*)
    FROM commercial_opportunities
    """).fetchone()[0]
except:
    oportunidades = 0

# propostas

try:
    propostas = cur.execute("""
    SELECT COUNT(*)
    FROM commercial_opportunities
    WHERE status='PROPOSTA_ENVIADA'
    """).fetchone()[0]
except:
    propostas = 0

# clientes ativos

try:
    clientes = cur.execute("""
    SELECT COUNT(*)
    FROM pipeline
    WHERE status='CLIENTE_ATIVO'
    """).fetchone()[0]
except:
    clientes = 0

# receita potencial

try:
    receita = cur.execute("""
    SELECT IFNULL(SUM(estimated_value),0)
    FROM commercial_opportunities
    """).fetchone()[0]
except:
    receita = 0

cur.execute("""

INSERT INTO automation_history(

    execution_date,
    analyzed_companies,
    opportunities,
    proposals,
    active_clients,
    potential_revenue

)

VALUES(

    ?,?,?,?,?,?

)

""",(

    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    empresas,
    oportunidades,
    propostas,
    clientes,
    receita

))

conn.commit()

total = cur.execute("""
SELECT COUNT(*)
FROM automation_history
""").fetchone()[0]

conn.close()

print("")
print("===================================")
print("AUTOMATION HISTORY ENGINE")
print("===================================")
print("")
print("REGISTRO SALVO")
print("")
print("EMPRESAS:", empresas)
print("OPORTUNIDADES:", oportunidades)
print("PROPOSTAS:", propostas)
print("CLIENTES:", clientes)
print(f"RECEITA: R$ {receita:,.2f}")
print("")
print("TOTAL DE SNAPSHOTS:", total)
print("")


