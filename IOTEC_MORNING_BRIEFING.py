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

receita_total = sum(
    item.get("valor", 0)
    for item in receitas
)

ids_receita = {
    item.get("contrato_id")
    for item in receitas
}

valor_receber = 0
contratos_pendentes = []

for contrato in contratos:
    pass

    if contrato["id"] not in ids_receita:
        pass

        valor_receber += contrato.get(
            "valor",
            0
        )

        contratos_pendentes.append(
            contrato
        )

meta = 100000

atingimento = (
    receita_total / meta * 100
    if meta > 0
    else 0
)

print("")
print("===================================")
print("IOTEC MORNING BRIEFING")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("INDICADORES")
print("===================================")

print("")
print("VISITAS:")
print(
    len(
        dados.get(
            "visitas",
            []
        )
    )
)

print("")
print("LEADS:")
print(len(leads))

print("")
print("PROPOSTAS:")
print(len(propostas))

print("")
print("CONTRATOS:")
print(len(contratos))

print("")
print("RECEITAS:")
print(len(receitas))

print("")
print("===================================")
print("FINANCEIRO")
print("===================================")

print("")
print(
    "FATURADO:"
)
print(
    f"R$ {receita_total:,.2f}"
)

print("")
print(
    "A RECEBER:"
)
print(
    f"R$ {valor_receber:,.2f}"
)

print("")
print(
    "POTENCIAL TOTAL:"
)
print(
    f"R$ {receita_total + valor_receber:,.2f}"
)

print("")
print(
    "META:"
)
print(
    f"R$ {meta:,.2f}"
)

print("")
print(
    "ATINGIMENTO:"
)
print(
    f"{atingimento:.2f}%"
)

print("")
print("===================================")
print("PRIORIDADES")
print("===================================")

if contratos_pendentes:
    pass

    for contrato in contratos_pendentes:
        pass

        print("")
        print(
            "FOLLOW-UP:"
        )

        print(
            contrato["id"]
        )

        print(
            "VALOR:"
        )

        print(
            f"R$ {contrato['valor']:,.2f}"
        )

else:
    pass

    print("")
    print(
        "SEM PENDENCIAS"
    )

print("")
print("===================================")
print("STATUS DO NUCLEO")
print("===================================")

if contratos_pendentes:
    pass

    print(
        "NUCLEO OPERACIONAL"
    )

    print(
        "EXISTEM RECEITAS A CAPTURAR"
    )

else:
    pass

    print(
        "PIPELINE TOTALMENTE CONCLUIDO"
    )

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "TRANSFORMAR CONTRATOS "
    "EM RECEITA."
)

print("")
print("MORNING BRIEFING ATIVO")




