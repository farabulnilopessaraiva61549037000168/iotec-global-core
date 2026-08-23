import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO = "IOTEC_PIPELINE_DATABASE.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

print("")
print("===================================")
print("IOTEC NEXT ACTION ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

leads = dados.get("leads", [])
propostas = dados.get("propostas", [])
contratos = dados.get("contratos", [])
receitas = dados.get("receita", [])

acoes = []

for lead in leads:
    pass

    possui_proposta = False

    for proposta in propostas:
        pass

        if proposta.get("lead_id") == lead["id"]:
            pass

            possui_proposta = True
            break

    if not possui_proposta:
        pass

        acoes.append({

            "prioridade": 1,
            "acao":
            f"GERAR PROPOSTA PARA {lead['id']}"
        })

for proposta in propostas:
    pass

    possui_contrato = False

    for contrato in contratos:
        pass

        if contrato.get("proposta_id") == proposta["id"]:
            pass

            possui_contrato = True
            break

    if not possui_contrato:
        pass

        acoes.append({

            "prioridade": 2,
            "acao":
            f"FAZER FOLLOW-UP DE {proposta['id']}"
        })

for contrato in contratos:
    pass

    possui_receita = False

    for receita in receitas:
        pass

        if receita.get("contrato_id") == contrato["id"]:
            pass

            possui_receita = True
            break

    if not possui_receita:
        pass

        acoes.append({

            "prioridade": 3,
            "acao":
            f"COBRAR CONTRATO {contrato['id']}"
        })

acoes.sort(
    key=lambda x: x["prioridade"]
)

print("")
print("===================================")
print("PROXIMAS ACOES")
print("===================================")

if not acoes:
    pass

    print("")
    print("PIPELINE SEM PENDENCIAS")

else:
    pass

    for i, acao in enumerate(
        acoes,
        start=1
    ):

        print("")
        print(f"#{i}")
        print(acao["acao"])

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "TODO GARGALO DEVE "
    "GERAR UMA ACAO."
)

print("")
print("NEXT ACTION ENGINE ATIVO")




