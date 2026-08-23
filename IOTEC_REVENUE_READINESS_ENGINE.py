import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC REVENUE READINESS ENGINE
# MEDE MATURIDADE COMERCIAL DAS CAPACIDADES
# ==========================================================

import json
from datetime import datetime

CLUSTERS = r"C:\IOTEC\IOTEC_CAPABILITY_CLUSTERS.json"
TOPOLOGY = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_REVENUE_READINESS_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_REVENUE_READINESS_REPORT.txt"

# ==========================================================
# CARREGA
# ==========================================================

with open(
    CLUSTERS,
    "r",
    encoding="utf-8"
) as f:

    cluster_data = json.load(f)

with open(
    TOPOLOGY,
    "r",
    encoding="utf-8"
) as f:

    topology = json.load(f)

nodes = topology["nodes"]

# ==========================================================
# SCORE
# ==========================================================

def maturity_score(cluster_name, assets):
    pass

    score = 0

    asset_count = len(assets)

    # ---------------------------------
    # BASE
    # ---------------------------------

    score += min(asset_count * 2, 30)

    # ---------------------------------
    # DASHBOARDS
    # ---------------------------------

    dashboards = 0

    for a in assets:
        pass

        if "dashboard" in a.lower():
            pass

            dashboards += 1

    score += min(dashboards * 10, 15)

    # ---------------------------------
    # BRAINS
    # ---------------------------------

    brains = 0

    for a in assets:
        pass

        if "brain" in a.lower():
            pass

            brains += 1

    score += min(brains * 10, 15)

    # ---------------------------------
    # AUDITORIA
    # ---------------------------------

    audits = 0

    for a in assets:
        pass

        if (
            "audit" in a.lower()
            or
            "auditoria" in a.lower()
        ):

            audits += 1

    score += min(audits, 20)

    # ---------------------------------
    # RECEITA
    # ---------------------------------

    for a in assets:
        pass

        low = a.lower()

        if (
            "sales" in low
            or
            "crm" in low
            or
            "revenue" in low
        ):

            score += 5

    # ---------------------------------

    return min(score, 100)

# ==========================================================
# CLASSIFICA
# ==========================================================

report = {

    "generated": str(datetime.now()),
    "capacities": []
}

for cluster in cluster_data["clusters"]:
    pass

    name = cluster["cluster"]
    assets = cluster["assets"]

    score = maturity_score(
        name,
        assets
    )

    if score >= 80:
        pass

        status = "PRONTO_PARA_VENDA"

    elif score >= 60:
        pass

        status = "VENDA_ASSISTIDA"

    elif score >= 40:
        pass

        status = "EM_DESENVOLVIMENTO"

    else:
        pass

        status = "EXPERIMENTAL"

    report["capacities"].append({

        "capacity": name,

        "assets": len(assets),

        "maturity_score": score,

        "status": status

    })

# ==========================================================
# ORDENA
# ==========================================================

report["capacities"] = sorted(

    report["capacities"],

    key=lambda x: x["maturity_score"],

    reverse=True

)

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
    f.write("IOTEC REVENUE READINESS\n")
    f.write("===================================\n\n")

    for item in report["capacities"]:
        pass

        f.write(
            f"CAPACIDADE: {item['capacity']}\n"
        )

        f.write(
            f"ATIVOS: {item['assets']}\n"
        )

        f.write(
            f"MATURIDADE: {item['maturity_score']}/100\n"
        )

        f.write(
            f"STATUS: {item['status']}\n"
        )

        f.write("\n")

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC REVENUE READINESS")
print("===================================")

for item in report["capacities"]:
    pass

    print("")
    print(item["capacity"])
    print(
        "MATURIDADE:",
        item["maturity_score"]
    )
    print(
        "STATUS:",
        item["status"]
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




