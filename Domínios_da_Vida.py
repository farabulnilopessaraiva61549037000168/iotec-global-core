import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
DOMINIOS = {

    "AGUA": {
        "prioridade": 1,
        "missao": "Garantir abastecimento"
    },

    "ALIMENTOS": {
        "prioridade": 1,
        "missao": "Garantir seguranÃƒÆ'Ã†â€™a alimentar"
    },

    "SAUDE": {
        "prioridade": 1,
        "missao": "Preservar vidas"
    },

    "ENERGIA": {
        "prioridade": 2,
        "missao": "Garantir continuidade"
    },

    "COMUNICACAO": {
        "prioridade": 2,
        "missao": "Manter coordenaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
    },

    "LOGISTICA": {
        "prioridade": 2,
        "missao": "Garantir distribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
    },

    "PECUARIA": {
        "prioridade": 3,
        "missao": "Preservar rebanhos"
    },

    "AGRICULTURA": {
        "prioridade": 3,
        "missao": "Garantir produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
    }

}




