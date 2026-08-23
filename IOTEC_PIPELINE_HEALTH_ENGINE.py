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
print("IOTEC PIPELINE HEALTH ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("VERIFICANDO INTEGRIDADE")
print("===================================")

propostas_orfas = []

for proposta in dados["propostas"]:
    pass

    if not proposta.get("lead_id"):
        pass

        propostas_orfas.append(
            proposta
        )

contratos_orfos = []

ids_propostas = {

    p["id"]

    for p in dados["propostas"]
}

for contrato in dados["contratos"]:
    pass

    if (
        contrato.get("proposta_id")
        not in ids_propostas
    ):

        contratos_orfos.append(
            contrato
        )

receitas_orfas = []

ids_contratos = {

    c["id"]

    for c in dados["contratos"]
}

for receita in dados["receita"]:
    pass

    if (
        receita.get("contrato_id")
        not in ids_contratos
    ):

        receitas_orfas.append(
            receita
        )

print("")
print("PROPOSTAS ORFAS:")
print(len(propostas_orfas))

for item in propostas_orfas:
    pass

    print("")
    print(item["id"])

print("")
print("CONTRATOS ORFOS:")
print(len(contratos_orfos))

print("")
print("RECEITAS ORFAS:")
print(len(receitas_orfas))

print("")
print("===================================")
print("STATUS")
print("===================================")

if (
    len(propostas_orfas) == 0
    and
    len(contratos_orfos) == 0
    and
    len(receitas_orfas) == 0
):

    print("BASE INTEGRA")

else:
    pass

    print("INCONSISTENCIAS DETECTADAS")

print("")
print("HEALTH ENGINE ATIVO")




