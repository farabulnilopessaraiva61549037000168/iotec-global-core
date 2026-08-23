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

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("EVENTOS")
print("")

for row in cur.execute(
    "SELECT id,event_type,processed FROM events"
):
    print(row)

conn.close()




