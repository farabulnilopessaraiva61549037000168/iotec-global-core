import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 DEPLOYMENT ENGINE
# ============================================================

from datetime import datetime
import random

# ============================================================
# CENTROS LOGÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂSTICOS
# ============================================================

CENTROS = {

    "FORTALEZA": {
        "lat": -3.7319,
        "lon": -38.5267
    },

    "QUIXADA": {
        "lat": -4.9694,
        "lon": -39.0153
    },

    "MORADA_NOVA": {
        "lat": -5.1067,
        "lon": -38.3725
    }

}

# ============================================================
# DESTINO
# ============================================================

OPERACAO = {

    "evento": "ROMPIMENTO_BARRAGEM",

    "destino": "IBICUITINGA",

    "pessoas_afetadas": 5000

}

# ============================================================
# RECURSOS
# ============================================================

RECURSOS = [

    {
        "item": "AGUA",
        "quantidade": "100000 L"
    },

    {
        "item": "REFEICOES",
        "quantidade": "15000"
    },

    {
        "item": "COLCHOES",
        "quantidade": "5000"
    },

    {
        "item": "COBERTORES",
        "quantidade": "5000"
    }

]

# ============================================================
# VEÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCULOS
# ============================================================

VEICULOS = [

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
# GERAR ETA
# ============================================================

def gerar_eta():
    pass

    horas = random.randint(1, 8)

    minutos = random.randint(0, 59)

    return f"{horas}h {minutos}m"

# ============================================================
# MOBILIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def mobilizar():
    pass

    print("\n================================================")

    print("X27 DEPLOYMENT ENGINE")

    print("================================================")

    print(f"DATA: {datetime.now()}")

    print(f"\nEVENTO : {OPERACAO['evento']}")

    print(f"DESTINO: {OPERACAO['destino']}")

    print(
        f"POPULACAO AFETADA: "
        f"{OPERACAO['pessoas_afetadas']}"
    )

    print("\n================================================")

    print("RECURSOS MOBILIZADOS")

    print("================================================")

    for recurso in RECURSOS:
        pass

        print(
            f"{recurso['item']} -> "
            f"{recurso['quantidade']}"
        )

# ============================================================
# DESPACHO
# ============================================================

def despachar():
    pass

    print("\n================================================")

    print("ORDEM DE DESPACHO")

    print("================================================")

    for veiculo in VEICULOS:
        pass

        origem = random.choice(
            list(CENTROS.keys())
        )

        eta = gerar_eta()

        print(

            f"{veiculo:<15}"

            f"ORIGEM={origem:<15}"

            f"ETA={eta}"

        )

# ============================================================
# COMANDO EXECUTIVO
# ============================================================

def comando():
    pass

    print("\n================================================")

    print("EXECUTIVE COMMAND")

    print("================================================")

    print("1 - Separar recursos")

    print("2 - Carregar veÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­culos")

    print("3 - Confirmar rotas")

    print("4 - Deslocar equipes")

    print("5 - Atualizar WAR ROOM")

    print("6 - Monitorar operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")

    print("7 - Confirmar entrega")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    mobilizar()

    despachar()

    comando()




