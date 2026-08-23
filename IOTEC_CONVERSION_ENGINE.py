import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

TRACE_DB = r"C:\IOTEC\IOTEC_HYDRO_TRACE.db"

conn = sqlite3.connect(TRACE_DB)

conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""

SELECT *

FROM hydro_trace

WHERE status='PROPOSAL'

ORDER BY proposal_value DESC

""").fetchall()

actions = []

potential_revenue = 0

print("")
print("===================================")
print("IOTEC CONVERSION ENGINE")
print("===================================")
print("")

for row in rows:
    pass

    hydro_id = row["hydro_id"]

    company = row["company"]

    product = row["product"]

    value = row["proposal_value"] or 0

    potential_revenue += value

    priority = "NORMAL"

    if value >= 15000:
        priority = "MAXIMA"

    elif value >= 8000:
        priority = "ALTA"

    action = {

        "hydro_id": hydro_id,

        "company": company,

        "product": product,

        "value": value,

        "priority": priority,

        "recommended_action":
            "FOLLOW_UP"

    }

    actions.append(action)

    print(
        hydro_id,
        "|",
        company,
        "|",
        f"R$ {value:,.2f}",
        "|",
        priority
    )

print("")
print(
    "PROPOSTAS ABERTAS:",
    len(actions)
)

print(
    f"RECEITA EM RISCO: "
    f"R$ {potential_revenue:,.2f}"
)

# ==========================
# SCORE DE CONVERSAO
# ==========================

if potential_revenue > 0:
    pass

    estimated_conversion = (
        potential_revenue * 0.33
    )

else:
    pass

    estimated_conversion = 0

print("")

print(
    f"RECEITA PROVAVEL: "
    f"R$ {estimated_conversion:,.2f}"
)

# ==========================
# RELATORIO
# ==========================

report = {

    "generated":
        str(datetime.now()),

    "open_proposals":
        len(actions),

    "pipeline_value":
        potential_revenue,

    "estimated_conversion":
        estimated_conversion,

    "actions":
        actions

}

OUTPUT = (
    r"C:\IOTEC\IOTEC_CONVERSION_REPORT.json"
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
print("JSON:")
print(OUTPUT)

print("")
print("CONCLUIDO")

conn.close()




