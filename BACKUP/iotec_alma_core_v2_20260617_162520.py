import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ALMA CORE v2
# GovernanÃƒÆ'Ã†â€™a Inteligente da Torre
# DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico + Mapa de SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde do Ecossistema
# ==========================================================

import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT_DIR = Path.cwd()

# -----------------------------
# SETORES (MAPA BASE)
# -----------------------------
SETOR_MAPA = {
    "presidencia": ["core", "master", "admin", "central", "strategy"],
    "recepcao": ["portal", "reception", "entrada", "frontend", "ui", "html"],
    "producao": ["pipeline", "automation", "worker", "build", "engine"],
    "atendimento": ["client", "chat", "ticket", "support", "msg"],
    "dados": ["data", "json", "csv", "report", "analytics"],
    "documentos": ["pdf", "doc", "contract", "proposal"],
    "almoxarifado": ["backup", "legacy", "old", "archive", "dump"],
}

# -----------------------------
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
def classificar(nome):
    n = nome.lower()

    for setor, keywords in SETOR_MAPA.items():
        for k in keywords:
            if k in n:
                return setor

    return "desconhecido"


# -----------------------------
# ESCANEAMENTO
# -----------------------------
def escanear():
    inventario = defaultdict(list)

    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            path = str(Path(root) / f)
            setor = classificar(f)
            inventario[setor].append(path)

    return inventario


# -----------------------------
# ANALISE DE SAÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DE DA TORRE
# -----------------------------
def analisar_saude(inventario):
    total = sum(len(v) for v in inventario.values())

    desconhecido = len(inventario.get("desconhecido", []))

    # setores crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos
    balanceamento = {}

    for setor, itens in inventario.items():
        balanceamento[setor] = round(len(itens) / total * 100, 2)

    return total, desconhecido, balanceamento


# -----------------------------
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE PROBLEMAS
# -----------------------------
def detectar_alertas(inventario):
    alertas = []

    if len(inventario.get("desconhecido", [])) > 1000:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Grande volume de arquivos sem classificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (DESCONHECIDO)")

    if len(inventario.get("producao", [])) < 50:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o pode estar subdimensionada")

    if len(inventario.get("recepcao", [])) > len(inventario.get("producao", [])) * 5:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  RecepÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o muito maior que produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (possÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel gargalo)")

    return alertas


# -----------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL
# -----------------------------
def relatorio(inventario):
    total, desconhecido, balanceamento = analisar_saude(inventario)
    alertas = detectar_alertas(inventario)

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ALMA CORE v2 - GOVERNANÃƒÆ'Ã†â€™A")
    print("====================================\n")

    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL DE ATIVOS: {total}")
    print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ DESCONHECIDOS: {desconhecido}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  DISTRIBUIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DA TORRE:")
    for setor, pct in balanceamento.items():
        print(f" - {setor.upper()}: {pct}%")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ ALERTAS:")
    if alertas:
        for a in alertas:
            print(" ", a)
    else:
        print(" ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Nenhum alerta crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico")

    print("\n====================================")
    print(f"Timestamp: {datetime.now()}")
    print("====================================\n")


# -----------------------------
# ALMA CORE v2
# -----------------------------
def alma_core_v2():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ALMA CORE v2 INICIADO - MODO GOVERNANÃƒÆ'Ã†â€™A\n")

    inventario = escanear()

    relatorio(inventario)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")


# -----------------------------
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
if __name__ == "__main__":
    alma_core_v2()


