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
print("IOTEC PIPELINE RECONCILIATOR")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

leads = dados["leads"]
propostas = dados["propostas"]

leads_sem_proposta = []

for lead in leads:
    pass

    possui = False

    for proposta in propostas:
        pass

        if proposta.get("lead_id") == lead["id"]:
            pass

            possui = True
            break

    if not possui:
        pass

        leads_sem_proposta.append(
            lead["id"]
        )

propostas_orfas = []

for proposta in propostas:
    pass

    if not proposta.get("lead_id"):
        pass

        propostas_orfas.append(
            proposta
        )

correcoes = 0

while (
    leads_sem_proposta
    and
    propostas_orfas
):

    lead = leads_sem_proposta.pop(0)

    proposta = propostas_orfas.pop(0)

    proposta["lead_id"] = lead

    correcoes += 1

    print("")
    print(
        proposta["id"],
        "->",
        lead
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

print("")
print("RECONCILIADOR ATIVO")




