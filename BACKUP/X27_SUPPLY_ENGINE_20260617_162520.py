import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 SUPPLY ENGINE
# ============================================================

from datetime import datetime

# ============================================================
# ESTOQUES ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICOS
# ============================================================

ESTOQUES = {

    "AGUA_LITROS": {
        "ESTADO": 500000,
        "REGIONAL": 150000,
        "EMERGENCIAL": 100000
    },

    "REFEICOES": {
        "ESTADO": 100000,
        "REGIONAL": 50000,
        "EMERGENCIAL": 25000
    },

    "COLCHOES": {
        "ESTADO": 20000,
        "REGIONAL": 5000,
        "EMERGENCIAL": 3000
    },

    "COBERTORES": {
        "ESTADO": 30000,
        "REGIONAL": 8000,
        "EMERGENCIAL": 4000
    }

}

# ============================================================
# NECESSIDADE
# ============================================================

NECESSIDADE = {

    "AGUA_LITROS": 100000,
    "REFEICOES": 15000,
    "COLCHOES": 5000,
    "COBERTORES": 5000

}

# ============================================================
# VERIFICAR DISPONIBILIDADE
# ============================================================

def verificar():
    pass

    print("\n================================================")
    print("X27 SUPPLY ENGINE")
    print("================================================")

    print(f"DATA: {datetime.now()}")

    print("\nANALISE DE SUPRIMENTOS")

    print("================================================")

    for item, quantidade in NECESSIDADE.items():
        pass

        estoque_total = sum(
            ESTOQUES[item].values()
        )

        saldo = estoque_total - quantidade

        print(f"\nITEM: {item}")

        print(f"NECESSARIO : {quantidade}")

        print(f"DISPONIVEL : {estoque_total}")

        if saldo >= 0:
            pass

            print("[OK] SUPRIMENTO DISPONIVEL")

        else:
            pass

            print("[CRITICO] FALTA SUPRIMENTO")

# ============================================================
# FORNECEDORES
# ============================================================

FORNECEDORES = {

    "AGUA_LITROS": [

        "Companhia Regional de Agua",
        "Reservatorio Estadual",
        "Operacao Emergencial"

    ],

    "REFEICOES": [

        "Cozinha Humanitaria",
        "Fornecedor Regional",
        "Operacao Alimentar"

    ],

    "COLCHOES": [

        "Defesa Civil",
        "Estoque Estadual"

    ],

    "COBERTORES": [

        "Assistencia Social",
        "Estoque Emergencial"

    ]

}

# ============================================================
# EXIBIR FONTES
# ============================================================

def fornecedores():
    pass

    print("\n================================================")
    print("FONTES DE SUPRIMENTO")
    print("================================================")

    for item, lista in FORNECEDORES.items():
        pass

        print(f"\n{item}")

        for fornecedor in lista:
            pass

            print(f" - {fornecedor}")

# ============================================================
# ORDEM LOGISTICA
# ============================================================

def ordem():
    pass

    print("\n================================================")
    print("X27 LOGISTIC ORDER")
    print("================================================")

    print("1 - Separar recursos")

    print("2 - Confirmar disponibilidade")

    print("3 - Definir transporte")

    print("4 - Definir rotas")

    print("5 - Iniciar distribuicao")

    print("6 - Atualizar WAR ROOM")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    verificar()

    fornecedores()

    ordem()


