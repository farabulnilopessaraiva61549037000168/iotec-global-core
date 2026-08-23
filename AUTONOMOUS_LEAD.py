import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - AUTONOMOUS LEAD HUNTER
# ============================================================
#
# OBJETIVO:
# Tornar o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo capaz de:
#
# - procurar oportunidades
# - registrar leads
# - classificar tickets
# - calcular potencial econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mico
# - gerar command tower
# - construir inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia comercial
#
# ============================================================

import json
import random
import math
import time
from datetime import datetime

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

LEADS_DIARIOS = 300

CONVERSAO_BASE = 0.12

RECORRENCIA = 0.38

SETOR_TICKETS = {

    "educacao": [800, 6000],

    "juridico": [3000, 18000],

    "corporativo": [5000, 30000],

    "automacao": [4000, 50000],

    "ia": [8000, 120000],

    "governo": [15000, 250000],

    "saude": [6000, 45000]

}

# ============================================================
# ESTRUTURA CENTRAL
# ============================================================

command_tower = {

    "timestamp": str(datetime.now()),

    "runtime": "ONLINE",

    "mode": "ECONOMIC_HUNTER",

    "leads": [],

    "setores": {},

    "receita_total": 0,

    "receita_recorrente": 0,

    "clientes_convertidos": 0

}

# ============================================================
# GERADOR DE LEADS
# ============================================================

print("\n")
print("======================================================")
print(" IOTEC AUTONOMOUS LEAD HUNTER")
print("======================================================")
print("\n")

print("[1/9] Escaneando rede econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mica...\n")

for i in range(LEADS_DIARIOS):
    pass

    setor = random.choice(
        list(SETOR_TICKETS.keys())
    )

    prioridade = random.randint(1, 10)

    urgencia = random.randint(1, 10)

    capacidade_financeira = random.randint(1, 10)

    maturidade_digital = random.randint(1, 10)

    interesse = (

        prioridade +

        urgencia +

        capacidade_financeira +

        maturidade_digital

    ) / 4

    conversao = (

        interesse / 10

    ) * CONVERSAO_BASE

    conversao = min(conversao, 0.94)

    convertido = (
        random.random() <= conversao
    )

    ticket = random.randint(

        SETOR_TICKETS[setor][0],

        SETOR_TICKETS[setor][1]

    )

    recorrente = (
        random.random() <= RECORRENCIA
    )

    score = round(

        (
            interesse * 2.2
        ) +
        (
            ticket / 1000
        ),

        2

    )

    lead = {

        "id": i + 1,

        "setor": setor,

        "prioridade": prioridade,

        "urgencia": urgencia,

        "capacidade_financeira": capacidade_financeira,

        "maturidade_digital": maturidade_digital,

        "interesse": round(interesse, 2),

        "conversao": round(conversao, 3),

        "convertido": convertido,

        "ticket": ticket,

        "recorrente": recorrente,

        "score": score

    }

    command_tower["leads"].append(lead)

print("[OK] Rede econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mica escaneada\n")

# ============================================================
# PROCESSAMENTO ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICO
# ============================================================

print("[2/9] Processando arrecadaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o...\n")

for lead in command_tower["leads"]:
    pass

    setor = lead["setor"]

    if setor not in command_tower["setores"]:
        pass

        command_tower["setores"][setor] = {

            "leads": 0,

            "clientes": 0,

            "receita": 0

        }

    command_tower["setores"][setor]["leads"] += 1

    if lead["convertido"]:
        pass

        command_tower["clientes_convertidos"] += 1

        command_tower["receita_total"] += lead["ticket"]

        command_tower["setores"][setor]["clientes"] += 1

        command_tower["setores"][setor]["receita"] += lead["ticket"]

        if lead["recorrente"]:
            pass

            recorrencia = lead["ticket"] * 0.35

            command_tower["receita_recorrente"] += recorrencia

# ============================================================
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLCULO OPERACIONAL
# ============================================================

print("[3/9] Construindo score operacional...\n")

receita_final = (

    command_tower["receita_total"]

    +

    command_tower["receita_recorrente"]

)

ticket_medio = (

    receita_final /

    max(command_tower["clientes_convertidos"], 1)

)

score_operacional = (

    (
        receita_final / 10000
    )

    +

    (
        ticket_medio / 1000
    )

    +

    (
        command_tower["clientes_convertidos"] * 1.5
    )

)

# ============================================================
# PROJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

print("[4/9] Projetando expansÃƒÆ'Ã†â€™o econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mica...\n")

mensal = receita_final * 30

anual = mensal * 12

# ============================================================
# RANKING DE SETORES
# ============================================================

print("[5/9] Ranqueando setores...\n")

ranking = sorted(

    command_tower["setores"].items(),

    key=lambda x: x[1]["receita"],

    reverse=True

)

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICO
# ============================================================

print("[6/9] Construindo relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio militar...\n")

command_tower["score_operacional"] = round(
    score_operacional,
    2
)

command_tower["ticket_medio"] = round(
    ticket_medio,
    2
)

command_tower["receita_final"] = round(
    receita_final,
    2
)

command_tower["mensal"] = round(
    mensal,
    2
)

command_tower["anual"] = round(
    anual,
    2
)

command_tower["ranking"] = ranking

# ============================================================
# SALVAMENTO
# ============================================================

print("[7/9] Salvando intelligence report...\n")

with open(

    "COMMAND_TOWER_REPORT.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        command_tower,

        f,

        indent=4,

        ensure_ascii=False

    )

# ============================================================
# DASHBOARD TERMINAL
# ============================================================

print("======================================================")
print(" COMMAND TOWER")
print("======================================================")
print("\n")

print(f"Leads captados: {LEADS_DIARIOS}")

print(
    f"Clientes convertidos: "
    f"{command_tower['clientes_convertidos']}"
)

print(
    f"Ticket mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dio: "
    f"R$ {ticket_medio:,.2f}"
)

print(
    f"Receita diÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria: "
    f"R$ {receita_final:,.2f}"
)

print(
    f"Receita mensal: "
    f"R$ {mensal:,.2f}"
)

print(
    f"Receita anual: "
    f"R$ {anual:,.2f}"
)

print(
    f"Score operacional: "
    f"{score_operacional:,.2f}"
)

print("\n")

print("======================================================")
print(" RANKING ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICO")
print("======================================================")
print("\n")

for setor, dados in ranking:
    pass

    print(f"SETOR: {setor.upper()}")

    print(f"Leads: {dados['leads']}")

    print(f"Clientes: {dados['clientes']}")

    print(
        f"Receita: "
        f"R$ {dados['receita']:,.2f}"
    )

    print("\n")

# ============================================================
# ENCERRAMENTO
# ============================================================

print("======================================================")
print(" IOTEC ECONOMIC NETWORK ONLINE")
print("======================================================")
print("\n")
print("[8/9] Command Tower sincronizada")
print("[9/9] Runtime econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mico operacional")
print("\n")
print("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO PRONTO PARA CAPTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O")
print("\n")




