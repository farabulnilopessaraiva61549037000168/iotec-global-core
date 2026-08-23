import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 PORTFOLIO MANAGER
# ============================================================
#
# VISAO EXECUTIVA CONSOLIDADA
#
# Programas
# Projetos
# Orcamentos
# Prazos
# Status
#
# ============================================================

from datetime import datetime

# ============================================================
# PROGRAMAS
# ============================================================

PROGRAMAS = [

    {
        "nome": "RESILIENCIA_MUNICIPAL",

        "orcamento": 900000,

        "status": "EM_EXECUCAO",

        "progresso": 38,

        "projetos": 3

    },

    {
        "nome": "SEGURANCA_HIDRICA",

        "orcamento": 2500000,

        "status": "PLANEJAMENTO",

        "progresso": 12,

        "projetos": 5

    },

    {
        "nome": "CONTINUIDADE_OPERACIONAL",

        "orcamento": 1800000,

        "status": "EM_EXECUCAO",

        "progresso": 61,

        "projetos": 4

    }

]

# ============================================================
# DASHBOARD
# ============================================================

def dashboard():
    pass

    print("\n================================================")

    print("X27 PORTFOLIO MANAGER")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    for programa in PROGRAMAS:
        pass

        print("\n------------------------------------------------")

        print(f"PROGRAMA  : {programa['nome']}")

        print(
            f"ORCAMENTO : "
            f"R$ {programa['orcamento']:,.2f}"
        )

        print(
            f"PROGRESSO : "
            f"{programa['progresso']}%"
        )

        print(
            f"STATUS    : "
            f"{programa['status']}"
        )

        print(
            f"PROJETOS  : "
            f"{programa['projetos']}"
        )

# ============================================================
# KPI EXECUTIVO
# ============================================================

def kpi():
    pass

    total_programas = len(PROGRAMAS)

    total_projetos = sum(
        p["projetos"]
        for p in PROGRAMAS
    )

    total_orcamento = sum(
        p["orcamento"]
        for p in PROGRAMAS
    )

    em_execucao = sum(
        1
        for p in PROGRAMAS
        if p["status"] == "EM_EXECUCAO"
    )

    planejamento = sum(
        1
        for p in PROGRAMAS
        if p["status"] == "PLANEJAMENTO"
    )

    media = (
        sum(
            p["progresso"]
            for p in PROGRAMAS
        )
        / total_programas
    )

    print("\n================================================")

    print("KPI EXECUTIVO")

    print("================================================")

    print(f"PROGRAMAS           : {total_programas}")

    print(f"PROJETOS            : {total_projetos}")

    print(
        f"ORCAMENTO TOTAL     : "
        f"R$ {total_orcamento:,.2f}"
    )

    print(f"EM EXECUCAO         : {em_execucao}")

    print(f"EM PLANEJAMENTO     : {planejamento}")

    print(
        f"PROGRESSO MEDIO     : "
        f"{media:.1f}%"
    )

# ============================================================
# ALERTAS
# ============================================================

def alertas():
    pass

    print("\n================================================")

    print("ALERTAS EXECUTIVOS")

    print("================================================")

    for programa in PROGRAMAS:
        pass

        if programa["progresso"] < 25:
            pass

            print(
                f"[CRITICO] "
                f"{programa['nome']} "
                f"abaixo de 25%"
            )

        elif programa["progresso"] < 50:
            pass

            print(
                f"[ATENCAO] "
                f"{programa['nome']} "
                f"abaixo de 50%"
            )

# ============================================================
# RANKING
# ============================================================

def ranking():
    pass

    print("\n================================================")

    print("RANKING DE PROGRAMAS")

    print("================================================")

    ordenado = sorted(
        PROGRAMAS,
        key=lambda x: x["orcamento"],
        reverse=True
    )

    posicao = 1

    for programa in ordenado:
        pass

        print(
            f"{posicao}ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº "
            f"{programa['nome']} "
            f"- R$ {programa['orcamento']:,.2f}"
        )

        posicao += 1

# ============================================================
# RESUMO EXECUTIVO
# ============================================================

def resumo():
    pass

    print("\n================================================")

    print("RESUMO EXECUTIVO")

    print("================================================")

    print("PORTFOLIO CONSOLIDADO")

    print("GOVERNANCA ATIVA")

    print("RASTREABILIDADE ATIVA")

    print("MONITORAMENTO CONTINUO")

    print("STATUS GERAL: OPERACIONAL")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    dashboard()

    kpi()

    alertas()

    ranking()

    resumo()




