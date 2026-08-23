import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC MISSION UPDATE ENGINE
# ==========================================================

import sqlite3
import sys

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

if len(sys.argv) < 2:
    pass

    print("")
    print("USO:")
    print("python IOTEC_MISSION_UPDATE_ENGINE.py lead")
    print("python IOTEC_MISSION_UPDATE_ENGINE.py proposal")
    print("python IOTEC_MISSION_UPDATE_ENGINE.py meeting")
    exit()

action = sys.argv[1].lower()

conn = sqlite3.connect(DB)
cur = conn.cursor()

row = cur.execute("""

SELECT

    id,

    target_leads,
    target_proposals,
    target_meetings,

    executed_leads,
    executed_proposals,
    executed_meetings

FROM missions

ORDER BY id DESC

LIMIT 1

""").fetchone()

mission_id = row[0]

tl,tp,tm = row[1],row[2],row[3]
el,ep,em = row[4],row[5],row[6]

if action == "lead":
    pass

    el += 1

elif action == "proposal":
    pass

    ep += 1

elif action == "meeting":
    pass

    em += 1

else:
    pass

    print("AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INVÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLIDA")
    exit()

target_total = tl + tp + tm
executed_total = el + ep + em

execution = round(
    (executed_total / target_total) * 100,
    2
)

cur.execute("""

UPDATE missions

SET

    executed_leads=?,
    executed_proposals=?,
    executed_meetings=?,
    execution_percent=?

WHERE id=?

""",

(
    el,
    ep,
    em,
    execution,
    mission_id
))

conn.commit()

print("")
print("===================================")
print("MISSION UPDATED")
print("===================================")

print("")
print("LEADS:", el)
print("PROPOSTAS:", ep)
print("REUNIOES:", em)

print("")
print(
    "EXECUCAO:",
    execution,
    "%"
)

conn.close()


