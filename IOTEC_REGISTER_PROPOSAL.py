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

if "propostas" not in dados:
    dados["propostas"] = []

proposta = {

    "data": str(datetime.now()),
    "cliente": "LEAD_PORTAL",
    "produto": "PLANO_DE_CONTINGENCIA",
    "valor": 8900,
    "status": "ENVIADA"
}

dados["propostas"].append(proposta)

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
print("PROPOSTA REGISTRADA")
print(proposta)




