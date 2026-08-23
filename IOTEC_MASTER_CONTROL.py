import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import subprocess
from datetime import datetime

print("")
print("===================================")
print("IOTEC MASTER CONTROL")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

motores = [

    "IOTEC_CLIENT_RECONCILIATOR.py",

    "IOTEC_DATABASE_AUDITOR.py",

    "IOTEC_FUNNEL_AUDITOR.py",

    "IOTEC_CHANNEL_STATUS.py",

    "IOTEC_EVIDENCE_COCKPIT.py",

    "IOTEC_SENTINEL_ENGINE.py"
]

print("")
print("===================================")
print("MOTORES CARREGADOS")
print("===================================")

for motor in motores:
    pass

    print("-", motor)

print("")
print("===================================")
print("EXECUCAO")
print("===================================")

sucesso = 0
falhas = 0

for motor in motores:
    pass

    print("")
    print("-----------------------------------")
    print("EXECUTANDO:")
    print(motor)
    print("-----------------------------------")

    try:
        pass

        resultado = subprocess.run(

            ["python", motor],

            capture_output=True,

            text=True,

            encoding="utf-8",

            errors="ignore"
        )

        if resultado.returncode == 0:
            pass

            sucesso += 1

            print(resultado.stdout)

        else:
            pass

            falhas += 1

            print("ERRO:")
            print(resultado.stderr)

    except Exception as erro:
        pass

        falhas += 1

        print("FALHA:")
        print(str(erro))

print("")
print("===================================")
print("RESUMO EXECUTIVO")
print("===================================")

print("MOTORES:")
print(len(motores))

print("SUCESSO:")
print(sucesso)

print("FALHAS:")
print(falhas)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "MONITORAR CLIENTES, "
    "OPORTUNIDADES, "
    "OPERACOES, "
    "CANAIS E RECEITA."
)

print("")
print("TORRE DE COMANDO ATIVA")




