import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path

ARQ = Path(
    r"C:\IOTEC\IOTEC_WAR_ROOM_DATABASE.json"
)

print("")
print("===================================")
print("IOTEC AUTO REPAIR CHANNELS")
print("===================================")

with open(
    ARQ,
    "r",
    encoding="utf-8-sig"
) as f:

    db = json.load(f)

oportunidades = db.get(
    "oportunidades",
    []
)

operacoes = db.get(
    "operacoes",
    []
)

corrigidas = 0

# ==================================
# NORMALIZA ORIGENS
# ==================================

for op in oportunidades:
    pass

    origem = str(
        op.get(
            "origem",
            ""
        )
    ).upper()

    if origem in [
        "WATTSAPP",
        "WHATSAP",
        "WHATSAPP"
    ]:

        op["origem"] = "WHATSAPP"

        corrigidas += 1

# ==================================
# HERDA ORIGEM NAS OPERACOES
# ==================================

mapa = {}

for op in oportunidades:
    pass

    mapa[
        op.get("id")
    ] = op.get(
        "origem",
        "DESCONHECIDA"
    )

for operacao in operacoes:
    pass

    if (
        "origem" not in operacao
        or
        not operacao["origem"]
    ):

        oportunidade_id = operacao.get(
            "oportunidade_id"
        )

        operacao["origem"] = mapa.get(
            oportunidade_id,
            "DESCONHECIDA"
        )

        corrigidas += 1

db["oportunidades"] = oportunidades
db["operacoes"] = operacoes

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
print("CORRECOES:")
print(corrigidas)

print("")
print("BANCO ATUALIZADO")
print("")
print("FIM")
from pathlib import Path

ARQ = Path(
    r"C:\IOTEC\IOTEC_WAR_ROOM_DATABASE.json"
)

print("")
print("===================================")
print("IOTEC AUTO REPAIR CHANNELS")
print("===================================")

with open(
    ARQ,
    "r",
    encoding="utf-8-sig"
) as f:

    db = json.load(f)

oportunidades = db.get(
    "oportunidades",
    []
)

operacoes = db.get(
    "operacoes",
    []
)

corrigidas = 0

# ==================================
# NORMALIZA ORIGENS
# ==================================

for op in oportunidades:
    pass

    origem = str(
        op.get(
            "origem",
            ""
        )
    ).upper()

    if origem in [
        "WATTSAPP",
        "WHATSAP",
        "WHATSAPP"
    ]:

        op["origem"] = "WHATSAPP"

        corrigidas += 1

# ==================================
# HERDA ORIGEM NAS OPERACOES
# ==================================

mapa = {}

for op in oportunidades:
    pass

    mapa[
        op.get("id")
    ] = op.get(
        "origem",
        "DESCONHECIDA"
    )

for operacao in operacoes:
    pass

    if (
        "origem" not in operacao
        or
        not operacao["origem"]
    ):

        oportunidade_id = operacao.get(
            "oportunidade_id"
        )

        operacao["origem"] = mapa.get(
            oportunidade_id,
            "DESCONHECIDA"
        )

        corrigidas += 1

db["oportunidades"] = oportunidades
db["operacoes"] = operacoes

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
print("CORRECOES:")
print(corrigidas)

print("")
print("BANCO ATUALIZADO")
print("")
print("FIM")


