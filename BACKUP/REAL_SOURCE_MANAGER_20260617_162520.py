import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS acquisition_sources (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source_name TEXT,

    source_type TEXT,

    source_url TEXT,

    active INTEGER DEFAULT 1,

    priority INTEGER DEFAULT 50,

    created_at TEXT

)

""")

conn.commit()

print("")
print("===================================")
print("REAL SOURCE MANAGER")
print("===================================")
print("")
print("TABELA acquisition_sources OK")
print("")

conn.close()


