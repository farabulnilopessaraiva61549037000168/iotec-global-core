import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ALMA CORE v5
# CONSOLIDADOR ARQUITETURAL FINAL
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo vs Produto vs Legado vs RuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico
# ==========================================================

import os
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

ROOT_DIR = Path.cwd()

# ----------------------------------------------------------
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ARQUITETURAL AVANÃƒÆ'Ã†â€™ADA
# ----------------------------------------------------------

NUCLEO = [
    "core", "master", "central", "kernel", "orchestrator",
    "engine", "system", "gateway", "brain", "main"
]

PRODUTO = [
    "portal", "frontend", "ui", "html", "client", "chat",
    "dashboard", "interface", "app"
]

LEGADO = [
    "backup", "legacy", "old", "archive", "dump", "v1", "v2", "v3"
]

INFRA = [
    "pipeline", "worker", "automation", "build", "script", "task"
]

DADOS = [
    "json", "csv", "data", "report", "analytics", "log"
]


# ----------------------------------------------------------
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ARQUITETURAL REAL
# ----------------------------------------------------------
def classificar_arquitetura(nome: str):
    pass

    n = nome.lower()

    if any(k in n for k in NUCLEO):
        return "NUCLEO"

    if any(k in n for k in PRODUTO):
        return "PRODUTO"

    if any(k in n for k in INFRA):
        return "INFRAESTRUTURA"

    if any(k in n for k in DADOS):
        return "DADOS"

    if any(k in n for k in LEGADO):
        return "LEGADO"

    return "RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO"


# ----------------------------------------------------------
# ESCANEAMENTO
# ----------------------------------------------------------
def escanear():
    mapa = defaultdict(list)

    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            path = str(Path(root) / f)
            categoria = classificar_arquitetura(f)
            mapa[categoria].append(path)

    return mapa


# ----------------------------------------------------------
# ANÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLISE DE ARQUITETURA
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
        "nucleo": len(mapa.get("NUCLEO", [])),
        "produto": len(mapa.get("PRODUTO", [])),
        "infra": len(mapa.get("INFRAESTRUTURA", [])),
        "dados": len(mapa.get("DADOS", [])),
        "legado": len(mapa.get("LEGADO", [])),
        "ruido": len(mapa.get("RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO", [])),
        "duplicados": len(duplicados),
        "top_duplicados": dict(list(duplicados.items())[:10])
    }


# ----------------------------------------------------------
# DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO ARQUITETURAL FINAL
# ----------------------------------------------------------
def diagnostico(r):
    pass

    alertas = []

    if r["nucleo"] < r["total"] * 0.03:
        alertas.append("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo extremamente subdimensionado")

    if r["ruido"] > r["total"] * 0.4:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Sistema com alto nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel de indefiniÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estrutural (RUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO)")

    if r["legado"] > r["nucleo"] * 5:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Legado excessivo dominando arquitetura atual")

    if r["produto"] < r["nucleo"] * 0.5:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Baixa conversÃƒÆ'Ã†â€™o de nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo em produto")

    if r["duplicados"] > 10000:
        alertas.append("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  DuplicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estrutural crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica")

    return alertas


# ----------------------------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL
# ----------------------------------------------------------
def relatorio(mapa):
    pass

    r = analisar(mapa)
    alertas = diagnostico(r)

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ALMA CORE v5 - ARQUITETO FINAL")
    print("====================================\n")

    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TOTAL DE ATIVOS: {r['total']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ARQUITETURA REAL:")
    print(f" - NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo: {r['nucleo']}")
    print(f" - Produto: {r['produto']}")
    print(f" - Infraestrutura: {r['infra']}")
    print(f" - Dados: {r['dados']}")
    print(f" - Legado: {r['legado']}")
    print(f" - RuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do: {r['ruido']}")
    print(f" - Duplicados: {r['duplicados']}\n")

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¨ DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO ESTRUTURAL:")
    if alertas:
        for a in alertas:
            print(" ", a)
    else:
        print(" ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Arquitetura relativamente saudÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel")

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ TOP DUPLICADOS:")
    for k, v in r["top_duplicados"].items():
        print(f" - {k}: {v}")

    print("\n====================================")
    print(f"Timestamp: {datetime.now()}")
    print("====================================\n")


# ----------------------------------------------------------
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ----------------------------------------------------------
def arquiteto_final():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ALMA CORE v5 - ARQUITETO FINAL INICIADO\n")

    mapa = escanear()
    relatorio(mapa)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ConsolidaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o arquitetural concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")


if __name__ == "__main__":
    arquiteto_final()




