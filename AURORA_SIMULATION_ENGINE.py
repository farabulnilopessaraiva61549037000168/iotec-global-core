import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# AURORA SIMULATION ENGINE
# ============================================================

from datetime import datetime
import json
import random
import os

DATABASE_FILE = "AURORA_DATABASE.json"

# ============================================================
# CARREGAR BANCO
# ============================================================

def carregar():
    pass

    if not os.path.exists(DATABASE_FILE):
        pass

        print("[ERRO] Banco nÃƒÆ'Ã†â€™o encontrado")
        return None

    with open(
        DATABASE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

# ============================================================
# SALVAR
# ============================================================

def salvar(db):
    pass

    with open(
        DATABASE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            db,
            f,
            ensure_ascii=False,
            indent=4
        )

# ============================================================
# EVENTOS POSSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS
# ============================================================

EVENTOS = {

    "SECA": 20,

    "ESTIAGEM": 15,

    "ONDA_CALOR": 25,

    "FRIO_EXTREMO": 15,

    "ENCHENTE": 35,

    "INUNDACAO": 40,

    "DESLIZAMENTO": 50,

    "QUEIMADA": 30,

    "INCENDIO_FLORESTAL": 35,

    "COLAPSO_HIDRICO": 60,

    "FALHA_ENERGETICA": 20
}

# ============================================================
# MUNICÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂPIOS TESTE
# ============================================================

MUNICIPIOS = [

    "IBICUITINGA",
    "QUIXADA",
    "QUIXERAMOBIM",
    "MORADA_NOVA",
    "LIMOEIRO_DO_NORTE",
    "ARACATI",
    "FORTALEZA"

]

# ============================================================
# GERAR INCIDENTE
# ============================================================

def gerar_incidente():
    pass

    db = carregar()

    if db is None:
        return

    evento = random.choice(list(EVENTOS.keys()))

    municipio = random.choice(MUNICIPIOS)

    peso = EVENTOS[evento]

    pessoas = random.randint(100, 50000)

    incidente = {

        "evento": evento,

        "municipio": municipio,

        "peso": peso,

        "pessoas_afetadas": pessoas,

        "data": datetime.now().isoformat()

    }

    db["eventos"].append(incidente)

    salvar(db)

    print("\n================================================")

    print("INCIDENTE SIMULADO")

    print("================================================")

    print(f"EVENTO   : {evento}")

    print(f"MUNICIPIO: {municipio}")

    print(f"PESO     : {peso}")

    print(f"PESSOAS  : {pessoas}")

    print("================================================")

# ============================================================
# PROTOCOLOS
# ============================================================

def recomendar(evento):
    pass

    protocolos = {

        "SECA":
        [
            "Monitorar reservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios",
            "Acionar abastecimento",
            "Proteger rebanhos"
        ],

        "ENCHENTE":
        [
            "Abrir abrigos",
            "Evacuar ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡reas crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticas",
            "Acionar Defesa Civil"
        ],

        "DESLIZAMENTO":
        [
            "Isolar encostas",
            "Retirar moradores",
            "Monitorar solo"
        ],

        "COLAPSO_HIDRICO":
        [
            "Plano emergencial de ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gua",
            "DistribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o por caminhÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
            "Monitoramento diÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio"
        ]
    }

    return protocolos.get(
        evento,
        ["Monitoramento contÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nuo"]
    )

# ============================================================
# EXECUTAR CENÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO
# ============================================================

def executar():
    pass

    evento = random.choice(
        list(EVENTOS.keys())
    )

    print("\n================================================")

    print("SIMULACAO AURORA")

    print("================================================")

    print(f"EVENTO: {evento}")

    print("\nPROTOCOLOS:")

    for item in recomendar(evento):
        pass

        print(f" - {item}")

    print("\n================================================")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    gerar_incidente()

    executar()




