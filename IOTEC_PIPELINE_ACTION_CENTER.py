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
print("IOTEC PIPELINE ACTION CENTER")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

leads = dados.get("leads", [])
propostas = dados.get("propostas", [])
contratos = dados.get("contratos", [])
receitas = dados.get("receita", [])

print("")
print("===================================")
print("ACOES NECESSARIAS")
print("===================================")

acoes = 0

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

        acoes += 1

        print("")
        print("LEAD SEM PROPOSTA")
        print("-----------------")
        print("ID:", lead["id"])
        print("PRODUTO:", lead.get("produto"))

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

        acoes += 1

        print("")
        print("PROPOSTA SEM CONTRATO")
        print("---------------------")
        print("ID:", proposta["id"])
        print("VALOR:", proposta.get("valor"))

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

        acoes += 1

        print("")
        print("CONTRATO SEM RECEITA")
        print("--------------------")
        print("ID:", contrato["id"])
        print("VALOR:", contrato.get("valor"))

print("")
print("===================================")
print("RESUMO EXECUTIVO")
print("===================================")

print("")
print("LEADS:", len(leads))
print("PROPOSTAS:", len(propostas))
print("CONTRATOS:", len(contratos))
print("RECEITAS:", len(receitas))

print("")
print("ACOES PENDENTES:")
print(acoes)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

if acoes == 0:
    pass

    print("PIPELINE COMPLETAMENTE SAUDAVEL")

else:
    pass

    print("EXISTEM ETAPAS PENDENTES")

print("")
print("ACTION CENTER ATIVO")




