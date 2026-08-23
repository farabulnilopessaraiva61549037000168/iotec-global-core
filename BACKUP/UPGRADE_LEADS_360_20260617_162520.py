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

campos = [

    ("phone","TEXT"),
    ("city","TEXT"),
    ("employees","INTEGER"),
    ("users_expected","INTEGER"),
    ("urgency","TEXT"),
    ("current_system","TEXT"),
    ("budget_estimate","REAL"),
    ("desired_deadline","TEXT"),
    ("lead_score","INTEGER")

]

for campo,tipo in campos:
    pass

    try:
        pass

        cur.execute(
            f"ALTER TABLE leads ADD COLUMN {campo} {tipo}"
        )

        print(f"[OK] {campo}")

    except:
        pass

        print(f"[EXISTE] {campo}")

conn.commit()
conn.close()

print("")
print("LEADS 360 INSTALADO")


