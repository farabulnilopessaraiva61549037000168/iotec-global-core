import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 AUTONOMY ENGINE
# ============================================================

from datetime import datetime

print("\n================================================")
print("X27 AUTONOMY ENGINE")
print("================================================")

print(f"DATA : {datetime.now()}")

ALERTAS = [

    {

        "setor": "SAUDE",

        "risco": "CRITICO"

    },

    {

        "setor": "INTERNET",

        "risco": "ALTO"

    }

]

for alerta in ALERTAS:
    pass

    print("\n------------------------------------------------")

    print("SETOR :", alerta["setor"])

    print("RISCO :", alerta["risco"])

    if alerta["setor"] == "SAUDE":
        pass

        print(
            "ACAO : "
            "EXPANDIR_CAPACIDADE"
        )

    if alerta["setor"] == "INTERNET":
        pass

        print(
            "ACAO : "
            "ATIVAR_REDUNDANCIA"
        )

print("\nAUTONOMIA ASSISTIDA ATIVA")




