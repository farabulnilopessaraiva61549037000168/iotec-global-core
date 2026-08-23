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

campos = [

    ("payment_provider","TEXT"),
    ("payment_link","TEXT"),
    ("payment_reference","TEXT"),
    ("payment_status","TEXT"),
    ("payment_date","TEXT")

]

for campo,tipo in campos:
    pass

    try:
        pass

        cur.execute(
            f"ALTER TABLE pipeline ADD COLUMN {campo} {tipo}"
        )

        print(f"[OK] {campo}")

    except:
        pass

        print(f"[EXISTE] {campo}")

conn.commit()
conn.close()

print("")
print("================================")
print("PAYMENT SCHEMA ATUALIZADO")
print("================================")
print("")




