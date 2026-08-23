import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC DAILY GROWTH MISSION ENGINE
# MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O COMERCIAL AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA
# ==========================================================

import json
from datetime import datetime

COCKPIT = r"C:\IOTEC\IOTEC_EXECUTIVE_COCKPIT.json"
CLUSTERS = r"C:\IOTEC\IOTEC_CAPABILITY_CLUSTERS.json"
READINESS = r"C:\IOTEC\IOTEC_REVENUE_READINESS_REPORT.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_DAILY_GROWTH_MISSION.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_DAILY_GROWTH_MISSION.txt"

# ==========================================================
# CARREGA
# ==========================================================

with open(COCKPIT,"r",encoding="utf-8") as f:
    cockpit = json.load(f)

with open(CLUSTERS,"r",encoding="utf-8") as f:
    clusters = json.load(f)

with open(READINESS,"r",encoding="utf-8") as f:
    readiness = json.load(f)

# ==========================================================
# ESCOLHE PRODUTO MAIS MADURO
# ==========================================================

best_name = None
best_score = -1

if "capabilities" in readiness:
    pass

    for item in readiness["capabilities"]:
        pass

        score = item.get(
            "maturity",
            0
        )

        if score > best_score:
            pass

            best_score = score
            best_name = item.get(
                "capability"
            )

# ==========================================================
# FALLBACK
# ==========================================================

if not best_name:
    pass

    best_name = "AUDITORIA_OPERACIONAL"
    best_score = 50

# ==========================================================
# MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

progress = cockpit.get(
    "growth_progress",
    0
)

if progress < 20:
    pass

    leads_target = 5
    proposals_target = 2
    meetings_target = 1

elif progress < 50:
    pass

    leads_target = 10
    proposals_target = 4
    meetings_target = 2

else:
    pass

    leads_target = 20
    proposals_target = 8
    meetings_target = 4

# ==========================================================
# RECEITA POTENCIAL
# ==========================================================

ticket = 5000

potential_revenue = (
    meetings_target *
    ticket
)

# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

report = {

    "generated":
    str(datetime.now()),

    "priority_product":
    best_name,

    "maturity":
    best_score,

    "mission": {

        "leads":
        leads_target,

        "proposals":
        proposals_target,

        "meetings":
        meetings_target

    },

    "potential_revenue":
    potential_revenue
}

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
    f.write("IOTEC DAILY GROWTH MISSION\n")
    f.write("===================================\n\n")

    f.write(
        f"PRODUTO PRIORITARIO: {best_name}\n"
    )

    f.write(
        f"MATURIDADE: {best_score}\n\n"
    )

    f.write("MISSAO DO DIA\n")
    f.write("-------------------------\n")

    f.write(
        f"LEADS: {leads_target}\n"
    )

    f.write(
        f"PROPOSTAS: {proposals_target}\n"
    )

    f.write(
        f"REUNIOES: {meetings_target}\n\n"
    )

    f.write(
        f"RECEITA POTENCIAL: R$ {potential_revenue:,.2f}\n"
    )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC DAILY GROWTH MISSION")
print("===================================")

print("")
print(
    "PRODUTO:",
    best_name
)

print(
    "MATURIDADE:",
    best_score
)

print("")
print("MISSAO")

print(
    "LEADS:",
    leads_target
)

print(
    "PROPOSTAS:",
    proposals_target
)

print(
    "REUNIOES:",
    meetings_target
)

print("")
print(
    "RECEITA POTENCIAL:",
    potential_revenue
)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")


