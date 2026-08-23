import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
IOTEC OPENING AUDIT
VersÃƒÂ£o: 1.0
Modo: SOMENTE LEITURA
Autor: IOTEC
=========================================================
"""

import os
import json
from datetime import datetime
from collections import Counter

# =========================================================
# CONFIGURAÃƒâ€¡Ãƒâ€¢ES
# =========================================================

ROOT = r"C:\IOTEC"

EXTENSOES = [
    ".py",
    ".html",
    ".css",
    ".js",
    ".json",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".md",
    ".txt",
    ".pdf",
    ".docx",
    ".xlsx",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".mp4",
    ".webm",
    ".mov",
    ".mp3",
    ".wav"
]

contador = Counter()

arquivos = []
pastas = []

# =========================================================
# CABEÃƒâ€¡ALHO
# =========================================================

print("=" * 70)
print("IOTEC OPENING AUDIT")
print("CHEF EXECUTIVO - AUDITORIA DE ABERTURA")
print("=" * 70)

print("\nInÃƒÂ­cio:", datetime.now())
print("DiretÃƒÂ³rio:", ROOT)
print()

# =========================================================
# VARREDURA
# =========================================================

for raiz, diretorios, ficheiros in os.walk(ROOT):

    pastas.append(raiz)

    for arquivo in ficheiros:

        caminho = os.path.join(raiz, arquivo)

        arquivos.append(caminho)

        ext = os.path.splitext(arquivo)[1].lower()

        contador[ext] += 1

# =========================================================
# RELATÃƒâ€œRIO
# =========================================================

print("=" * 70)
print("RESUMO")
print("=" * 70)

print(f"Pastas encontradas : {len(pastas)}")
print(f"Arquivos encontrados: {len(arquivos)}")

print()

print("=" * 70)
print("ARQUIVOS POR EXTENSÃƒÆ'O")
print("=" * 70)

for ext, qtd in sorted(contador.items()):

    print(f"{ext:12} {qtd}")

# =========================================================
# JSON
# =========================================================

relatorio = {

    "data": str(datetime.now()),
    "diretorio": ROOT,
    "pastas": len(pastas),
    "arquivos": len(arquivos),
    "extensoes": dict(contador)

}

with open("IOTEC_OPENING_REPORT.json",
          "w",
          encoding="utf-8") as arq:

    json.dump(
        relatorio,
        arq,
        indent=4,
        ensure_ascii=False
    )

# =========================================================
# TXT
# =========================================================

with open("IOTEC_OPENING_REPORT.txt",
          "w",
          encoding="utf-8") as txt:

    txt.write("=" * 60 + "\n")
    txt.write("IOTEC OPENING AUDIT\n")
    txt.write("=" * 60 + "\n\n")

    txt.write(f"Data: {datetime.now()}\n")
    txt.write(f"DiretÃƒÂ³rio: {ROOT}\n\n")

    txt.write(f"Pastas: {len(pastas)}\n")
    txt.write(f"Arquivos: {len(arquivos)}\n\n")

    txt.write("Arquivos por extensÃƒÂ£o\n\n")

    for ext, qtd in sorted(contador.items()):

        txt.write(f"{ext:12} {qtd}\n")

print()
print("=" * 70)
print("RELATÃƒâ€œRIO GERADO COM SUCESSO")
print("=" * 70)

print("Arquivo TXT  : IOTEC_OPENING_REPORT.txt")
print("Arquivo JSON : IOTEC_OPENING_REPORT.json")

print("\nFim:", datetime.now())
print("=" * 70)



