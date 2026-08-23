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

DIRETRIZ = ROOT / "IOTEC_STRATEGIC_DIRECTIVE.json"

with open(
    DIRETRIZ,
    "r",
    encoding="utf-8"
) as f:

    estrategia = json.load(f)

execucao = {

    "gerado_em": str(datetime.now()),

    "estado": "ATIVO",

    "missoes": [],

    "cronometro": {},

    "painel": {}
}

for categoria, dados in estrategia[
    "categorias_prioritarias"
].items():

    execucao[
        "missoes"
    ].append({

        "categoria":
            categoria,

        "status":
            "AGUARDANDO_FONTES",

        "meta_minima":
            dados["meta_minima"],

        "meta_ideal":
            dados["meta_ideal"],

        "fontes_atuais":
            0,

        "progresso":
            0
    })

execucao[
    "cronometro"
] = {

    "inicio":
        str(datetime.now()),

    "dias_planejamento":
        30,

    "objetivo":
        "Construir catalogo de fontes"
}

execucao[
    "painel"
] = {

    "categorias":
        len(
            execucao["missoes"]
        ),

    "missoes_ativas":
        len(
            execucao["missoes"]
        ),

    "fontes_catalogadas":
        0,

    "fontes_validadas":
        0
}

ARQUIVO = (
    ROOT /
    "IOTEC_STRATEGY_EXECUTION.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        execucao,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nIOTEC STRATEGY EXECUTION\n")

print(
    "MISSOES:",
    len(execucao["missoes"])
)

print(
    "CRONOMETRO:",
    execucao["cronometro"]["dias_planejamento"],
    "dias"
)

print(
    "\nCATEGORIAS:"
)

for item in execucao["missoes"]:
    pass

    print(
        item["categoria"],
        "->",
        item["status"]
    )

print("\nARQUIVO:")
print(ARQUIVO)




