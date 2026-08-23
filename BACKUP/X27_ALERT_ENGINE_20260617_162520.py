import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 ALERT ENGINE
# ============================================================

from datetime import datetime

ALERTAS = [

    {

        "setor": "SAUDE",

        "capacidade": 40,

        "forecast": 16,

        "acao":
        "EXPANDIR_CAPACIDADE_HOSPITALAR"

    },

    {

        "setor": "INTERNET",

        "capacidade": 65,

        "forecast": 41,

        "acao":
        "AMPLIAR_REDUNDANCIA"

    }

]

print("\n================================================")
print("X27 ALERT CENTER")
print("================================================")

print(f"DATA : {datetime.now()}")

for alerta in ALERTAS:
    pass

    print("\n------------------------------------------------")

    print(
        f"SETOR      : "
        f"{alerta['setor']}"
    )

    print(
        f"CAPACIDADE : "
        f"{alerta['capacidade']}%"
    )

    print(
        f"FORECAST   : "
        f"{alerta['forecast']}%"
    )

    print(
        f"ACAO       : "
        f"{alerta['acao']}"
    )

    if alerta["forecast"] < 25:
        pass

        print("PRIORIDADE : IMEDIATA")

    else:
        pass

        print("PRIORIDADE : ALTA")


