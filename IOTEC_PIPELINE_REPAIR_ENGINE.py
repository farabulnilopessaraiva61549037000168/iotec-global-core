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
print("IOTEC PIPELINE REPAIR ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

leads = dados["leads"]
propostas = dados["propostas"]

ids_utilizados = set()

for proposta in propostas:
    pass

    if proposta.get("lead_id"):
        pass

        ids_utilizados.add(
            proposta["lead_id"]
        )

correcoes = 0

for proposta in propostas:
    pass

    if proposta.get("lead_id"):
        pass

        continue

    lead_livre = None

    for lead in leads:
        pass

        if lead["id"] not in ids_utilizados:
            pass

            lead_livre = lead["id"]
            break

    if lead_livre:
        pass

        proposta["lead_id"] = lead_livre

        ids_utilizados.add(
            lead_livre
        )

        correcoes += 1

        print("")
        print("CORRECAO:")
        print(
            proposta["id"],
            "->",
            lead_livre
        )

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dados,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("RESUMO")
print("===================================")

print("CORRECOES:")
print(correcoes)

if correcoes == 0:
    pass

    print("")
    print(
        "NENHUM LEAD DISPONIVEL "
        "PARA ASSOCIACAO."
    )

print("")
print("REPAIR ENGINE ATIVO")




