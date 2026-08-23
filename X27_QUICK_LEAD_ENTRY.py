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

while True:

    print()
    empresa = input("Empresa (ENTER para sair): ").strip()

    if empresa == "":
        break

    cidade = input("Cidade: ").strip()
    segmento = input("Segmento: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    cur.execute("""
    INSERT INTO real_leads(
        created_at,
        company,
        city,
        segment,
        contact_name,
        phone,
        email,
        source,
        status,
        estimated_value,
        notes
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """,(
        str(datetime.now()),
        empresa,
        cidade,
        segmento,
        "",
        telefone,
        email,
        "MANUAL",
        "NOVO",
        0,
        ""
    ))

    conn.commit()

    print("LEAD SALVO")

conn.close()

print()
print("CAPTURA FINALIZADA")



