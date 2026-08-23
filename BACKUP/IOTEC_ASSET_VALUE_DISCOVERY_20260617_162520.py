import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ASSET VALUE DISCOVERY
# DESCOBRE ATIVOS COM POTENCIAL ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICO
# ==========================================================

import os
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT = r"C:\IOTEC\IOTEC_ASSET_VALUE_REPORT.json"

KEYWORDS = {

    "VENDA_IMEDIATA": [
        "crm",
        "sales",
        "lead",
        "proposal",
        "revenue",
        "cliente",
        "pipeline"
    ],

    "ALTO_VALOR": [
        "brain",
        "intelligence",
        "analytics",
        "dashboard",
        "audit",
        "monitor"
    ],

    "CONSULTORIA": [
        "auditoria",
        "economic",
        "diagnostic",
        "forense",
        "controladoria"
    ],

    "AUTOMACAO": [
        "automation",
        "autonomous",
        "scheduler",
        "workflow"
    ]
}

assets = []

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if not (
            file.endswith(".py")
            or file.endswith(".json")
        ):
            continue

        name = file.lower()

        score = 0
        category = "INTERNO"

        for cls, words in KEYWORDS.items():
            pass

            found = False

            for word in words:
                pass

                if word in name:
                    pass

                    found = True
                    break

            if found:
                pass

                category = cls

                if cls == "VENDA_IMEDIATA":
                    score += 100

                elif cls == "ALTO_VALOR":
                    score += 80

                elif cls == "CONSULTORIA":
                    score += 70

                elif cls == "AUTOMACAO":
                    score += 60

        if score > 0:
            pass

            assets.append({

                "file": file,

                "category": category,

                "score": score

            })

assets = sorted(
    assets,
    key=lambda x: x["score"],
    reverse=True
)

report = {

    "generated": str(datetime.now()),

    "assets_found": len(assets),

    "top_assets": assets[:100]
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

print("")
print("===================================")
print("IOTEC ASSET VALUE DISCOVERY")
print("===================================")
print("")

print(
    "ATIVOS:",
    len(assets)
)

print("")
print("TOP 20")
print("")

for item in assets[:20]:
    pass

    print(
        f"{item['score']} | "
        f"{item['category']} | "
        f"{item['file']}"
    )

print("")
print("RELATORIO:")
print(OUTPUT)

print("")
print("CONCLUIDO")


