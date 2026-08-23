import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
CAPABILITIES = {

    "RESILIENCIA": {
        "mercado": "PREFEITURAS",
        "valor_medio": 100000
    },

    "DIGITAL_TWIN": {
        "mercado": "INFRAESTRUTURA",
        "valor_medio": 150000
    },

    "CONTINUIDADE_OPERACIONAL": {
        "mercado": "EMPRESAS",
        "valor_medio": 200000
    },

    "GOVERNANCA": {
        "mercado": "SETOR_PUBLICO",
        "valor_medio": 80000
    },

    "ROBOTICA_ASSISTIVA": {
        "mercado": "SAUDE",
        "valor_medio": 500000
    }

}




