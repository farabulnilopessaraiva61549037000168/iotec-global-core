# ==========================================================
# 101_DEPENDENCY_GRAPH_ENGINE.py
# IOTEC DEPENDENCY GRAPH ENGINE
# ==========================================================

import os
import re
import json
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

IGNORAR = {
    "__pycache__",
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "env",
    "Lib",
    "Scripts",
    "site-packages",
    "dist",
    "build"
}

imports = re.compile(r'^\s*(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+))')
jsons = re.compile(r'IOTEC_[A-Za-z0-9_]+\.json')

grafo = {
    "generated_at": datetime.now().isoformat(),
    "modules": []
}

dependencias = defaultdict(int)
json_total = set()

print("=" * 90)
print("IOTEC DEPENDENCY GRAPH ENGINE")
print("=" * 90)
print()

print("Mapeando dependÃƒÂªncias...\n")

total_py = 0

for pasta, diretorios, arquivos in os.walk(ROOT):

    diretorios[:] = [d for d in diretorios if d not in IGNORAR]

    for arquivo in arquivos:

        if not arquivo.lower().endswith(".py"):
            continue

        caminho = os.path.join(pasta, arquivo)

        total_py += 1

        internos = []
        externos = []
        usados_json = []

        try:

            with open(caminho, "r", encoding="utf8", errors="ignore") as f:

                texto = f.read()

            for linha in texto.splitlines():

                m = imports.search(linha)

                if not m:
                    continue

                modulo = m.group(1) or m.group(2)

                if modulo.startswith("IOTEC"):

                    internos.append(modulo)

                else:

                    externos.append(modulo.split(".")[0])

            encontrados = jsons.findall(texto)

            for j in encontrados:

                usados_json.append(j)

                json_total.add(j)

            dependencias[arquivo] = (

                len(internos)
                + len(externos)
                + len(usados_json)

            )

            grafo["modules"].append({

                "module": arquivo,

                "imports_internal": sorted(set(internos)),

                "imports_external": sorted(set(externos)),

                "json_dependencies": sorted(set(usados_json))

            })

            print("Ã°Å¸Å¸Â¢", arquivo)

        except:

            print("Ã°Å¸â€Â´", arquivo)

grafo["modules"].sort(
    key=lambda x: x["module"]
)

with open(
    "IOTEC_DEPENDENCY_GRAPH.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        grafo,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("=" * 90)
print("RESUMO")
print("=" * 90)
print()

print("MÃƒÂ³dulos Python.............", total_py)
print("JSON encontrados...........", len(json_total))
print("MÃƒÂ³dulos catalogados........", len(grafo["modules"]))
print()

print("=" * 90)
print("TOP 20 MAIS CONECTADOS")
print("=" * 90)
print()

ranking = sorted(
    dependencias.items(),
    key=lambda x: x[1],
    reverse=True
)

for nome, valor in ranking[:20]:

    print(f"{valor:3}  {nome}")

print()

print("=" * 90)
print("ARQUIVO GERADO")
print("=" * 90)
print()

print("IOTEC_DEPENDENCY_GRAPH.json")

print()

print("=" * 90)
print("MISSÃƒÆ'O")
print("=" * 90)
print()

print("O Kernel passa")
print("a compreender")
print("como todos")
print("os mÃƒÂ³dulos")
print("estÃƒÂ£o ligados.")
print()

print("Nenhuma dependÃƒÂªncia")
print("permanece")
print("desconhecida.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("DEPENDENCY GRAPH OPERACIONAL.")


