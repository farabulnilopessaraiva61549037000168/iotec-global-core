import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC CAPABILITY CLUSTER ENGINE
# TRANSFORMA ATIVOS EM CAPACIDADES REAIS
# ==========================================================

import json
from collections import defaultdict
from datetime import datetime

INPUT = r"C:\IOTEC\IOTEC_ASSET_VALUE_REPORT.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_CAPABILITY_CLUSTERS.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_CAPABILITY_CLUSTERS.txt"

# ==========================================================
# CLUSTERS
# ==========================================================

CLUSTERS = {

    "AUDITORIA_FINANCEIRA": [
        "paypal",
        "economic",
        "controladoria",
        "finance",
        "revenue"
    ],

    "AUDITORIA_OPERACIONAL": [
        "auditoria",
        "audit",
        "nucleo",
        "diagnostica",
        "estrategica",
        "projac"
    ],

    "IA_COMERCIAL": [
        "sales",
        "lead",
        "proposal",
        "crm",
        "commercial"
    ],

    "INTELIGENCIA_EXECUTIVA": [
        "brain",
        "intelligence",
        "dashboard",
        "analytics"
    ],

    "GOVTECH": [
        "govtech",
        "pipeline",
        "municipio",
        "prefeitura"
    ],

    "AUTOMACAO": [
        "automation",
        "autonomous",
        "scheduler",
        "workflow"
    ]
}

# ==========================================================
# CARREGA
# ==========================================================

with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

assets = data["top_assets"]

clusters = defaultdict(list)

# ==========================================================
# CLASSIFICA
# ==========================================================

for item in assets:
    pass

    filename = item["file"]
    name = filename.lower()

    matched = False

    for cluster, words in CLUSTERS.items():
        pass

        for word in words:
            pass

            if word in name:
                pass

                clusters[cluster].append(
                    filename
                )

                matched = True
                break

        if matched:
            break

    if not matched:
        pass

        clusters["OUTROS"].append(
            filename
        )

# ==========================================================
# MONTA RELATORIO
# ==========================================================

report = {

    "generated": str(datetime.now()),
    "clusters": []
}

for cluster, files in clusters.items():
    pass

    unique_files = sorted(
        list(set(files))
    )

    report["clusters"].append({

        "cluster": cluster,

        "assets_count": len(
            unique_files
        ),

        "assets": unique_files

    })

report["clusters"] = sorted(

    report["clusters"],

    key=lambda x: x["assets_count"],

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
    f.write("IOTEC CAPABILITY CLUSTERS\n")
    f.write("===================================\n\n")

    for cluster in report["clusters"]:
        pass

        f.write(
            f"CAPACIDADE: {cluster['cluster']}\n"
        )

        f.write(
            f"ATIVOS: {cluster['assets_count']}\n"
        )

        f.write("\n")

        for asset in cluster["assets"][:30]:
            pass

            f.write(
                f" - {asset}\n"
            )

        f.write("\n")

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC CAPABILITY CLUSTER ENGINE")
print("===================================")

for cluster in report["clusters"]:
    pass

    print(
        f"{cluster['cluster']} -> "
        f"{cluster['assets_count']} ativos"
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




