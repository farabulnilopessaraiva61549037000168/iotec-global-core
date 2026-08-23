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
print("IOTEC DATABASE AUDITOR")
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

print("")
print("CLIENTES:")
print(len(clientes))

print("")
print("OPORTUNIDADES:")
print(len(oportunidades))

print("")
print("OPERACOES:")
print(len(operacoes))

print("")
print("===================================")
print("DETALHES")
print("===================================")

for op in oportunidades:
    pass

    print("")
    print("OPORTUNIDADE")

    for k, v in op.items():
        pass

        print(
            k,
            "->",
            v
        )

print("")
print("===================================")
print("OPERACOES")
print("===================================")

for op in operacoes:
    pass

    print("")

    for k, v in op.items():
        pass

        print(
            k,
            "->",
            v
        )

print("")
print("AUDITORIA FINALIZADA")


