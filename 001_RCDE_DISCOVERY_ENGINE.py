# ==============================================================================
# IOTEC RCDE - DISCOVERY ENGINE V1
# Descobre automaticamente funÃ§Ãµes, classes, mÃ©todos e importaÃ§Ãµes
# ==============================================================================

from pathlib import Path
import ast
import json

ROOT = Path.home() / "Documents" / "OMEGA_BASE"

EXTENSOES = {".py"}

resultado = {
    "arquivos": [],
    "estatisticas": {
        "arquivos": 0,
        "funcoes": 0,
        "classes": 0,
        "metodos": 0,
        "imports": 0
    }
}


class Analyzer(ast.NodeVisitor):

    def __init__(self, arquivo):
        self.arquivo = arquivo

        self.funcoes = []
        self.classes = []
        self.imports = []

    def visit_FunctionDef(self, node):

        self.funcoes.append({
            "nome": node.name,
            "linha": node.lineno,
            "args": [a.arg for a in node.args.args],
            "doc": ast.get_docstring(node)
        })

        self.generic_visit(node)

    def visit_ClassDef(self, node):

        classe = {
            "nome": node.name,
            "linha": node.lineno,
            "metodos": []
        }

        for item in node.body:

            if isinstance(item, ast.FunctionDef):

                classe["metodos"].append({
                    "nome": item.name,
                    "linha": item.lineno,
                    "args": [a.arg for a in item.args.args],
                    "doc": ast.get_docstring(item)
                })

        self.classes.append(classe)

        self.generic_visit(node)

    def visit_Import(self, node):

        for alias in node.names:

            self.imports.append(alias.name)

    def visit_ImportFrom(self, node):

        modulo = node.module if node.module else ""

        self.imports.append(modulo)


for arquivo in ROOT.rglob("*.py"):

    try:

        codigo = arquivo.read_text(
            encoding="utf8",
            errors="ignore"
        )

        tree = ast.parse(codigo)

    except Exception:

        continue

    resultado["estatisticas"]["arquivos"] += 1

    analisador = Analyzer(str(arquivo))

    analisador.visit(tree)

    resultado["estatisticas"]["funcoes"] += len(analisador.funcoes)
    resultado["estatisticas"]["classes"] += len(analisador.classes)

    for c in analisador.classes:
        resultado["estatisticas"]["metodos"] += len(c["metodos"])

    resultado["estatisticas"]["imports"] += len(analisador.imports)

    resultado["arquivos"].append({

        "arquivo": str(arquivo),

        "imports": analisador.imports,

        "funcoes": analisador.funcoes,

        "classes": analisador.classes

    })


saida = ROOT / "RCDE_DISCOVERY.json"

with open(saida, "w", encoding="utf8") as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 80)
print("RCDE DISCOVERY ENGINE")
print("=" * 80)

print()

for k, v in resultado["estatisticas"].items():

    print(f"{k:20}: {v}")

print()
print("Arquivo salvo:")
print(saida)

