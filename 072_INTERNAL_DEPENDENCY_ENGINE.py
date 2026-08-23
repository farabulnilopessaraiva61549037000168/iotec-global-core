# ==========================================================
# 072_INTERNAL_DEPENDENCY_ENGINE.py
# IOTEC INTERNAL DEPENDENCY ENGINE
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

print("="*70)
print("IOTEC INTERNAL DEPENDENCY ENGINE")
print("="*70)
print()

# ==========================================================
# INVENTÃƒÂRIO DOS MÃƒâ€œDULOS
# ==========================================================

MODULOS = {}

for raiz, pastas, arquivos in os.walk(ROOT):

    pastas[:] = [p for p in pastas if p not in IGNORE]

    for arq in arquivos:

        if arq.endswith(".py"):

            nome = os.path.splitext(arq)[0]

            MODULOS[nome] = os.path.join(raiz, arq)

print("MÃƒÂ³dulos internos :", len(MODULOS))
print()

# ==========================================================
# DEPENDÃƒÅ NCIAS INTERNAS
# ==========================================================

IMPORT = re.compile(r'^\s*import\s+(.+)', re.MULTILINE)
FROM = re.compile(r'^\s*from\s+([A-Za-z0-9_\.]+)\s+import', re.MULTILINE)

GRAFO = defaultdict(set)
REFERENCIAS = defaultdict(int)

for modulo, caminho in MODULOS.items():

    try:

        texto = open(
            caminho,
            encoding="utf-8",
            errors="ignore"
        ).read()

    except:

        continue

    encontrados = set()

    # import xxx

    for linha in IMPORT.findall(texto):

        partes = linha.split(",")

        for p in partes:

            nome = p.strip().split(".")[0]

            if nome in MODULOS:

                encontrados.add(nome)

    # from xxx import yyy

    for linha in FROM.findall(texto):

        nome = linha.strip().split(".")[0]

        if nome in MODULOS:

            encontrados.add(nome)

    GRAFO[modulo] = encontrados

    for x in encontrados:

        REFERENCIAS[x] += 1

# ==========================================================
# MAIS UTILIZADOS
# ==========================================================

print("="*70)
print("TOP 50 MÃƒâ€œDULOS CENTRAIS")
print("="*70)
print()

ranking = sorted(
    REFERENCIAS.items(),
    key=lambda x:x[1],
    reverse=True
)

if len(ranking)==0:

    print("Nenhuma dependÃƒÂªncia interna encontrada.")

else:

    for nome,total in ranking[:50]:

        print(f"{total:4}  {nome}")

print()

# ==========================================================
# MAIORES ORQUESTRADORES
# ==========================================================

print("="*70)
print("TOP 30 ORQUESTRADORES")
print("="*70)
print()

ranking = sorted(
    GRAFO.items(),
    key=lambda x:len(x[1]),
    reverse=True
)

for nome,deps in ranking[:30]:

    print()

    print(nome)

    print("Conecta com :",len(deps),"mÃƒÂ³dulos")

    for d in sorted(deps):

        print("   ->",d)

print()

# ==========================================================
# ISOLADOS
# ==========================================================

print("="*70)
print("MÃƒâ€œDULOS SEM DEPENDÃƒÅ NCIAS INTERNAS")
print("="*70)
print()

isolados = []

for modulo,deps in GRAFO.items():

    if len(deps)==0:

        isolados.append(modulo)

for x in sorted(isolados)[:100]:

    print(x)

print()

# ==========================================================
# HUBS
# ==========================================================

print("="*70)
print("HUBS DA PLATAFORMA")
print("="*70)
print()

for nome,total in ranking[:15]:

    if len(total) >= 5:

        print(nome)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("O Kernel identificou")
print("as dependÃƒÂªncias")
print("entre mÃƒÂ³dulos")
print("da prÃƒÂ³pria IOTEC.")

print()

print("A PresidÃƒÂªncia agora")
print("conhece os")
print("verdadeiros")
print("hubs internos.")


