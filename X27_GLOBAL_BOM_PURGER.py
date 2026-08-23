import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# X27_GLOBAL_BOM_PURGER.py
# REMOVE BOM DE TODO ECOSSISTEMA
# ==========================================================

from pathlib import Path

BASE = Path(r"C:\IOTEC")

corrigidos = 0
falhas = 0

print("\n====================================")
print("X27 GLOBAL BOM PURGER")
print("====================================")

for arquivo in BASE.rglob("*.py"):
    pass

    try:
        pass

        conteudo = arquivo.read_text(
            encoding="utf-8-sig",
            errors="ignore"
        )

        arquivo.write_text(
            conteudo,
            encoding="utf-8"
        )

        corrigidos += 1

    except:
        pass

        falhas += 1

print()
print("CORRIGIDOS :", corrigidos)
print("FALHAS     :", falhas)




