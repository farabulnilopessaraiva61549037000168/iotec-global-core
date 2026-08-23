import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC CYCLE AUDITOR
# ==========================================================

import sqlite3

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

total = cur.execute("""

SELECT COUNT(*)

FROM missions

""").fetchone()[0]

completed = cur.execute("""

SELECT COUNT(*)

FROM missions

WHERE status='COMPLETED'

""").fetchone()[0]

open_missions = cur.execute("""

SELECT COUNT(*)

FROM missions

WHERE status='OPEN'

""").fetchone()[0]

revenue = cur.execute("""

SELECT
SUM(potential_revenue)

FROM missions

""").fetchone()[0]

current = cur.execute("""

SELECT

    id,
    product,
    target_leads,
    target_proposals,
    target_meetings

FROM missions

WHERE status='OPEN'

ORDER BY id DESC

LIMIT 1

""").fetchone()

success = 0

if total > 0:
    pass

    success = round(
        (completed / total) * 100,
        2
    )

print("")
print("===================================")
print("IOTEC CYCLE AUDITOR")
print("===================================")

print("")
print("TOTAL MISSIONS:", total)

print(
    "COMPLETED:",
    completed
)

print(
    "OPEN:",
    open_missions
)

print(
    "SUCCESS RATE:",
    success,
    "%"
)

print("")
print(
    "ACCUMULATED REVENUE:",
    revenue
)

if current:
    pass

    print("")
    print("CURRENT MISSION")

    print(
        "ID:",
        current[0]
    )

    print(
        "PRODUCT:",
        current[1]
    )

    print(
        "LEADS:",
        current[2]
    )

    print(
        "PROPOSALS:",
        current[3]
    )

    print(
        "MEETINGS:",
        current[4]
    )

print("")
print("CONCLUIDO")

conn.close()




