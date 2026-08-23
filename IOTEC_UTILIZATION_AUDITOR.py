import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC UTILIZATION AUDITOR
# AUDITORIA DE UTILIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REAL
# ==========================================================

import sqlite3
import json
import os
from datetime import datetime

LEDGER_DB = r"C:\IOTEC\IOTEC_CONTROL_TOWER_LEDGER.db"
WAREHOUSE_DB = r"C:\IOTEC\IOTEC_KNOWLEDGE_WAREHOUSE.db"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_UTILIZATION_REPORT.json"
OUTPUT_TXT = r"C:\IOTEC\IOTEC_UTILIZATION_REPORT.txt"

report = {
    "generated": str(datetime.now()),
    "metrics": {}
}

# ==========================================================
# CONTROL TOWER
# ==========================================================

if os.path.exists(LEDGER_DB):
    pass

    conn = sqlite3.connect(LEDGER_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    try:
        pass

        motors = cur.execute(
            "SELECT COUNT(*) FROM motors"
        ).fetchone()[0]

        report["metrics"]["registered_motors"] = motors

    except:
        report["metrics"]["registered_motors"] = 0

    try:
        pass

        events = cur.execute(
            "SELECT COUNT(*) FROM production_events"
        ).fetchone()[0]

        report["metrics"]["production_events"] = events

    except:
        report["metrics"]["production_events"] = 0

    try:
        pass

        history = cur.execute(
            "SELECT COUNT(*) FROM production_history"
        ).fetchone()[0]

        report["metrics"]["production_history"] = history

    except:
        report["metrics"]["production_history"] = 0

    conn.close()

# ==========================================================
# WAREHOUSE
# ==========================================================

if os.path.exists(WAREHOUSE_DB):
    pass

    conn = sqlite3.connect(WAREHOUSE_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    try:
        pass

        warehouse = cur.execute(
            "SELECT COUNT(*) FROM warehouse"
        ).fetchone()[0]

        report["metrics"]["warehouse_items"] = warehouse

    except:
        report["metrics"]["warehouse_items"] = 0

    try:
        pass

        reservoirs = cur.execute(
            "SELECT COUNT(*) FROM reservoirs"
        ).fetchone()[0]

        report["metrics"]["reservoir_items"] = reservoirs

    except:
        report["metrics"]["reservoir_items"] = 0

    conn.close()

# ==========================================================
# SCORE
# ==========================================================

registered = report["metrics"].get(
    "registered_motors",
    0
)

events = report["metrics"].get(
    "production_events",
    0
)

warehouse = report["metrics"].get(
    "warehouse_items",
    0
)

reservoirs = report["metrics"].get(
    "reservoir_items",
    0
)

utilization_score = (
    events +
    warehouse +
    reservoirs
)

report["metrics"]["utilization_score"] = utilization_score

if registered > 0:
    pass

    report["metrics"]["coverage_percent"] = round(

        (utilization_score / registered) * 100,

        2

    )

else:
    pass

    report["metrics"]["coverage_percent"] = 0

# ==========================================================
# JSON
# ==========================================================

with open(
    OUTPUT_JSON,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# TXT
# ==========================================================

with open(
    OUTPUT_TXT,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC UTILIZATION AUDITOR\n")
    f.write("===================================\n\n")

    for k, v in report["metrics"].items():
        pass

        f.write(
            f"{k}: {v}\n"
        )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC UTILIZATION AUDITOR")
print("===================================")

for k, v in report["metrics"].items():
    pass

    print(
        f"{k}: {v}"
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




