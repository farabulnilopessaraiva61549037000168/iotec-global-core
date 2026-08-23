import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ALMA CORE v4 - GOVERNADOR DO ECOSSISTEMA
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo oficial + histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico + experimental + ruÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do
# ==========================================================

import os
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

ROOT_DIR = Path.cwd()

# ----------------------------------------------------------
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTELIGENTE (3 DIMENSÃƒÆ'Ã†â€™ES)
# ----------------------------------------------------------

NUCLEO_INDICADORES = [
    "core", "master", "central", "engine", "orchestrator",
    "api", "kernel", "system", "main", "gateway"
]

HISTORICO_INDICADORES = [
    "backup", "legacy", "old", "archive", "dump", "v1", "v2", "v3"
]

EXPERIMENTAL_INDICADORES = [
    "test", "dev", "lab", "sandbox", "beta", "prototype"
]


# ----------------------------------------------------------
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ----------------------------------------------------------
def classificar_fase(nome: str):
    pass

    n = nome.lower()

    if any(k in n for k in NUCLEO_INDICADORES):
        return "NUCLEO_OFICIAL"

    if any(k in n for k in HISTORICO_INDICADORES):
        return "HISTORICO"

    if any(k in n for k in EXPERIMENTAL_INDICADORES):
        return "EXPERIMENTAL"

    return "RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO/NAO_CLASSIFICADO"


# ----------------------------------------------------------
# ESCANEAMENTO
# ----------------------------------------------------------
def escanear():
    mapa = defaultdict(list)

    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            path = str(Path(root) / f)
            categoria = classificar_fase(f)
            mapa[categoria].append(path)

    return mapa


# ----------------------------------------------------------
# ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE ESTRUTURAL
# ----------------------------------------------------------
def analisar(mapa):
    pass

    total = sum(len(v) for v in mapa.values())

    duplicados = Counter(
        [os.path.basename(p) for v in mapa.values() for p in v]
    )

    duplicados = {k: v for k, v in duplicados.items() if v > 1}

    return {
        "total": total,
        "nucleo": len(mapa.get("NUCLEO_OFICIAL", [])),
        "historico": len(mapa.get("HISTORICO", [])),
        "experimental": len(mapa.get("EXPERIMENTAL", [])),
        "ruido": len(mapa.get("RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO/NAO_CLASSIFICADO", [])),
        "duplicados": len(duplicados),
        "top_duplicados": dict(list(duplicados.items())[:10])
    }


# ----------------------------------------------------------
# DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO DE ARQUITETURA
# ----------------------------------------------------------
def diagnostico(rel):
    pass

    alertas = []

    if rel["nucleo"] < rel["total"] * 0.05:
        alertas.append("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo oficial muito pequeno vs sistema total")

    if rel["ruido"] > rel["total"] * 0.2:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Alto nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel de ruÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do estrutural")

    if rel["duplicados"] > 5000:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Excesso crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico de duplicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de arquivos")

    if rel["historico"] > rel["nucleo"] * 3:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Sistema carregado de versÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes antigas")

    return alertas


# ----------------------------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL
# ----------------------------------------------------------
def relatorio(mapa):
    pass

    rel = analisar(mapa)
    alertas = diagnostico(rel)

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ALMA CORE v4 - GOVERNADOR")
    print("====================================\n")

    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL DE ATIVOS: {rel['total']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº DISTRIBUIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ESTRUTURAL:")
    print(f" - NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Oficial: {rel['nucleo']}")
    print(f" - HistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico: {rel['historico']}")
    print(f" - Experimental: {rel['experimental']}")
    print(f" - RuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do: {rel['ruido']}")
    print(f" - Duplicados: {rel['duplicados']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ ALERTAS ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICOS:")
    if alertas:
        for a in alertas:
            print(" ", a)
    else:
        print(" ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Estrutura relativamente estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ TOP DUPLICADOS:")
    for k, v in rel["top_duplicados"].items():
        print(f" - {k}: {v}")

    print("\n====================================")
    print(f"Timestamp: {datetime.now()}")
    print("====================================\n")


# ----------------------------------------------------------
# CORE
# ----------------------------------------------------------
def governador():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ALMA CORE v4 - GOVERNADOR INICIADO\n")

    mapa = escanear()
    relatorio(mapa)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â GovernanÃƒÆ'Ã†â€™a concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")


# ----------------------------------------------------------
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ----------------------------------------------------------
if __name__ == "__main__":
    governador()




