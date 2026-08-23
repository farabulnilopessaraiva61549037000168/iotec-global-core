import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

conn = sqlite3.connect("tower.db")
cursor = conn.cursor()

new_columns = [
    ("company", "TEXT"),
    ("whatsapp", "TEXT")
]

for col, typ in new_columns:
    pass

    try:
        cursor.execute(
            f"ALTER TABLE leads ADD COLUMN {col} {typ}"
        )
        print(f"[OK] Added column: {col}")

    except Exception as e:
        print(f"[SKIP] {col}: {e}")

conn.commit()
conn.close()

print("")
print("DATABASE MIGRATION COMPLETED")




