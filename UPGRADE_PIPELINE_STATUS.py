import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN client_name TEXT
    """)

except:
    pass

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN phone TEXT
    """)

except:
    pass

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN report_file TEXT
    """)

except:
    pass

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN proposal_file TEXT
    """)

except:
    pass

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN payment_link TEXT
    """)

except:
    pass

try:
    pass

    cur.execute("""
    ALTER TABLE pipeline
    ADD COLUMN last_contact TEXT
    """)

except:
    pass

conn.commit()
conn.close()

print("PIPELINE EXPANDIDO")




