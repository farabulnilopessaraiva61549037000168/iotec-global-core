import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

CATALOGO = ROOT / "SOURCE_CATALOG.json"

if not CATALOGO.exists():
    pass

    print(
        "SOURCE_CATALOG.json NAO ENCONTRADO"
    )

    raise SystemExit

with open(
    CATALOGO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

estatisticas = {

    "categorias": 0,

    "fontes": 0,

    "vazias": 0
}

for categoria, info in dados[
    "categorias"
].items():

    estatisticas[
        "categorias"
    ] += 1

    qtd = len(
        info.get(
            "fontes",
            []
        )
    )

    estatisticas[
        "fontes"
    ] += qtd

    if qtd == 0:
        pass

        estatisticas[
            "vazias"
        ] += 1

dados[
    "ultima_atualizacao"
] = str(
    datetime.now()
)

saida = ROOT / (
    "SOURCE_CATALOG_STATUS.json"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        {

            "estatisticas":
                estatisticas,

            "catalogo":
                dados

        },
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    "\nSOURCE CATALOG\n"
)

print(
    "CATEGORIAS:",
    estatisticas[
        "categorias"
    ]
)

print(
    "FONTES:",
    estatisticas[
        "fontes"
    ]
)

print(
    "VAZIAS:",
    estatisticas[
        "vazias"
    ]
)

print(
    "\nSTATUS:"
)

for categoria, info in dados[
    "categorias"
].items():

    print(
        categoria,
        "->",
        len(
            info.get(
                "fontes",
                []
            )
        ),
        "fontes"
    )

print(
    "\nARQUIVO:"
)

print(saida)


