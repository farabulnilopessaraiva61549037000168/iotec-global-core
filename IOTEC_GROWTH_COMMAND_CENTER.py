import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC GROWTH COMMAND CENTER
# CENTRO DE COMANDO DE CRESCIMENTO
# ==========================================================

import json
from datetime import datetime

TRACTION = r"C:\IOTEC\IOTEC_TRACTION_REPORT.json"
FLOW = r"C:\IOTEC\IOTEC_REVENUE_FLOW_REPORT.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_GROWTH_COMMAND_CENTER.json"
OUTPUT_TXT = r"C:\IOTEC\IOTEC_GROWTH_COMMAND_CENTER.txt"

# ==========================================================
# CARREGA
# ==========================================================

with open(TRACTION, "r", encoding="utf-8") as f:
    traction = json.load(f)

with open(FLOW, "r", encoding="utf-8") as f:
    flow = json.load(f)

# ==========================================================
# DADOS ATUAIS
# ==========================================================

current_leads = traction["current"]["leads"]
current_clients = traction["current"]["clients"]
current_payments = traction["current"]["payments"]

target_leads = traction["targets_30_days"]["leads"]
target_clients = traction["targets_30_days"]["clients"]
target_payments = traction["targets_30_days"]["payments"]

# ==========================================================
# GAP
# ==========================================================

gap_leads = max(0, target_leads - current_leads)
gap_clients = max(0, target_clients - current_clients)
gap_payments = max(0, target_payments - current_payments)

# ==========================================================
# PLANO
# ==========================================================

daily_leads_needed = round(gap_leads / 30, 2)
weekly_clients_needed = round(gap_clients / 4, 2)

actions = []

if gap_leads > 0:
    pass

    actions.append(
        f"Captar {daily_leads_needed} leads por dia"
    )

    actions.append(
        "Executar prospecÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o diÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria"
    )

    actions.append(
        "Publicar conteÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºdo diariamente"
    )

if gap_clients > 0:
    pass

    actions.append(
        f"Converter {weekly_clients_needed} clientes por semana"
    )

if gap_payments > 0:
    pass

    actions.append(
        "Gerar novas propostas comerciais"
    )

    actions.append(
        "Executar follow-up automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico"
    )

# ==========================================================
# SCORE
# ==========================================================

progress = 0

if target_leads:
    progress += (current_leads / target_leads) * 40

if target_clients:
    progress += (current_clients / target_clients) * 30

if target_payments:
    progress += (current_payments / target_payments) * 30

progress = round(min(progress, 100), 2)

# ==========================================================
# RELATORIO
# ==========================================================

report = {

    "generated": str(datetime.now()),

    "current": {

        "leads": current_leads,
        "clients": current_clients,
        "payments": current_payments

    },

    "targets": {

        "leads": target_leads,
        "clients": target_clients,
        "payments": target_payments

    },

    "gap": {

        "leads": gap_leads,
        "clients": gap_clients,
        "payments": gap_payments

    },

    "growth_progress": progress,

    "actions": actions
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
    f.write("IOTEC GROWTH COMMAND CENTER\n")
    f.write("===================================\n\n")

    f.write(
        f"LEADS: {current_leads}/{target_leads}\n"
    )

    f.write(
        f"CLIENTES: {current_clients}/{target_clients}\n"
    )

    f.write(
        f"PAGAMENTOS: {current_payments}/{target_payments}\n\n"
    )

    f.write(
        f"GAP LEADS: {gap_leads}\n"
    )

    f.write(
        f"GAP CLIENTES: {gap_clients}\n"
    )

    f.write(
        f"GAP PAGAMENTOS: {gap_payments}\n\n"
    )

    f.write(
        f"PROGRESSO: {progress}%\n\n"
    )

    f.write("ACOES\n")
    f.write("-------------------------\n")

    for action in actions:
        pass

        f.write(
            f"- {action}\n"
        )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC GROWTH COMMAND CENTER")
print("===================================")

print("")
print("PROGRESSO:", progress, "%")

print("")
print("GAPS")

print("LEADS:", gap_leads)
print("CLIENTES:", gap_clients)
print("PAGAMENTOS:", gap_payments)

print("")
print("ACOES")

for action in actions:
    pass

    print("-", action)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")




