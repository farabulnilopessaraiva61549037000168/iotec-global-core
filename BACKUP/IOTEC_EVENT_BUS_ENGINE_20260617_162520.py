import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC EVENT BUS ENGINE
# BARRAMENTO CENTRAL DE EVENTOS
# ==========================================================

import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==========================================================
# EVENTS
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    source TEXT,

    event_type TEXT,

    payload TEXT,

    processed INTEGER DEFAULT 0

)

""")

conn.commit()

# ==========================================================
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ==========================================================

def publish_event(
    source,
    event_type,
    payload
):

    cur.execute("""

    INSERT INTO events (

        timestamp,
        source,
        event_type,
        payload

    )

    VALUES (

        ?,?,?,?

    )

    """,

    (

        str(datetime.now()),
        source,
        event_type,
        json.dumps(payload)

    ))

    conn.commit()

def pending_events():
    pass

    return cur.execute("""

    SELECT

        id,
        source,
        event_type,
        payload

    FROM events

    WHERE processed=0

    ORDER BY id

    """).fetchall()

def mark_processed(event_id):
    pass

    cur.execute("""

    UPDATE events

    SET processed=1

    WHERE id=?

    """,

    (event_id,))

    conn.commit()

# ==========================================================
# TESTE INICIAL
# ==========================================================

exists = cur.execute("""

SELECT COUNT(*)

FROM events

""").fetchone()[0]

if exists == 0:
    pass

    publish_event(

        "SYSTEM",

        "BOOT",

        {

            "message":
            "EVENT BUS ONLINE"

        }

    )

# ==========================================================
# DASHBOARD
# ==========================================================

total = cur.execute("""

SELECT COUNT(*)

FROM events

""").fetchone()[0]

pending = cur.execute("""

SELECT COUNT(*)

FROM events

WHERE processed=0

""").fetchone()[0]

print("")
print("===================================")
print("IOTEC EVENT BUS ENGINE")
print("===================================")

print("")
print("TOTAL EVENTS:", total)

print(
    "PENDING EVENTS:",
    pending
)

print("")
print("DATABASE:")
print(DB)

print("")
print("CONCLUIDO")

conn.close()


