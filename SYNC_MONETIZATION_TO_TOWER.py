import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
TOWER_DB = r"C:\IOTEC_OMEGA_X\CORE\runtime\iotec.db"

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
    l.email,
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

print("")
print("=" * 50)
print("IOTEC MONETIZATION SYNC")
print("=" * 50)
print(f"Oportunidades sincronizadas: {sincronizados}")
print("=" * 50)
print("")




