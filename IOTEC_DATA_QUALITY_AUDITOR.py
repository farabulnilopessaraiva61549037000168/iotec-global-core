import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from collections import Counter
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

MAX_FILES = 3000

resultado = {
    "data": str(datetime.now()),
    "arquivos_lidos": 0,
    "tipos": Counter(),
    "campos": Counter(),
    "maiores_json": [],
    "amostras": []
}

jsons = list(ROOT.rglob("*.json"))

for arq in jsons[:MAX_FILES]:
    pass

    try:
        pass

        tamanho = arq.stat().st_size

        resultado["maiores_json"].append(
            (arq.name, tamanho)
        )

        with open(
            arq,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            dados = json.load(f)

        resultado["arquivos_lidos"] += 1

        tipo = type(dados).__name__

        resultado["tipos"][tipo] += 1

        if isinstance(dados, dict):
            pass

            for chave in dados.keys():
                pass

                resultado["campos"][chave] += 1

        elif isinstance(dados, list):
            pass

            if len(dados):
                pass

                item = dados[0]

                if isinstance(item, dict):
                    pass

                    for chave in item.keys():
                        pass

                        resultado["campos"][chave] += 1

        if len(resultado["amostras"]) < 20:
            pass

            resultado["amostras"].append({
                "arquivo": arq.name,
                "tipo": tipo,
                "bytes": tamanho
            })

    except:
        pass

resultado["maiores_json"] = sorted(
    resultado["maiores_json"],
    key=lambda x: x[1],
    reverse=True
)[:100]

resultado["tipos"] = dict(
    resultado["tipos"].most_common(50)
)

resultado["campos"] = dict(
    resultado["campos"].most_common(200)
)

saida = ROOT / "IOTEC_DATA_QUALITY_REPORT.json"

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

print("\nAUDITORIA FINALIZADA\n")

print(
    "Arquivos lidos:",
    resultado["arquivos_lidos"]
)

print(
    "\nTOP 20 CAMPOS:"
)

for k, v in list(
    resultado["campos"].items()
)[:20]:

    print(f"{k}: {v}")

print(
    f"\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {saida}"
)




