import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_REAL_ENTITY_EXTRACTOR.py

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ARQUIVO_ORIGEM = ROOT / "BUSINESS_REALITY_REPORT.json"

ARQUIVO_MASTER = ROOT / "BUSINESS_MASTER_RESERVOIR.json"

REAL_RESERVOIR = {
    "gerado_em": str(datetime.now()),
    "reais": [],
    "provaveis_reais": [],
    "estatisticas": {}
}

with open(
    ARQUIVO_ORIGEM,
    "r",
    encoding="utf-8"
) as f:

    reality = json.load(f)

with open(
    ARQUIVO_MASTER,
    "r",
    encoding="utf-8"
) as f:

    master = json.load(f)

status_por_arquivo = {}

for registro in reality["registros"]:
    pass

    status_por_arquivo[
        registro["arquivo"]
    ] = registro["status"]

for registro in master["registros"]:
    pass

    arquivo = registro["arquivo"]

    status = status_por_arquivo.get(
        arquivo,
        "DESCONHECIDO"
    )

    if status == "REAL":
        pass

        REAL_RESERVOIR[
            "reais"
        ].append(registro)

    elif status == "PROVAVEL_REAL":
        pass

        REAL_RESERVOIR[
            "provaveis_reais"
        ].append(registro)

REAL_RESERVOIR[
    "estatisticas"
] = {

    "reais":
        len(
            REAL_RESERVOIR["reais"]
        ),

    "provaveis_reais":
        len(
            REAL_RESERVOIR[
                "provaveis_reais"
            ]
        ),

    "total":
        len(
            REAL_RESERVOIR["reais"]
        )
        +
        len(
            REAL_RESERVOIR[
                "provaveis_reais"
            ]
        )
}

saida = ROOT / "REAL_BUSINESS_RESERVOIR.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        REAL_RESERVOIR,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nREAL ENTITY EXTRACTION\n")

print(
    "REAIS:",
    REAL_RESERVOIR[
        "estatisticas"
    ]["reais"]
)

print(
    "PROVAVEIS:",
    REAL_RESERVOIR[
        "estatisticas"
    ]["provaveis_reais"]
)

print(
    "TOTAL:",
    REAL_RESERVOIR[
        "estatisticas"
    ]["total"]
)

print(
    "\nARQUIVO:"
)

print(saida)


