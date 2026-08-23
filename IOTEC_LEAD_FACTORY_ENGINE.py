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

novo_id = f"LEAD_{len(leads)+1:04d}"

novo_lead = {

    "id": novo_id,
    "data": str(datetime.now()),
    "produto": "PLANO_DE_CONTINGENCIA",
    "origem": "PORTAL_REAL",
    "status": "NOVO"
}

leads.append(novo_lead)

dados["leads"] = leads

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
print("IOTEC LEAD FACTORY ENGINE")
print("===================================")

print("")
print("NOVO LEAD CRIADO")
print(novo_lead)

print("")
print("TOTAL DE LEADS:")
print(len(leads))




