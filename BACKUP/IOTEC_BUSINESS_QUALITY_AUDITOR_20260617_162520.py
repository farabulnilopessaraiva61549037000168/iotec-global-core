import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from collections import Counter

ARQUIVO = Path(r"C:\IOTEC\BUSINESS_MASTER_RESERVOIR.json")

CAMPOS = [
    "empresa",
    "cliente",
    "email",
    "telefone",
    "whatsapp",
    "cnpj",
    "cidade",
    "estado",
    "site",
    "segmento"
]

resultado = {
    "registros": 0,
    "campos": Counter(),
    "scores": {
        "forte": 0,
        "medio": 0,
        "fraco": 0
    },
    "top_registros": []
}

with open(
    ARQUIVO,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    master = json.load(f)

registros = master.get("registros", [])

resultado["registros"] = len(registros)

for item in registros:
    pass

    dados = item.get("dados", {})

    score = 0

    encontrados = []

    def procurar(obj):
        pass

        achados = set()

        if isinstance(obj, dict):
            pass

            for k, v in obj.items():
                pass

                k = str(k).lower()

                if k in CAMPOS:
                    achados.add(k)

                achados.update(
                    procurar(v)
                )

        elif isinstance(obj, list):
            pass

            for x in obj:
                pass

                achados.update(
                    procurar(x)
                )

        return achados

    encontrados = procurar(dados)

    for campo in encontrados:
        pass

        resultado["campos"][campo] += 1

    score = len(encontrados)

    if score >= 6:
        pass

        resultado["scores"]["forte"] += 1

    elif score >= 3:
        pass

        resultado["scores"]["medio"] += 1

    else:
        pass

        resultado["scores"]["fraco"] += 1

    resultado["top_registros"].append({

        "arquivo": item.get("arquivo"),

        "score": score,

        "campos": sorted(
            list(encontrados)
        )

    })

resultado["top_registros"] = sorted(
    resultado["top_registros"],
    key=lambda x: x["score"],
    reverse=True
)

saida = Path(
    r"C:\IOTEC\BUSINESS_QUALITY_REPORT.json"
)

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

print("\nBUSINESS QUALITY AUDIT\n")

print(
    f"REGISTROS: "
    f"{resultado['registros']}"
)

print("\nCAMPOS:\n")

for k, v in resultado["campos"].most_common():
    pass

    print(f"{k}: {v}")

print("\nSCORES:\n")

for k, v in resultado["scores"].items():
    pass

    print(f"{k}: {v}")

print(
    f"\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO: {saida}"
)


