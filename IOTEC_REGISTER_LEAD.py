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

lead = {

    "data": str(datetime.now()),
    "produto": "PLANO_DE_CONTINGENCIA",
    "origem": "PORTAL"
}

dados["leads"].append(lead)

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
print("LEAD REGISTRADO")
print(lead)




