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

ARQUIVO = ROOT / "IOTEC_PRODUCT_CATALOG_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("CATALOGO NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

resultado = {

    "gerado_em": str(datetime.now()),

    "produtos": []
}

for oferta in dados["catalogo"]:
    pass

    for produto in oferta["produtos"]:
        pass

        nome = produto["produto"]

        ticket = produto["ticket"]

        if ticket <= 5000:
            pass

            prazo = 5
            complexidade = 1
            escalabilidade = 5

        elif ticket <= 15000:
            pass

            prazo = 15
            complexidade = 2
            escalabilidade = 4

        elif ticket <= 30000:
            pass

            prazo = 30
            complexidade = 3
            escalabilidade = 3

        else:
            pass

            prazo = 60
            complexidade = 5
            escalabilidade = 2

        score = (
            (ticket / 1000)
            +
            (escalabilidade * 10)
            -
            (complexidade * 5)
            -
            (prazo / 10)
        )

        resultado["produtos"].append({

            "oferta": oferta["oferta"],

            "produto": nome,

            "ticket": ticket,

            "prazo_dias": prazo,

            "complexidade": complexidade,

            "escalabilidade": escalabilidade,

            "score_viabilidade":
                round(score, 2)
        })

resultado["produtos"] = sorted(

    resultado["produtos"],

    key=lambda x: x["score_viabilidade"],

    reverse=True
)

SAIDA = (
    ROOT /
    "IOTEC_COMMERCIAL_VIABILITY_REPORT.json"
)

with open(
    SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nCOMMERCIAL VIABILITY ENGINE\n")

print(
    "PRODUTOS:",
    len(
        resultado["produtos"]
    )
)

print("\nTOP 10:\n")

for item in resultado["produtos"][:10]:
    pass

    print(
        f"{item['produto']} "
        f"| SCORE={item['score_viabilidade']} "
        f"| TICKET={item['ticket']}"
    )

print("\nARQUIVO:")
print(SAIDA)




