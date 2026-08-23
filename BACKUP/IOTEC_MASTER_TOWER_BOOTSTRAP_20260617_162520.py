import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC MASTER TOWER BOOTSTRAP
# ACOPLADOR DA TORRE MESTRA
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ALTERA MOTORES
# ==========================================================

import json
from datetime import datetime

TOPOLOGY = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

OUTPUT = r"C:\IOTEC\IOTEC_MASTER_TOWER.json"

with open(
    TOPOLOGY,
    "r",
    encoding="utf-8"
) as f:

    topo = json.load(f)

nodes = topo["nodes"]

master = {

    "generated": str(datetime.now()),

    "master_brain": None,

    "unified_brain": None,

    "orchestrator": None,

    "control_tower": None,

    "memory": None,

    "commercial": [],

    "revenue": [],

    "ledger": r"C:\IOTEC\IOTEC_CONTROL_TOWER_LEDGER.db"
}

# ==========================================================
# DESCOBERTA AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA
# ==========================================================

for name in nodes.keys():
    pass

    upper = name.upper()

    if "CENTRAL_BRAIN" in upper:
        master["master_brain"] = name

    elif "UNIFIED_BRAIN" in upper:
        master["unified_brain"] = name

    elif "NUCLEUS_ORCHESTRATOR" in upper:
        master["orchestrator"] = name

    elif "CONTROL_TOWER" in upper:
        master["control_tower"] = name

    elif "MEMORY_ENGINE" in upper:
        master["memory"] = name

    elif "CRM_ENGINE" in upper:
        master["commercial"].append(name)

    elif "SALES_BRAIN" in upper:
        master["commercial"].append(name)

    elif "REVENUE_OPERATION_CENTER" in upper:
        master["revenue"].append(name)

# ==========================================================
# SALVA
# ==========================================================

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        master,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

print("")
print("===================================")
print("IOTEC MASTER TOWER BOOTSTRAP")
print("===================================")

print("")
print("MASTER BRAIN:")
print(master["master_brain"])

print("")
print("UNIFIED BRAIN:")
print(master["unified_brain"])

print("")
print("ORCHESTRATOR:")
print(master["orchestrator"])

print("")
print("CONTROL TOWER:")
print(master["control_tower"])

print("")
print("MEMORY:")
print(master["memory"])

print("")
print("COMMERCIAL:")
for item in master["commercial"]:
    print(" -", item)

print("")
print("REVENUE:")
for item in master["revenue"]:
    print(" -", item)

print("")
print("LEDGER:")
print(master["ledger"])

print("")
print("ARQUIVO:")
print(OUTPUT)

print("")
print("CONCLUIDO")


