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
        "IOTEC_SOURCE_CATALOG.json nÃƒÆ'Ã†â€™o encontrado"
    )

with open(
    CATALOGO,
    "r",
    encoding="utf-8"
) as f:

    catalogo = json.load(f)

governanca = {

    "gerado_em": str(datetime.now()),

    "diagnostico": {},

    "prioridades": [],

    "acoes_recomendadas": []
}

total_fontes = 0

for categoria, dados in catalogo[
    "categorias"
].items():

    qtd = len(
        dados.get(
            "fontes",
            []
        )
    )

    total_fontes += qtd

    if qtd == 0:
        pass

        status = "CRITICO"

        governanca[
            "prioridades"
        ].append(categoria)

        governanca[
            "acoes_recomendadas"
        ].append({

            "categoria":
                categoria,

            "acao":
                "CATALOGAR_FONTES"
        })

    elif qtd < 5:
        pass

        status = "BAIXO"

    elif qtd < 20:
        pass

        status = "MEDIO"

    else:
        pass

        status = "ALTO"

    governanca[
        "diagnostico"
    ][categoria] = {

        "fontes":
            qtd,

        "status":
            status
    }

governanca[
    "resumo"
] = {

    "fontes_totais":
        total_fontes,

    "categorias":
        len(
            catalogo[
                "categorias"
            ]
        ),

    "categorias_criticas":
        len(
            governanca[
                "prioridades"
            ]
        )
}

saida = (
    ROOT /
    "IOTEC_SOURCE_GOVERNANCE_REPORT.json"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        governanca,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nSOURCE GOVERNANCE\n")

for categoria, info in governanca[
    "diagnostico"
].items():

    print(
        categoria,
        "->",
        info["status"],
        "(",
        info["fontes"],
        "fontes )"
    )

print(
    "\nCATEGORIAS CRITICAS:",
    len(
        governanca[
            "prioridades"
        ]
    )
)

print(
    "\nRELATORIO:"
)

print(saida)




