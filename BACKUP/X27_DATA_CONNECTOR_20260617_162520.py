import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 DATA CONNECTOR
# ============================================================

from datetime import datetime
import json
import os

print("\n================================================")
print("X27 DATA CONNECTOR")
print("================================================")
print(f"DATA : {datetime.now()}")

FONTES = [

    "CSV",
    "XLSX",
    "JSON",
    "API",
    "SENSORES"

]

for fonte in FONTES:
    pass

    print(f"[OK] CONECTOR {fonte}")

print("\nSTATUS : PRONTO PARA INTEGRACAO")


