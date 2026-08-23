import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

conn = sqlite3.connect("enterprise.db")
cursor = conn.cursor()

try:
    cursor.execute(
        "ALTER TABLE leads ADD COLUMN priority TEXT"
    )
    print("[OK] priority added")

except Exception as e:
    print("[SKIP]", e)

conn.commit()

cursor.execute("PRAGMA table_info(leads)")

print("\nCURRENT COLUMNS:\n")

for row in cursor.fetchall():
    print(row)

conn.close()


