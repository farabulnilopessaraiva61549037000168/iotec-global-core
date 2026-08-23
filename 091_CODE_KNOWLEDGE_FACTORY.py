# ==========================================================
# 091_CODE_KNOWLEDGE_FACTORY.py
# IOTEC CODE KNOWLEDGE FACTORY
# ==========================================================

import os
import ast
import json
from datetime import datetime

print("=" * 80)
print("IOTEC CODE KNOWLEDGE FACTORY")
print("=" * 80)
print()

ROOT = r"C:\IOTEC"

biblioteca = []

arquivos = 0

print("Estudando conhecimento da plataforma...")
print()

for pasta, _, files in os.walk(ROOT):

    for arquivo in files:

        if not arquivo.endswith(".py"):
            continue

        arquivos += 1

        caminho = os.path.join(pasta, arquivo)

        try:

            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                codigo = f.read()

            arvore = ast.parse(codigo)

        except Exception:
            continue

        funcoes = []
        classes = []
        imports = []

        for nodo in ast.walk(arvore):

            if isinstance(nodo, ast.FunctionDef):
                funcoes.append(nodo.name)

            elif isinstance(nodo, ast.ClassDef):
                classes.append(nodo.name)

            elif isinstance(nodo, ast.Import):

                for i in nodo.names:
                    imports.append(i.name)

            elif isinstance(nodo, ast.ImportFrom):

                if nodo.module:
                    imports.append(nodo.module)

        livro = {

            "arquivo": arquivo,
            "caminho": caminho,
            "classes": sorted(classes),
            "funcoes": sorted(funcoes),
            "imports": sorted(set(imports)),
            "total_classes": len(classes),
            "total_funcoes": len(funcoes),
            "total_imports": len(set(imports))

        }

        biblioteca.append(livro)

print("=" * 80)
print("RESUMO")
print("=" * 80)
print()

print("Arquivos estudados :", len(biblioteca))
print()

print("=" * 80)
print("TOP 20 LIVROS")
print("=" * 80)
print()

biblioteca.sort(
    key=lambda x: (
        x["total_funcoes"] +
        x["total_classes"] +
        x["total_imports"]
    ),
    reverse=True
)

for livro in biblioteca[:20]:

    score = (
        livro["total_funcoes"] +
        livro["total_classes"] +
        livro["total_imports"]
    )

    print()
    print(livro["arquivo"])
    print("Score.............", score)
    print("FunÃƒÂ§ÃƒÂµes..........", livro["total_funcoes"])
    print("Classes..........", livro["total_classes"])
    print("Imports..........", livro["total_imports"])

print()

saida = {

    "gerado_em": datetime.now().isoformat(),

    "arquivos_estudados": len(biblioteca),

    "biblioteca": biblioteca

}

with open(
    "IOTEC_CODE_LIBRARY.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        saida,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 80)
print("ARQUIVO GERADO")
print("=" * 80)
print()

print("IOTEC_CODE_LIBRARY.json")
print()

print("=" * 80)
print("MISSÃƒÆ'O")
print("=" * 80)
print()

print("Cada mÃƒÂ³dulo deixa")
print("de ser apenas")
print("um arquivo Python.")
print()

print("Passa a representar")
print("um livro da")
print("Biblioteca Viva")
print("da IOTEC.")
print()

print("=" * 80)
print("STATUS")
print("=" * 80)
print()

print("FÃƒÂBRICA DE CONHECIMENTO ATIVA.")


