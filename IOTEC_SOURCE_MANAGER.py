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

CATALOGO = ROOT / "IOTEC_SOURCE_CATALOG.json"

if not CATALOGO.exists():
    raise FileNotFoundError(
        "Catalogo nao encontrado"
    )

with open(
    CATALOGO,
    "r",
    encoding="utf-8"
) as f:

    catalogo = json.load(f)

estatisticas = {
    "gerado_em": str(datetime.now()),
    "total_fontes": 0,
    "categorias_preenchidas": 0,
    "categorias_vazias": 0
}

for categoria, dados in catalogo[
    "categorias"
].items():

    qtd = len(
        dados.get(
            "fontes",
            []
        )
    )

    estatisticas[
        "total_fontes"
    ] += qtd

    if qtd > 0:
        pass

        estatisticas[
            "categorias_preenchidas"
        ] += 1

        dados["status"] = "ATIVA"

    else:
        pass

        estatisticas[
            "categorias_vazias"
        ] += 1

        dados["status"] = "VAZIA"

catalogo[
    "estatisticas"
] = estatisticas

with open(
    CATALOGO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        catalogo,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nSOURCE MANAGER\n")

print(
    "TOTAL FONTES:",
    estatisticas["total_fontes"]
)

print(
    "CATEGORIAS ATIVAS:",
    estatisticas[
        "categorias_preenchidas"
    ]
)

print(
    "CATEGORIAS VAZIAS:",
    estatisticas[
        "categorias_vazias"
    ]
)

print(
    "\nCATALOGO ATUALIZADO:"
)

print(CATALOGO)




