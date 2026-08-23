import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 STRATEGIC AI
# ============================================================

from datetime import datetime

RECOMENDACOES = [

    {
        "acao":
        "EXPANDIR_CAPACIDADE_HOSPITALAR",

        "impacto":
        "ALTO",

        "prazo":
        "90 DIAS",

        "prioridade":
        1
    },

    {
        "acao":
        "EXPANDIR_ABRIGOS",

        "impacto":
        "ALTO",

        "prazo":
        "60 DIAS",

        "prioridade":
        2
    },

    {
        "acao":
        "AMPLIAR_REDUNDANCIA_DE_INTERNET",

        "impacto":
        "ALTO",

        "prazo":
        "45 DIAS",

        "prioridade":
        3
    }

]

print("\n================================================")
print("X27 STRATEGIC AI")
print("================================================")

print(f"DATA : {datetime.now()}")

for item in RECOMENDACOES:
    pass

    print("\n------------------------------------------------")

    print("ACAO       :", item["acao"])

    print("IMPACTO    :", item["impacto"])

    print("PRAZO      :", item["prazo"])

    print("PRIORIDADE :", item["prioridade"])

print("\n================================================")
print("RECOMENDACOES ESTRATEGICAS GERADAS")
print("================================================")




