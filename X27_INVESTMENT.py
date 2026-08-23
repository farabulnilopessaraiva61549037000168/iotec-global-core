import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 INVESTMENT ENGINE
# ============================================================
#
# PLANEJAMENTO DE INVESTIMENTOS
#
# Responde:
#
# Quanto investir?
# Onde investir?
# Qual retorno esperado?
#
# ============================================================

from datetime import datetime

# ============================================================
# ORÃƒÆ'Ã†â€™AMENTO DISPONÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEL
# ============================================================

ORCAMENTO = 1000000

# ============================================================
# PRIORIDADES
# ============================================================

SETORES = {

    "SAUDE": {

        "prioridade": 1,

        "percentual": 40,

        "ganho": 30

    },

    "ABRIGOS": {

        "prioridade": 2,

        "percentual": 30,

        "ganho": 25

    },

    "INTERNET": {

        "prioridade": 3,

        "percentual": 20,

        "ganho": 35

    },

    "ENERGIA": {

        "prioridade": 4,

        "percentual": 5,

        "ganho": 10

    },

    "LOGISTICA": {

        "prioridade": 5,

        "percentual": 5,

        "ganho": 10

    }

}

# ============================================================
# INVESTIMENTO
# ============================================================

def investimento():
    pass

    print("\n================================================")

    print("X27 INVESTMENT ENGINE")

    print("================================================")

    print(f"DATA      : {datetime.now()}")

    print(f"ORCAMENTO : R$ {ORCAMENTO:,.2f}")

    print("\n================================================")

    print("PLANO DE INVESTIMENTO")

    print("================================================")

    impacto_total = 0

    valor_total = 0

    for setor, dados in SETORES.items():
        pass

        valor = (

            ORCAMENTO

            * dados["percentual"]

            / 100

        )

        impacto_total += dados["ganho"]

        valor_total += valor

        print("\n------------------------------------------------")

        print(f"SETOR        : {setor}")

        print(f"PRIORIDADE   : {dados['prioridade']}")

        print(
            f"INVESTIMENTO : "
            f"R$ {valor:,.2f}"
        )

        print(
            f"GANHO ESPERADO : "
            f"+{dados['ganho']}%"
        )

    print("\n================================================")

    print("RESUMO EXECUTIVO")

    print("================================================")

    print(
        f"TOTAL INVESTIDO : "
        f"R$ {valor_total:,.2f}"
    )

    print(
        f"GANHO GLOBAL    : "
        f"+{impacto_total}%"
    )

# ============================================================
# PORTFÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œLIO
# ============================================================

def portfolio():
    pass

    print("\n================================================")

    print("PORTFOLIO DE PROJETOS")

    print("================================================")

    print("\n[PROJETO 01]")

    print("AmpliaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Hospitalar")

    print("Prazo : 90 dias")

    print("Impacto : ALTO")

    print("\n[PROJETO 02]")

    print("ExpansÃƒÆ'Ã†â€™o de Abrigos")

    print("Prazo : 60 dias")

    print("Impacto : ALTO")

    print("\n[PROJETO 03]")

    print("Internet Redundante")

    print("Prazo : 45 dias")

    print("Impacto : ALTO")

# ============================================================
# ROI
# ============================================================

def roi():
    pass

    print("\n================================================")

    print("ROI ESTIMADO")

    print("================================================")

    print("RISCO REDUZIDO")

    print("CAPACIDADE EXPANDIDA")

    print("RESILIENCIA AUMENTADA")

    print("TEMPO DE RESPOSTA MENOR")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    investimento()

    portfolio()

    roi()




