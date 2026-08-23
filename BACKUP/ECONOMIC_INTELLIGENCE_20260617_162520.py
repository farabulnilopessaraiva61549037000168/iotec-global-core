import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import random
import math
from datetime import datetime

# ============================================================
# IOTEC - ECONOMIC INTELLIGENCE ENGINE
# ============================================================

print("\n")
print("===================================================")
print(" IOTEC ECONOMIC INTELLIGENCE ENGINE")
print("===================================================")
print("\n")

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ============================================================

LEADS_DIA = 120

CONVERSAO_MEDIA = 0.14

TICKET_MIN = 800
TICKET_MAX = 18000

RECORRENCIA = 0.32

SETOR_PESOS = {

    "educacao": 1.2,
    "corporativo": 1.8,
    "juridico": 1.5,
    "saude": 2.0,
    "automacao": 2.4,
    "ia": 2.8,
    "governo": 3.2

}

# ============================================================
# GERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE LEADS
# ============================================================

print("[1/8] Gerando rede de leads...\n")

leads = []

for i in range(LEADS_DIA):
    pass

    setor = random.choice(list(SETOR_PESOS.keys()))

    prioridade = random.randint(1, 10)

    urgencia = random.randint(1, 10)

    capacidade_financeira = random.randint(1, 10)

    interesse = (
        prioridade
        + urgencia
        + capacidade_financeira
    ) / 3

    peso = SETOR_PESOS[setor]

    chance_conversao = (
        interesse / 10
    ) * CONVERSAO_MEDIA * peso

    chance_conversao = min(chance_conversao, 0.92)

    convertido = random.random() <= chance_conversao

    ticket = random.randint(TICKET_MIN, TICKET_MAX)

    recorrente = random.random() <= RECORRENCIA

    leads.append({

        "id": i + 1,

        "setor": setor,

        "prioridade": prioridade,

        "urgencia": urgencia,

        "capacidade_financeira": capacidade_financeira,

        "interesse": round(interesse, 2),

        "chance_conversao": round(chance_conversao, 3),

        "convertido": convertido,

        "ticket": ticket,

        "recorrente": recorrente

    })

print("[OK] Leads gerados\n")

# ============================================================
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLCULO DE FATURAMENTO
# ============================================================

print("[2/8] Calculando arrecadaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o operacional...\n")

faturamento = 0

faturamento_recorrente = 0

clientes_convertidos = 0

for lead in leads:
    pass

    if lead["convertido"]:
        pass

        clientes_convertidos += 1

        faturamento += lead["ticket"]

        if lead["recorrente"]:
            pass

            faturamento_recorrente += (
                lead["ticket"] * 0.35
            )

faturamento_total = (
    faturamento +
    faturamento_recorrente
)

ticket_medio = (
    faturamento_total / clientes_convertidos
    if clientes_convertidos > 0
    else 0
)

# ============================================================
# INTELIGÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA SETORIAL
# ============================================================

print("[3/8] Escaneando setores econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´micos...\n")

setores = {}

for lead in leads:
    pass

    setor = lead["setor"]

    if setor not in setores:
        pass

        setores[setor] = {

            "leads": 0,
            "clientes": 0,
            "receita": 0

        }

    setores[setor]["leads"] += 1

    if lead["convertido"]:
        pass

        setores[setor]["clientes"] += 1

        setores[setor]["receita"] += lead["ticket"]

# ============================================================
# SCORE OPERACIONAL
# ============================================================

print("[4/8] Calculando score operacional...\n")

score_operacional = (

    (clientes_convertidos * 1.8)

    + (ticket_medio / 100)

    + (faturamento_total / 10000)

)

score_operacional = round(score_operacional, 2)

# ============================================================
# PROJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O MENSAL
# ============================================================

print("[5/8] Projetando crescimento mensal...\n")

faturamento_mensal = faturamento_total * 30

faturamento_anual = faturamento_mensal * 12

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO MASTER
# ============================================================

print("[6/8] Construindo relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gico...\n")

relatorio = {

    "timestamp": str(datetime.now()),

    "leads_dia": LEADS_DIA,

    "clientes_convertidos": clientes_convertidos,

    "ticket_medio": round(ticket_medio, 2),

    "faturamento_diario": round(faturamento_total, 2),

    "faturamento_mensal": round(faturamento_mensal, 2),

    "faturamento_anual": round(faturamento_anual, 2),

    "score_operacional": score_operacional,

    "setores": setores

}

# ============================================================
# SALVAMENTO
# ============================================================

print("[7/8] Salvando relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio...\n")

with open(
    "IOTEC_ECONOMIC_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

# ============================================================
# EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

print("===================================================")
print(" IOTEC ECONOMIC REPORT")
print("===================================================")
print("\n")

print(f"Leads captados por dia: {LEADS_DIA}")

print(f"Clientes convertidos: {clientes_convertidos}")

print(f"Ticket mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dio: R$ {ticket_medio:,.2f}")

print(f"Faturamento diÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio: R$ {faturamento_total:,.2f}")

print(f"Faturamento mensal: R$ {faturamento_mensal:,.2f}")

print(f"Faturamento anual: R$ {faturamento_anual:,.2f}")

print(f"Score operacional: {score_operacional}")

print("\n")

print("===================================================")
print(" SETORES ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICOS")
print("===================================================")
print("\n")

for setor, dados in setores.items():
    pass

    print(f"SETOR: {setor.upper()}")

    print(f"Leads: {dados['leads']}")

    print(f"Clientes: {dados['clientes']}")

    print(f"Receita: R$ {dados['receita']:,.2f}")

    print("\n")

print("===================================================")
print(" COMMAND TOWER ONLINE")
print("===================================================")
print("\n")


