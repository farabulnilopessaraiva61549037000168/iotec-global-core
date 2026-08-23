import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ARQ = Path(
    r"C:\IOTEC\IOTEC_WAR_ROOM_DATABASE.json"
)

print("")
print("===================================")
print("IOTEC CLIENT RECONCILIATOR")
print("===================================")

with open(
    ARQ,
    "r",
    encoding="utf-8-sig"
) as f:

    db = json.load(f)

clientes = db.get(
    "clientes",
    []
)

oportunidades = db.get(
    "oportunidades",
    []
)

operacoes = db.get(
    "operacoes",
    []
)

nomes_existentes = set()

for c in clientes:
    pass

    nome = c.get(
        "nome",
        ""
    ).strip().upper()

    if nome:
        pass

        nomes_existentes.add(nome)

novos = 0

# ============================
# OPORTUNIDADES
# ============================

for op in oportunidades:
    pass

    nome = op.get(
        "cliente",
        ""
    ).strip()

    if not nome:
        pass

        continue

    chave = nome.upper()

    if chave not in nomes_existentes:
        pass

        clientes.append({

            "id":
                len(clientes) + 1,

            "nome":
                nome,

            "origem":
                op.get(
                    "origem",
                    "DESCONHECIDA"
                ),

            "criado_em":
                str(
                    datetime.now()
                )
        })

        nomes_existentes.add(
            chave
        )

        novos += 1

# ============================
# OPERACOES
# ============================

for op in operacoes:
    pass

    nome = op.get(
        "cliente",
        ""
    ).strip()

    if not nome:
        pass

        continue

    chave = nome.upper()

    if chave not in nomes_existentes:
        pass

        clientes.append({

            "id":
                len(clientes) + 1,

            "nome":
                nome,

            "origem":
                "OPERACAO",

            "criado_em":
                str(
                    datetime.now()
                )
        })

        nomes_existentes.add(
            chave
        )

        novos += 1

db["clientes"] = clientes

with open(
    ARQ,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        db,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("CLIENTES CADASTRADOS:")
print(novos)

print("")
print("TOTAL DE CLIENTES:")
print(len(clientes))

print("")
print("RECONCILIACAO FINALIZADA")




