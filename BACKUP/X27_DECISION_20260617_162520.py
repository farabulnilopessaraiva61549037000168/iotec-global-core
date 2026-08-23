import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 DECISION ENGINE
# ============================================================
#
# IOTEC ECOSYSTEM
#
# X27
# Motor de DecisÃƒÆ'Ã†â€™o Operacional
#
# ============================================================

from datetime import datetime

# ============================================================
# BASE DE DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

ACOES = {

    "NODE_AGUA": {

        "CRITICO": [
            "Acionar caminhÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes-pipa",
            "Priorizar hospitais",
            "Priorizar escolas",
            "Declarar emergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia hÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­drica"
        ],

        "ALERTA": [
            "Monitorar reservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios",
            "Preparar abastecimento emergencial"
        ]
    },

    "NODE_SAUDE": {

        "CRITICO": [
            "Transferir pacientes",
            "Abrir hospital de campanha",
            "Solicitar equipes extras",
            "Acionar municÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­pios vizinhos"
        ],

        "ALERTA": [
            "Expandir capacidade",
            "Monitorar leitos"
        ]
    },

    "NODE_ABRIGOS": {

        "CRITICO": [
            "Abrir novos abrigos",
            "Solicitar colchÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
            "Solicitar cobertores",
            "Solicitar alimentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
        ],

        "ALERTA": [
            "Preparar abrigos reserva"
        ]
    },

    "NODE_ENERGIA": {

        "CRITICO": [
            "Acionar geradores",
            "Priorizar hospitais",
            "Priorizar telecomunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
            "Solicitar suporte emergencial"
        ],

        "ALERTA": [
            "Preparar contingÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia energÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica"
        ]
    },

    "NODE_LOGISTICA": {

        "CRITICO": [
            "Redefinir rotas",
            "Mobilizar transporte alternativo",
            "Criar corredor humanitÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio"
        ],

        "ALERTA": [
            "Atualizar mapa operacional"
        ]
    }

}

# ============================================================
# CENÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO DE TESTE
# ============================================================

STATUS_NODES = {

    "NODE_AGUA": "NORMAL",

    "NODE_SAUDE": "CRITICO",

    "NODE_ABRIGOS": "ATENCAO",

    "NODE_ENERGIA": "ALERTA",

    "NODE_LOGISTICA": "ALERTA"

}

# ============================================================
# PRIORIDADES
# ============================================================

PESO = {

    "CRITICO": 100,

    "ALERTA": 70,

    "ATENCAO": 40,

    "NORMAL": 10

}

# ============================================================
# GERAR PLANO
# ============================================================

def gerar_plano():
    pass

    print("\n================================================")

    print("X27 DECISION ENGINE")

    print("================================================")

    print(f"DATA: {datetime.now()}")

    print("\nORDEM OPERACIONAL\n")

    ranking = []

    for node, status in STATUS_NODES.items():
        pass

        ranking.append(

            (
                PESO[status],
                node,
                status
            )

        )

    ranking.sort(reverse=True)

    prioridade = 1

    for _, node, status in ranking:
        pass

        if status == "NORMAL":
            continue

        print("------------------------------------------------")

        print(f"PRIORIDADE {prioridade}")

        print(f"NODE   : {node}")

        print(f"STATUS : {status}")

        print("\nACOES:")

        if node in ACOES:
            pass

            if status in ACOES[node]:
                pass

                for acao in ACOES[node][status]:
                    pass

                    print(f" - {acao}")

        prioridade += 1

    print("\n================================================")

    print("PLANO OPERACIONAL GERADO")

    print("================================================")

# ============================================================
# RESUMO EXECUTIVO
# ============================================================

def resumo():
    pass

    criticos = 0
    alertas = 0

    for status in STATUS_NODES.values():
        pass

        if status == "CRITICO":
            criticos += 1

        elif status == "ALERTA":
            alertas += 1

    print("\n================================================")

    print("X27 EXECUTIVE SUMMARY")

    print("================================================")

    print(f"NODES CRITICOS : {criticos}")

    print(f"NODES ALERTA   : {alertas}")

    print("\nRECOMENDACAO:")

    if criticos > 0:
        pass

        print("Mobilizacao imediata")

    elif alertas > 0:
        pass

        print("Monitoramento reforcado")

    else:
        pass

        print("Operacao estavel")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    gerar_plano()

    resumo()


