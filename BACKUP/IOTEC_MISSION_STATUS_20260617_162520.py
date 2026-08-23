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

    product,

    target_leads,
    target_proposals,
    target_meetings,

    executed_leads,
    executed_proposals,
    executed_meetings,

    execution_percent

FROM missions

ORDER BY id DESC

LIMIT 1

""").fetchone()

print("")
print("===================================")
print("IOTEC MISSION STATUS")
print("===================================")

print("")
print("PRODUTO:", row[0])

print("")
print("META")
print("LEADS:", row[1])
print("PROPOSTAS:", row[2])
print("REUNIOES:", row[3])

print("")
print("EXECUTADO")
print("LEADS:", row[4])
print("PROPOSTAS:", row[5])
print("REUNIOES:", row[6])

print("")
print("EXECUCAO:", row[7], "%")

conn.close()


