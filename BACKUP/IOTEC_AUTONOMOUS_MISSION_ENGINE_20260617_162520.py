import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

row = cur.execute("""

SELECT

    id,
    product,
    execution_percent,
    status

FROM missions

ORDER BY id DESC

LIMIT 1

""").fetchone()

mission_id = row[0]
product = row[1]
execution_percent = row[2]
status = row[3]

print("")
print("===================================")
print("IOTEC AUTONOMOUS MISSION ENGINE")
print("===================================")

print("")
print("MISSION:", mission_id)
print("PRODUCT:", product)
print("EXECUTION:", execution_percent)
print("STATUS:", status)

if execution_percent >= 100 and status == "OPEN":
    pass

    cur.execute("""

    UPDATE missions

    SET status='COMPLETED'

    WHERE id=?

    """,

    (mission_id,))

    conn.commit()

    print("")
    print("MISSION CLOSED")

else:
    pass

    print("")
    print("MISSION STILL RUNNING")

conn.close()

print("")
print("CONCLUIDO")


