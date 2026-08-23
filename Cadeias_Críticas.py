import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
CADEIAS_CRITICAS = {

    "AGUA": [

        "RESERVATORIOS",
        "TRATAMENTO",
        "DISTRIBUICAO",
        "POPULACAO"

    ],

    "ALIMENTOS": [

        "PRODUCAO",
        "ARMAZENAMENTO",
        "TRANSPORTE",
        "MERCADOS"

    ],

    "ENERGIA": [

        "GERACAO",
        "TRANSMISSAO",
        "DISTRIBUICAO",
        "CONSUMO"

    ]

}




