import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 PROJECT ENGINE
# ============================================================
#
# GESTAO DE PROJETOS ESTRATEGICOS
#
# ============================================================

from datetime import datetime

# ============================================================
# PROJETOS
# ============================================================

PROJETOS = [

    {
        "nome": "AMPLIACAO_HOSPITALAR",
        "investimento": 400000,
        "prazo": 90,
        "impacto": "ALTO",
        "responsavel": "NODE_SAUDE"
    },

    {
        "nome": "EXPANSAO_ABRIGOS",
        "investimento": 300000,
        "prazo": 60,
        "impacto": "ALTO",
        "responsavel": "NODE_ABRIGOS"
    },

    {
        "nome": "INTERNET_REDUNDANTE",
        "investimento": 200000,
        "prazo": 45,
        "impacto": "ALTO",
        "responsavel": "NODE_COMUNICACAO"
    }

]

# ============================================================
# FASES
# ============================================================

FASES = [

    "PLANEJAMENTO",

    "CONTRATACAO",

    "EXECUCAO",

    "VALIDACAO",

    "OPERACAO"

]

# ============================================================
# EXIBICAO
# ============================================================

def projetos():
    pass

    print("\n================================================")

    print("X27 PROJECT ENGINE")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    for projeto in PROJETOS:
        pass

        print("\n------------------------------------------------")

        print(f"PROJETO     : {projeto['nome']}")

        print(f"INVESTIMENTO: R$ {projeto['investimento']:,.2f}")

        print(f"PRAZO       : {projeto['prazo']} dias")

        print(f"IMPACTO     : {projeto['impacto']}")

        print(f"RESPONSAVEL : {projeto['responsavel']}")

        print("\nFASES:")

        for fase in FASES:
            pass

            print(f" [ ] {fase}")

# ============================================================
# PORTFOLIO
# ============================================================

def portfolio():
    pass

    total = sum(
        p["investimento"]
        for p in PROJETOS
    )

    print("\n================================================")

    print("PORTFOLIO EXECUTIVO")

    print("================================================")

    print(f"PROJETOS : {len(PROJETOS)}")

    print(f"INVESTIMENTO TOTAL : R$ {total:,.2f}")

# ============================================================
# ROADMAP
# ============================================================

def roadmap():
    pass

    print("\n================================================")

    print("ROADMAP ESTRATEGICO")

    print("================================================")

    print("FASE 1 -> SAUDE")

    print("FASE 2 -> ABRIGOS")

    print("FASE 3 -> COMUNICACAO")

    print("FASE 4 -> ENERGIA")

    print("FASE 5 -> LOGISTICA")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    projetos()

    portfolio()

    roadmap()


