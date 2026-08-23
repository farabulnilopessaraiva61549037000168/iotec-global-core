# ============================================================
# IOTEC PRODUCT SCORING ENGINE
# MÃƒâ€œDULO 006
# VersÃƒÂ£o: 2026.1
# Modo: SOMENTE LEITURA
#
# LÃƒÂª:
#     IOTEC_CAPABILITY_CONSOLIDATION.json
#
# Gera:
#     IOTEC_PRODUCT_SCORE.json
#
# NÃƒÂ£o modifica nenhum arquivo da plataforma.
# ============================================================

import json
from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()

SOURCE = ROOT / "IOTEC_CAPABILITY_CONSOLIDATION.json"

OUTPUT = ROOT / "IOTEC_PRODUCT_SCORE.json"

if not SOURCE.exists():
    raise FileNotFoundError(
        f"Arquivo nÃƒÂ£o encontrado: {SOURCE}"
    )

with open(SOURCE, "r", encoding="utf-8") as f:
    data = json.load(f)

# ------------------------------------------------------------

MARKET = {

    "AI_ENGINE":100,
    "COMMERCIAL_ENGINE":100,
    "API_ENGINE":95,
    "DATABASE_ENGINE":90,
    "DASHBOARD_ENGINE":90,
    "AUTOMATION_ENGINE":85,
    "PDF_ENGINE":75,
    "ROBOTICS_ENGINE":80

}

REPORT = {
    "generated_at":datetime.now().isoformat(),
    "ranking":[]
}

for engine,info in data["engines"].items():

    occ = info["occurrences"]

    market = MARKET.get(engine,50)

    maturity = min(100,40 + occ)

    score = round(
        maturity*0.40 +
        market*0.60,
        2
    )

    REPORT["ranking"].append({

        "engine":engine,

        "occurrences":occ,

        "market":market,

        "maturity":maturity,

        "score":score

    })

REPORT["ranking"].sort(
    key=lambda x:x["score"],
    reverse=True
)

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        REPORT,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*60)
print("IOTEC PRODUCT SCORING ENGINE")
print("="*60)

print()

for i,item in enumerate(REPORT["ranking"],1):

    print(
        f"{i:02d} - "
        f"{item['engine']:22}"
        f"Score:{item['score']:6}"
        f"  Motores:{item['occurrences']}"
    )

print()

print("Arquivo gerado:")
print(OUTPUT)

print()

print("STATUS: OK")

