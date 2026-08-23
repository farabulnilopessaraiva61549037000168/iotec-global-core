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

ARQUIVOS = [
    "IOTEC_SOURCE_CATALOG.json",
    "IOTEC_STRATEGY_EXECUTION.json",
    "IOTEC_COMMERCIAL_ASSIMILATION_DIRECTIVE.json"
]

relatorio = {
    "gerado_em": str(datetime.now()),
    "necessidades": [],
    "prioridade_maxima": None
}

# categorias esperadas
categorias = [
    "EMPRESAS",
    "ESCOLAS",
    "UNIVERSIDADES",
    "FORNECEDORES",
    "TERCEIRIZADAS",
    "PARCEIROS"
]

catalogo = ROOT / "IOTEC_SOURCE_CATALOG.json"

if catalogo.exists():
    pass

    with open(
        catalogo,
        "r",
        encoding="utf-8"
    ) as f:

        dados = json.load(f)

    for categoria in categorias:
        pass

        qtd = len(
            dados.get(
                "categorias",
                {}
            ).get(
                categoria,
                {}
            ).get(
                "fontes",
                []
            )
        )

        if qtd == 0:
            pass

            relatorio[
                "necessidades"
            ].append({

                "categoria":
                    categoria,

                "impacto":
                    "ALTO",

                "status":
                    "SEM_DADOS",

                "acao":
                    "OBTER_FONTES"
            })

        elif qtd < 5:
            pass

            relatorio[
                "necessidades"
            ].append({

                "categoria":
                    categoria,

                "impacto":
                    "MEDIO",

                "status":
                    "DADOS_INSUFICIENTES",

                "acao":
                    "EXPANDIR_FONTES"
            })

if relatorio["necessidades"]:
    pass

    relatorio[
        "prioridade_maxima"
    ] = relatorio[
        "necessidades"
    ][0]["categoria"]

ARQUIVO = (
    ROOT /
    "IOTEC_DATA_NEEDS_REPORT.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nDATA NEEDS ENGINE\n")

print(
    "NECESSIDADES:",
    len(
        relatorio[
            "necessidades"
        ]
    )
)

for item in relatorio[
    "necessidades"
]:

    print(
        item["categoria"],
        "->",
        item["status"]
    )

print(
    "\nPRIORIDADE:"
)

print(
    relatorio[
        "prioridade_maxima"
    ]
)

print(
    "\nARQUIVO:"
)

print(ARQUIVO)


