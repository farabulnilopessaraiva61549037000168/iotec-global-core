import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import glob
import ast
from collections import Counter

ROOT = r"C:\IOTEC"

print("=" * 70)
print("IOTEC ARCHITECTURE ANALYZER")
print("=" * 70)
print()

arquivos = sorted(glob.glob(os.path.join(ROOT, "*.py")))

imports = Counter()

print(f"Arquivos Python encontrados: {len(arquivos)}")
print()

for arquivo in arquivos:

    nome = os.path.basename(arquivo)

    try:

        with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
            codigo = f.read()

        arvore = ast.parse(codigo)

        modulos = set()

        for node in ast.walk(arvore):

            if isinstance(node, ast.Import):

                for n in node.names:
                    modulos.add(n.name.split(".")[0])

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    modulos.add(node.module.split(".")[0])

        for m in modulos:
            imports[m] += 1

        print(f"[OK] {nome:40} {len(modulos):2} imports")

    except Exception as erro:

        print(f"[ERRO] {nome}")
        print("       ", erro)

print()
print("=" * 70)
print("DEPENDÃŠNCIAS MAIS UTILIZADAS")
print("=" * 70)

for modulo, qtd in imports.most_common():

    print(f"{modulo:25} {qtd}")

print()
print("=" * 70)
print("ANÃLISE CONCLUÃDA")
print("=" * 70)




