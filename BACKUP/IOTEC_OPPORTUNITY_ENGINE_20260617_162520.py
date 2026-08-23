import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS opportunities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    organization TEXT,
    segment TEXT,
    product TEXT,
    estimated_value REAL,
    probability INTEGER,
    status TEXT
)
""")

opportunities = [

    (
        str(datetime.now()),
        "Prefeitura Modelo",
        "PREFEITURAS",
        "GovTech Analytics",
        15000.00,
        70,
        "PROSPECCAO"
    ),

    (
        str(datetime.now()),
        "Escola Alfa",
        "EDUCACAO",
        "Auditoria Operacional",
        5000.00,
        60,
        "PROSPECCAO"
    ),

    (
        str(datetime.now()),
        "Clinica Vida",
        "SAUDE",
        "Auditoria Inteligente",
        8000.00,
        50,
        "QUALIFICACAO"
    )

]

for row in opportunities:
    pass

    cur.execute("""
    INSERT INTO opportunities(
        created_at,
        organization,
        segment,
        product,
        estimated_value,
        probability,
        status
    )
    VALUES(
        ?,?,?,?,?,?,?
    )
    """, row)

conn.commit()

print("")
print("===================================")
print("IOTEC OPPORTUNITY ENGINE")
print("===================================")
print("")

pipeline = 0

for row in cur.execute("""

SELECT

    organization,
    segment,
    product,
    estimated_value,
    probability,
    status

FROM opportunities

ORDER BY estimated_value DESC

"""):

    weighted = row[3] * (row[4] / 100)
    pipeline += weighted

    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"{row[2]} | "
        f"R$ {row[3]:,.2f} | "
        f"{row[4]}% | "
        f"{row[5]}"
    )

print("")
print(f"PIPELINE PONDERADO: R$ {pipeline:,.2f}")

conn.close()


