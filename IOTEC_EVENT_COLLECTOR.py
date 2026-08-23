import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import os
from datetime import datetime

ARQUIVO = "IOTEC_TRAFFIC_LOG.json"

if not os.path.exists(ARQUIVO):
    pass

    estrutura = {
        "visitas": [],
        "formularios": [],
        "leads": []
    }

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            estrutura,
            f,
            indent=4,
            ensure_ascii=False
        )

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

evento = {

    "data": str(datetime.now()),
    "pagina": "HOME",
    "origem": "PORTAL"
}

dados["visitas"].append(evento)

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
print("VISITA REGISTRADA")
print(evento)




