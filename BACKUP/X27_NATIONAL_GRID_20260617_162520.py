import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 NATIONAL GRID
# ============================================================

from datetime import datetime

NODES = [

    "IBICUITINGA",

    "QUIXADA",

    "MORADA_NOVA",

    "LIMOEIRO_DO_NORTE",

    "ARACATI"

]

print("\n================================================")

print("X27 NATIONAL GRID")

print("================================================")

print(f"DATA : {datetime.now()}")

print("\nNODES CONECTADOS")

print("------------------------------------------------")

for node in NODES:
    pass

    print(f"[ONLINE] {node}")

print("\n================================================")

print("STATUS")

print("================================================")

print("MALHA NACIONAL OPERACIONAL")


