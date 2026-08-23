import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 EXECUTIVE COMMAND
# ============================================================
#
# IOTEC ECOSYSTEM
#
# X27
# CENTRO EXECUTIVO DE COMANDO
#
# Consolida:
# - InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
# - DecisÃƒÆ'Ã†â€™o
# - Recursos
# - Suprimentos
# - LogÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica
# - Rastreamento
# - ComunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
# - Escalonamento
#
# ============================================================

from datetime import datetime
import random

# ============================================================
# DADOS OPERACIONAIS
# ============================================================

OPERACAO = {

    "evento": "ROMPIMENTO_BARRAGEM",

    "municipio": "IBICUITINGA",

    "populacao_afetada": 5000

}

# ============================================================
# STATUS DOS NODES
# ============================================================

STATUS_NODES = {

    "SAUDE": "CRITICO",

    "ENERGIA": "ALERTA",

    "COMUNICACAO": "OPERACIONAL",

    "AGUA": "NORMAL",

    "LOGISTICA": "ALERTA",

    "ABRIGOS": "ATENCAO"

}

# ============================================================
# COMUNICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

COMMS = {

    "internet": False,

    "telefonia": True,

    "satelite": True,

    "mesh": True,

    "geradores": True

}

# ============================================================
# TRACKING
# ============================================================

TRACKING = {

    "ativos_em_campo": 8,

    "entregues": 2,

    "atrasados": 2

}

# ============================================================
# RECURSOS
# ============================================================

RECURSOS = {

    "agua": 100000,

    "refeicoes": 15000,

    "colchoes": 5000,

    "cobertores": 5000

}

# ============================================================
# RESILIENCE INDEX
# ============================================================

def resilience():
    pass

    score = 0

    if COMMS["telefonia"]:
        score += 20

    if COMMS["satelite"]:
        score += 20

    if COMMS["mesh"]:
        score += 20

    if COMMS["geradores"]:
        score += 20

    if COMMS["internet"]:
        score += 20

    return score

# ============================================================
# STATUS GERAL
# ============================================================

def status_geral():
    pass

    criticos = 0

    for valor in STATUS_NODES.values():
        pass

        if valor == "CRITICO":
            pass

            criticos += 1

    if criticos >= 3:
        pass

        return "CRISE"

    elif criticos >= 1:
        pass

        return "OPERACAO CRITICA"

    return "OPERACAO CONTROLADA"

# ============================================================
# WAR ROOM
# ============================================================

def war_room():
    pass

    print("\n================================================")
    print("X27 EXECUTIVE COMMAND")
    print("================================================")

    print(f"DATA       : {datetime.now()}")
    print(f"EVENTO     : {OPERACAO['evento']}")
    print(f"MUNICIPIO  : {OPERACAO['municipio']}")
    print(f"POPULACAO  : {OPERACAO['populacao_afetada']}")

    print("\n================================================")
    print("STATUS OPERACIONAL")
    print("================================================")

    for node, status in STATUS_NODES.items():
        pass

        print(f"{node:<15} {status}")

    print("\n================================================")
    print("COMUNICACAO")
    print("================================================")

    for item, valor in COMMS.items():
        pass

        print(f"{item.upper():<15} {valor}")

    print("\n================================================")
    print("TRACKING")
    print("================================================")

    print(
        f"ATIVOS CAMPO : "
        f"{TRACKING['ativos_em_campo']}"
    )

    print(
        f"ENTREGUES    : "
        f"{TRACKING['entregues']}"
    )

    print(
        f"ATRASADOS    : "
        f"{TRACKING['atrasados']}"
    )

    print("\n================================================")
    print("RECURSOS")
    print("================================================")

    print(
        f"AGUA         : "
        f"{RECURSOS['agua']} L"
    )

    print(
        f"REFEICOES    : "
        f"{RECURSOS['refeicoes']}"
    )

    print(
        f"COLCHOES     : "
        f"{RECURSOS['colchoes']}"
    )

    print(
        f"COBERTORES   : "
        f"{RECURSOS['cobertores']}"
    )

# ============================================================
# ORDEM EXECUTIVA
# ============================================================

def ordem_executiva():
    pass

    print("\n================================================")
    print("ORDEM EXECUTIVA")
    print("================================================")

    print("1 - Transferir pacientes")

    print("2 - Acionar hospital parceiro")

    print("3 - Despachar caminhao reserva")

    print("4 - Atualizar WAR ROOM")

    print("5 - Garantir comunicacao")

    print("6 - Monitoramento continuo")

# ============================================================
# RESUMO
# ============================================================

def resumo():
    pass

    indice = resilience()

    print("\n================================================")
    print("RESUMO EXECUTIVO")
    print("================================================")

    print(f"RESILIENCE INDEX : {indice}")

    print(
        f"STATUS GERAL     : "
        f"{status_geral()}"
    )

    print(
        f"ORDEM            : "
        f"X27-{random.randint(1000,9999)}"
    )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    war_room()

    ordem_executiva()

    resumo()


