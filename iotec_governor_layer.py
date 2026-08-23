import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC GOVERNOR LAYER v1.0
# Camada de governanÃƒÆ'Ã†â€™a do ecossistema
# ==========================================================

import os
import json
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº REGRAS DE GOVERNO
# -----------------------------
REGRAS = {
    "core": ["core", "master", "central", "orquestr", "govern"],
    "producao": ["pipeline", "build", "gerar", "process", "automation"],
    "recepcao": ["form", "html", "interface", "chat", "cliente"],
    "dados": ["json", "csv", "db", "data", "event"],
    "presidencia": ["admin", "audit", "verify", "control", "gov"],
    "almoxarifado": ["backup", "legacy", "archive", "old"],
    "documentos": ["doc", "pdf", "readme", "md"],
    "atendimento": ["ticket", "msg", "support", "chat"]
}


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
def classificar(path):
    p = path.lower()

    for setor, palavras in REGRAS.items():
        for palavra in palavras:
            if palavra in p:
                return setor

    return "ruido"


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ ESCANEAMENTO
# -----------------------------
def escanear(root):
    mapa = defaultdict(list)
    total = 0

    for base, _, files in os.walk(root):
        for f in files:
            full = os.path.join(base, f)
            setor = classificar(full)
            mapa[setor].append(full)
            total += 1

    return mapa, total


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â DUPLICADOS
# -----------------------------
def duplicados(mapa):
    freq = defaultdict(int)

    for setor in mapa:
        for file in mapa[setor]:
            nome = os.path.basename(file)
            freq[nome] += 1

    return {k: v for k, v in freq.items() if v > 1}


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  PESO DE IMPORTÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡NCIA
# -----------------------------
PESO = {
    "core": 100,
    "presidencia": 80,
    "producao": 70,
    "dados": 60,
    "atendimento": 50,
    "recepcao": 40,
    "documentos": 30,
    "almoxarifado": 20,
    "ruido": 1
}


def calcular_score(mapa):
    score = {}

    for setor, itens in mapa.items():
        score[setor] = len(itens) * PESO.get(setor, 1)

    return dict(sorted(score.items(), key=lambda x: -x[1]))


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DE GOVERNO
# -----------------------------
def relatorio(mapa, total):
    dup = duplicados(mapa)
    score = calcular_score(mapa)

    return {
        "timestamp": str(datetime.now()),
        "total_ativos": total,
        "estrutura": {k: len(v) for k, v in mapa.items()},
        "duplicados": dup,
        "score_governanca": score
    }


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO VISUAL
# -----------------------------
def imprimir(rel):
    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº IOTEC - GOVERNOR LAYER")
    print("====================================")

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL DE ATIVOS: {rel['total_ativos']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  ESTRUTURA:")
    for k, v in rel["estrutura"].items():
        print(f" - {k}: {v}")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â SCORE DE IMPORTÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡NCIA:")
    for k, v in rel["score_governanca"].items():
        print(f" - {k}: {v}")

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  TOP DUPLICADOS:")
    for k, v in sorted(rel["duplicados"].items(), key=lambda x: -x[1])[:10]:
        print(f" - {k}: {v}")

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â GOVERNANÃƒÆ'Ã†â€™A FINALIZADA")
    print("====================================\n")


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¾ SALVAR
# -----------------------------
def salvar(rel):
    with open("iotec_governanca.json", "w", encoding="utf-8") as f:
        json.dump(rel, f, indent=4, ensure_ascii=False)


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
if __name__ == "__main__":
    mapa, total = escanear(ROOT)
    rel = relatorio(mapa, total)

    imprimir(rel)
    salvar(rel)




