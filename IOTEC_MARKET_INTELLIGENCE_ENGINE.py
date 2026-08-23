import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_MARKET_INTELLIGENCE.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS segments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    segment TEXT,
    pain TEXT,
    solution TEXT,
    priority INTEGER
)
""")

segments = [

    (
        str(datetime.now()),
        "EDUCACAO",
        "Baixa visibilidade de indicadores",
        "Auditoria Operacional",
        10
    ),

    (
        str(datetime.now()),
        "SAUDE",
        "Processos manuais e retrabalho",
        "Auditoria Inteligente",
        9
    ),

    (
        str(datetime.now()),
        "PREFEITURAS",
        "Falta de dashboards gerenciais",
        "GovTech Analytics",
        10
    ),

    (
        str(datetime.now()),
        "CONTABILIDADE",
        "Controle operacional",
        "Inteligencia Executiva",
        8
    ),

    (
        str(datetime.now()),
        "INDUSTRIA",
        "Gargalos produtivos",
        "Auditoria Operacional",
        9
    )

]

for row in segments:
    pass

    cur.execute("""
    INSERT INTO segments(
        created_at,
        segment,
        pain,
        solution,
        priority
    )
    VALUES(
        ?,?,?,?,?
    )
    """, row)

conn.commit()

print("")
print("===================================")
print("IOTEC MARKET INTELLIGENCE")
print("===================================")
print("")

for row in cur.execute("""
SELECT
    segment,
    solution,
    priority
FROM segments
ORDER BY priority DESC
"""):

    print(
        f"{row[0]} -> {row[1]} -> PRIORIDADE {row[2]}"
    )

print("")
print("DATABASE:")
print(DB)

conn.close()




