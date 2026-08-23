import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 COMMAND CENTER
# ============================================================

from datetime import datetime

print("\n================================================")
print("X27 COMMAND CENTER")
print("================================================")

print(f"DATA : {datetime.now()}")

print("\n================================================")
print("SITUACAO GERAL")
print("================================================")

print("RESILIENCE INDEX : 87")

print("PROGRAMAS        : 3")

print("PROJETOS         : 12")

print("ORCAMENTO        : R$ 5.200.000")

print("ALERTAS          : 2")

print("RISCOS CRITICOS  : 1")

print("\n================================================")
print("GRID NACIONAL")
print("================================================")

print("[ONLINE] IBICUITINGA")

print("[ONLINE] QUIXADA")

print("[ONLINE] MORADA_NOVA")

print("[ONLINE] LIMOEIRO_DO_NORTE")

print("[ONLINE] ARACATI")

print("\n================================================")
print("PRIORIDADE MAXIMA")
print("================================================")

print("SAUDE")

print("\nRECOMENDACAO:")

print("EXPANDIR_CAPACIDADE_HOSPITALAR")

print("\n================================================")
print("STATUS")
print("================================================")

print("X27 OPERACIONAL")


