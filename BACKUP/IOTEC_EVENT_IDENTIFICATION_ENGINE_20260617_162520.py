import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC EVENT IDENTIFICATION ENGINE
# ==========================================================

import sqlite3

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

events = cur.execute("""

SELECT

    event_type,
    COUNT(*)

FROM events

GROUP BY event_type

ORDER BY COUNT(*) DESC

""").fetchall()

print("")
print("===================================")
print("IOTEC EVENT IDENTIFICATION")
print("===================================")

print("")

for event_type, total in events:
    pass

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

    print(
        f"{event_type} -> {destination} ({total})"
    )

print("")
print("CONCLUIDO")

conn.close()


