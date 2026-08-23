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

ARQUIVOS = [
    "IOTEC_SOURCE_CATALOG.json",
    "IOTEC_SOURCE_GOVERNANCE_REPORT.json",
    "IOTEC_ACQUISITION_PLAN.json",
    "IOTEC_STRATEGY_EXECUTION.json",
    "IOTEC_META_STATE.json"
]

radar = {

    "gerado_em": str(datetime.now()),

    "oportunidades": [],

    "riscos": [],

    "prioridade_maxima": None
}

for nome in ARQUIVOS:
    pass

    arq = ROOT / nome

    if not arq.exists():
        pass

        radar["riscos"].append(
            f"Arquivo ausente: {nome}"
        )

meta = ROOT / "IOTEC_META_STATE.json"

if meta.exists():
    pass

    with open(
        meta,
        "r",
        encoding="utf-8"
    ) as f:

        estado = json.load(f)

    prioridade = estado.get(
        "prioridade_global"
    )

    radar[
        "prioridade_maxima"
    ] = prioridade

    if prioridade == "CATALOGACAO_DE_FONTES":
        pass

        radar[
            "oportunidades"
        ].append({

            "acao":
                "Construir primeiras fontes externas",

            "impacto":
                "ALTO"
        })

        radar[
            "oportunidades"
        ].append({

            "acao":
                "Validar fontes futuras",

            "impacto":
                "ALTO"
        })

        radar[
            "oportunidades"
        ].append({

            "acao":
                "Criar classificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o por categoria",

            "impacto":
                "MEDIO"
        })

saida = (
    ROOT /
    "IOTEC_OPPORTUNITY_RADAR.json"
)

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        radar,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nOPPORTUNITY RADAR\n")

print(
    "PRIORIDADE:",
    radar["prioridade_maxima"]
)

print(
    "\nOPORTUNIDADES:"
)

for item in radar["oportunidades"]:
    pass

    print(
        "-",
        item["acao"],
        "(",
        item["impacto"],
        ")"
    )

print(
    "\nRISCOS:"
)

for risco in radar["riscos"]:
    pass

    print("-", risco)

print(
    "\nARQUIVO:"
)

print(saida)




