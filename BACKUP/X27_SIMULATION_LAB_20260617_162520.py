import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 SIMULATION LAB
# ============================================================

from datetime import datetime
import random

CENARIOS = [

    "SECA",

    "ROMPIMENTO_BARRAGEM",

    "INCENDIO_FLORESTAL",

    "FALHA_ENERGIA",

    "COLAPSO_INTERNET",

    "PERDA_GPS"

]

cenario = random.choice(CENARIOS)

print("\n================================================")
print("X27 SIMULATION LAB")
print("================================================")
print(f"DATA : {datetime.now()}")

print("\nCENARIO SIMULADO")

print("------------------------------------------------")

print(f"EVENTO : {cenario}")

impacto = random.randint(1, 10)

afetados = random.randint(100, 10000)

print(f"IMPACTO : {impacto}")

print(f"AFETADOS : {afetados}")

print("\nRESPOSTA ESPERADA")

print("------------------------------------------------")

print("ATIVAR WAR ROOM")

print("ATIVAR COMMAND CENTER")

print("ATIVAR CONTINUITY ENGINE")

print("ATIVAR ALERT ENGINE")

print("ATIVAR STRATEGIC AI")

print("\n================================================")
print("SIMULACAO CONCLUIDA")
print("================================================")


