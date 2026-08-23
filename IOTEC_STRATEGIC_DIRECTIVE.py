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

DIRETRIZ = {

    "gerado_em": str(datetime.now()),

    "estado_arquitetural": {

        "infraestrutura": "MADURA",

        "reservatorios": "OPERACIONAIS",

        "auditorias": "OPERACIONAIS",

        "catalogacao": "INICIADA",

        "aquisicao_externa": "PRIORIDADE_MAXIMA"
    },

    "descobertas": [

        "Motores existentes sÃƒÆ'Ã†â€™o suficientes para fase atual",

        "ReservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios existentes sÃƒÆ'Ã†â€™o suficientes para fase atual",

        "Dados internos predominam sobre dados externos",

        "CatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo de fontes foi criado",

        "EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gia de aquisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o torna-se prioridade"
    ],

    "principios": [

        "NÃƒÆ'Ã†â€™o duplicar motores sem necessidade",

        "NÃƒÆ'Ã†â€™o criar reservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios redundantes",

        "Priorizar fontes externas reais",

        "Separar dados internos de dados externos",

        "Toda fonte deve ser catalogada",

        "Toda fonte deve possuir categoria",

        "Toda categoria deve possuir estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gia"
    ],

    "categorias_prioritarias": {

        "EMPRESAS": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        },

        "ESCOLAS": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        },

        "UNIVERSIDADES": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        },

        "FORNECEDORES": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        },

        "TERCEIRIZADAS": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        },

        "PARCEIROS": {

            "meta_minima": 5,

            "meta_ideal": 20,

            "status": "CRITICO"
        }
    },

    "pipeline_recomendado": [

        "DESCOBERTA",

        "VALIDACAO",

        "CLASSIFICACAO",

        "CATALOGO",

        "GOVERNANCA",

        "OPERACAO"
    ],

    "perguntas_obrigatorias": [

        "Qual fonte utiliza?",

        "Qual categoria atende?",

        "Qual reservatorio abastece?",

        "Qual resultado produz?",

        "Qual a qualidade da fonte?",

        "A fonte e interna ou externa?"
    ]
}

ARQUIVO = (
    ROOT /
    "IOTEC_STRATEGIC_DIRECTIVE.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        DIRETRIZ,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nIOTEC STRATEGIC DIRECTIVE\n")

print(
    "DIRETRIZ ESTRATEGICA REGISTRADA"
)

print(
    "\nPRIORIDADE:"
)

print(
    "AQUISICAO EXTERNA"
)

print(
    "\nARQUIVO:"
)

print(ARQUIVO)




