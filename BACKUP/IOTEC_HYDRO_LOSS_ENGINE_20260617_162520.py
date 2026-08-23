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

conn = sqlite3.connect(DB)

conn.row_factory = sqlite3.Row

cur = conn.cursor()

rows = cur.execute("""

SELECT *

FROM hydro_trace

""").fetchall()

total = len(rows)

lead_count = total
opp_count = 0
proposal_count = 0
contract_count = 0

for row in rows:
    pass

    status = row["status"]

    if status in [
        "OPPORTUNITY",
        "PROPOSAL",
        "CONTRACT"
    ]:
        opp_count += 1

    if status in [
        "PROPOSAL",
        "CONTRACT"
    ]:
        proposal_count += 1

    if status == "CONTRACT":
        contract_count += 1

# ==========================
# PERDAS
# ==========================

if lead_count > 0:
    pass

    lead_loss = (
        (
            lead_count -
            opp_count
        )
        /
        lead_count
    ) * 100

else:
    pass

    lead_loss = 0

if opp_count > 0:
    pass

    opp_loss = (
        (
            opp_count -
            proposal_count
        )
        /
        opp_count
    ) * 100

else:
    pass

    opp_loss = 0

if proposal_count > 0:
    pass

    proposal_loss = (
        (
            proposal_count -
            contract_count
        )
        /
        proposal_count
    ) * 100

else:
    pass

    proposal_loss = 0

# ==========================
# EFICIENCIA FINAL
# ==========================

if lead_count > 0:
    pass

    final_efficiency = (
        contract_count /
        lead_count
    ) * 100

else:
    pass

    final_efficiency = 0

# ==========================
# INDICE DE DESPERDICIO
# ==========================

waste_index = (
    lead_loss +
    opp_loss +
    proposal_loss
) / 3

# ==========================
# STATUS
# ==========================

if waste_index < 20:
    pass

    status = "USINA EFICIENTE"

elif waste_index < 50:
    pass

    status = "PERDA MODERADA"

elif waste_index < 75:
    pass

    status = "PERDA ALTA"

else:
    pass

    status = "PERDA CRITICA"

# ==========================
# RELATORIO
# ==========================

report = {

    "generated":
        str(datetime.now()),

    "rivers":
        total,

    "lead_loss":
        round(lead_loss,2),

    "opportunity_loss":
        round(opp_loss,2),

    "proposal_loss":
        round(proposal_loss,2),

    "final_efficiency":
        round(final_efficiency,2),

    "waste_index":
        round(waste_index,2),

    "status":
        status

}

OUTPUT = (
    r"C:\IOTEC\IOTEC_HYDRO_LOSS_REPORT.json"
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
print("IOTEC HYDRO LOSS ENGINE")
print("===================================")
print("")

print(
    f"RIOS: {total}"
)

print("")

print(
    f"PERDA LEAD->OPP: "
    f"{lead_loss:.2f}%"
)

print(
    f"PERDA OPP->PROPOSTA: "
    f"{opp_loss:.2f}%"
)

print(
    f"PERDA PROPOSTA->CONTRATO: "
    f"{proposal_loss:.2f}%"
)

print("")

print(
    f"EFICIENCIA FINAL: "
    f"{final_efficiency:.2f}%"
)

print(
    f"DESPERDICIO: "
    f"{waste_index:.2f}%"
)

print("")

print(
    f"STATUS: {status}"
)

print("")

print("JSON:")
print(OUTPUT)

print("")
print("CONCLUIDO")

conn.close()


