# ============================================================
# IOTEC PRODUCT DISCOVERY ENGINE
# MÃƒÂ³dulo 004
# VersÃƒÂ£o: 2026.1
# Modo: SOMENTE LEITURA
#
# Procura capacidades comerciais existentes no cÃƒÂ³digo.
# NÃƒÂ£o modifica nenhum arquivo.
# ============================================================

from pathlib import Path
import json
from datetime import datetime

ROOT = Path.cwd()

KEYWORDS = {
    "IA": [
        "openai", "gpt", "llm", "agent", "ai", "neural"
    ],
    "Dashboard": [
        "dashboard", "panel", "cockpit", "monitor"
    ],
    "Banco de Dados": [
        "sqlite", "database", "mysql", "postgres"
    ],
    "OCR": [
        "ocr", "tesseract"
    ],
    "PDF": [
        "pdf", "report", "fpdf", "reportlab"
    ],
    "API": [
        "flask", "fastapi", "api"
    ],
    "AutomaÃƒÂ§ÃƒÂ£o": [
        "automation", "scheduler", "queue", "worker"
    ],
    "RobÃƒÂ³tica": [
        "arduino", "esp32", "robot", "sensor", "iot"
    ],
    "Comercial": [
        "crm", "lead", "proposal", "contract",
        "sale", "client"
    ]
}

report = {
    "generated_at": datetime.now().isoformat(),
    "products": {}
}

for category in KEYWORDS:
    report["products"][category] = []

for py in ROOT.rglob("*.py"):

    try:

        text = py.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()

        for category, words in KEYWORDS.items():

            if any(word in text for word in words):

                report["products"][category].append(str(py))

    except Exception:
        pass

OUTPUT = ROOT / "IOTEC_PRODUCT_DISCOVERY.json"

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 60)
print("IOTEC PRODUCT DISCOVERY ENGINE")
print("=" * 60)

for category in report["products"]:

    print(
        f"{category:20} : "
        f"{len(report['products'][category])}"
    )

print("\nArquivo gerado:")
print(OUTPUT)

print("\nSTATUS: OK")

