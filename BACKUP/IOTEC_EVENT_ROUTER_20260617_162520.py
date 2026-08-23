import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC EVENT ROUTER
# ==========================================================

import sqlite3
import json

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

events = cur.execute("""

SELECT

    id,
    source,
    event_type,
    payload

FROM events

WHERE processed = 0

ORDER BY id

""").fetchall()

print("")
print("===================================")
print("IOTEC EVENT ROUTER")
print("===================================")

processed = 0

for event in events:
    pass

    event_id = event[0]
    source = event[1]
    event_type = event[2]
    payload = event[3]

    destination = "UNKNOWN"

    if event_type == "LEAD":
        pass

        destination = "MISSION_LEDGER"

    elif event_type == "PROPOSAL":
        pass

        destination = "SALES_BRAIN"

    elif event_type == "MEETING":
        pass

        destination = "MISSION_LEDGER"

    elif event_type == "PAYMENT":
        pass

        destination = "REVENUE_CENTER"

    elif event_type == "CLIENT":
        pass

        destination = "EXECUTIVE_COCKPIT"

    elif event_type == "BOOT":
        pass

        destination = "CONTROL_TOWER"

    cur.execute("""

    UPDATE events

    SET processed = 1

    WHERE id = ?

    """,

    (event_id,))

    processed += 1

    print("")
    print(
        f"EVENTO {event_id}"
    )

    print(
        f"{event_type}"
    )

    print(
        f"DESTINO -> {destination}"
    )

conn.commit()

print("")
print(
    "EVENTOS PROCESSADOS:",
    processed
)

conn.close()


