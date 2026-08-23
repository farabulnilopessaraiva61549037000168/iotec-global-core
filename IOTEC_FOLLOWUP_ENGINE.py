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

propostas = dados.get("propostas", [])
contratos = dados.get("contratos", [])

print("")
print("===================================")
print("IOTEC FOLLOWUP ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("PROPOSTAS PENDENTES")
print("===================================")

pendencias = 0

for proposta in propostas:
    pass

    possui_contrato = False

    for contrato in contratos:
        pass

        if (
            contrato.get("proposta_id")
            ==
            proposta["id"]
        ):

            possui_contrato = True
            break

    if not possui_contrato:
        pass

        pendencias += 1

        print("")
        print("-----------------------------------")
        print("PROPOSTA:")
        print(proposta["id"])

        print("")
        print("CLIENTE:")
        print(
            proposta.get(
                "cliente",
                "NAO INFORMADO"
            )
        )

        print("")
        print("PRODUTO:")
        print(
            proposta.get(
                "produto",
                "-"
            )
        )

        print("")
        print("VALOR:")
        print(
            f"R$ {proposta.get('valor',0):,.2f}"
        )

        print("")
        print("ACAO:")
        print(
            "REALIZAR FOLLOW-UP"
        )

        print("")
        print("PRIORIDADE:")
        print("ALTA")

        print("")
        print("STATUS:")
        print(
            proposta.get(
                "status",
                "-"
            )
        )

if pendencias == 0:
    pass

    print("")
    print("NENHUMA PENDENCIA")

print("")
print("===================================")
print("RESUMO")
print("===================================")

print("")
print("PROPOSTAS PENDENTES:")
print(pendencias)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "TODA PROPOSTA SEM "
    "CONTRATO DEVE "
    "GERAR FOLLOW-UP."
)

print("")
print("FOLLOWUP ENGINE ATIVO")




