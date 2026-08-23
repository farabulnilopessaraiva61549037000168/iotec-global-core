# ============================================================
# IOTEC - MÃƒâ€œDULO 002
# CORE DISCOVERY ENGINE
# VersÃƒÂ£o: 2026.1
# Modo: SOMENTE LEITURA
# Objetivo:
#   Criar um ÃƒÂ­ndice pesquisÃƒÂ¡vel de todos os scripts Python
#   existentes na plataforma.
# ============================================================

from pathlib import Path
import json
from datetime import datetime

ROOT = Path.cwd()

INDEX = {
    "generated_at": datetime.now().isoformat(),
    "root": str(ROOT),
    "summary": {},
    "categories": {
        "core": [],
        "database": [],
        "api": [],
        "commercial": [],
        "ai": [],
        "security": [],
        "dashboard": [],
        "automation": [],
        "robotics": [],
        "education": [],
        "other": []
    }
}

KEYWORDS = {
    "core": [
        "core","kernel","main","bootstrap",
        "startup","engine","nucleus","omega"
    ],

    "database": [
        "db","database","sqlite","mysql",
        "postgres","mongo"
    ],

    "api": [
        "api","flask","fastapi","django",
        "endpoint","server"
    ],

    "commercial": [
        "crm","client","lead","proposal",
        "contract","sale","revenue","commercial"
    ],

    "ai": [
        "ai","gpt","llm","agent","neural",
        "intelligence","model"
    ],

    "security": [
        "security","auth","login","token",
        "crypto","permission"
    ],

    "dashboard": [
        "dashboard","panel","cockpit",
        "monitor","viewer"
    ],

    "automation": [
        "automation","scheduler","worker",
        "queue","task"
    ],

    "robotics": [
        "robot","arduino","esp32",
        "sensor","iot"
    ],

    "education": [
        "education","school","student",
        "teacher","class"
    ]
}

TOTAL = 0

for file in ROOT.rglob("*.py"):

    TOTAL += 1

    name = file.name.lower()

    added = False

    for category, words in KEYWORDS.items():

        if any(word in name for word in words):

            INDEX["categories"][category].append(str(file))
            added = True
            break

    if not added:
        INDEX["categories"]["other"].append(str(file))

INDEX["summary"] = {

    "python_files": TOTAL,

    "core":
        len(INDEX["categories"]["core"]),

    "database":
        len(INDEX["categories"]["database"]),

    "api":
        len(INDEX["categories"]["api"]),

    "commercial":
        len(INDEX["categories"]["commercial"]),

    "ai":
        len(INDEX["categories"]["ai"]),

    "security":
        len(INDEX["categories"]["security"]),

    "dashboard":
        len(INDEX["categories"]["dashboard"]),

    "automation":
        len(INDEX["categories"]["automation"]),

    "robotics":
        len(INDEX["categories"]["robotics"]),

    "education":
        len(INDEX["categories"]["education"]),

    "other":
        len(INDEX["categories"]["other"])
}

OUTPUT = ROOT / "IOTEC_PLATFORM_INDEX.json"

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(INDEX, f, indent=4, ensure_ascii=False)

print("=" * 60)
print("IOTEC CORE DISCOVERY ENGINE")
print("=" * 60)

for key, value in INDEX["summary"].items():
    print(f"{key:15}: {value}")

print("\nÃƒÂndice salvo em:")
print(OUTPUT)

print("\nSTATUS: DISCOVERY FINALIZADO")

