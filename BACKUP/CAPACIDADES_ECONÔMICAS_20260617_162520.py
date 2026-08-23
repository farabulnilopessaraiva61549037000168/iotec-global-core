import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - SONDA DE CAPACIDADES ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICAS
# ============================================================
# OBJETIVO:
# Vasculhar o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo procurando:
# - APIs
# - IA
# - automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
# - dashboards
# - OCR
# - monitoramento
# - analytics
# - monetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o potencial
# - deploys
# - microserviÃƒÆ'Ã†â€™os
#
# Gera relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio completo em JSON + TXT
# ============================================================

import os
import json
import re
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================

ROOT_DIR = r"C:\IOTEC"   # ALTERE SE NECESSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO

OUTPUT_JSON = "IOTEC_CAPABILITIES_REPORT.json"
OUTPUT_TXT  = "IOTEC_CAPABILITIES_REPORT.txt"

# ============================================================
# PALAVRAS-CHAVE E SCORE
# ============================================================

KEYWORDS = {
    "AI_ENGINE": [
        "openai",
        "gpt",
        "llm",
        "langchain",
        "agent",
        "ai",
        "intelligence"
    ],

    "MONITORING": [
        "monitor",
        "health",
        "analytics",
        "metrics",
        "dashboard",
        "stream",
        "telemetry"
    ],

    "AUTOMATION": [
        "automation",
        "auto",
        "scheduler",
        "trigger",
        "workflow",
        "pipeline"
    ],

    "OCR_DOCUMENT": [
        "ocr",
        "pdf",
        "document",
        "scan",
        "vision"
    ],

    "API_SERVICE": [
        "api",
        "fastapi",
        "flask",
        "express",
        "router",
        "endpoint"
    ],

    "AUTH_SECURITY": [
        "login",
        "auth",
        "token",
        "jwt",
        "session"
    ],

    "DATABASE": [
        "supabase",
        "postgres",
        "mongodb",
        "sqlite",
        "mysql"
    ],

    "DEPLOY_INFRA": [
        "render",
        "netlify",
        "docker",
        "deploy",
        "cloud",
        "server"
    ]
}

# ============================================================
# SCORE ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICO
# ============================================================

VALUE_SCORE = {
    "AI_ENGINE": 10,
    "MONITORING": 9,
    "AUTOMATION": 9,
    "OCR_DOCUMENT": 8,
    "API_SERVICE": 8,
    "AUTH_SECURITY": 6,
    "DATABASE": 5,
    "DEPLOY_INFRA": 9
}

# ============================================================
# EXTENSÃƒÆ'Ã†â€™ES
# ============================================================

VALID_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".env",
    ".md"
]

# ============================================================
# RESULTADOS
# ============================================================

report = {
    "generated_at": str(datetime.now()),
    "root": ROOT_DIR,
    "files_scanned": 0,
    "capabilities": [],
    "economic_opportunities": []
}

# ============================================================
# ANALISADOR
# ============================================================

def analyze_file(filepath):
    pass

    findings = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()

            for capability, words in KEYWORDS.items():
                pass

                found = []

                for word in words:
                    if word in content:
                        found.append(word)

                if found:
                    pass

                    findings.append({
                        "capability": capability,
                        "keywords": found,
                        "score": VALUE_SCORE[capability]
                    })

    except:
        pass

    return findings

# ============================================================
# SCAN
# ============================================================

for root, dirs, files in os.walk(ROOT_DIR):
    pass

    for file in files:
        pass

        ext = os.path.splitext(file)[1].lower()

        if ext in VALID_EXTENSIONS:
            pass

            path = os.path.join(root, file)

            report["files_scanned"] += 1

            results = analyze_file(path)

            if results:
                pass

                capability_data = {
                    "file": path,
                    "findings": results
                }

                report["capabilities"].append(capability_data)

# ============================================================
# AGRUPAMENTO ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICO
# ============================================================

economic_map = {}

for item in report["capabilities"]:
    pass

    for finding in item["findings"]:
        pass

        cap = finding["capability"]

        if cap not in economic_map:
            economic_map[cap] = 0

        economic_map[cap] += finding["score"]

# ============================================================
# PRIORIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

sorted_caps = sorted(
    economic_map.items(),
    key=lambda x: x[1],
    reverse=True
)

for cap, score in sorted_caps:
    pass

    recommendation = ""

    if score >= 100:
        recommendation = "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ ALTÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂSSIMO POTENCIAL COMERCIAL"

    elif score >= 50:
        recommendation = "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ ALTO POTENCIAL"

    elif score >= 20:
        recommendation = "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¢ POTENCIAL MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIO"

    else:
        recommendation = "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Âª BAIXO POTENCIAL"

    report["economic_opportunities"].append({
        "capability": cap,
        "score": score,
        "recommendation": recommendation
    })

# ============================================================
# EXPORT JSON
# ============================================================

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

# ============================================================
# EXPORT TXT
# ============================================================

with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    pass

    f.write("\n")
    f.write("====================================================\n")
    f.write(" IOTEC - RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE CAPACIDADES ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICAS\n")
    f.write("====================================================\n\n")

    f.write(f"ROOT: {ROOT_DIR}\n")
    f.write(f"ARQUIVOS ESCANEADOS: {report['files_scanned']}\n")
    f.write(f"GERADO EM: {report['generated_at']}\n\n")

    f.write("====================================================\n")
    f.write(" OPORTUNIDADES ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICAS\n")
    f.write("====================================================\n\n")

    for opp in report["economic_opportunities"]:
        pass

        f.write(f"CAPACIDADE: {opp['capability']}\n")
        f.write(f"SCORE: {opp['score']}\n")
        f.write(f"STATUS: {opp['recommendation']}\n")
        f.write("\n")

    f.write("====================================================\n")
    f.write(" CAPACIDADES DETECTADAS\n")
    f.write("====================================================\n\n")

    for cap in report["capabilities"]:
        pass

        f.write(f"ARQUIVO: {cap['file']}\n")

        for finding in cap["findings"]:
            pass

            f.write(f"  -> {finding['capability']}\n")
            f.write(f"     KEYWORDS: {finding['keywords']}\n")
            f.write(f"     SCORE: {finding['score']}\n")

        f.write("\n")

print("\n================================================")
print(" ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC SONDA FINALIZADA")
print("================================================")
print(f" Arquivos escaneados: {report['files_scanned']}")
print(f" RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio JSON: {OUTPUT_JSON}")
print(f" RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio TXT : {OUTPUT_TXT}")
print("================================================\n")


