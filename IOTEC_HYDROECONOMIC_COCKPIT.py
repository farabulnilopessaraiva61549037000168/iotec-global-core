import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

REPORT = r"C:\IOTEC\IOTEC_HYDROECONOMIC_REPORT.json"

try:
    pass

    with open(
        REPORT,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

except:
    pass

    print("RELATORIO NAO ENCONTRADO")
    raise SystemExit

reservoir = data.get("reservoir", 0)

accounts = data.get("accounts", 0)

leads = data.get("leads", 0)

opportunities = data.get(
    "opportunities",
    0
)

proposals = data.get(
    "proposals",
    0
)

contracts = data.get(
    "contracts",
    0
)

revenue = data.get(
    "revenue",
    0
)

# ==========================
# NIVEL DA BARRAGEM
# ==========================

MAX_CAPACITY = 1000

reservoir_level = (
    reservoir /
    MAX_CAPACITY
) * 100

if reservoir_level > 100:
    reservoir_level = 100

# ==========================
# VAZAO
# ==========================

flow = (
    leads +
    opportunities +
    proposals +
    contracts
)

# ==========================
# EFICIENCIAS REAIS
# ==========================

if opportunities > 0:
    pass

    proposal_rate = (
        proposals /
        opportunities
    ) * 100

else:
    pass

    proposal_rate = 0

if proposals > 0:
    pass

    contract_rate = (
        contracts /
        proposals
    ) * 100

else:
    pass

    contract_rate = 0

# ==========================
# POTENCIA
# ==========================

power = (
    proposal_rate *
    contract_rate
) / 100

# ==========================
# ESTAGIO DA USINA
# ==========================

if revenue < 10000:
    pass

    stage = "EM EXPANSAO"

elif revenue < 50000:
    pass

    stage = "MONETIZANDO"

elif revenue < 250000:
    pass

    stage = "EM ESCALA"

else:
    pass

    stage = "OPERACAO CONSOLIDADA"

# ==========================
# PROJECAO
# ==========================

next_contracts = contracts * 2

next_revenue = revenue * 2

# ==========================
# RELATORIO
# ==========================

print("")
print("===================================")
print("IOTEC HYDROECONOMIC COCKPIT")
print("===================================")
print("")

print(
    f"NIVEL DA BARRAGEM: "
    f"{reservoir_level:.2f}%"
)

print(
    f"RESERVATORIO: "
    f"{reservoir}"
)

print("")

print("VAZAO")

print(
    f"EVENTOS: "
    f"{flow}"
)

print(
    f"CONTAS: "
    f"{accounts}"
)

print(
    f"LEADS: "
    f"{leads}"
)

print(
    f"OPORTUNIDADES: "
    f"{opportunities}"
)

print(
    f"PROPOSTAS: "
    f"{proposals}"
)

print(
    f"CONTRATOS: "
    f"{contracts}"
)

print("")
print("TURBINAS")

print(
    f"OPP->PROPOSTA: "
    f"{proposal_rate:.2f}%"
)

print(
    f"PROPOSTA->CONTRATO: "
    f"{contract_rate:.2f}%"
)

print("")
print(
    f"POTENCIA ECONOMICA: "
    f"{power:.2f}%"
)

print("")
print(
    f"GERACAO: "
    f"R$ {revenue:,.2f}"
)

print("")
print("PROJECAO")

print(
    f"CONTRATOS FUTUROS: "
    f"{next_contracts}"
)

print(
    f"RECEITA FUTURA: "
    f"R$ {next_revenue:,.2f}"
)

print("")
print(
    f"STATUS DA USINA: "
    f"{stage}"
)

print("")
print(
    f"GERADO EM: "
    f"{datetime.now()}"
)

print("")
print("CONCLUIDO")




