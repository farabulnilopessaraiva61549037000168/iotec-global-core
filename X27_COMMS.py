import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 COMMS ENGINE
# ============================================================

from datetime import datetime

# ============================================================
# STATUS
# ============================================================

internet = False
telefonia = True
energia = False

# ============================================================
# ANALISE
# ============================================================

print("\n================================================")
print("X27 COMMS ENGINE")
print("================================================")

print(f"DATA: {datetime.now()}")

print("\nSERVICOS")

print(f"INTERNET : {internet}")
print(f"TELEFONIA: {telefonia}")
print(f"ENERGIA  : {energia}")

print("\n================================================")
print("PLANO DE CONTINGENCIA")
print("================================================")

if not energia:
    pass

    print("[ACAO] Acionar geradores")

if not internet:
    pass

    print("[ACAO] Acionar internet satelital")

    print("[ACAO] Ativar rede mesh")

    print("[ACAO] Priorizar hospitais")

if not telefonia:
    pass

    print("[ACAO] Acionar radios VHF")

    print("[ACAO] Acionar radios UHF")

print("\n================================================")
print("STATUS OPERACIONAL")
print("================================================")

if internet or telefonia:
    pass

    print("COMUNICACAO MANTIDA")

else:
    pass

    print("COMUNICACAO CRITICA")




