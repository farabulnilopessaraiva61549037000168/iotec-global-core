import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==============================================================================
# IOTEC VALIDATION ENGINE
# MISSÃƒÆ'O 001 - VALIDAÃƒâ€¡ÃƒÆ'O DA INFRAESTRUTURA COMERCIAL
# ==============================================================================

import os
import importlib.util
from pathlib import Path

BASE = Path(r"C:\IOTEC")

MODULOS = [
    "PAYMENT_ENGINE.py",
    "IOTEC_PAYMENT_BRIDGE_ENGINE.py",
    "paypal_server.py",
    "CONFIRM_PAYMENT.py",
    "IOTEC_PAYPAL_MONITOR.py",
    "monitor_paypal.py",
    "eh_pagamento_paypal.py"
]

print("=" * 70)
print("IOTEC - OPERAÃƒâ€¡ÃƒÆ'O INVENTÃƒÂRIO")
print("=" * 70)
print()

total = 0
ok = 0

for arquivo in MODULOS:

    total += 1

    caminho = BASE / arquivo

    if not caminho.exists():
        print(f"[ERRO] {arquivo}")
        print("       Arquivo nÃƒÂ£o encontrado.\n")
        continue

    print(f"[OK] {arquivo}")

    try:

        spec = importlib.util.spec_from_file_location(
            arquivo.replace(".py", ""),
            caminho
        )

        modulo = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(modulo)

        print("       Importado com sucesso.")

        ok += 1

    except Exception as erro:

        print("       Falha ao importar.")
        print(f"       {erro}")

    print()

print("=" * 70)
print("RESUMO")
print("=" * 70)

print(f"MÃƒÂ³dulos encontrados : {total}")
print(f"Importados          : {ok}")
print(f"Falhas              : {total-ok}")

if ok == total:

    print()
    print("STATUS:")
    print("INFRAESTRUTURA COMERCIAL VALIDADA.")

else:

    print()
    print("STATUS:")
    print("EXISTEM MÃƒâ€œDULOS QUE PRECISAM DE CORREÃƒâ€¡ÃƒÆ'O.")

print("=" * 70)



