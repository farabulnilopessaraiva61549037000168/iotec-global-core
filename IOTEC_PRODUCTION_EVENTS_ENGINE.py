import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC PRODUCTION EVENTS ENGINE
# REGISTRA PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DOS MOTORES
# ==========================================================

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_CONTROL_TOWER_LEDGER.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==========================================================
# TABELA DE EVENTOS
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS production_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    motor TEXT,

    event_type TEXT,

    production TEXT,

    reservoir TEXT,

    value_score INTEGER,

    notes TEXT

)

""")

conn.commit()

# ==========================================================
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE REGISTRO
# ==========================================================

def register_event(
    motor,
    event_type,
    production,
    reservoir,
    value_score=0,
    notes=""
):

    cur.execute("""

    INSERT INTO production_events (

        timestamp,
        motor,
        event_type,
        production,
        reservoir,
        value_score,
        notes

    )

    VALUES (

        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?

    )

    """,

    (

        str(datetime.now()),
        motor,
        event_type,
        production,
        reservoir,
        value_score,
        notes

    ))

    conn.commit()

# ==========================================================
# EVENTO DE TESTE
# ==========================================================

register_event(

    motor="SALES_BRAIN",

    event_type="SYSTEM_START",

    production="LEDGER ONLINE",

    reservoir="COMMERCIAL",

    value_score=10,

    notes="Primeiro evento registrado"

)

# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

print("")
print("===================================")
print("IOTEC PRODUCTION EVENTS ENGINE")
print("===================================")

total = cur.execute(
    "SELECT COUNT(*) FROM production_events"
).fetchone()[0]

print("")
print("EVENTOS REGISTRADOS:", total)

print("")
print("ULTIMOS EVENTOS")
print("")

rows = cur.execute("""

SELECT

    timestamp,
    motor,
    event_type,
    reservoir,
    value_score

FROM production_events

ORDER BY id DESC

LIMIT 10

""").fetchall()

for row in rows:
    pass

    print(row)

print("")
print("DATABASE:")
print(DB)
print("")
print("CONCLUIDO")

conn.close()




