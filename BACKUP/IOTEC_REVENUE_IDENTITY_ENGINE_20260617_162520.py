import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC_REVENUE_IDENTITY_ENGINE.py
# MOTOR DE AUTOIDENTIDADE ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICA
# VersÃƒÆ'Ã†â€™o: 1.0
# Autor: IOTEC
# ==========================================================

import os
import json
import sqlite3
from pathlib import Path

ROOT = r"C:\IOTEC"

CAPABILITY_MAP = {}
FILES_FOUND = []

KEYWORDS = {
    "CRM": ["crm"],
    "BI": ["dashboard", "powerbi", "indicator"],
    "AUTOMACAO": ["automation", "workflow", "orchestrator"],
    "AUDITORIA": ["audit", "inspector", "scanner"],
    "IA": ["ai", "intelligence", "neural", "brain"],
    "INTEGRACAO": ["integration", "bridge", "connector"],
    "COMERCIAL": ["sales", "lead", "opportunity", "commercial"],
    "FINANCEIRO": ["billing", "invoice", "payment", "revenue"],
}

print("")
print("===================================")
print("IOTEC REVENUE IDENTITY ENGINE")
print("===================================")
print("")

# ----------------------------------------------------------
# INVENTARIO DE ARQUIVOS
# ----------------------------------------------------------

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        path = os.path.join(root, file)

        FILES_FOUND.append(path)

        lower = file.lower()

        for capability, words in KEYWORDS.items():
            pass

            for word in words:
                pass

                if word in lower:
                    pass

                    CAPABILITY_MAP.setdefault(
                        capability,
                        []
                    ).append(path)

# ----------------------------------------------------------
# CONTAGEM
# ----------------------------------------------------------

SUMMARY = {}

for capability, items in CAPABILITY_MAP.items():
    pass

    SUMMARY[capability] = len(items)

# ----------------------------------------------------------
# GRAVA MAPA DE CAPACIDADES
# ----------------------------------------------------------

capability_file = os.path.join(
    ROOT,
    "CAPABILITY_MAP.json"
)

with open(
    capability_file,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        CAPABILITY_MAP,
        f,
        indent=4,
        ensure_ascii=False
    )

# ----------------------------------------------------------
# MATRIZ ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICA
# ----------------------------------------------------------

REVENUE_MATRIX = {
    "CRM": {
        "mercados": [
            "CLINICAS",
            "CONTABILIDADES",
            "ESCOLAS"
        ],
        "ticket": 3500
    },

    "AUTOMACAO": {
        "mercados": [
            "INDUSTRIAS",
            "CLINICAS"
        ],
        "ticket": 10000
    },

    "AUDITORIA": {
        "mercados": [
            "INDUSTRIAS",
            "PREFEITURAS"
        ],
        "ticket": 5000
    },

    "BI": {
        "mercados": [
            "EMPRESAS",
            "CONTABILIDADES"
        ],
        "ticket": 2500
    },

    "IA": {
        "mercados": [
            "TODOS"
        ],
        "ticket": 15000
    }
}

# ----------------------------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ----------------------------------------------------------

report = []

report.append("")
report.append("===================================")
report.append("AUTOIDENTIDADE ECONOMICA")
report.append("===================================")
report.append("")

report.append(
    f"ARQUIVOS ANALISADOS: {len(FILES_FOUND)}"
)

report.append("")

report.append("CAPACIDADES IDENTIFICADAS")
report.append("")

for cap, qty in SUMMARY.items():
    pass

    report.append(
        f"{cap}: {qty} MODULOS"
    )

report.append("")
report.append("MERCADOS POTENCIAIS")
report.append("")

for cap, data in REVENUE_MATRIX.items():
    pass

    report.append(
        f"{cap} -> "
        f"{', '.join(data['mercados'])}"
    )

report.append("")
report.append("REVENUE PRIORITY")
report.append("")

for cap, data in REVENUE_MATRIX.items():
    pass

    report.append(
        f"{cap} | "
        f"Ticket MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dio: "
        f"R$ {data['ticket']:,.2f}"
    )

report_file = os.path.join(
    ROOT,
    "REVENUE_EXTRACTION_REPORT.txt"
)

with open(
    report_file,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(report))

print(
    f"MAPA: {capability_file}"
)

print(
    f"RELATORIO: {report_file}"
)

print("")
print("CONCLUIDO")
print("")


