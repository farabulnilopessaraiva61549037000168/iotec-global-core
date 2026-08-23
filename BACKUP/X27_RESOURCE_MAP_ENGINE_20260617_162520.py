import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 RESOURCE MAP ENGINE
# ============================================================

from datetime import datetime

RECURSOS = {

    "FORTALEZA": {

        "AGUA": 750000,

        "MEDICAMENTOS": 120000,

        "COLCHOES": 28000

    },

    "QUIXADA": {

        "EQUIPES_MEDICAS": 15,

        "AMBULANCIAS": 8

    },

    "MORADA_NOVA": {

        "ABRIGOS": 12,

        "COBERTORES": 42000

    }

}

print("\n================================================")
print("X27 RESOURCE MAP ENGINE")
print("================================================")
print(f"DATA : {datetime.now()}")

for cidade, recursos in RECURSOS.items():
    pass

    print("\n------------------------------------------------")

    print(f"NODE : {cidade}")

    for recurso, valor in recursos.items():
        pass

        print(f"{recurso:<20} {valor}")

print("\n================================================")
print("STATUS")
print("================================================")
print("MAPA DE RECURSOS OPERACIONAL")


