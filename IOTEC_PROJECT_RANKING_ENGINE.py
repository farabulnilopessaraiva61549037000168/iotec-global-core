import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path
from datetime import datetime

ROOT = r"C:\IOTEC"

print("="*80)
print("IOTEC PROJECT RANKING ENGINE")
print("="*80)
print("INÃƒÂCIO:", datetime.now())
print()

PROJETOS = []

ARQUIVOS_CHAVE = {
    "package.json":15,
    "requirements.txt":15,
    "pyproject.toml":15,
    "render.yaml":10,
    "netlify.toml":10,
    "vite.config.js":10,
    "vite.config.ts":10,
    "next.config.js":10,
    "index.html":10,
    "app.py":12,
    "main.py":12,
    "server.py":12,
    ".env":5,
    "README.md":8,
    "README":8
}

for raiz, dirs, files in os.walk(ROOT):

    score = 0
    itens = []

    for f in files:

        nome = f

        if nome in ARQUIVOS_CHAVE:

            score += ARQUIVOS_CHAVE[nome]
            itens.append(nome)

    if score > 0:

        PROJETOS.append({

            "caminho":raiz,
            "score":score,
            "itens":itens

        })

PROJETOS.sort(
    key=lambda x:x["score"],
    reverse=True
)

print()
print("="*80)
print("TOP PROJETOS")
print("="*80)

for i,p in enumerate(PROJETOS[:30],1):

    print(f"{i:02d}  SCORE {p['score']:3}  {p['caminho']}")

print()

with open(
    "IOTEC_PROJECT_RANKING.json",
    "w",
    encoding="utf-8"
) as arq:

    json.dump(
        PROJETOS,
        arq,
        indent=4,
        ensure_ascii=False
    )

with open(
    "IOTEC_PROJECT_RANKING.txt",
    "w",
    encoding="utf-8"
) as txt:

    txt.write("="*80+"\n")
    txt.write("IOTEC PROJECT RANKING\n")
    txt.write("="*80+"\n\n")

    txt.write("DATA\n")
    txt.write(str(datetime.now())+"\n\n")

    for i,p in enumerate(PROJETOS,1):

        txt.write(f"{i:03d}\n")
        txt.write(f"SCORE : {p['score']}\n")
        txt.write(f"LOCAL : {p['caminho']}\n")
        txt.write("ARQUIVOS\n")

        for item in p["itens"]:

            txt.write(f"   - {item}\n")

        txt.write("\n")

print()
print("="*80)
print("TOTAL DE PROJETOS :",len(PROJETOS))
print("RELATÃƒâ€œRIO GERADO")
print("="*80)

print("TXT  -> IOTEC_PROJECT_RANKING.txt")
print("JSON -> IOTEC_PROJECT_RANKING.json")

print()
print("FIM:",datetime.now())



