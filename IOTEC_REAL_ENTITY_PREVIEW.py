import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path

ARQUIVO = Path(
    r"C:\IOTEC\REAL_BUSINESS_RESERVOIR.json"
)

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

contador = 0

for grupo in ["reais", "provaveis_reais"]:
    pass

    print("\n")
    print("=" * 60)
    print(grupo.upper())
    print("=" * 60)

    for item in dados.get(grupo, []):
        pass

        contador += 1

        print("\nREGISTRO", contador)

        print(
            "ARQUIVO:",
            item.get("arquivo")
        )

        texto = json.dumps(
            item.get("dados", {}),
            ensure_ascii=False
        )

        print(
            texto[:1000]
        )

        print("\n")

        if contador >= 20:
            break

    if contador >= 20:
        break




