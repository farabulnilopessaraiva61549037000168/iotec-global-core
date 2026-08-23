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

leads = [

    (
        "EMPRESA ALFA INDUSTRIAL",
        "Fortaleza",
        "INDUSTRIA",
        "",
        "",
        "",
        "X27_SEED",
        "DESCOBERTO",
        50000,
        "Analise de Dados Industriais"
    ),

    (
        "GRUPO BETA LOGISTICA",
        "Fortaleza",
        "LOGISTICA",
        "",
        "",
        "",
        "X27_SEED",
        "DESCOBERTO",
        25000,
        "Automacao Operacional"
    ),

    (
        "COMERCIAL GAMMA",
        "Quixada",
        "COMERCIO",
        "",
        "",
        "",
        "X27_SEED",
        "DESCOBERTO",
        15000,
        "Dashboard Executivo"
    )

]

for l in leads:

    cur.execute("""
    INSERT INTO real_leads
    (
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
    """,
    (
        str(datetime.now()),
        *l
    ))

conn.commit()

print("LEADS INSERIDOS:", len(leads))

conn.close()



