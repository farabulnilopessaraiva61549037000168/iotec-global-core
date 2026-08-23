import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 EVENT BUS
# ============================================================

from datetime import datetime
import json

ARQUIVO = "X27_DATABASE.json"

def registrar(tipo, origem, mensagem):
    pass

    evento = {

        "data": str(datetime.now()),

        "tipo": tipo,

        "origem": origem,

        "mensagem": mensagem

    }

    try:
        pass

        with open(
            ARQUIVO,
            "r",
            encoding="utf-8"
        ) as f:

            banco = json.load(f)

    except:
        pass

        banco = {}

    if "event_bus" not in banco:
        pass

        banco["event_bus"] = []

    banco["event_bus"].append(evento)

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            banco,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"[EVENTO] "
        f"{tipo} "
        f"- "
        f"{origem}"
    )

registrar(

    "ALERTA",

    "CAPACITY_ENGINE",

    "SAUDE_CRITICA"

)


