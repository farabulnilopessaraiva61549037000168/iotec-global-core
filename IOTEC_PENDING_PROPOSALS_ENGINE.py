import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO = "IOTEC_TRAFFIC_LOG.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

propostas = dados.get(
    "propostas",
    []
)

contratos = dados.get(
    "contratos",
    []
)

print("")
print("===================================")
print("IOTEC PENDING PROPOSALS ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("ANALISANDO PIPELINE")
print("===================================")

total_pendentes = 0

for indice, proposta in enumerate(
    propostas,
    start=1
):

    possui_contrato = False

    for contrato in contratos:
        pass

        if (
            contrato.get("cliente")
            ==
            proposta.get("cliente")
        ) and (
            contrato.get("produto")
            ==
            proposta.get("produto")
        ):

            possui_contrato = True
            break

    if not possui_contrato:
        pass

        total_pendentes += 1

        print("")
        print("-----------------------------------")
        print(f"PENDENCIA #{total_pendentes}")
        print("-----------------------------------")

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
                "NAO INFORMADO"
            )
        )

        print("")
        print("VALOR:")
        print(
            f"R$ {proposta.get('valor',0):,.2f}"
        )

        print("")
        print("STATUS:")
        print(
            proposta.get(
                "status",
                "DESCONHECIDO"
            )
        )

print("")
print("===================================")
print("RESUMO")
print("===================================")

print("")
print("PROPOSTAS:")
print(len(propostas))

print("")
print("CONTRATOS:")
print(len(contratos))

print("")
print("PENDENCIAS:")
print(total_pendentes)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

if total_pendentes > 0:
    pass

    print(
        "EXISTEM PROPOSTAS "
        "SEM CONTRATO."
    )

else:
    pass

    print(
        "TODAS AS PROPOSTAS "
        "POSSUEM CONTRATO."
    )

print("")
print("PENDING PROPOSALS ENGINE ATIVO")




