import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime
from pathlib import Path

ACCOUNT_DB = r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.db"

OUTPUT = r"C:\IOTEC\IOTEC_REAL_REVENUE_REPORT.json"

conn = sqlite3.connect(ACCOUNT_DB)
cur = conn.cursor()

print("")
print("===================================")
print("IOTEC REAL REVENUE ENGINE")
print("===================================")
print("")

try:
    pass

    rows = cur.execute("""

    SELECT

        company,
        segment,
        status,
        priority

    FROM accounts

    ORDER BY priority DESC

    """).fetchall()

except:
    pass

    rows = []

pipeline = []

for row in rows:
    pass

    company = row[0]
    segment = row[1]
    status = row[2]
    priority = row[3]

    if priority >= 10:
        pass

        suggested_product = "GovTech Analytics"

        estimated_value = 15000

    elif priority >= 9:
        pass

        suggested_product = "Auditoria Inteligente"

        estimated_value = 8000

    else:
        pass

        suggested_product = "Auditoria Operacional"

        estimated_value = 5000

    pipeline.append({

        "company": company,
        "segment": segment,
        "status": status,
        "priority": priority,
        "product": suggested_product,
        "estimated_value": estimated_value

    })

total_pipeline = sum(
    x["estimated_value"]
    for x in pipeline
)

report = {

    "generated": str(datetime.now()),
    "accounts": len(rows),
    "pipeline_value": total_pipeline,
    "accounts_ready_for_contact": len(rows),
    "opportunities": pipeline

}

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

print(
    "CONTAS ANALISADAS:",
    len(rows)
)

print(
    f"PIPELINE POTENCIAL: "
    f"R$ {total_pipeline:,.2f}"
)

print("")

for item in pipeline:
    pass

    print(
        item["company"],
        "|",
        item["product"],
        "|",
        f"R$ {item['estimated_value']:,.2f}"
    )

print("")
print("RELATORIO:")
print(OUTPUT)

print("")
print("PROXIMO PASSO:")
print(
    "CONTATAR EMPRESAS REAIS"
)

print("")
print("CONCLUIDO")

conn.close()


