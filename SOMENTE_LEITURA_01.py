# ============================================================
# IOTEC - MÃƒâ€œDULO 003
# STRUCTURE ENGINE
# VersÃƒÂ£o: 2026.1
# Modo: SOMENTE LEITURA
#
# Analisa todos os arquivos Python sem executÃƒÂ¡-los.
# Extrai:
#   - Classes
#   - FunÃƒÂ§ÃƒÂµes
#   - Imports
#   - Linhas
#   - Tamanho
#
# Gera:
#   IOTEC_STRUCTURE_REPORT.json
# ============================================================

from pathlib import Path
import ast
import json
from datetime import datetime

ROOT = Path.cwd()

REPORT = {
    "generated_at": datetime.now().isoformat(),
    "root": str(ROOT),
    "summary": {
        "files": 0,
        "classes": 0,
        "functions": 0,
        "imports": 0
    },
    "files": []
}


def analyse_python(file):

    data = {
        "file": str(file),
        "lines": 0,
        "size_kb": 0,
        "classes": [],
        "functions": [],
        "imports": [],
        "error": None
    }

    try:

        source = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        data["lines"] = len(source.splitlines())
        data["size_kb"] = round(file.stat().st_size / 1024, 2)

        tree = ast.parse(source)

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                data["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                data["functions"].append(node.name)

            elif isinstance(node, ast.Import):

                for alias in node.names:
                    data["imports"].append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    data["imports"].append(node.module)

    except Exception as e:

        data["error"] = str(e)

    return data


for py in ROOT.rglob("*.py"):

    REPORT["summary"]["files"] += 1

    info = analyse_python(py)

    REPORT["summary"]["classes"] += len(info["classes"])
    REPORT["summary"]["functions"] += len(info["functions"])
    REPORT["summary"]["imports"] += len(info["imports"])

    REPORT["files"].append(info)

OUTPUT = ROOT / "IOTEC_STRUCTURE_REPORT.json"

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        REPORT,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 60)
print("IOTEC STRUCTURE ENGINE")
print("=" * 60)

print()

print("Arquivos :", REPORT["summary"]["files"])
print("Classes  :", REPORT["summary"]["classes"])
print("FunÃƒÂ§ÃƒÂµes  :", REPORT["summary"]["functions"])
print("Imports  :", REPORT["summary"]["imports"])

print()
print("RelatÃƒÂ³rio salvo em:")
print(OUTPUT)

print()
print("STATUS: OK")

