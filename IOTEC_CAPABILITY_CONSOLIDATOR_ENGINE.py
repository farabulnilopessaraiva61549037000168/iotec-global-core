# ============================================================
# IOTEC CAPABILITY CONSOLIDATOR ENGINE
# MÃƒâ€œDULO 005
# VERSÃƒÆ'O 2026.1
#
# MISSÃƒÆ'O:
# Descobrir os motores reutilizÃƒÂ¡veis da plataforma.
#
# NÃƒÂ£o altera nenhum arquivo.
# Apenas gera inteligÃƒÂªncia estrutural.
# ============================================================

from pathlib import Path
import ast
import json
from collections import defaultdict
from datetime import datetime

ROOT = Path.cwd()

ENGINES = defaultdict(list)

REPORT = {
    "generated_at": datetime.now().isoformat(),
    "engines": {}
}

KEYWORDS = {

    "PDF_ENGINE": [
        "pdf",
        "reportlab",
        "fpdf"
    ],

    "DATABASE_ENGINE": [
        "sqlite",
        "mysql",
        "postgres",
        "database"
    ],

    "API_ENGINE": [
        "flask",
        "fastapi",
        "api"
    ],

    "AI_ENGINE": [
        "openai",
        "gpt",
        "agent",
        "llm",
        "neural"
    ],

    "COMMERCIAL_ENGINE": [
        "crm",
        "lead",
        "proposal",
        "contract",
        "sale"
    ],

    "AUTOMATION_ENGINE": [
        "automation",
        "worker",
        "queue",
        "scheduler"
    ],

    "ROBOTICS_ENGINE": [
        "arduino",
        "esp32",
        "sensor",
        "robot",
        "iot"
    ],

    "DASHBOARD_ENGINE": [
        "dashboard",
        "panel",
        "cockpit"
    ]
}


def analyse(file):

    try:

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()

        tree = ast.parse(text)

    except Exception:

        return

    classes = []

    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    for engine, words in KEYWORDS.items():

        if any(word in text for word in words):

            ENGINES[engine].append({

                "file": str(file),

                "classes": classes,

                "functions": len(functions)

            })


for py in ROOT.rglob("*.py"):

    analyse(py)

for engine in ENGINES:

    REPORT["engines"][engine] = {

        "occurrences": len(ENGINES[engine]),

        "files": ENGINES[engine]

    }

OUTPUT = ROOT / "IOTEC_CAPABILITY_CONSOLIDATION.json"

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
print("IOTEC CAPABILITY CONSOLIDATOR")
print("=" * 60)

for engine in REPORT["engines"]:

    print(

        f"{engine:25}"

        f"{REPORT['engines'][engine]['occurrences']}"

    )

print()

print("Arquivo:")

print(OUTPUT)

print()

print("STATUS: OK")

