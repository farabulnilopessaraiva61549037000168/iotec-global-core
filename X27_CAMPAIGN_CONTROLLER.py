import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_CAMPAIGNS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    campaign_name TEXT,
    segment TEXT,
    target_companies INTEGER,
    target_proposals INTEGER,
    target_contracts INTEGER,
    target_revenue REAL,
    status TEXT
)
""")

conn.commit()

campanhas = [

    (
        str(datetime.now()),
        "CAMPANHA_IND_BRASIL_001",
        "INDUSTRIA",
        50,
        10,
        2,
        30000,
        "ATIVA"
    ),

    (
        str(datetime.now()),
        "CAMPANHA_LOGISTICA_BRASIL_001",
        "LOGISTICA",
        30,
        6,
        1,
        15000,
        "ATIVA"
    ),

    (
        str(datetime.now()),
        "CAMPANHA_ENERGIA_BRASIL_001",
        "ENERGIA",
        20,
        4,
        1,
        25000,
        "ATIVA"
    )

]

for campanha in campanhas:

    cur.execute("""
    INSERT INTO campaigns
    (
        created_at,
        campaign_name,
        segment,
        target_companies,
        target_proposals,
        target_contracts,
        target_revenue,
        status
    )
    VALUES (?,?,?,?,?,?,?,?)
    """, campanha)

conn.commit()

print("=" * 70)
print("X27 CAMPAIGN CONTROLLER")
print("=" * 70)
print()

cur.execute("""
SELECT
campaign_name,
segment,
target_companies,
target_revenue,
status
FROM campaigns
ORDER BY id DESC
""")

for row in cur.fetchall():

    print("CAMPANHA :", row[0])
    print("SEGMENTO :", row[1])
    print("EMPRESAS :", row[2])
    print("META R$  :", f"{row[3]:,.2f}")
    print("STATUS   :", row[4])
    print("-" * 50)

conn.close()

print()
print("=" * 70)
print("MISSAO LIBERADA")
print("=" * 70)

print("""
O nÃƒÂºcleo passa a operar por campanhas.

ETAPA 1
Localizar empresas

ETAPA 2
Registrar leads

ETAPA 3
Qualificar

ETAPA 4
Proposta

ETAPA 5
Contrato

ETAPA 6
Receita
""")



