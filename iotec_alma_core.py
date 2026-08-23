import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ALMA CORE
# Sistema de OrganizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Inteligente do Ecossistema
# MetÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fora: "A Alma que organiza a Torre"
# ==========================================================

import os
from pathlib import Path
from datetime import datetime

# -----------------------------
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO PRÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIO (RAIZ)
# -----------------------------
ROOT_DIR = Path.cwd()  # diretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio onde o script ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© executado

# -----------------------------
# MAPA DA TORRE (DEPARTAMENTOS)
# -----------------------------
DEPARTAMENTOS = {
    "presidencia": ["strategy", "core", "master", "admin"],
    "recepcao": ["portal", "reception", "entry", "frontend", "ui", "html"],
    "producao": ["pipeline", "automation", "build", "generate", "worker"],
    "atendimento": ["ticket", "support", "client", "chat", "service"],
    "dados": ["data", "analytics", "report", "csv", "json"],
    "almoxarifado": ["backup", "archive", "old", "deprecated", "legacy"],
    "documentos": ["pdf", "doc", "contract", "proposal"],
    "desconhecido": []
}

# -----------------------------
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: IDENTIFICAR SETOR
# -----------------------------
def classificar_arquivo(nome_arquivo: str):
    nome = nome_arquivo.lower()

    for setor, palavras in DEPARTAMENTOS.items():
        for p in palavras:
            if p in nome:
                return setor

    return "desconhecido"


# -----------------------------
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: ESCANEAR O NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# -----------------------------
def escanear_nucleo(caminho: Path):
    inventario = {}

    for root, dirs, files in os.walk(caminho):
        for file in files:
            caminho_completo = Path(root) / file
            setor = classificar_arquivo(file)

            if setor not in inventario:
                inventario[setor] = []

            inventario[setor].append(str(caminho_completo))

    return inventario


# -----------------------------
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: GERAR RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# -----------------------------
def gerar_relatorio(inventario):
    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ IOTEC - RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DA TORRE")
    print("====================================\n")

    total = 0

    for setor, itens in inventario.items():
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â SETOR: {setor.upper()}")
        print(f"   itens encontrados: {len(itens)}\n")

        total += len(itens)

        for i in itens[:10]:  # limita visualizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
            print(f"   - {i}")

        if len(itens) > 10:
            print("   ...")

        print("\n------------------------------------\n")

    print(f"TOTAL DE ATIVOS NA TORRE: {total}")
    print("====================================\n")


# -----------------------------
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: ALMA CORE (ORQUESTRADOR)
# -----------------------------
def alma_core():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ALMA CORE INICIADA")
    print("Escaneando a torre...\n")

    inventario = escanear_nucleo(ROOT_DIR)

    print("Organizando setores...\n")

    gerar_relatorio(inventario)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â OrganizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")
    print(f"Timestamp: {datetime.now()}")


# -----------------------------
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
if __name__ == "__main__":
    alma_core()




