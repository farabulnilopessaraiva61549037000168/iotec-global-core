# ==========================================================
# 071_DEPENDENCY_GRAPH_ENGINE.py
# IOTEC DEPENDENCY GRAPH ENGINE
# ==========================================================

import os
import re
from collections import defaultdict

ROOT = r"C:\IOTEC"

IGNORE = {
    "venv",
    "__pycache__",
    "BACKUP",
    "ENCODING_BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "FROZEN"
}

IMPORT_RE = re.compile(r'^\s*import\s+(.+)', re.MULTILINE)
FROM_RE   = re.compile(r'^\s*from\s+([A-Za-z0-9_\.]+)\s+import', re.MULTILINE)

grafo = defaultdict(list)
dependencias = defaultdict(int)

print("="*70)
print("IOTEC DEPENDENCY GRAPH ENGINE")
print("="*70)
print()

for raiz, pastas, arquivos in os.walk(ROOT):

    pastas[:] = [p for p in pastas if p not in IGNORE]

    for arquivo in arquivos:

        if not arquivo.endswith(".py"):
            continue

        caminho = os.path.join(raiz, arquivo)

        try:

            texto = open(
                caminho,
                encoding="utf-8",
                errors="ignore"
            ).read()

        except:
            continue

        atual = os.path.splitext(arquivo)[0]

        encontrados = set()

        for m in IMPORT_RE.findall(texto):

            for parte in m.split(","):

                parte = parte.strip()

                if parte:

                    encontrados.add(parte.split(".")[0])

        for m in FROM_RE.findall(texto):

            encontrados.add(m.split(".")[0])

        for modulo in sorted(encontrados):

            grafo[atual].append(modulo)
            dependencias[modulo]+=1

print("MÃƒâ€œDULOS ANALISADOS :", len(grafo))
print()

print("="*70)
print("TOP 50 MAIS DEPENDIDOS")
print("="*70)
print()

ranking = sorted(
    dependencias.items(),
    key=lambda x:x[1],
    reverse=True
)

for modulo,total in ranking[:50]:

    print(f"{total:4}  {modulo}")

print()

print("="*70)
print("TOP 30 MÃƒâ€œDULOS MAIS CONECTADOS")
print("="*70)
print()

ranking2 = sorted(
    grafo.items(),
    key=lambda x:len(x[1]),
    reverse=True
)

for modulo,deps in ranking2[:30]:

    print()

    print(modulo)

    print("DependÃƒÂªncias :",len(deps))

    for d in deps[:15]:

        print("   ->",d)

print()

print("="*70)
print("MÃƒâ€œDULOS ISOLADOS")
print("="*70)
print()

isolados = []

for modulo,deps in grafo.items():

    if len(deps)==0:

        isolados.append(modulo)

for modulo in sorted(isolados)[:100]:

    print(modulo)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia agora")
print("conhece o mapa")
print("de dependÃƒÂªncias")
print("da plataforma.")

print()

print("O prÃƒÂ³ximo passo")
print("serÃƒÂ¡ identificar")
print("os mÃƒÂ³dulos")
print("verdadeiramente")
print("centrais.")


