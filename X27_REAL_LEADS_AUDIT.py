import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("="*70)
print("REAL LEADS STRUCTURE")
print("="*70)

cur.execute("PRAGMA table_info(real_leads)")

for c in cur.fetchall():
    print(c)

print()
print("="*70)
print("REGISTROS")
print("="*70)

cur.execute("""
SELECT
company,
city,
segment,
status
FROM real_leads
LIMIT 50
""")

for r in cur.fetchall():
    print(r)

conn.close()



