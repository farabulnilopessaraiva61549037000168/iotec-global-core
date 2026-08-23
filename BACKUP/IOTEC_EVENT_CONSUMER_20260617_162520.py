import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC EVENT CONSUMER
# ==========================================================

import sqlite3
import subprocess
from datetime import datetime

EVENT_DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(EVENT_DB)
cur = conn.cursor()

# ==========================================================
# LOG DE CONSUMO
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS consumed_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_id INTEGER,

    event_type TEXT,

    consumed_at TEXT,

    action TEXT

)

""")

conn.commit()

# ==========================================================
# EVENTOS PROCESSADOS
# ==========================================================

events = cur.execute("""

SELECT

    id,
    event_type

FROM events

WHERE processed = 1

AND id NOT IN (

    SELECT event_id
    FROM consumed_events

)

ORDER BY id

""").fetchall()

print("")
print("===================================")
print("IOTEC EVENT CONSUMER")
print("===================================")

consumed = 0

for event_id, event_type in events:
    pass

    action = "NONE"

    try:
        pass

        if event_type == "LEAD":
            pass

            subprocess.run(

                [
                    "python",
                    r"C:\IOTEC\IOTEC_MISSION_UPDATE_ENGINE.py",
                    "lead"
                ],

                capture_output=True

            )

            action = "MISSION_LEAD"

        elif event_type == "PROPOSAL":
            pass

            subprocess.run(

                [
                    "python",
                    r"C:\IOTEC\IOTEC_MISSION_UPDATE_ENGINE.py",
                    "proposal"
                ],

                capture_output=True

            )

            action = "MISSION_PROPOSAL"

        elif event_type == "MEETING":
            pass

            subprocess.run(

                [
                    "python",
                    r"C:\IOTEC\IOTEC_MISSION_UPDATE_ENGINE.py",
                    "meeting"
                ],

                capture_output=True

            )

            action = "MISSION_MEETING"

        elif event_type == "PAYMENT":
            pass

            action = "REVENUE_UPDATE"

        else:
            pass

            action = "NO_HANDLER"

        cur.execute("""

        INSERT INTO consumed_events (

            event_id,
            event_type,
            consumed_at,
            action

        )

        VALUES (

            ?,?,?,?

        )

        """,

        (

            event_id,
            event_type,
            str(datetime.now()),
            action

        ))

        conn.commit()

        consumed += 1

        print(
            f"EVENT {event_id} -> {action}"
        )

    except Exception as e:
        pass

        print(
            f"ERRO EVENTO {event_id}: {e}"
        )

print("")
print(
    "EVENTOS CONSUMIDOS:",
    consumed
)

print("")
print("DATABASE:")
print(EVENT_DB)

print("")
print("CONCLUIDO")

conn.close()


