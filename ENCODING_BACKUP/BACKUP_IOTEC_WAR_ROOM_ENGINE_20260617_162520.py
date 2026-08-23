import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

DB = ROOT / "IOTEC_WAR_ROOM_DATABASE.json"

with open(
    DB,
    "r",
    encoding="utf-8"
) as f:

    banco = json.load(f)

print("\nWAR ROOM ENGINE\n")

print("1 - NOVA OPORTUNIDADE")
print("2 - DASHBOARD")

opcao = input("\nOPCAO: ")

if opcao == "1":
    pass

    cliente = input("CLIENTE: ")
    produto = input("PRODUTO: ")
    origem = input("ORIGEM: ")

    oportunidade = {

        "id":
            len(
                banco["oportunidades"]
            ) + 1,

        "cliente":
            cliente,

        "produto":
            produto,

        "origem":
            origem,

        "status":
            "AGUARDANDO_ANALISE",

        "data":
            str(
                datetime.now()
            )
    }

    banco["oportunidades"].append(
        oportunidade
    )

    with open(
        DB,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            banco,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(
        "\nOPORTUNIDADE REGISTRADA"
    )

elif opcao == "2":
    pass

    print(
        "\nDASHBOARD\n"
    )

    print(
        "CLIENTES:",
        len(
            banco["clientes"]
        )
    )

    print(
        "OPORTUNIDADES:",
        len(
            banco["oportunidades"]
        )
    )

    print(
        "OPERACOES:",
        len(
            banco["operacoes"]
        )
    )

    print(
        "TAREFAS:",
        len(
            banco["tarefas"]
        )
    )

else:
    pass

    print(
        "\nOPCAO INVALIDA"
    )


