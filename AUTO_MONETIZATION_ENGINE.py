import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import time
from datetime import datetime

CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
TOWER_DB = r"C:\IOTEC_OMEGA_X\CORE\runtime\iotec.db"

def promote_leads():
    pass

    conn = sqlite3.connect(CRM_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    leads = cur.execute("""
        SELECT id
        FROM leads
    """).fetchall()

    novos = 0

    for lead in leads:
        pass

        lead_id = lead[0]

        existe = cur.execute("""
            SELECT COUNT(*)
            FROM opportunities
            WHERE lead_id=?
        """,(lead_id,)).fetchone()[0]

        if existe == 0:
            pass

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
                "ANALISE",
                2500.0,
                "PENDENTE",
                datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            ))

            novos += 1

    conn.commit()
    conn.close()

    return novos

def sync_tower():
    pass

    crm = sqlite3.connect(CRM_DB)
    crm.row_factory = sqlite3.Row

    tower = sqlite3.connect(TOWER_DB)

    crm_cur = crm.cursor()
    tower_cur = tower.cursor()

    oportunidades = crm_cur.execute("""

        SELECT
            o.id,
            l.company,
            l.sector,
            o.proposal_value,
            o.payment_status

        FROM opportunities o

        JOIN leads l
        ON l.id = o.lead_id

    """).fetchall()

    sincronizados = 0

    for op in oportunidades:
        pass

        order_id = f"CRM-{op['id']}"

        existe = tower_cur.execute("""
            SELECT COUNT(*)
            FROM orders
            WHERE id=?
        """,(order_id,)).fetchone()[0]

        if existe == 0:
            pass

            tower_cur.execute("""
                INSERT INTO orders
                VALUES(?,?,?,?,?,?,?,?)
            """,(

                order_id,
                op["company"],
                "BRAZIL",
                op["sector"],
                "OPPORTUNITY",
                float(op["proposal_value"]),
                op["payment_status"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ))

            sincronizados += 1

    tower.commit()

    crm.close()
    tower.close()

    return sincronizados

print("=" * 60)
print("IOTEC AUTO MONETIZATION ENGINE")
print("=" * 60)

while True:
    pass

    novos_leads = promote_leads()

    novas_orders = sync_tower()

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"Leads promovidos={novos_leads} | "
        f"Orders sincronizadas={novas_orders}"
    )

    time.sleep(30)




