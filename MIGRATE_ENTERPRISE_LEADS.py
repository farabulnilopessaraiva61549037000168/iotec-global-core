import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

conn = sqlite3.connect("enterprise.db")
cursor = conn.cursor()

for col in ["company", "whatsapp"]:
    pass

    try:
        cursor.execute(
            f"ALTER TABLE leads ADD COLUMN {col} TEXT"
        )
        print(f"[OK] Added {col}")

    except Exception as e:
        print(f"[SKIP] {col}: {e}")

conn.commit()

cursor.execute("PRAGMA table_info(leads)")
print("\nCURRENT COLUMNS:\n")

for row in cursor.fetchall():
    print(row)

conn.close()




