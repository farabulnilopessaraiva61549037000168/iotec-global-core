import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import subprocess
import os

ENGINES = [

    "TARGET_ENGINE.py",
    "ADAPTIVE_RESERVOIR_ENGINE.py",
    "SALES_BRAIN.py",
    "FOLLOWUP_SCHEDULER.py",
    "REVENUE_COMMAND_CENTER.py",
    "COMMUNICATION_GUARDIAN.py"

]

print("")
print("======================================================")
print("IOTEC EXECUTIVE ORCHESTRATOR")
print("======================================================")
print("")

sucesso = 0
falhas = 0

for engine in ENGINES:
    pass

    print("")
    print("------------------------------------------------------")
    print("EXECUTANDO:", engine)
    print("------------------------------------------------------")
    print("")

    caminho = os.path.join(
        r"C:\IOTEC",
        engine
    )

    if not os.path.exists(caminho):
        pass

        print("ARQUIVO NAO ENCONTRADO")
        print(caminho)

        falhas += 1
        continue

    try:
        pass

        resultado = subprocess.run(

            ["python", caminho],

            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"

        )

        print(resultado.stdout)

        if resultado.returncode == 0:
            pass

            sucesso += 1

        else:
            pass

            falhas += 1

            print("")
            print("ERRO:")
            print(resultado.stderr)

    except Exception as e:
        pass

        falhas += 1

        print("")
        print("FALHA:")
        print(str(e))

print("")
print("======================================================")
print("RESUMO EXECUTIVO")
print("======================================================")
print("")

print("ENGINES EXECUTADAS:", len(ENGINES))
print("SUCESSO:", sucesso)
print("FALHAS:", falhas)

print("")

if falhas == 0:
    pass

    print("STATUS GERAL: OPERACIONAL")

elif falhas <= 2:
    pass

    print("STATUS GERAL: ATENCAO")

else:
    pass

    print("STATUS GERAL: CRITICO")

print("")
print("======================================================")




