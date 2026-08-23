# ==========================================================
# 046B_DEEP_INVENTORY_ENGINE.py
# INVENTÃƒÂRIO PROFUNDO DA IOTEC
# ==========================================================

import os
from collections import Counter, defaultdict

ROOT = "."

EXTENSOES = Counter()
TECNOLOGIAS = Counter()
PASTAS = Counter()

PALAVRAS = {
    "flask":"Flask",
    "fastapi":"FastAPI",
    "sqlite3":"SQLite",
    "requests":"Requests",
    "pandas":"Pandas",
    "numpy":"NumPy",
    "matplotlib":"Matplotlib",
    "openpyxl":"OpenPyXL",
    "jinja2":"Jinja2",
    "threading":"Threading",
    "subprocess":"Subprocess",
    "asyncio":"AsyncIO",
    "socket":"Socket",
    "selenium":"Selenium",
    "uuid":"UUID",
    "json":"JSON",
    "logging":"Logging"
}

arquivos_python = []

print("="*70)
print("IOTEC DEEP INVENTORY ENGINE")
print("="*70)
print()

for raiz,dirs,files in os.walk(ROOT):

    pasta = os.path.relpath(raiz,ROOT)
    PASTAS[pasta]+=len(files)

    for nome in files:

        caminho=os.path.join(raiz,nome)

        ext=os.path.splitext(nome)[1].lower()

        EXTENSOES[ext]+=1

        if ext==".py":

            arquivos_python.append(caminho)

            try:

                texto=open(
                    caminho,
                    encoding="utf8",
                    errors="ignore"
                ).read().lower()

            except:

                continue

            for chave,tec in PALAVRAS.items():

                if chave in texto:

                    TECNOLOGIAS[tec]+=1

print("Arquivos Python :",len(arquivos_python))
print()

print("="*70)
print("EXTENSÃƒâ€¢ES")
print("="*70)

for ext,total in EXTENSOES.most_common():

    print(f"{ext:<10}{total}")

print()

print("="*70)
print("TECNOLOGIAS ENCONTRADAS")
print("="*70)

for nome,total in TECNOLOGIAS.most_common():

    print(f"{nome:<20}{total}")

print()

print("="*70)
print("PASTAS MAIS POPULOSAS")
print("="*70)

for pasta,total in PASTAS.most_common(30):

    print(f"{total:6}  {pasta}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)

print()
print("InventÃƒÂ¡rio concluÃƒÂ­do.")
print("O Kernel agora conhece")
print("as tecnologias utilizadas")
print("e onde elas estÃƒÂ£o.")
print()


