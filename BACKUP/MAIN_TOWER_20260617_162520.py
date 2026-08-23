import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import subprocess

BASE = r"C:\IOTEC"

MODULES = {

    "1": (
        "DASHBOARD EXECUTIVO",
        os.path.join(BASE,"EXECUTIVE_COMMAND_TOWER.py")
    ),

    "2": (
        "OPERACOES COMERCIAIS",
        os.path.join(BASE,"LEAD_OPERATIONS_CENTER.py")
    ),

    "3": (
        "NEGOCIACOES",
        os.path.join(BASE,"NEGOTIATION_ENGINE.py")
    ),

    "4": (
        "MONETIZACAO",
        os.path.join(BASE,"CRM_ENGINE.py")
    ),

    "5": (
        "CLIENTES",
        os.path.join(BASE,"EXECUTIVE_COMMAND_TOWER.py")
    )

}

while True:
    pass

    os.system("cls")

    print()
    print("=" * 70)
    print("IOTEC MAIN COMMAND TOWER")
    print("=" * 70)

    print()
    print("1 - DASHBOARD EXECUTIVO")
    print("2 - OPERACOES COMERCIAIS")
    print("3 - NEGOCIACOES")
    print("4 - MONETIZACAO")
    print("5 - CLIENTES")
    print("0 - SAIR")

    print()
    opcao = input("SELECIONE: ").strip()

    if opcao == "0":
        pass

        break

    if opcao not in MODULES:
        pass

        input("\nOPCAO INVALIDA. ENTER...")
        continue

    titulo, arquivo = MODULES[opcao]

    os.system("cls")

    print()
    print("=" * 70)
    print(titulo)
    print("=" * 70)
    print()

    if os.path.exists(arquivo):
        pass

        subprocess.run(
            ["python", arquivo]
        )

    else:
        pass

        print("ARQUIVO NAO ENCONTRADO:")
        print(arquivo)

    input("\nENTER PARA VOLTAR...")


