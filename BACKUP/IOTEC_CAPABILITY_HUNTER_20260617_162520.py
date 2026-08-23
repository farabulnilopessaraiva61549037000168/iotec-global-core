import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC CAPABILITY HUNTER
# ARQUEOLOGIA DE CAPACIDADES DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ============================================================
# OBJETIVO:
# Vasculhar o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo IOTEC em busca de:
# - produtos ocultos
# - automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
# - dashboards
# - APIs
# - IA
# - pipelines
# - sistemas vendÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡veis
#
# MODO:
# SOMENTE LEITURA
# (nÃƒÆ'Ã†â€™o altera, nÃƒÆ'Ã†â€™o move e nÃƒÆ'Ã†â€™o apaga arquivos)
# ============================================================

import os
import json
from collections import defaultdict
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================

ROOT_PATH = r"C:\IOTEC"

EXTENSOES_ANALISADAS = [
    ".py",
    ".js",
    ".ts",
    ".html",
    ".json",
    ".md"
]

# ============================================================
# PALAVRAS-CHAVE DE CAPACIDADE
# ============================================================

CAPACIDADES = {
    "dashboard": [
        "dashboard",
        "analytics",
        "plotly",
        "grafico",
        "chart",
        "painel"
    ],

    "api": [
        "flask",
        "fastapi",
        "endpoint",
        "api",
        "router"
    ],

    "automacao": [
        "automation",
        "bot",
        "whatsapp",
        "selenium",
        "playwright",
        "scraping"
    ],

    "ia": [
        "openai",
        "llm",
        "gpt",
        "neural",
        "ai",
        "machine learning"
    ],

    "pdf_relatorio": [
        "pdf",
        "report",
        "relatorio",
        "xlsx",
        "planilha"
    ],

    "frontend": [
        "react",
        "html",
        "css",
        "frontend",
        "interface",
        "ui"
    ],

    "dados": [
        "pandas",
        "numpy",
        "csv",
        "json",
        "sqlite",
        "database"
    ],

    "pipeline": [
        "pipeline",
        "engine",
        "workflow",
        "orchestrator"
    ],

    "comercial": [
        "cliente",
        "ticket",
        "orcamento",
        "pedido",
        "contrato"
    ]
}

# ============================================================
# RESULTADOS
# ============================================================

resultados = defaultdict(list)
score_global = defaultdict(int)

# ============================================================
# ANALISADOR
# ============================================================

def analisar_arquivo(path_arquivo):
    pass

    try:
        pass

        with open(path_arquivo, "r", encoding="utf-8", errors="ignore") as f:
            conteudo = f.read().lower()

        encontrou = []

        for categoria, palavras in CAPACIDADES.items():
            pass

            score_local = 0

            for palavra in palavras:
                pass

                if palavra.lower() in conteudo:
                    score_local += 1

            if score_local > 0:
                pass

                score_global[categoria] += score_local

                encontrou.append({
                    "categoria": categoria,
                    "score": score_local
                })

        return encontrou

    except:
        return []

# ============================================================
# VARREDURA
# ============================================================

print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC CAPABILITY HUNTER INICIADO")
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â½ Vasculhando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...\n")

total_arquivos = 0

for raiz, dirs, arquivos in os.walk(ROOT_PATH):
    pass

    for arquivo in arquivos:
        pass

        extensao = os.path.splitext(arquivo)[1].lower()

        if extensao in EXTENSOES_ANALISADAS:
            pass

            total_arquivos += 1

            caminho = os.path.join(raiz, arquivo)

            capacidades = analisar_arquivo(caminho)

            if capacidades:
                pass

                resultados[caminho] = capacidades

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ============================================================

print("\n===================================================")
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - MAPA DE CAPACIDADES")
print("===================================================\n")

print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL ANALISADO: {total_arquivos}\n")

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â SCORE GLOBAL DE CAPACIDADES:\n")

ranking = sorted(
    score_global.items(),
    key=lambda x: x[1],
    reverse=True
)

for categoria, score in ranking:
    print(f" - {categoria.upper()}: {score}")

print("\n===================================================")
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ CAPACIDADES DETECTADAS")
print("===================================================\n")

contador = 0

for caminho, caps in resultados.items():
    pass

    contador += 1

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ {caminho}")

    for item in caps:
        pass

        print(
            f"   -> {item['categoria'].upper()} "
            f"(score: {item['score']})"
        )

    if contador >= 100:
        print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  LIMITE VISUAL ATINGIDO")
        break

# ============================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

export = {
    "timestamp": str(datetime.now()),
    "total_arquivos": total_arquivos,
    "score_global": dict(score_global),
    "resultados": dict(resultados)
}

with open("iotec_capability_map.json", "w", encoding="utf-8") as f:
    json.dump(export, f, indent=4, ensure_ascii=False)

print("\n===================================================")
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¾ RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO SALVO:")
print(" iotec_capability_map.json")
print("===================================================\n")

print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ARQUEOLOGIA CONCLUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDA")


