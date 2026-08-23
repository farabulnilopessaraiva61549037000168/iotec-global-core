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

    "estado_atual": {

        "arquitetura": "MADURA",
        "auditoria": "MADURA",
        "governanca": "MADURA",
        "catalogacao": "INICIADA",
        "fontes_reais": "INSUFICIENTES"
    },

    "principio_central": (

        "O crescimento futuro depende da "
        "incorporacao de fontes externas reais."
    ),

    "combustivel_do_nucleo": [

        "produtos",
        "clientes",
        "fornecedores",
        "terceirizadas",
        "parceiros",
        "historico_de_resultados"
    ],

    "dados_prioritarios": {

        "produtos": [
            "nome",
            "preco",
            "custo",
            "margem",
            "prazo"
        ],

        "clientes": [
            "empresa",
            "segmento",
            "cidade",
            "contato"
        ],

        "fornecedores": [
            "nome",
            "servico",
            "custo",
            "prazo"
        ],

        "resultados": [
            "receita",
            "vendas",
            "conversoes",
            "ticket_medio"
        ]
    },

    "pipeline": [

        "DESCoberta",
        "CATALOGACAO",
        "VALIDACAO",
        "CLASSIFICACAO",
        "MAPA_DE_META",
        "EXECUCAO",
        "AUDITORIA_FINAL"
    ],

    "regras": [

        "Nao criar motores redundantes",

        "Nao criar reservatorios redundantes",

        "Nao utilizar simulacoes como dados reais",

        "Priorizar fontes reais",

        "Todo mapa de meta deve possuir auditoria final",

        "Toda receita deve ser rastreavel"
    ],

    "relatorio_final_obrigatorio": [

        "meta_financeira",

        "receita_real",

        "ticket_medio",

        "taxa_conversao",

        "dias_de_pico",

        "dias_de_queda",

        "percentual_de_atingimento",

        "saldo_final",

        "licoes_aprendidas"
    ],

    "objetivo": {

        "meta_mensal_referencia": 100000,

        "observacao":
        (
            "Nao calcular projecoes sem "
            "dados reais suficientes."
        )
    }
}

ARQUIVO = (
    ROOT /
    "IOTEC_COMMERCIAL_ASSIMILATION_DIRECTIVE.json"
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

print("\nCOMMERCIAL ASSIMILATION DIRECTIVE\n")

print(
    "DIRETRIZ REGISTRADA"
)

print(
    "\nMETA REFERENCIA:"
)

print(
    "R$ 100.000 / MES"
)

print(
    "\nARQUIVO:"
)

print(ARQUIVO)


