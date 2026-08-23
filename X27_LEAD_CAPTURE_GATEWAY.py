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
    segment TEXT,
    demand TEXT,
    status TEXT
)
""")

conn.commit()

print("=" * 70)
print("IOTEC REAL LEAD ENTRY")
print("=" * 70)
print()

while True:

    empresa = input("Empresa (ENTER para sair): ").strip()

    if empresa == "":
        break

    contato = input("Contato: ").strip()
    email = input("Email: ").strip()
    telefone = input("Telefone: ").strip()
    segmento = input("Segmento: ").strip()
    demanda = input("Necessidade: ").strip()

    cur.execute("""
    INSERT INTO real_leads
    (
        created_at,
        company,
        contact,
        email,
        phone,
        segment,
        demand,
        status
    )
    VALUES (?,?,?,?,?,?,?,?)
    """,
    (
        str(datetime.now()),
        empresa,
        contato,
        email,
        telefone,
        segmento,
        demanda,
        "NOVO"
    ))

    conn.commit()

    print()
    print("LEAD REGISTRADO")
    print()

conn.close()

print()
print("=" * 70)
print("FINALIZADO")
print("=" * 70)



