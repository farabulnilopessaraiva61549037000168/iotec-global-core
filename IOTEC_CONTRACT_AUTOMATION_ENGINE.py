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
print("IOTEC CONTRACT AUTOMATION ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

criados = 0

ids_contratos = {
    c.get("proposta_id")
    for c in contratos
}

for proposta in propostas:
    pass

    if proposta["id"] in ids_contratos:
        continue

    novo_contrato = {

        "id":
        f"CONT_{len(contratos)+1:04d}",

        "proposta_id":
        proposta["id"],

        "cliente":
        proposta["cliente"],

        "produto":
        proposta["produto"],

        "valor":
        proposta["valor"],

        "status":
        "AGUARDANDO_ASSINATURA",

        "data":
        str(datetime.now())
    }

    contratos.append(
        novo_contrato
    )

    criados += 1

    print("")
    print("CONTRATO GERADO:")
    print(novo_contrato["id"])

dados["contratos"] = contratos

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

print("CONTRATOS GERADOS:")
print(criados)

print("")
print("CONTRACT AUTOMATION ATIVO")




