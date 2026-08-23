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
print("IOTEC AUTOMATION COMMAND ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

leads = dados.get("leads", [])
propostas = dados.get("propostas", [])
contratos = dados.get("contratos", [])

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

        nova_proposta = {

            "id":
            f"PROP_{len(propostas)+1:04d}",

            "lead_id":
            lead["id"],

            "cliente":
            "AUTO_PIPELINE",

            "produto":
            lead.get("produto"),

            "valor":
            8900,

            "status":
            "GERADA_AUTOMATICAMENTE",

            "data":
            str(datetime.now())
        }

        propostas.append(
            nova_proposta
        )

        acoes.append(
            f"PROPOSTA CRIADA -> {nova_proposta['id']}"
        )

dados["propostas"] = propostas

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
print("ACOES EXECUTADAS")
print("===================================")

if not acoes:
    pass

    print("")
    print("NENHUMA ACAO NECESSARIA")

else:
    pass

    for acao in acoes:
        pass

        print(acao)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "IDENTIFICAR GARGALO, "
    "EXECUTAR ACAO."
)

print("")
print("AUTOMATION COMMAND ENGINE ATIVO")




