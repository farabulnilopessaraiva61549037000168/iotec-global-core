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

ofertas = {

    "gerado_em": str(datetime.now()),

    "estado": "MAPEAMENTO",

    "perguntas_criticas": [

        "O que vendemos?",

        "Quem compra?",

        "Qual problema resolvemos?",

        "Quanto cobramos?",

        "Qual o custo?",

        "Qual a margem?",

        "Qual a capacidade mensal?",

        "Qual o prazo de entrega?",

        "Precisa de terceirizada?",

        "Precisa de fornecedor?",

        "Existe demanda conhecida?",

        "Existe historico de vendas?"
    ],

    "frentes_identificadas": [

        "Automacao Educacional",

        "Geracao de Provas",

        "Atividades Escolares",

        "Painel de Indicadores",

        "Analise de Dados",

        "Dashboards",

        "Sistemas Internos",

        "Consultoria",

        "Projetos Sob Demanda"
    ],

    "status": {

        "catalogo_de_produtos": "PENDENTE",

        "catalogo_de_precos": "PENDENTE",

        "catalogo_de_clientes": "PENDENTE",

        "catalogo_de_fornecedores": "PENDENTE"
    }
}

ARQUIVO = ROOT / "IOTEC_OFFER_DISCOVERY_REPORT.json"

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        ofertas,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nOFFER DISCOVERY ENGINE\n")

print(
    "PERGUNTAS:",
    len(
        ofertas[
            "perguntas_criticas"
        ]
    )
)

print(
    "FRENTES:",
    len(
        ofertas[
            "frentes_identificadas"
        ]
    )
)

print(
    "\nARQUIVO:"
)

print(ARQUIVO)


