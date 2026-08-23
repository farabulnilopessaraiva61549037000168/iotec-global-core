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
CREATE TABLE IF NOT EXISTS real_leads(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    company TEXT,
    city TEXT,
    segment TEXT,
    contact_name TEXT,
    phone TEXT,
    email TEXT,
    source TEXT,
    status TEXT,
    estimated_value REAL,
    notes TEXT
)
""")

conn.commit()

print("=" * 70)
print("IOTEC REAL LEADS DATABASE")
print("=" * 70)

print()
print("BANCO CRIADO:")
print(DB)

print()
print("STATUS VALIDOS:")
print("NOVO")
print("CONTATADO")
print("REUNIAO")
print("PROPOSTA")
print("NEGOCIACAO")
print("FECHADO")
print("PERDIDO")

print()
print("OBJETIVO:")
print("ARMAZENAR APENAS CLIENTES REAIS")

conn.close()



