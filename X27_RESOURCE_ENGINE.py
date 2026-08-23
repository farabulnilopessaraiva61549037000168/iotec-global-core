import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 RESOURCE ENGINE
# ============================================================

from datetime import datetime

# ============================================================
# FATORES OPERACIONAIS
# ============================================================

AGUA_POR_PESSOA = 20          # litros
REFEICOES_POR_PESSOA = 3      # refeiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
COLCHOES_POR_PESSOA = 1
COBERTORES_POR_PESSOA = 1

# ============================================================
# CALCULAR RECURSOS
# ============================================================

def calcular_recursos(pessoas):
    pass

    return {

        "agua_litros":
            pessoas * AGUA_POR_PESSOA,

        "refeicoes":
            pessoas * REFEICOES_POR_PESSOA,

        "colchoes":
            pessoas * COLCHOES_POR_PESSOA,

        "cobertores":
            pessoas * COBERTORES_POR_PESSOA,

        "ambulancias":
            max(1, pessoas // 1000),

        "equipes_medicas":
            max(1, pessoas // 500),

        "equipes_psicossociais":
            max(1, pessoas // 1000),

        "abrigos":
            max(1, pessoas // 500)

    }

# ============================================================
# EXIBIR PLANO
# ============================================================

def gerar_plano(evento, municipio, pessoas):
    pass

    recursos = calcular_recursos(pessoas)

    print("\n================================================")
    print("X27 RESOURCE ENGINE")
    print("================================================")

    print(f"DATA       : {datetime.now()}")
    print(f"EVENTO     : {evento}")
    print(f"MUNICIPIO  : {municipio}")
    print(f"POPULACAO  : {pessoas}")

    print("\n================================================")
    print("RECURSOS NECESSARIOS")
    print("================================================")

    print(f"AGUA (L)            : {recursos['agua_litros']}")
    print(f"REFEICOES           : {recursos['refeicoes']}")
    print(f"COLCHOES            : {recursos['colchoes']}")
    print(f"COBERTORES          : {recursos['cobertores']}")
    print(f"AMBULANCIAS         : {recursos['ambulancias']}")
    print(f"EQUIPES MEDICAS     : {recursos['equipes_medicas']}")
    print(f"EQUIPES PSICOSSOCIAIS: {recursos['equipes_psicossociais']}")
    print(f"ABRIGOS             : {recursos['abrigos']}")

    print("\n================================================")
    print("PRIORIDADES")
    print("================================================")

    print("1 - Garantir ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gua")
    print("2 - Garantir atendimento mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dico")
    print("3 - Garantir abrigo")
    print("4 - Garantir alimentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")
    print("5 - Garantir comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")

# ============================================================
# ORDEM EXECUTIVA
# ============================================================

def ordem_executiva(evento, pessoas):
    pass

    print("\n================================================")
    print("X27 EXECUTIVE ORDER")
    print("================================================")

    if pessoas > 10000:
        pass

        print("NIVEL : CRITICO")
        print("MOBILIZACAO NACIONAL")

    elif pessoas > 5000:
        pass

        print("NIVEL : ALERTA MAXIMO")
        print("MOBILIZACAO REGIONAL")

    elif pessoas > 1000:
        pass

        print("NIVEL : ALERTA")
        print("MOBILIZACAO MUNICIPAL")

    else:
        pass

        print("NIVEL : ATENCAO")
        print("MONITORAMENTO REFORCADO")

# ============================================================
# TESTE
# ============================================================

if __name__ == "__main__":
    pass

    EVENTO = "ROMPIMENTO_BARRAGEM"

    MUNICIPIO = "IBICUITINGA"

    PESSOAS_AFETADAS = 5000

    gerar_plano(
        EVENTO,
        MUNICIPIO,
        PESSOAS_AFETADAS
    )

    ordem_executiva(
        EVENTO,
        PESSOAS_AFETADAS
    )




