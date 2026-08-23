import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS pipeline(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    opportunity_id INTEGER,

    status TEXT,

    report_sent INTEGER DEFAULT 0,

    meeting_scheduled INTEGER DEFAULT 0,

    proposal_sent INTEGER DEFAULT 0,

    proposal_value REAL DEFAULT 0,

    payment_received INTEGER DEFAULT 0,

    observations TEXT,

    updated_at TEXT

)

""")

conn.commit()

# cria pipeline para oportunidades existentes

ops = cur.execute("""

SELECT id
FROM opportunities

""").fetchall()

for op in ops:
    pass

    op_id = op[0]

    exists = cur.execute("""

    SELECT COUNT(*)
    FROM pipeline
    WHERE opportunity_id=?

    """,(op_id,)).fetchone()[0]

    if exists == 0:
        pass

        cur.execute("""

        INSERT INTO pipeline(

            opportunity_id,
            status,
            updated_at

        )

        VALUES(?,?,datetime('now'))

        """,(

            op_id,
            "ANALISE"

        ))

conn.commit()

conn.close()

print("PIPELINE B2B CRIADO")


