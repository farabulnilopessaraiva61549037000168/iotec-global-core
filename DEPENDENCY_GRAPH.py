import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import glob
import ast
from collections import defaultdict

ROOT = r"C:\IOTEC"

print("=" * 70)
print("IOTEC DEPENDENCY GRAPH")
print("=" * 70)
print()

arquivos = sorted(glob.glob(os.path.join(ROOT, "*.py")))

dependencias = defaultdict(list)
modulos = {}

# Descobre o nome de todos os mÃ³dulos
for arq in arquivos:
    nome = os.path.basename(arq)
    modulo = os.path.splitext(nome)[0]
    modulos[modulo] = nome

# Analisa os imports
for arq in arquivos:

    nome = os.path.basename(arq)

    try:

        with open(arq, "r", encoding="utf-8", errors="ignore") as f:
            codigo = f.read()

        arvore = ast.parse(codigo)

        for node in ast.walk(arvore):

            if isinstance(node, ast.Import):

                for n in node.names:

                    if n.name in modulos:

                        dependencias[nome].append(modulos[n.name])

            elif isinstance(node, ast.ImportFrom):

                if node.module and node.module in modulos:

                    dependencias[nome].append(modulos[node.module])

    except Exception:
        pass

print(f"Arquivos analisados: {len(arquivos)}")
print()

total_relacoes = 0

for modulo in sorted(dependencias):

    deps = sorted(set(dependencias[modulo]))

    if deps:

        total_relacoes += len(deps)

        print(modulo)

        for dep in deps:

            print("   â""â"€â"€", dep)

        print()

print("=" * 70)
print(f"DEPENDÃŠNCIAS ENCONTRADAS: {total_relacoes}")
print("=" * 70)




