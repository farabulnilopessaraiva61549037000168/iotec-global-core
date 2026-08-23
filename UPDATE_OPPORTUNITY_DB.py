import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("PRAGMA table_info(opportunities)")
cols = [c[1] for c in cur.fetchall()]

novas = [
    ("updated_at","TEXT"),
    ("country","TEXT"),
    ("city","TEXT"),
    ("contact","TEXT"),
    ("email","TEXT"),
    ("phone","TEXT"),
    ("website","TEXT"),
    ("campaign","TEXT"),
    ("lead_source","TEXT"),
    ("budget","REAL"),
    ("market_score","INTEGER"),
    ("priority","TEXT"),
    ("urgency","TEXT"),
    ("decision_maker","TEXT"),
    ("assigned_operator","TEXT"),
    ("recommended_action","TEXT"),
    ("notes","TEXT")
]

for nome, tipo in novas:
    if nome not in cols:
        print(f"Criando coluna: {nome}")
        cur.execute(f"ALTER TABLE opportunities ADD COLUMN {nome} {tipo}")

conn.commit()

print("\nBanco atualizado com sucesso!")

conn.close()



