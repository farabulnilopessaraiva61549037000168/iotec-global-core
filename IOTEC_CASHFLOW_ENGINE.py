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

contratos = dados.get("contratos", [])
receitas = dados.get("receita", [])

print("")
print("===================================")
print("IOTEC CASHFLOW ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("CONTRATOS PENDENTES")
print("===================================")

pendentes = 0
valor_pendente = 0

ids_receita = {

    r.get("contrato_id")

    for r in receitas
}

for contrato in contratos:
    pass

    if contrato["id"] not in ids_receita:
        pass

        pendentes += 1

        valor_pendente += contrato.get(
            "valor",
            0
        )

        print("")
        print("CONTRATO:")
        print(contrato["id"])

        print("")
        print("CLIENTE:")
        print(
            contrato.get(
                "cliente",
                "-"
            )
        )

        print("")
        print("VALOR:")
        print(
            f"R$ {contrato.get('valor',0):,.2f}"
        )

        print("")
        print("STATUS:")
        print(
            contrato.get(
                "status",
                "-"
            )
        )

        print("")
        print("ACAO:")
        print(
            "COBRAR / RECEBER"
        )

print("")
print("===================================")
print("RESUMO FINANCEIRO")
print("===================================")

print("")
print("CONTRATOS PENDENTES:")
print(pendentes)

print("")
print("VALOR A RECEBER:")
print(
    f"R$ {valor_pendente:,.2f}"
)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "CONTRATO SEM RECEITA "
    "DEVE GERAR COBRANCA."
)

print("")
print("CASHFLOW ENGINE ATIVO")




