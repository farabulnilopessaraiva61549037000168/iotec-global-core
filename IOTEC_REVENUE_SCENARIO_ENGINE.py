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

    nome = produto["produto"]

    ticket = produto["ticket"]

    vendas_meta = max(
        1,
        round(META_MENSAL / ticket)
    )

    pessimista = max(
        1,
        round(vendas_meta * 0.30)
    )

    conservador = max(
        1,
        round(vendas_meta * 0.60)
    )

    realista = max(
        1,
        round(vendas_meta * 0.85)
    )

    otimista = max(
        1,
        round(vendas_meta * 1.20)
    )

    receita_pessimista = pessimista * ticket
    receita_conservadora = conservador * ticket
    receita_realista = realista * ticket
    receita_otimista = otimista * ticket

    gap_meta = META_MENSAL - receita_realista

    resultado["cenarios"].append({

        "produto": nome,

        "oferta": produto["oferta"],

        "ticket": ticket,

        "vendas_meta": vendas_meta,

        "pessimista_vendas": pessimista,
        "conservador_vendas": conservador,
        "realista_vendas": realista,
        "otimista_vendas": otimista,

        "receita_pessimista": receita_pessimista,
        "receita_conservadora": receita_conservadora,
        "receita_realista": receita_realista,
        "receita_otimista": receita_otimista,

        "gap_meta": gap_meta
    })

resultado["cenarios"] = sorted(

    resultado["cenarios"],

    key=lambda x: x["receita_realista"],

    reverse=True
)

TOP5 = resultado["cenarios"][:5]

resultado["recomendacao"] = {

    "melhores_candidatos": TOP5
}

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_REVENUE_SCENARIO_REPORT.json"
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

print("\nREVENUE SCENARIO ENGINE\n")

print(
    "META:",
    f"R$ {META_MENSAL:,.2f}"
)

print("\nTOP 5 CENARIOS REALISTAS:\n")

for item in TOP5:
    pass

    print(
        f"{item['produto']}"
    )

    print(
        f"  Ticket: R$ {item['ticket']:,.2f}"
    )

    print(
        f"  Receita Realista: "
        f"R$ {item['receita_realista']:,.2f}"
    )

    print(
        f"  Receita Otimista: "
        f"R$ {item['receita_otimista']:,.2f}"
    )

    print(
        f"  Gap Meta: "
        f"R$ {item['gap_meta']:,.2f}"
    )

    print()

print("ARQUIVO:")
print(ARQUIVO_SAIDA)




