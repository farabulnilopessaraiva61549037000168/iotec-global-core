# ============================================================
# IOTEC PRODUCT READINESS ENGINE
# VersÃƒÂ£o 1.0
# SOMENTE LEITURA
#
# Entrada:
#     IOTEC_CAPABILITY_CONSOLIDATION.json
#
# SaÃƒÂ­da:
#     IOTEC_PRODUCT_READINESS.json
#
# ============================================================

import json
import ast
from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()

INPUT = ROOT / "IOTEC_CAPABILITY_CONSOLIDATION.json"
OUTPUT = ROOT / "IOTEC_PRODUCT_READINESS.json"

if not INPUT.exists():
    raise FileNotFoundError(INPUT)

with open(INPUT, "r", encoding="utf-8") as f:
    consolidation = json.load(f)

ENGINES = consolidation.get("engines", {})

# ------------------------------------------------------------

def score_file(path):

    p = Path(path)

    result = {
        "exists": False,
        "main": False,
        "api": False,
        "database": False,
        "html": False,
        "readme": False,
        "requirements": False,
        "classes": 0,
        "functions": 0,
        "score": 0
    }

    if not p.exists():
        return result

    result["exists"] = True

    folder = p.parent

    if (folder / "README.md").exists():
        result["readme"] = True

    if (folder / "requirements.txt").exists():
        result["requirements"] = True

    try:

        source = p.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception:
        return result

    low = source.lower()

    if "__name__" in source:
        result["main"] = True

    if (
        "fastapi" in low or
        "flask" in low or
        "@app.route" in low or
        "@router." in low
    ):
        result["api"] = True

    if (
        "sqlite3" in low or
        "sqlalchemy" in low or
        "psycopg" in low or
        "mysql" in low
    ):
        result["database"] = True

    if (
        ".html" in low or
        "render_template" in low
    ):
        result["html"] = True

    try:

        tree = ast.parse(source)

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                result["classes"] += 1

            elif isinstance(node, ast.FunctionDef):
                result["functions"] += 1

    except Exception:
        pass

    score = 0

    if result["exists"]:
        score += 10

    if result["main"]:
        score += 20

    if result["api"]:
        score += 20

    if result["database"]:
        score += 15

    if result["html"]:
        score += 10

    if result["readme"]:
        score += 10

    if result["requirements"]:
        score += 10

    score += min(result["classes"],10)
    score += min(result["functions"],5)

    result["score"] = min(score,100)

    return result

# ------------------------------------------------------------

REPORT = {

    "generated_at": datetime.now().isoformat(),

    "engines":[]
}

for engine_name, engine in ENGINES.items():

    files = engine.get("files", [])

    total_score = 0

    analysed = []

    for item in files:

        path = item.get("file")

        info = score_file(path)

        analysed.append({

            "file": path,

            **info

        })

        total_score += info["score"]

    avg = 0

    if analysed:
        avg = round(total_score / len(analysed),2)

    REPORT["engines"].append({

        "engine": engine_name,

        "files": len(analysed),

        "average_readiness": avg,

        "details": analysed

    })

REPORT["engines"].sort(
    key=lambda x: x["average_readiness"],
    reverse=True
)

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

print("="*60)
print("IOTEC PRODUCT READINESS ENGINE")
print("="*60)
print()

for e in REPORT["engines"]:

    print(
        f"{e['engine']:<24}"
        f"{e['average_readiness']:>6}"
    )

print()
print("Arquivo gerado:")
print(OUTPUT)
print()
print("STATUS: OK")

