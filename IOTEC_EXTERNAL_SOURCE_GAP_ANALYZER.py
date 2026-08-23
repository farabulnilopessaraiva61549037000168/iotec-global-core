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

ARQUIVO = ROOT / "IOTEC_ENDPOINT_DISCOVERY_REPORT.json"

FONTES_DESEJADAS = {

    "EMPRESAS": [
        "empresa",
        "cnpj",
        "segmento"
    ],

    "ESCOLAS": [
        "escola",
        "alunos",
        "diretor"
    ],

    "UNIVERSIDADES": [
        "universidade",
        "curso",
        "campus"
    ],

    "FORNECEDORES": [
        "fornecedor",
        "contato",
        "produto"
    ],

    "TERCEIRIZADAS": [
        "grafica",
        "logistica",
        "impressao"
    ],

    "PARCEIROS": [
        "parceiro",
        "convenio",
        "integracao"
    ]
}

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    endpoints = json.load(f)

dominios = set(
    endpoints.get(
        "dominios_descobertos",
        []
    )
)

resultado = {

    "gerado_em":
        str(datetime.now()),

    "fontes_conectadas": [],

    "fontes_ausentes": [],

    "estatisticas": {}
}

for categoria in FONTES_DESEJADAS:
    pass

    resultado[
        "fontes_ausentes"
    ].append({

        "categoria":
            categoria,

        "status":
            "SEM_FONTE_REAL"
    })

resultado[
    "estatisticas"
] = {

    "dominios_detectados":
        len(dominios),

    "fontes_conectadas":
        len(
            resultado[
                "fontes_conectadas"
            ]
        ),

    "fontes_ausentes":
        len(
            resultado[
                "fontes_ausentes"
            ]
        )
}

saida = (
    ROOT /
    "IOTEC_EXTERNAL_SOURCE_GAP_REPORT.json"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nEXTERNAL SOURCE GAP ANALYSIS\n")

print(
    "DOMINIOS:",
    resultado["estatisticas"][
        "dominios_detectados"
    ]
)

print(
    "FONTES CONECTADAS:",
    resultado["estatisticas"][
        "fontes_conectadas"
    ]
)

print(
    "FONTES AUSENTES:",
    resultado["estatisticas"][
        "fontes_ausentes"
    ]
)

print("\nLACUNAS:\n")

for item in resultado[
    "fontes_ausentes"
]:

    print(
        item["categoria"],
        "->",
        item["status"]
    )

print("\nRELATORIO:")
print(saida)




