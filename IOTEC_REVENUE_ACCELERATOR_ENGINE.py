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

leads = len(dados.get("leads", []))
propostas = len(dados.get("propostas", []))
contratos = len(dados.get("contratos", []))

print("")
print("===================================")
print("IOTEC REVENUE ACCELERATOR")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("LEADS:")
print(leads)

print("PROPOSTAS:")
print(propostas)

print("CONTRATOS:")
print(contratos)

print("")
print("ACOES NECESSARIAS")
print("===================================")

if leads > propostas:
    pass

    faltantes = leads - propostas

    print("")
    print("ALERTA:")
    print(
        f"{faltantes} LEADS SEM PROPOSTA"
    )

if propostas > contratos:
    pass

    faltantes = propostas - contratos

    print("")
    print("ALERTA:")
    print(
        f"{faltantes} PROPOSTAS SEM CONTRATO"
    )

if leads == 0:
    pass

    print("")
    print("ALERTA:")
    print(
        "SEM LEADS NOVOS"
    )

print("")
print("ORDEM MOR:")
print(
    "TODO LEAD DEVE VIRAR PROPOSTA."
)

print("")
print("REVENUE ACCELERATOR ATIVO")




