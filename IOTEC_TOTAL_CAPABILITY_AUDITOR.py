import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_TOTAL_CAPABILITY_AUDITOR.py

import sqlite3
import json
from datetime import datetime

MASTER = r"C:\IOTEC\IOTEC_MASTER_TOWER.json"
WAREHOUSE_DB = r"C:\IOTEC\IOTEC_KNOWLEDGE_WAREHOUSE.db"

with open(MASTER,"r",encoding="utf-8") as f:
    tower = json.load(f)

conn = sqlite3.connect(WAREHOUSE_DB)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

warehouse = cur.execute(
    "SELECT COUNT(*) FROM warehouse"
).fetchone()[0]

reservoirs = cur.execute(
    "SELECT COUNT(*) FROM reservoirs"
).fetchone()[0]

summary = {

    "generated": str(datetime.now()),

    "brains": 2,

    "orchestrators": 1,

    "control_towers": 1,

    "memory_engines": 1,

    "commercial_engines":
        len(tower["commercial"]),

    "revenue_engines":
        len(tower["revenue"]),

    "warehouse_items":
        warehouse,

    "reservoir_items":
        reservoirs
}

with open(
    r"C:\IOTEC\IOTEC_TOTAL_CAPABILITIES_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        summary,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("IOTEC TOTAL CAPABILITY AUDITOR")
print("===================================")
print("")
print(json.dumps(summary, indent=4))
print("")
print("CONCLUIDO")

conn.close()




