import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC_HIDDEN_CAPABILITIES_ENGINE.py
# CAÃƒÆ'Ã†â€™ADOR DE CAPACIDADES OCULTAS
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ALTERA NADA
# SOMENTE INVESTIGA
# ==========================================================

import os
import re
import json
from collections import defaultdict

ROOT = r"C:\IOTEC"

IGNORE = {
    "venv",
    "node_modules",
    "__pycache__",
    "DUPLICADOS",
    ".git",
    "backup",
    "backups"
}

# -----------------------------------------
# PALAVRAS DE NEGÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œCIO
# -----------------------------------------

BUSINESS_SIGNALS = {

    "COMERCIAL": [
        "lead",
        "cliente",
        "customer",
        "sales",
        "proposal",
        "opportunity"
    ],

    "AUTOMACAO": [
        "automation",
        "workflow",
        "trigger",
        "schedule"
    ],

    "AUDITORIA": [
        "audit",
        "auditoria",
        "scanner",
        "inspection"
    ],

    "IA": [
        "brain",
        "ai",
        "neural",
        "intelligence",
        "prediction"
    ],

    "BI": [
        "dashboard",
        "report",
        "analytics",
        "indicator"
    ],

    "FINANCEIRO": [
        "payment",
        "invoice",
        "billing",
        "revenue"
    ]
}

# -----------------------------------------
# RESULTADOS
# -----------------------------------------

capability_hits = defaultdict(int)

hidden_assets = []

functions_found = defaultdict(list)

print("")
print("===================================")
print("HIDDEN CAPABILITIES ENGINE")
print("===================================")
print("")

# -----------------------------------------
# VARREDURA
# -----------------------------------------

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]

    for file in files:
        pass

        if not file.endswith(".py"):
            continue

        path = os.path.join(root, file)

        try:
            pass

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                content = f.read().lower()

        except:
            continue

        # ---------------------------------
        # FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
        # ---------------------------------

        funcs = re.findall(
            r"def\s+([a-zA-Z0-9_]+)",
            content
        )

        functions_found[file] = funcs

        # ---------------------------------
        # CAPACIDADES
        # ---------------------------------

        score = 0

        for cap, words in BUSINESS_SIGNALS.items():
            pass

            hits = sum(
                content.count(w)
                for w in words
            )

            if hits > 0:
                pass

                capability_hits[cap] += hits

                score += hits

        # ---------------------------------
        # ATIVOS OCULTOS
        # ---------------------------------

        if score > 20:
            pass

            hidden_assets.append({
                "arquivo": file,
                "score": score,
                "funcoes": len(funcs)
            })

# -----------------------------------------
# ORDENA
# -----------------------------------------

hidden_assets = sorted(
    hidden_assets,
    key=lambda x: x["score"],
    reverse=True
)

# -----------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# -----------------------------------------

report = []

report.append("")
report.append("===================================")
report.append("CAPACIDADES OCULTAS")
report.append("===================================")
report.append("")

for cap, value in sorted(
    capability_hits.items(),
    key=lambda x: x[1],
    reverse=True
):

    report.append(
        f"{cap}: {value}"
    )

report.append("")
report.append("===================================")
report.append("TOP ATIVOS SUBESTIMADOS")
report.append("===================================")
report.append("")

for item in hidden_assets[:100]:
    pass

    report.append(
        f"{item['arquivo']} | "
        f"SCORE={item['score']} | "
        f"FUNCOES={item['funcoes']}"
    )

report.append("")
report.append("===================================")
report.append("HIPOTESES ECONOMICAS")
report.append("===================================")
report.append("")

report.append(
    "Verificar ativos com score alto"
)

report.append(
    "Agrupar ativos por problema resolvido"
)

report.append(
    "Detectar ativos sem monetizacao"
)

report.append(
    "Detectar combinacoes de modulos"
)

# -----------------------------------------
# EXPORTA
# -----------------------------------------

out = os.path.join(
    ROOT,
    "HIDDEN_CAPABILITIES_REPORT.txt"
)

with open(
    out,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(report))

print("")
print("RELATORIO GERADO:")
print(out)
print("")
print("CONCLUIDO")
print("")


