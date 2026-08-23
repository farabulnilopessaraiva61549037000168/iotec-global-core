import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
VALUE_CATALOG = {

    "LANDING_PAGE": {
        "categoria": "PULSEIRA",
        "valor_base": 5000
    },

    "DASHBOARD": {
        "categoria": "COLAR",
        "valor_base": 20000
    },

    "RESILIENCIA_MUNICIPAL": {
        "categoria": "JOIA_RARA",
        "valor_base": 100000
    },

    "DIGITAL_TWIN": {
        "categoria": "JOIA_RARA",
        "valor_base": 150000
    },

    "CENTRO_OPERACIONAL": {
        "categoria": "COROA_REAL",
        "valor_base": 300000
    },

    "PLATAFORMA_NACIONAL": {
        "categoria": "ARTEFATO_UNICO",
        "valor_base": 1000000
    }

}




