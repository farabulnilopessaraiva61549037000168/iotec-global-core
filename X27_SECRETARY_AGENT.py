import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS real_leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    company TEXT,
    contact TEXT,
    email TEXT,
    phone TEXT,
    city TEXT,
    segment TEXT,
    demand TEXT,
    score INTEGER,
    status TEXT
)
""")

conn.commit()

print("=" * 70)
print("X27 SECRETARY AGENT")
print("=" * 70)
print()

oportunidades = [

    {
        "company": "INDUSTRIA ALFA",
        "city": "Fortaleza",
        "segment": "INDUSTRIA",
        "demand": "Analise de Dados Industriais",
        "score": 95
    },

    {
        "company": "GRUPO BETA",
        "city": "Fortaleza",
        "segment": "LOGISTICA",
        "demand": "Automacao Operacional",
        "score": 88
    },

    {
        "company": "COMERCIAL GAMMA",
        "city": "Quixada",
        "segment": "COMERCIO",
        "demand": "Dashboard Executivo",
        "score": 80
    }

]

novos = 0

for op in oportunidades:

    cur.execute("""
    SELECT COUNT(*)
    FROM real_leads
    WHERE company = ?
    """, (op["company"],))

    existe = cur.fetchone()[0]

    if existe:
        continue

    cur.execute("""
    INSERT INTO real_leads
    (
        created_at,
        company,
        contact,
        email,
        phone,
        city,
        segment,
        demand,
        score,
        status
    )
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """,
    (
        str(datetime.now()),
        op["company"],
        "",
        "",
        "",
        op["city"],
        op["segment"],
        op["demand"],
        op["score"],
        "DESCOBERTO"
    ))

    novos += 1

conn.commit()

print("OPORTUNIDADES INSERIDAS :", novos)
print()

cur.execute("""
SELECT
company,
city,
segment,
demand,
score,
status
FROM real_leads
ORDER BY score DESC
LIMIT 20
""")

for linha in cur.fetchall():

    print(
        f"{linha[0]:25} "
        f"{linha[1]:12} "
        f"{linha[2]:15} "
        f"{linha[4]:3} "
        f"{linha[5]}"
    )

conn.close()

print()
print("=" * 70)
print("MISSAO DA SECRETARIA")
print("=" * 70)

print("""
1 - Descobrir oportunidades
2 - Registrar CRM
3 - Qualificar
4 - Preparar proposta
5 - Aguardar aprovacao
6 - Registrar retorno
7 - Converter em contrato
""")



