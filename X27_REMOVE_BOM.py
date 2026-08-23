import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

ROOT = r"C:\IOTEC"

corrigidos = 0
falhas = 0

for arquivo in Path(ROOT).rglob("*.py"):

    try:

        conteudo = arquivo.read_text(
            encoding="utf-8-sig",
            errors="ignore"
        )

        arquivo.write_text(
            conteudo,
            encoding="utf-8"
        )

        corrigidos += 1

    except Exception:
        falhas += 1

print()
print("===================================")
print("X27 REMOVE BOM")
print("===================================")
print()
print("CORRIGIDOS :", corrigidos)
print("FALHAS     :", falhas)



