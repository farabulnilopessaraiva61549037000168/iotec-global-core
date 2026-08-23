import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ALMA CORE v3
# CONSOLIDADOR DA TORRE
# ClusterizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o + DetecÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de duplicidade + SugestÃƒÆ'Ã†â€™o estrutural
# ==========================================================

import os
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

ROOT_DIR = Path.cwd()

# ----------------------------------------------------------
# MAPA BASE DE SETORES
# ----------------------------------------------------------
SETOR_MAPA = {
    "presidencia": ["core", "master", "central", "admin", "orchestrator"],
    "recepcao": ["portal", "ui", "frontend", "html", "interface"],
    "producao": ["pipeline", "engine", "worker", "automation", "build"],
    "atendimento": ["chat", "client", "ticket", "support", "msg"],
    "dados": ["json", "csv", "data", "analytics", "report"],
    "documentos": ["pdf", "doc", "contract", "proposal"],
    "almoxarifado": ["backup", "legacy", "old", "archive", "dump"],
}

# ----------------------------------------------------------
# CLASSIFICADOR BASE
# ----------------------------------------------------------
def classificar(nome: str):
    n = nome.lower()

    for setor, palavras in SETOR_MAPA.items():
        for p in palavras:
            if p in n:
                return setor

    return "desconhecido"


# ----------------------------------------------------------
# ESCANEAMENTO COMPLETO
# ----------------------------------------------------------
def escanear():
    inventario = defaultdict(list)

    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            caminho = str(Path(root) / f)
            setor = classificar(f)
            inventario[setor].append(caminho)

    return inventario


# ----------------------------------------------------------
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE DUPLICADOS (por nome base)
# ----------------------------------------------------------
def detectar_duplicados(inventario):
    nomes = []

    for itens in inventario.values():
        for path in itens:
            nomes.append(os.path.basename(path))

    contagem = Counter(nomes)

    duplicados = {k: v for k, v in contagem.items() if v > 1}

    return duplicados


# ----------------------------------------------------------
# CLUSTERIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CAOS (DESCONHECIDO)
# ----------------------------------------------------------
def cluster_desconhecido(inventario):
    grupos = defaultdict(list)

    for path in inventario.get("desconhecido", []):
        nome = os.path.basename(path).lower()

        # cluster simples por prefixo
        chave = nome[:3]
        grupos[chave].append(path)

    return grupos


# ----------------------------------------------------------
# SUGESTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CONSOLIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ----------------------------------------------------------
def sugerir_consolidacao(duplicados):
    sugestoes = []

    for nome, qtd in duplicados.items():
        if qtd > 5:
            sugestoes.append(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ CONSOLIDAR URGENTE: {nome} ({qtd} cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pias)")
        elif qtd > 2:
            sugestoes.append(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸  POSSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEL DUPLICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: {nome} ({qtd})")

    return sugestoes


# ----------------------------------------------------------
# MAPA DE SAÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DE ESTRUTURAL
# ----------------------------------------------------------
def relatorio(inventario):
    total = sum(len(v) for v in inventario.values())

    duplicados = detectar_duplicados(inventario)
    clusters = cluster_desconhecido(inventario)
    sugestoes = sugerir_consolidacao(duplicados)

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ALMA CORE v3 - CONSOLIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O")
    print("====================================\n")

    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL DE ATIVOS: {total}")
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â ITENS DUPLICADOS: {len(duplicados)}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ ALERTAS DE CONSOLIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:")
    if sugestoes:
        for s in sugestoes:
            print(" ", s)
    else:
        print(" ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Nenhuma duplicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica detectada")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â© CLUSTERS DE DESCONHECIDO:")
    for k, v in list(clusters.items())[:10]:
        print(f" - Grupo '{k}': {len(v)} itens")

    print("\n====================================")
    print(f"Timestamp: {datetime.now()}")
    print("====================================\n")


# ----------------------------------------------------------
# CORE
# ----------------------------------------------------------
def alma_core_v3():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ALMA CORE v3 INICIADO - MODO CONSOLIDADOR\n")

    inventario = escanear()
    relatorio(inventario)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ConsolidaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")


# ----------------------------------------------------------
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ----------------------------------------------------------
if __name__ == "__main__":
    alma_core_v3()


