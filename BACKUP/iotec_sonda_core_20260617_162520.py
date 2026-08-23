import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC SONDA CORE v3.1
# RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio leve + exportaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o JSON
# ==========================================================

import os
import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

ROOT_DIR = Path.cwd()

# ----------------------------------------------------------
# CLASSIFICADOR SIMPLES
# ----------------------------------------------------------
def classificar(nome):
    n = nome.lower()

    if any(x in n for x in ["core", "master", "central"]):
        return "presidencia"
    if any(x in n for x in ["portal", "html", "ui", "frontend"]):
        return "recepcao"
    if any(x in n for x in ["pipeline", "engine", "worker"]):
        return "producao"
    if any(x in n for x in ["chat", "client", "ticket"]):
        return "atendimento"
    if any(x in n for x in ["json", "csv", "data", "report"]):
        return "dados"
    if any(x in n for x in ["pdf", "doc"]):
        return "documentos"
    if any(x in n for x in ["backup", "legacy", "old"]):
        return "almoxarifado"

    return "desconhecido"


# ----------------------------------------------------------
# ESCANEAR
# ----------------------------------------------------------
def escanear():
    inv = defaultdict(list)

    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            path = str(Path(root) / f)
            setor = classificar(f)
            inv[setor].append(path)

    return inv


# ----------------------------------------------------------
# ANALISE
# ----------------------------------------------------------
def analisar(inv):
    total = sum(len(v) for v in inv.values())

    duplicados = Counter([os.path.basename(p) for v in inv.values() for p in v])
    duplicados = {k: v for k, v in duplicados.items() if v > 1}

    desconhecido = len(inv.get("desconhecido", []))

    return {
        "total": total,
        "desconhecido": desconhecido,
        "duplicados": duplicados,
        "distribuicao": {k: len(v) for k, v in inv.items()}
    }


# ----------------------------------------------------------
# EXPORTAR JSON
# ----------------------------------------------------------
def exportar(relatorio):
    file = "sonda_relatorio.json"

    with open(file, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)

    return file


# ----------------------------------------------------------
# EXECUTAR SONDA
# ----------------------------------------------------------
def sonda():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  SONDA ALMA CORE INICIADA (modo leve)\n")

    inv = escanear()
    rel = analisar(inv)

    arquivo = exportar(rel)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ RESUMO RÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂPIDO")
    print(f"TOTAL: {rel['total']}")
    print(f"DESCONHECIDOS: {rel['desconhecido']}")
    print(f"DUPLICADOS: {len(rel['duplicados'])}")
    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  DISTRIBUIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:")
    for k, v in rel["distribuicao"].items():
        print(f" - {k}: {v}")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¾ RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO SALVO EM:")
    print(f" {arquivo}")

    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â SONDA FINALIZADA")


if __name__ == "__main__":
    sonda()


