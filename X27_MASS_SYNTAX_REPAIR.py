import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import ast
from pathlib import Path

ROOT = r"C:\IOTEC"

corrigidos = 0
falhas = 0

for arquivo in Path(ROOT).rglob("*.py"):
    pass

    try:
        pass

        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        texto = texto.replace("\u00A0", " ")
        texto = texto.replace("", "")
        texto = texto.replace("", "")
        texto = texto.replace("", "")
        texto = texto.replace("", "")
        texto = texto.replace("", "")
        texto = texto.replace("", "")

        linhas = texto.splitlines()
        novas = []

        for linha in linhas:
            pass

            novas.append(linha.rstrip())

            if linha.strip().startswith("if ") and linha.strip().endswith(":"):
                novas.append("    pass")

            elif linha.strip().startswith("try:"):
                novas.append("    pass")

            elif linha.strip().startswith("except"):
                novas.append("    pass")

            elif linha.strip().startswith("class ") and linha.strip().endswith(":"):
                novas.append("    pass")

        texto = "\n".join(novas)

        arquivo.write_text(
            texto,
            encoding="utf-8"
        )

        corrigidos += 1

    except:
        pass

        falhas += 1

print()
print("CORRIGIDOS :", corrigidos)
print("FALHAS     :", falhas)




