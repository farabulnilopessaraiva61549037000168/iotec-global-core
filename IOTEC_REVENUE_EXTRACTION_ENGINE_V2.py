import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC_REVENUE_EXTRACTION_ENGINE_V2.py
# MOTOR DE EXTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE RECEITA V2
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O MODIFICA ARQUIVOS EXISTENTES
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O REESCREVE MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# APENAS ANALISA E ORGANIZA
# ==========================================================

import os
import json
from collections import defaultdict

ROOT = r"C:\IOTEC"

# ----------------------------------------------------------
# PASTAS IGNORADAS
# ----------------------------------------------------------

IGNORE_DIRS = {
    "venv",
    "node_modules",
    "__pycache__",
    "DUPLICADOS",
    "backup",
    "backups",
    "dist",
    "build",
    ".git"
}

# ----------------------------------------------------------
# MAPA DE CAPACIDADES
# ----------------------------------------------------------

CAPABILITIES = {

    "CRM": [
        "crm",
        "customer",
        "client",
        "cliente",
        "sales",
        "lead"
    ],

    "COMERCIAL": [
        "commercial",
        "opportunity",
        "proposal",
        "sales",
        "lead",
        "funnel"
    ],

    "AUTOMACAO": [
        "automation",
        "workflow",
        "orchestrator",
        "scheduler",
        "trigger"
    ],

    "AUDITORIA": [
        "audit",
        "auditoria",
        "scanner",
        "inspector",
        "forense"
    ],

    "BI": [
        "dashboard",
        "report",
        "analytics",
        "economic",
        "indicator"
    ],

    "IA": [
        "ai",
        "brain",
        "intelligence",
        "neural",
        "assistant"
    ],

    "FINANCEIRO": [
        "billing",
        "invoice",
        "payment",
        "revenue",
        "paypal"
    ],

    "INTEGRACAO": [
        "bridge",
        "connector",
        "integration",
        "gateway",
        "api"
    ]
}

# ----------------------------------------------------------
# COMPETÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIAS ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICAS
# ----------------------------------------------------------

COMPETENCIES = {

    "INTELIGENCIA_COMERCIAL": {
        "capabilities": [
            "CRM",
            "COMERCIAL",
            "BI"
        ],
        "market": [
            "CLINICAS",
            "CONTABILIDADES",
            "ESCOLAS"
        ],
        "ticket": 3500
    },

    "AUTOMACAO_INDUSTRIAL": {
        "capabilities": [
            "AUTOMACAO",
            "IA",
            "AUDITORIA"
        ],
        "market": [
            "INDUSTRIAS"
        ],
        "ticket": 10000
    },

    "AUDITORIA_OPERACIONAL": {
        "capabilities": [
            "AUDITORIA",
            "BI"
        ],
        "market": [
            "PREFEITURAS",
            "INDUSTRIAS"
        ],
        "ticket": 5000
    },

    "INTELIGENCIA_EXECUTIVA": {
        "capabilities": [
            "BI",
            "IA",
            "FINANCEIRO"
        ],
        "market": [
            "EMPRESAS"
        ],
        "ticket": 2500
    }
}

# ----------------------------------------------------------
# INVENTÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO
# ----------------------------------------------------------

inventory = defaultdict(list)

total_files = 0

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE_DIRS
    ]

    for file in files:
        pass

        total_files += 1

        full = os.path.join(root, file)

        name = file.lower()

        for cap, words in CAPABILITIES.items():
            pass

            if any(w in name for w in words):
                pass

                inventory[cap].append(full)

# ----------------------------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ----------------------------------------------------------

report = []

report.append("")
report.append("===================================")
report.append("IOTEC REVENUE EXTRACTION ENGINE")
report.append("===================================")
report.append("")

report.append(
    f"ARQUIVOS ANALISADOS: {total_files}"
)

report.append("")

report.append("CAPACIDADES")
report.append("")

for cap in sorted(inventory.keys()):
    pass

    report.append(
        f"{cap}: {len(inventory[cap])}"
    )

report.append("")
report.append("===================================")
report.append("COMPETENCIAS ECONOMICAS")
report.append("===================================")
report.append("")

ranking = []

for comp, cfg in COMPETENCIES.items():
    pass

    score = 0

    modules = []

    for cap in cfg["capabilities"]:
        pass

        qty = len(inventory.get(cap, []))

        score += qty

        modules.extend(
            inventory.get(cap, [])[:5]
        )

    ranking.append(
        (
            score,
            comp,
            cfg
        )
    )

ranking.sort(reverse=True)

for score, comp, cfg in ranking:
    pass

    report.append("")
    report.append(f"COMPETENCIA: {comp}")

    report.append(
        f"MERCADOS: "
        f"{', '.join(cfg['market'])}"
    )

    report.append(
        f"TICKET MEDIO: "
        f"R$ {cfg['ticket']:,.2f}"
    )

    report.append(
        f"MATURIDADE: {score}"
    )

    report.append("")

# ----------------------------------------------------------
# TOP PRIORIDADES
# ----------------------------------------------------------

report.append("")
report.append("===================================")
report.append("TOP PRIORIDADES")
report.append("===================================")

for pos, (score, comp, cfg) in enumerate(
        ranking[:10],
        start=1
):

    report.append(
        f"{pos}ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº {comp}"
    )

    report.append(
        f"Ticket: R$ {cfg['ticket']:,.2f}"
    )

    report.append(
        f"Maturidade: {score}"
    )

    report.append("")

# ----------------------------------------------------------
# ATIVOS NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O MONETIZADOS
# ----------------------------------------------------------

report.append("")
report.append("===================================")
report.append("ATIVOS DE ALTO VALOR")
report.append("===================================")

keywords = [
    "dashboard",
    "executive",
    "economic",
    "crm",
    "sales",
    "brain",
    "audit"
]

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE_DIRS
    ]

    for file in files:
        pass

        lower = file.lower()

        if any(
            k in lower
            for k in keywords
        ):

            report.append(file)

# ----------------------------------------------------------
# EXPORTA
# ----------------------------------------------------------

json_file = os.path.join(
    ROOT,
    "REVENUE_INTELLIGENCE_MAP.json"
)

with open(
    json_file,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        inventory,
        f,
        indent=4,
        ensure_ascii=False
    )

txt_file = os.path.join(
    ROOT,
    "REVENUE_INTELLIGENCE_REPORT.txt"
)

with open(
    txt_file,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(report))

print("")
print("===================================")
print("REVENUE EXTRACTION ENGINE V2")
print("===================================")
print("")
print("MAPA:")
print(json_file)
print("")
print("RELATORIO:")
print(txt_file)
print("")
print("CONCLUIDO")
print("")




