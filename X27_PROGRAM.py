import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 PROGRAM ENGINE
# ============================================================

from datetime import datetime

# ============================================================
# PROGRAMAS
# ============================================================

PROGRAMAS = [

    {
        "nome": "RESILIENCIA_MUNICIPAL",

        "projetos": [

            "AMPLIACAO_HOSPITALAR",

            "EXPANSAO_ABRIGOS",

            "INTERNET_REDUNDANTE"

        ],

        "orcamento": 900000,

        "progresso": 38,

        "status": "EM_EXECUCAO"

    }

]

# ============================================================
# DASHBOARD
# ============================================================

def dashboard():
    pass

    print("\n================================================")

    print("X27 PROGRAM ENGINE")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    for programa in PROGRAMAS:
        pass

        print("\n------------------------------------------------")

        print(f"PROGRAMA : {programa['nome']}")

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

        print("\nPROJETOS:")

        for projeto in programa["projetos"]:
            pass

            print(f" [OK] {projeto}")

# ============================================================
# KPI
# ============================================================

def kpi():
    pass

    print("\n================================================")

    print("KPI EXECUTIVO")

    print("================================================")

    total_programas = len(PROGRAMAS)

    total_orcamento = sum(
        p["orcamento"]
        for p in PROGRAMAS
    )

    media_progresso = (

        sum(
            p["progresso"]
            for p in PROGRAMAS
        )

        / total_programas

    )

    print(f"PROGRAMAS : {total_programas}")

    print(
        f"ORCAMENTO TOTAL : "
        f"R$ {total_orcamento:,.2f}"
    )

    print(
        f"PROGRESSO MEDIO : "
        f"{media_progresso:.1f}%"
    )

# ============================================================
# ALERTAS
# ============================================================

def alertas():
    pass

    print("\n================================================")

    print("ALERTAS")

    print("================================================")

    for programa in PROGRAMAS:
        pass

        if programa["progresso"] < 50:
            pass

            print(
                f"[ATENCAO] "
                f"{programa['nome']} "
                f"abaixo de 50%"
            )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    dashboard()

    kpi()

    alertas()




