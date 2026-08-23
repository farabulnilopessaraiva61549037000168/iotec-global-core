import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 LOG CENTER
# ============================================================

from datetime import datetime

ARQUIVO = "X27_SYSTEM.log"

def log(evento):
    pass

    linha = (

        f"{datetime.now()} | "

        f"{evento}\n"

    )

    with open(

        ARQUIVO,

        "a",

        encoding="utf-8"

    ) as f:

        f.write(linha)

    print("[LOG]", evento)

log("SISTEMA INICIALIZADO")

log("MISSION CONTROL ONLINE")

log("HEALTH CHECK EXECUTADO")




