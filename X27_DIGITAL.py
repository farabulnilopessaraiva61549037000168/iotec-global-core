import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 DIGITAL TWIN
# ============================================================

from datetime import datetime

# ============================================================
# IDENTIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

MUNICIPIO = {

    "nome": "IBICUITINGA",

    "populacao": 12000,

    "area_km2": 425,

    "status": "OPERACIONAL"

}

# ============================================================
# INFRAESTRUTURA
# ============================================================

INFRA = {

    "hospitais": 1,

    "postos_saude": 6,

    "escolas": 12,

    "abrigos": 3,

    "reservatorios": 4,

    "subestacoes": 2

}

# ============================================================
# RECURSOS
# ============================================================

RECURSOS = {

    "agua": 78,

    "energia": 83,

    "internet": 65,

    "saude": 40,

    "logistica": 70

}

# ============================================================
# RISCOS
# ============================================================

RISCOS = {

    "seca": "ALTO",

    "enchente": "BAIXO",

    "incendio": "MEDIO",

    "energia": "MEDIO"

}

# ============================================================
# DIGITAL TWIN
# ============================================================

def twin():
    pass

    print("\n================================================")

    print("X27 DIGITAL TWIN")

    print("================================================")

    print(f"DATA : {datetime.now()}")

    print(f"MUNICIPIO : {MUNICIPIO['nome']}")

    print(f"POPULACAO : {MUNICIPIO['populacao']}")

    print(f"AREA KMÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²  : {MUNICIPIO['area_km2']}")

    print(f"STATUS    : {MUNICIPIO['status']}")

# ============================================================
# INFRA
# ============================================================

def infraestrutura():
    pass

    print("\n================================================")

    print("INFRAESTRUTURA")

    print("================================================")

    for item, valor in INFRA.items():
        pass

        print(f"{item.upper():<20} {valor}")

# ============================================================
# RECURSOS
# ============================================================

def recursos():
    pass

    print("\n================================================")

    print("CAPACIDADE OPERACIONAL")

    print("================================================")

    for item, valor in RECURSOS.items():
        pass

        print(f"{item.upper():<20} {valor}%")

# ============================================================
# RISCOS
# ============================================================

def riscos():
    pass

    print("\n================================================")

    print("RISCOS")

    print("================================================")

    for item, valor in RISCOS.items():
        pass

        print(f"{item.upper():<20} {valor}")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    twin()

    infraestrutura()

    recursos()

    riscos()




