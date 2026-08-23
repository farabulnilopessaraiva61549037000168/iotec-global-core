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
from datetime import datetime

ROOT = r"C:\IOTEC"

RESULT = {
    "frontend": [],
    "backend": [],
    "databases": [],
    "projects": [],
    "important_files": [],
    "statistics": {}
}

stats = {
    "pastas": 0,
    "arquivos": 0
}

print("="*70)
print("IOTEC ARCHITECTURE DISCOVERY")
print("="*70)
print("InÃƒÂ­cio:", datetime.now())
print()

for raiz, diretorios, arquivos in os.walk(ROOT):

    stats["pastas"] += 1

    encontrou = False

    for arq in arquivos:

        stats["arquivos"] += 1

        caminho = os.path.join(raiz, arq)
        nome = arq.lower()

        # -----------------------------
        # FRONTEND
        # -----------------------------

        if nome == "package.json":

            RESULT["projects"].append({
                "tipo":"Node/React",
                "caminho":raiz
            })

        if nome == "vite.config.js" or \
           nome == "vite.config.ts":

            RESULT["frontend"].append({
                "framework":"Vite",
                "caminho":raiz
            })

        if nome == "index.html":

            RESULT["frontend"].append({
                "framework":"HTML",
                "arquivo":caminho
            })

        # -----------------------------
        # BACKEND
        # -----------------------------

        if nome == "app.py":

            RESULT["backend"].append({
                "tipo":"Flask provÃƒÂ¡vel",
                "arquivo":caminho
            })

        if nome == "server.py":

            RESULT["backend"].append({
                "tipo":"Servidor",
                "arquivo":caminho
            })

        if nome == "main.py":

            RESULT["backend"].append({
                "tipo":"Main",
                "arquivo":caminho
            })

        if nome == "requirements.txt":

            RESULT["backend"].append({
                "tipo":"Python",
                "arquivo":caminho
            })

        if nome == "pyproject.toml":

            RESULT["backend"].append({
                "tipo":"Python Moderno",
                "arquivo":caminho
            })

        # -----------------------------
        # BANCO
        # -----------------------------

        if nome.endswith(".db") or \
           nome.endswith(".sqlite") or \
           nome.endswith(".sqlite3"):

            try:
                tamanho = os.path.getsize(caminho)
            except:
                tamanho = 0

            RESULT["databases"].append({
                "arquivo":caminho,
                "tamanho_mb":round(tamanho/1024/1024,2)
            })

        # -----------------------------
        # IMPORTANTES
        # -----------------------------

        if nome in [
            ".env",
            "dockerfile",
            "render.yaml",
            "netlify.toml",
            "readme.md",
            "readme"
        ]:

            RESULT["important_files"].append(caminho)

# ==============================
# ESTATÃƒÂSTICAS
# ==============================

RESULT["statistics"] = {
    "pastas":stats["pastas"],
    "arquivos":stats["arquivos"],
    "frontends":len(RESULT["frontend"]),
    "backends":len(RESULT["backend"]),
    "bancos":len(RESULT["databases"]),
    "projetos":len(RESULT["projects"]),
    "arquivos_importantes":len(RESULT["important_files"])
}

# ==============================
# TXT
# ==============================

with open("IOTEC_ARCHITECTURE_REPORT.txt","w",encoding="utf-8") as f:

    f.write("="*70+"\n")
    f.write("IOTEC ARCHITECTURE REPORT\n")
    f.write("="*70+"\n\n")

    f.write("DATA\n")
    f.write(str(datetime.now())+"\n\n")

    for k,v in RESULT["statistics"].items():
        f.write(f"{k}: {v}\n")

    f.write("\n")
    f.write("="*70+"\n")
    f.write("FRONTENDS\n")
    f.write("="*70+"\n")

    for item in RESULT["frontend"]:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

    f.write("\n")
    f.write("="*70+"\n")
    f.write("BACKENDS\n")
    f.write("="*70+"\n")

    for item in RESULT["backend"]:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

    f.write("\n")
    f.write("="*70+"\n")
    f.write("DATABASES\n")
    f.write("="*70+"\n")

    for item in RESULT["databases"]:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

    f.write("\n")
    f.write("="*70+"\n")
    f.write("PROJETOS\n")
    f.write("="*70+"\n")

    for item in RESULT["projects"]:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

    f.write("\n")
    f.write("="*70+"\n")
    f.write("ARQUIVOS IMPORTANTES\n")
    f.write("="*70+"\n")

    for item in RESULT["important_files"]:
        f.write(item+"\n")

# ==============================
# JSON
# ==============================

with open("IOTEC_ARCHITECTURE_REPORT.json","w",encoding="utf-8") as f:
    json.dump(RESULT,f,indent=4,ensure_ascii=False)

print("="*70)
print("DESCOBERTA CONCLUÃƒÂDA")
print("="*70)

for k,v in RESULT["statistics"].items():
    print(f"{k:25} {v}")

print()
print("RelatÃƒÂ³rio TXT : IOTEC_ARCHITECTURE_REPORT.txt")
print("RelatÃƒÂ³rio JSON: IOTEC_ARCHITECTURE_REPORT.json")
print()
print("Fim:",datetime.now())
print("="*70)



