import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_CONTROL_TOWER_LEDGER.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("MOTORES REGISTRADOS")
print("")

for row in cur.execute(
    """
    SELECT
        motor,
        layer,
        status
    FROM motors
    ORDER BY layer, motor
    """
):
    print(row)

conn.close()




