import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
019_KERNEL_ORCHESTRATOR.py

KERNEL ORCHESTRATOR

Coordena toda a plataforma.

======================================================================
"""

import subprocess
import time
from datetime import datetime
from pathlib import Path

# ================================================================

CICLO_SEGUNDOS = 10

MODULOS = [

    ("Control Center", "IOTEC_CONTROL_CENTER.py"),

    ("Database Center", "018_DATABASE_CENTER.py"),

    ("Kernel Brain", "013_KERNEL_BRAIN.py"),

    ("PlantÃƒÂ£o", "PLANTAO_DE_EVENTOS.py"),

]

# ================================================================


def executar(nome, arquivo):

    print()

    print("=" * 70)

    print("EXECUTANDO:", nome)

    print("=" * 70)

    if not Path(arquivo).exists():

        print("Arquivo nÃƒÂ£o encontrado:", arquivo)

        return False

    resultado = subprocess.run(

        ["python", arquivo],

        capture_output=True,

        text=True

    )

    if resultado.returncode == 0:

        print("STATUS........ OK")

    else:

        print("STATUS........ ERRO")

        print(resultado.stderr)

    return resultado.returncode == 0


# ================================================================


def resumo(total, sucesso):

    print()

    print("=" * 70)

    print("RESUMO DO CICLO")

    print("=" * 70)

    print()

    print("HorÃƒÂ¡rio........", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    print("MÃƒÂ³dulos........", total)

    print("Executados.....", sucesso)

    print("Falhas.........", total - sucesso)

    print()

    print("=" * 70)


# ================================================================


def iniciar():

    print("=" * 70)

    print("IOTEC KERNEL ORCHESTRATOR")

    print("=" * 70)

    print()

    ciclo = 1

    while True:

        print()

        print("=" * 70)

        print(f"CICLO {ciclo}")

        print("=" * 70)

        sucesso = 0

        for nome, arquivo in MODULOS:

            if executar(nome, arquivo):

                sucesso += 1

        resumo(len(MODULOS), sucesso)

        print()

        print(f"PrÃƒÂ³ximo ciclo em {CICLO_SEGUNDOS} segundos...")

        print("Pressione CTRL+C para encerrar.")

        try:

            time.sleep(CICLO_SEGUNDOS)

        except KeyboardInterrupt:

            print()

            print("=" * 70)

            print("ORCHESTRATOR ENCERRADO PELO USUÃƒÂRIO")

            print("=" * 70)

            break

        ciclo += 1


# ================================================================

if __name__ == "__main__":

    iniciar()



