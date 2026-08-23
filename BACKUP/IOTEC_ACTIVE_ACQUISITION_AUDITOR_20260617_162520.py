import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

ALVOS = [
    "IOTEC_WEB_OBSERVER",
    "SIGNAL_MAPPER",
    "IOTEC_AUDITOR_PAYPAL",
    "paypal_server",
    "CREATIVE_EXPLORER",
    "TOKEN",
    "Specter"
]

resultado = {
    "encontrados": [],
    "nao_encontrados": []
}

for alvo in ALVOS:
    pass

    achou = False

    for arq in ROOT.rglob("*.py"):
        pass

        if alvo.lower() in arq.name.lower():
            pass

            achou = True

            try:
                pass

                stat = arq.stat()

                resultado["encontrados"].append({

                    "arquivo": str(arq),

                    "bytes": stat.st_size

                })

            except:
                pass

    if not achou:
        pass

        resultado["nao_encontrados"].append(
            alvo
        )

saida = ROOT / "IOTEC_ACTIVE_ACQUISITION_REPORT.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nACTIVE ACQUISITION AUDIT\n")

print(
    "MOTORES ENCONTRADOS:",
    len(resultado["encontrados"])
)

print(
    "NAO ENCONTRADOS:",
    len(resultado["nao_encontrados"])
)

for item in resultado["encontrados"]:
    pass

    print(
        Path(item["arquivo"]).name,
        "->",
        item["bytes"],
        "bytes"
    )

print("\nRELATORIO:")
print(saida)


