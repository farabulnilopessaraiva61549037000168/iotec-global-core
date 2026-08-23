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

resultado = {

    "gerado_em": str(datetime.now()),

    "oportunidades": [],

    "ranking": [],

    "alertas": []
}

if not CATALOGO.exists():
    pass

    resultado["alertas"].append(
        "CATALOGO_INEXISTENTE"
    )

else:
    pass

    with open(
        CATALOGO,
        "r",
        encoding="utf-8"
    ) as f:

        catalogo = json.load(f)

    for categoria, dados in catalogo[
        "categorias"
    ].items():

        fontes = dados.get(
            "fontes",
            []
        )

        score = len(fontes)

        resultado[
            "ranking"
        ].append({

            "categoria":
                categoria,

            "fontes":
                score,

            "prioridade":
                (
                    "ALTA"
                    if score == 0
                    else "NORMAL"
                )
        })

        if score == 0:
            pass

            resultado[
                "oportunidades"
            ].append({

                "tipo":
                    "EXPANSAO",

                "categoria":
                    categoria,

                "acao":
                    "CAPTAR_FONTES"
            })

resultado[
    "ranking"
] = sorted(

    resultado[
        "ranking"
    ],

    key=lambda x: x["fontes"]
)

ARQUIVO = (
    ROOT /
    "IOTEC_OPPORTUNITY_INTERCEPTOR_REPORT.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    "\nOPPORTUNITY INTERCEPTOR\n"
)

print(
    "OPORTUNIDADES:",
    len(
        resultado[
            "oportunidades"
        ]
    )
)

print(
    "\nRANKING:\n"
)

for item in resultado[
    "ranking"
]:

    print(
        item["categoria"],
        "->",
        item["fontes"],
        "fontes"
    )

print(
    "\nARQUIVO:"
)

print(ARQUIVO)


