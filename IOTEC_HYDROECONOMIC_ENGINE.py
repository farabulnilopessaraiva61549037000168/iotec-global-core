import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

ACCOUNT_DB = r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.db"
OPP_DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"
PROPOSAL_DB = r"C:\IOTEC\IOTEC_PROPOSALS.db"
CONTRACT_DB = r"C:\IOTEC\IOTEC_CONTRACTS.db"

# ==========================
# RESERVATORIO
# ==========================

reservoir = 0

try:
    conn = sqlite3.connect(ACCOUNT_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    accounts = cur.execute(
        "SELECT COUNT(*) FROM accounts"
    ).fetchone()[0]

    leads = cur.execute(
        "SELECT COUNT(*) FROM leads"
    ).fetchone()[0]

    conn.close()

except:
    accounts = 0
    leads = 0

reservoir = accounts + leads

# ==========================
# VAZAO
# ==========================

try:
    conn = sqlite3.connect(OPP_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    opportunities = cur.execute(
        "SELECT COUNT(*) FROM opportunities"
    ).fetchone()[0]

    conn.close()

except:
    opportunities = 0

# ==========================
# PROPOSTAS
# ==========================

try:
    conn = sqlite3.connect(PROPOSAL_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    proposals = cur.execute(
        "SELECT COUNT(*) FROM proposals"
    ).fetchone()[0]

    proposal_value = cur.execute(
        """
        SELECT
        COALESCE(SUM(value),0)
        FROM proposals
        """
    ).fetchone()[0]

    conn.close()

except:
    proposals = 0
    proposal_value = 0

# ==========================
# CONTRATOS
# ==========================

try:
    conn = sqlite3.connect(CONTRACT_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    contracts = cur.execute(
        "SELECT COUNT(*) FROM contracts"
    ).fetchone()[0]

    revenue = cur.execute(
        """
        SELECT
        COALESCE(
        SUM(contract_value),
        0
        )
        FROM contracts
        """
    ).fetchone()[0]

    conn.close()

except:
    contracts = 0
    revenue = 0

# ==========================
# EFICIENCIAS
# ==========================

if leads > 0:
    opp_efficiency = (
        opportunities / leads
    ) * 100
else:
    opp_efficiency = 0

if opportunities > 0:
    proposal_efficiency = (
        proposals / opportunities
    ) * 100
else:
    proposal_efficiency = 0

if proposals > 0:
    contract_efficiency = (
        contracts / proposals
    ) * 100
else:
    contract_efficiency = 0

# ==========================
# POTENCIA ECONOMICA
# ==========================

power_index = (
    opp_efficiency +
    proposal_efficiency +
    contract_efficiency
) / 3

# ==========================
# PREVISAO
# ==========================

predicted_contracts = contracts * 2

predicted_revenue = revenue * 2

# ==========================
# RELATORIO
# ==========================

report = {

    "generated": str(datetime.now()),

    "reservoir": reservoir,

    "accounts": accounts,

    "leads": leads,

    "opportunities": opportunities,

    "proposals": proposals,

    "contracts": contracts,

    "proposal_value": proposal_value,

    "revenue": revenue,

    "opp_efficiency": round(
        opp_efficiency,
        2
    ),

    "proposal_efficiency": round(
        proposal_efficiency,
        2
    ),

    "contract_efficiency": round(
        contract_efficiency,
        2
    ),

    "power_index": round(
        power_index,
        2
    ),

    "predicted_contracts": predicted_contracts,

    "predicted_revenue": predicted_revenue

}

with open(
    r"C:\IOTEC\IOTEC_HYDROECONOMIC_REPORT.json",
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
print("IOTEC HYDROECONOMIC ENGINE")
print("===================================")
print("")

print("RESERVATORIO:", reservoir)

print("CONTAS:", accounts)
print("LEADS:", leads)

print("")
print("VAZAO")

print("OPORTUNIDADES:", opportunities)
print("PROPOSTAS:", proposals)
print("CONTRATOS:", contracts)

print("")
print("EFICIENCIAS")

print(
    f"LEAD->OPP: "
    f"{opp_efficiency:.2f}%"
)

print(
    f"OPP->PROP: "
    f"{proposal_efficiency:.2f}%"
)

print(
    f"PROP->CONTRATO: "
    f"{contract_efficiency:.2f}%"
)

print("")
print(
    f"POTENCIA: "
    f"{power_index:.2f}%"
)

print("")
print(
    f"RECEITA: "
    f"R$ {revenue:,.2f}"
)

print("")
print("PREVISAO")

print(
    "CONTRATOS:",
    predicted_contracts
)

print(
    f"RECEITA FUTURA: "
    f"R$ {predicted_revenue:,.2f}"
)

print("")
print("JSON:")
print(
    r"C:\IOTEC\IOTEC_HYDROECONOMIC_REPORT.json"
)

print("")
print("CONCLUIDO")




