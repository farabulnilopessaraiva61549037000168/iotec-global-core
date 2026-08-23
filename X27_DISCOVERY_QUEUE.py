import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("=" * 70)
print("X27 DISCOVERY QUEUE")
print("=" * 70)

segmentos = [
    "INDUSTRIA",
    "LOGISTICA",
    "ENERGIA"
]

for segmento in segmentos:

    cur.execute("""
    SELECT COUNT(*)
    FROM real_leads
    WHERE segment=?
    """, (segmento,))

    encontrados = cur.fetchone()[0]

    meta = {
        "INDUSTRIA": 50,
        "LOGISTICA": 30,
        "ENERGIA": 20
    }[segmento]

    faltam = meta - encontrados

    print()
    print("SEGMENTO :", segmento)
    print("META     :", meta)
    print("ATUAL    :", encontrados)
    print("FALTAM   :", faltam)

print()
print("=" * 70)
print("MISSAO DA SECRETARIA")
print("=" * 70)

print("""
INDUSTRIA -> localizar 49 empresas
LOGISTICA -> localizar 29 empresas
ENERGIA -> localizar 20 empresas

Objetivo:
alimentar o banco IOTEC_REAL_LEADS.db
""")

conn.close()



