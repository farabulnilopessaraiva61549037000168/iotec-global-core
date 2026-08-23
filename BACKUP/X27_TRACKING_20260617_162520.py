import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 TRACKING ENGINE
# ============================================================

from datetime import datetime
import random

# ============================================================
# ATIVOS EM CAMPO
# ============================================================

ATIVOS = [

    "CAMINHAO_01",
    "CAMINHAO_02",
    "CAMINHAO_03",
    "CAMINHAO_04",

    "CARRETA_01",
    "CARRETA_02",

    "AMBULANCIA_01",
    "AMBULANCIA_02"

]

# ============================================================
# LOCALIDADES
# ============================================================

LOCALIDADES = [

    "FORTALEZA",
    "QUIXADA",
    "MORADA_NOVA",
    "LIMOEIRO_DO_NORTE",
    "ARACATI",
    "IBICUITINGA"

]

# ============================================================
# STATUS
# ============================================================

STATUS = [

    "EM_TRANSITO",
    "OPERANDO",
    "CHEGOU_DESTINO",
    "ATRASADO"

]

# ============================================================
# CARGAS
# ============================================================

CARGAS = [

    "AGUA",
    "REFEICOES",
    "COLCHOES",
    "COBERTORES",
    "MEDICAMENTOS",
    "EQUIPE_MEDICA"

]

# ============================================================
# GERAR ETA
# ============================================================

def gerar_eta():
    pass

    horas = random.randint(0, 8)

    minutos = random.randint(0, 59)

    return f"{horas}h {minutos}m"

# ============================================================
# RASTREAMENTO
# ============================================================

def rastrear():
    pass

    print("\n================================================")
    print("X27 TRACKING ENGINE")
    print("================================================")

    print(f"DATA: {datetime.now()}")

    ativos_campo = 0
    entregues = 0
    atrasados = 0

    for ativo in ATIVOS:
        pass

        status = random.choice(STATUS)

        local = random.choice(LOCALIDADES)

        carga = random.choice(CARGAS)

        velocidade = random.randint(40, 100)

        eta = gerar_eta()

        print("\n------------------------------------------------")

        print(f"ATIVO      : {ativo}")

        print(f"STATUS     : {status}")

        print(f"LOCAL      : {local}")

        print(f"CARGA      : {carga}")

        print(f"VELOCIDADE : {velocidade} km/h")

        print(f"ETA        : {eta}")

        if status == "EM_TRANSITO":
            ativos_campo += 1

        elif status == "OPERANDO":
            ativos_campo += 1

        elif status == "CHEGOU_DESTINO":
            entregues += 1

        elif status == "ATRASADO":
            atrasados += 1

    return ativos_campo, entregues, atrasados

# ============================================================
# WAR ROOM
# ============================================================

def war_room(ativos, entregues, atrasados):
    pass

    print("\n================================================")
    print("X27 OPERATIONS MAP")
    print("================================================")

    print(f"ATIVOS EM CAMPO : {ativos}")

    print(f"ENTREGUES       : {entregues}")

    print(f"ATRASADOS       : {atrasados}")

    print(f"DATA            : {datetime.now()}")

    print("================================================")

# ============================================================
# ALERTAS
# ============================================================

def alertas(atrasados):
    pass

    print("\n================================================")
    print("X27 ALERT CENTER")
    print("================================================")

    if atrasados == 0:
        pass

        print("[OK] OPERACAO DENTRO DA NORMALIDADE")

    else:
        pass

        print(f"[ALERTA] {atrasados} ATIVOS ATRASADOS")

        print("VERIFICAR ROTAS")

        print("VERIFICAR COMUNICACAO")

        print("VERIFICAR LOGISTICA")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    ativos, entregues, atrasados = rastrear()

    war_room(
        ativos,
        entregues,
        atrasados
    )

    alertas(
        atrasados
    )


