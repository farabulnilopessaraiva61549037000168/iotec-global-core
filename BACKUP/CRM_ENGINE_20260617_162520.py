import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# CRM_ENGINE.py

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

def init_crm():
    pass

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS opportunities(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        lead_id INTEGER,

        stage TEXT,

        proposal_value REAL,

        payment_status TEXT,

        created TEXT

    )
    """)

    conn.commit()
    conn.close()

def create_opportunity(lead_id, value):
    pass

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO opportunities(
        lead_id,
        stage,
        proposal_value,
        payment_status,
        created
    )
    VALUES(?,?,?,?,?)
    """,(
        lead_id,
        "PROPOSTA_ENVIADA",
        value,
        "PENDENTE",
        datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ))

    conn.commit()
    conn.close()

def dashboard():
    pass

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    leads = cur.execute(
        "SELECT COUNT(*) FROM leads"
    ).fetchone()[0]

    propostas = cur.execute(
        "SELECT COUNT(*) FROM opportunities"
    ).fetchone()[0]

    receita_prevista = cur.execute(
        "SELECT COALESCE(SUM(proposal_value),0) FROM opportunities"
    ).fetchone()[0]

    receita_recebida = cur.execute("""
        SELECT COALESCE(SUM(proposal_value),0)
        FROM opportunities
        WHERE payment_status='RECEBIDO'
    """).fetchone()[0]

    conn.close()

    return {

        "leads": leads,
        "propostas": propostas,
        "receita_prevista": receita_prevista,
        "receita_recebida": receita_recebida

    }

if __name__ == "__main__":
    pass

    init_crm()

    print(
        dashboard()
    )


