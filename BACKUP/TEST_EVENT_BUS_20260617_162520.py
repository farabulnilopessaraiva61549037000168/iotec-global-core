import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

conn = sqlite3.connect(
    r"C:\IOTEC\IOTEC_EVENT_BUS.db"
)

cur = conn.cursor()

print("")
print("EVENTOS")
print("")

for row in cur.execute(
    "SELECT id,event_type,processed FROM events"
):
    print(row)

conn.close()


