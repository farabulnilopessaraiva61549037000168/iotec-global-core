import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_EVIDENCE_COCKPIT.py

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ARQ_RECEITA = ROOT / "IOTEC_REAL_REVENUE.json"

ARQ_WARROOM = ROOT / "IOTEC_WAR_ROOM_DATABASE.json"

META_MENSAL = 100000.0

print("")
print("===================================")
print("IOTEC EVIDENCE COCKPIT")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

# ===================================
# RECEITA
# ===================================

receita_total = 0.0

if ARQ_RECEITA.exists():
    pass

    try:
        pass

        with open(
            ARQ_RECEITA,
            "r",
            encoding="utf-8-sig"
        ) as f:

            receita = json.load(f)

        eventos = receita.get(
            "eventos",
            []
        )

        receita_total = sum(
            x.get("valor", 0)
            for x in eventos
        )

    except Exception as erro:
        pass

        print(
            "ERRO RECEITA:",
            erro
        )

# ===================================
# WAR ROOM
# ===================================

clientes = 0
oportunidades = 0
operacoes = 0

if ARQ_WARROOM.exists():
    pass

    try:
        pass

        with open(
            ARQ_WARROOM,
            "r",
            encoding="utf-8-sig"
        ) as f:

            banco = json.load(f)

        clientes = len(
            banco.get(
                "clientes",
                []
            )
        )

        oportunidades = len(
            banco.get(
                "oportunidades",
                []
            )
        )

        operacoes = len(
            banco.get(
                "operacoes",
                []
            )
        )

    except Exception as erro:
        pass

        print(
            "ERRO WAR ROOM:",
            erro
        )

# ===================================
# META
# ===================================

faltante = max(
    0,
    META_MENSAL - receita_total
)

atingimento = round(
    (receita_total / META_MENSAL) * 100,
    2
)

# ===================================
# RELATORIO
# ===================================

print("")
print("===================================")
print("MAPA DE META")
print("===================================")

print(
    f"META: R$ {META_MENSAL:,.2f}"
)

print(
    f"REALIZADO: R$ {receita_total:,.2f}"
)

print(
    f"FALTANTE: R$ {faltante:,.2f}"
)

print(
    f"ATINGIMENTO: {atingimento}%"
)

print("")
print("===================================")
print("ATIVIDADE REAL")
print("===================================")

print(
    "CLIENTES:",
    clientes
)

print(
    "OPORTUNIDADES:",
    oportunidades
)

print(
    "OPERACOES:",
    operacoes
)

print("")
print("===================================")
print("STATUS")
print("===================================")

if oportunidades == 0:
    pass

    print(
        "SEM CAPTACAO DETECTADA"
    )

else:
    pass

    print(
        "CAPTACAO DETECTADA"
    )

if operacoes == 0:
    pass

    print(
        "SEM OPERACOES ABERTAS"
    )

else:
    pass

    print(
        "OPERACOES EM ANDAMENTO"
    )

print("")
print("===================================")
print("PRODUTIVIDADE")
print("===================================")

if receita_total == 0:
    pass

    print(
        "SEM RECEITA REAL"
    )

else:
    pass

    print(
        "RECEITA REAL REGISTRADA"
    )

print("")
print("FIM DO RELATORIO")




