import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import subprocess

ROOT = r"C:\IOTEC"

print("="*70)
print("IOTEC BOOT MANAGER")
print("="*70)
print()

ESSENCIAIS = [

"CONTROL_CENTER.py",

"CORE_PHILOSOPHY.py",

"PAYMENT_ENGINE.py",

"paypal_server.py"

]

for modulo in ESSENCIAIS:

    caminho = os.path.join(ROOT, modulo)

    if os.path.exists(caminho):

        print(f"[OK] {modulo}")

    else:

        print(f"[ERRO] {modulo}")

print()
print("="*70)
print("BOOT CHECK FINALIZADO")
print("="*70)




