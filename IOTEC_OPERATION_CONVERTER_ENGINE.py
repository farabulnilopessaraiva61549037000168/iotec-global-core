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

if not DB.exists():
    pass

    print(
        "WAR ROOM DATABASE NAO ENCONTRADO"
    )

    raise SystemExit

with open(
    DB,
    "r",
    encoding="utf-8"
) as f:

    banco = json.load(f)

print(
    "\nOPERATION CONVERTER ENGINE\n"
)

if len(
    banco["oportunidades"]
) == 0:

    print(
        "SEM OPORTUNIDADES"
    )

    raise SystemExit

print(
    "OPORTUNIDADES:\n"
)

for op in banco["oportunidades"]:
    pass

    print(
        f"ID={op['id']} | "
        f"{op['cliente']} | "
        f"{op['produto']} | "
        f"{op['status']}"
    )

id_oportunidade = int(

    input(
        "\nID DA OPORTUNIDADE: "
    )
)

valor = float(

    input(
        "VALOR DA OPERACAO (R$): "
    )
)

encontrada = None

for op in banco["oportunidades"]:
    pass

    if op["id"] == id_oportunidade:
        pass

        encontrada = op
        break

if encontrada is None:
    pass

    print(
        "OPORTUNIDADE NAO ENCONTRADA"
    )

    raise SystemExit

operacao = {

    "id":
        len(
            banco["operacoes"]
        ) + 1,

    "oportunidade_id":
        encontrada["id"],

    "cliente":
        encontrada["cliente"],

    "produto":
        encontrada["produto"],

    "valor":
        valor,

    "status":
        "OPERACAO_ABERTA",

    "data_abertura":
        str(
            datetime.now()
        )
}

banco["operacoes"].append(
    operacao
)

encontrada["status"] = (
    "CONVERTIDA"
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
    "\nOPERACAO CRIADA\n"
)

print(
    "CLIENTE:",
    operacao["cliente"]
)

print(
    "PRODUTO:",
    operacao["produto"]
)

print(
    "VALOR:",
    f"R$ {valor:,.2f}"
)

print(
    "STATUS:",
    operacao["status"]
)

print(
    "\nBANCO ATUALIZADO:"
)

print(
    DB
)




