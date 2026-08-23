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

ARQUIVO = ROOT / "IOTEC_SOURCE_GOVERNANCE_REPORT.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    gov = json.load(f)

plano = {

    "gerado_em": str(datetime.now()),

    "missao": (
        "Expandir catalogo de fontes externas"
    ),

    "prioridades": [],

    "tarefas": []
}

for categoria, info in gov[
    "diagnostico"
].items():

    if info["status"] == "CRITICO":
        pass

        plano[
            "prioridades"
        ].append(categoria)

        plano[
            "tarefas"
        ].append({

            "categoria":
                categoria,

            "objetivo":
                "Cadastrar primeiras fontes",

            "meta_minima":
                5,

            "meta_ideal":
                20
        })

saida = (
    ROOT /
    "IOTEC_ACQUISITION_PLAN.json"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        plano,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nACQUISITION PLAN\n")

print(
    "PRIORIDADES:",
    len(
        plano["prioridades"]
    )
)

for item in plano["tarefas"]:
    pass

    print(
        item["categoria"],
        "->",
        item["meta_minima"],
        "/",
        item["meta_ideal"]
    )

print("\nARQUIVO:")
print(saida)


