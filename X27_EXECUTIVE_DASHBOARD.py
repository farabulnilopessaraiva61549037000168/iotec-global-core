import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 EXECUTIVE DASHBOARD
# ============================================================

from datetime import datetime

PROGRAMAS = 3
PROJETOS = 12

ORCAMENTO = 5200000

RISCOS_CRITICOS = 2

ALERTAS = 4

RESILIENCE_INDEX = 87

print("\n================================================")
print("X27 EXECUTIVE DASHBOARD")
print("================================================")

print(f"DATA : {datetime.now()}")

print("\nPROGRAMAS          :", PROGRAMAS)

print("PROJETOS           :", PROJETOS)

print(f"ORCAMENTO          : R$ {ORCAMENTO:,.2f}")

print("RISCOS CRITICOS    :", RISCOS_CRITICOS)

print("ALERTAS            :", ALERTAS)

print("RESILIENCE INDEX   :", RESILIENCE_INDEX)

print("\nSTATUS : OPERACIONAL")

print("================================================")




