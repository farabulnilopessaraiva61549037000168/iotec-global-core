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

META_MENSAL = 100000.0
DIAS_CICLO = 30

ARQUIVO = ROOT / "IOTEC_COMMERCIAL_VIABILITY_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("RELATORIO DE VIABILIDADE NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

resultado = {

    "gerado_em": str(datetime.now()),

    "meta_mensal": META_MENSAL,

    "dias_ciclo": DIAS_CICLO,

    "produtos": [],

    "ranking_execucao": [],

    "projecao": {}
}

for item in dados["produtos"]:
    pass

    ticket = item["ticket"]

    vendas_necessarias = max(
        1,
        round(META_MENSAL / ticket)
    )

    receita_prevista = (
        vendas_necessarias *
        ticket
    )

    score = (
        item["score_viabilidade"]
    )

    resultado["produtos"].append({

        "produto":
            item["produto"],

        "oferta":
            item["oferta"],

        "ticket":
            ticket,

        "score":
            score,

        "vendas_necessarias":
            vendas_necessarias,

        "receita_prevista":
            receita_prevista
    })

resultado["ranking_execucao"] = sorted(

    resultado["produtos"],

    key=lambda x: (
        x["vendas_necessarias"],
        -x["score"]
    )
)

top = resultado["ranking_execucao"][0]

resultado["projecao"] = {

    "produto_prioritario":
        top["produto"],

    "ticket":
        top["ticket"],

    "vendas_necessarias":
        top["vendas_necessarias"],

    "receita_prevista":
        top["receita_prevista"],

    "meta":
        META_MENSAL
}

cronograma = []

for dia in [1, 7, 15, 21, 30]:
    pass

    percentual = dia / DIAS_CICLO

    receita_esperada = round(
        META_MENSAL * percentual,
        2
    )

    cronograma.append({

        "dia": dia,

        "percentual_meta":
            round(
                percentual * 100,
                2
            ),

        "receita_esperada":
            receita_esperada
    })

resultado["cronograma"] = cronograma

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_GOAL_EXECUTION_REPORT.json"
)

with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nGOAL EXECUTION ENGINE\n")

print(
    "META:",
    f"R$ {META_MENSAL:,.2f}"
)

print(
    "\nPRODUTO PRIORITARIO:"
)

print(
    top["produto"]
)

print(
    "\nTICKET:"
)

print(
    f"R$ {top['ticket']:,.2f}"
)

print(
    "\nVENDAS NECESSARIAS:"
)

print(
    top["vendas_necessarias"]
)

print(
    "\nCRONOGRAMA:"
)

for c in cronograma:
    pass

    print(
        f"DIA {c['dia']} "
        f"-> {c['percentual_meta']}% "
        f"-> R$ {c['receita_esperada']:,.2f}"
    )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)




