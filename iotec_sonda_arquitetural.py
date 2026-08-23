import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC SONDA ARQUITETURAL v1.0
# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: Mapear, classificar e estruturar a "torre digital"
# Sem destruiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de arquivos. Apenas diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico e mapa.
# ==========================================================

import os
import json
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

CATEGORIAS = {
    "core": ["core", "central", "master", "orquestr"],
    "recepcao": ["formulario", "form", "chat", "cliente", "interface", "html"],
    "producao": ["pipeline", "build", "gerar", "process", "automation"],
    "dados": ["data", "json", "csv", "db", "event"],
    "presidencia": ["admin", "govern", "control", "audit", "verify"],
    "almoxarifado": ["backup", "legacy", "old", "archive"],
    "documentos": ["doc", "pdf", "readme", "md", "leafdoc"],
    "atendimento": ["ticket", "support", "chat", "msg"],
}

def classificar(path):
    p = path.lower()

    for setor, palavras in CATEGORIAS.items():
        for palavra in palavras:
            if palavra in p:
                return setor

    return "desconhecido"


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


def duplicados(mapa):
    freq = defaultdict(int)

    for setor in mapa:
        for file in mapa[setor]:
            nome = os.path.basename(file)
            freq[nome] += 1

    return {k: v for k, v in freq.items() if v > 1}


def relatorio(mapa, total):
    dup = duplicados(mapa)

    estrutura = {k: len(v) for k, v in mapa.items()}

    return {
        "timestamp": str(datetime.now()),
        "total_ativos": total,
        "estrutura": estrutura,
        "duplicados": dup
    }


def imprimir(rel):
    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - MAPA ARQUITETURAL LIMPO")
    print("====================================")

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL: {rel['total_ativos']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ESTRUTURA:")
    for k, v in rel["estrutura"].items():
        print(f" - {k}: {v}")

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  TOP DUPLICADOS:")
    for k, v in sorted(rel["duplicados"].items(), key=lambda x: -x[1])[:10]:
        print(f" - {k}: {v}")

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MAPEAMENTO CONCLUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO")
    print("====================================\n")


def salvar(rel):
    with open("iotec_mapa_arquitetural.json", "w", encoding="utf-8") as f:
        json.dump(rel, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    mapa, total = escanear(ROOT)
    rel = relatorio(mapa, total)

    imprimir(rel)
    salvar(rel)




