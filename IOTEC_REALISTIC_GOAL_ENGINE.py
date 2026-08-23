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

ARQUIVO = ROOT / "IOTEC_COMMERCIAL_VIABILITY_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("RELATORIO NAO ENCONTRADO")
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

    "cenarios": []
}

for produto in dados["produtos"]:
    pass

    ticket = produto["ticket"]

    vendas = max(
        1,
        round(META_MENSAL / ticket)
    )

    complexidade = produto["complexidade"]

    escalabilidade = produto["escalabilidade"]

    prazo = produto["prazo_dias"]

    probabilidade = (
        100
        - (complexidade * 12)
        + (escalabilidade * 8)
        - (prazo / 5)
    )

    probabilidade = max(
        5,
        min(
            95,
            round(probabilidade, 1)
        )
    )

    if probabilidade < 25:
        pass

        classificacao = "PESSIMISTA"

    elif probabilidade < 45:
        pass

        classificacao = "CONSERVADOR"

    elif probabilidade < 65:
        pass

        classificacao = "REALISTA"

    elif probabilidade < 80:
        pass

        classificacao = "OTIMISTA"

    else:
        pass

        classificacao = "AGRESSIVO"

    risco_concentracao = "ALTO"

    if vendas >= 10:
        risco_concentracao = "BAIXO"

    elif vendas >= 5:
        risco_concentracao = "MEDIO"

    resultado["cenarios"].append({

        "produto":
            produto["produto"],

        "oferta":
            produto["oferta"],

        "ticket":
            ticket,

        "vendas_necessarias":
            vendas,

        "probabilidade":
            probabilidade,

        "cenario":
            classificacao,

        "risco_concentracao":
            risco_concentracao
    })

resultado["cenarios"] = sorted(

    resultado["cenarios"],

    key=lambda x: (
        -x["probabilidade"],
        x["vendas_necessarias"]
    )
)

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_REALISTIC_GOAL_REPORT.json"
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

print("\nREALISTIC GOAL ENGINE\n")

print(
    "META:",
    f"R$ {META_MENSAL:,.2f}"
)

print("\nTOP 10 CENARIOS:\n")

for item in resultado["cenarios"][:10]:
    pass

    print(
        f"{item['produto']} | "
        f"{item['cenario']} | "
        f"{item['probabilidade']}% | "
        f"{item['vendas_necessarias']} vendas"
    )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)




