import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 RISK FORECAST ENGINE
# ============================================================

from datetime import datetime

SETORES = {

    "SAUDE": 40,
    "INTERNET": 65,
    "ABRIGOS": 55,
    "ENERGIA": 83,
    "AGUA": 78

}

def projetar(valor, meses):
    pass

    perda = meses * 2

    resultado = valor - perda

    if resultado < 0:
        resultado = 0

    return resultado

print("\n================================================")
print("X27 RISK FORECAST ENGINE")
print("================================================")
print(f"DATA : {datetime.now()}")

for setor, valor in SETORES.items():
    pass

    print("\n------------------------------------------------")

    print(f"SETOR : {setor}")

    print(f"ATUAL : {valor}%")

    print(f"90 DIAS  : {projetar(valor,3)}%")

    print(f"180 DIAS : {projetar(valor,6)}%")

    print(f"365 DIAS : {projetar(valor,12)}%")

    if valor < 50:
        pass

        print("RISCO : CRITICO")

    elif valor < 70:
        pass

        print("RISCO : ALTO")

    else:
        pass

        print("RISCO : MODERADO")




