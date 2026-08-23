import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# LIVE_TOWER_ALERT.py

import sqlite3
import time
import os

DATABASE = "enterprise.db"

last_id = 0

while True:
    pass

    try:
        pass

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT
            id,
            protocol,
            name,
            service,
            score

        FROM leads

        ORDER BY id DESC

        LIMIT 1

        """)

        row = cursor.fetchone()

        conn.close()

        if row:
            pass

            lead_id = row[0]

            if lead_id != last_id:
                pass

                last_id = lead_id

                print("\n================================================")
                print(" NEW OPPORTUNITY DETECTED ")
                print("================================================")
                print(f"PROTOCOL : {row[1]}")
                print(f"NAME     : {row[2]}")
                print(f"SERVICE  : {row[3]}")
                print(f"SCORE    : {row[4]}")
                print("================================================\n")

        time.sleep(2)

    except Exception as e:
        pass

        print(e)

        time.sleep(5)


