import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_HYDRO_TRACE.db"

conn = sqlite3.connect(DB, timeout=30)

conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""

SELECT *

FROM hydro_trace

ORDER BY hydro_id

""").fetchall()

total = len(rows)

contracts = 0
proposals = 0
opportunities = 0
leads = 0

blocked = []

for row in rows:
    pass

    status = row["status"]

    if status == "CONTRACT":
        contracts += 1

    elif status == "PROPOSAL":
        proposals += 1

        blocked.append({

            "hydro_id":
                row["hydro_id"],

            "company":
                row["company"],

            "stage":
                "PROPOSAL"

        })

    elif status == "OPPORTUNITY":
        opportunities += 1

        blocked.append({

            "hydro_id":
                row["hydro_id"],

            "company":
                row["company"],

            "stage":
                "OPPORTUNITY"

        })

    else:
        pass

        leads += 1

        blocked.append({

            "hydro_id":
                row["hydro_id"],

            "company":
                row["company"],

            "stage":
                "LEAD"

        })

# ==========================
# PRESSAO
# ==========================

if contracts > 0:
    pass

    pressure = (
        len(blocked)
        /
        contracts
    ) * 100

else:
    pass

    pressure = (
        len(blocked)
        * 100
    )

# ==========================
# EFICIENCIA
# ==========================

if total > 0:
    pass

    efficiency = (
        contracts
        /
        total
    ) * 100

else:
    pass

    efficiency = 0

# ==========================
# STATUS
# ==========================

if pressure < 50:
    pass

    plant_status = "FLUXO LIVRE"

elif pressure < 150:
    pass

    plant_status = "PRESSAO MODERADA"

elif pressure < 300:
    pass

    plant_status = "PRESSAO ALTA"

else:
    pass

    plant_status = "PRESSAO CRITICA"

# ==========================
# RELATORIO
# ==========================

report = {

    "generated":
        str(datetime.now()),

    "total_rivers":
        total,

    "contracts":
        contracts,

    "proposals":
        proposals,

    "opportunities":
        opportunities,

    "leads":
        leads,

    "pressure":
        round(
            pressure,
            2
        ),

    "efficiency":
        round(
            efficiency,
            2
        ),

    "plant_status":
        plant_status,

    "blocked_rivers":
        blocked

}

OUTPUT = (
    r"C:\IOTEC\IOTEC_HYDRO_PRESSURE_REPORT.json"
)

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("IOTEC HYDRO PRESSURE ENGINE")
print("===================================")
print("")

print(
    "RIOS:",
    total
)

print(
    "CONTRATOS:",
    contracts
)

print(
    "PROPOSTAS:",
    proposals
)

print(
    "OPORTUNIDADES:",
    opportunities
)

print(
    "LEADS:",
    leads
)

print("")

print(
    f"PRESSAO: "
    f"{pressure:.2f}%"
)

print(
    f"EFICIENCIA: "
    f"{efficiency:.2f}%"
)

print("")

print(
    "STATUS:",
    plant_status
)

print("")

print(
    "RIOS REPRESADOS:"
)

for item in blocked:
    pass

    print(
        item["hydro_id"],
        "|",
        item["company"],
        "|",
        item["stage"]
    )

print("")
print("JSON:")
print(OUTPUT)

print("")
print("CONCLUIDO")

conn.close()




