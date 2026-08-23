import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)

cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

leads = cur.execute("""

SELECT id, company
FROM leads

""").fetchall()

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
            2500,
            "PENDENTE",
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

        ))

conn.commit()

conn.close()

print("OPORTUNIDADES SINCRONIZADAS")




