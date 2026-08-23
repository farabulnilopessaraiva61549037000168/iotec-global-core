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

leads = dados.get("leads", [])
propostas = dados.get("propostas", [])
contratos = dados.get("contratos", [])
receitas = dados.get("receita", [])

valor_receita = sum(
    item.get("valor", 0)
    for item in receitas
)

meta = 100000

atingimento = (
    valor_receita / meta * 100
    if meta > 0
    else 0
)

print("")
print("===================================")
print("IOTEC EXECUTIVE DASHBOARD")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("FUNIL EXECUTIVO")
print("===================================")

print("LEADS:", len(leads))
print("PROPOSTAS:", len(propostas))
print("CONTRATOS:", len(contratos))
print("RECEITAS:", len(receitas))

print("")
print("===================================")
print("CONVERSAO")
print("===================================")

lead_proposta = (
    len(propostas) / len(leads) * 100
    if len(leads)
    else 0
)

proposta_contrato = (
    len(contratos) / len(propostas) * 100
    if len(propostas)
    else 0
)

contrato_receita = (
    len(receitas) / len(contratos) * 100
    if len(contratos)
    else 0
)

print(
    "LEAD -> PROPOSTA:",
    f"{lead_proposta:.2f}%"
)

print(
    "PROPOSTA -> CONTRATO:",
    f"{proposta_contrato:.2f}%"
)

print(
    "CONTRATO -> RECEITA:",
    f"{contrato_receita:.2f}%"
)

print("")
print("===================================")
print("RECEITA")
print("===================================")

print(
    "RECEITA TOTAL:",
    f"R$ {valor_receita:,.2f}"
)

print(
    "META:",
    f"R$ {meta:,.2f}"
)

print(
    "ATINGIMENTO:",
    f"{atingimento:.2f}%"
)

print("")
print("===================================")
print("PROXIMA ACAO")
print("===================================")

pendencias = 0

for proposta in propostas:
    pass

    possui_contrato = any(

        contrato.get("proposta_id")
        == proposta["id"]

        for contrato in contratos
    )

    if not possui_contrato:
        pass

        pendencias += 1

        print(
            "FOLLOW-UP:",
            proposta["id"]
        )

if pendencias == 0:
    pass

    print(
        "SEM PENDENCIAS"
    )

print("")
print("===================================")
print("STATUS")
print("===================================")

if pendencias == 0:
    pass

    print(
        "PIPELINE SAUDAVEL"
    )

else:
    pass

    print(
        "PIPELINE EM EXPANSAO"
    )

print("")
print("DASHBOARD ATIVO")




