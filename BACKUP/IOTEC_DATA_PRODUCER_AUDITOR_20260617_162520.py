import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_DATA_PRODUCER_AUDITOR.py

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

MOTORES_ALVO = [

    "SIGNAL_MAPPER",

    "IOTEC_WEB_OBSERVER",

    "IOTEC_AUDITOR_PAYPAL",

    "paypal_server",

    "Specter.Fortress",

    "TOKEN",

    "token",

    "CREATIVE_EXPLORER"
]

RESULTADO = {

    "gerado_em": str(datetime.now()),

    "motores": [],

    "json_recentes": [],

    "ranking_produtores": []
}

print("\nANALISANDO MOTORES...\n")

for motor in MOTORES_ALVO:
    pass

    encontrados = []

    for arq in ROOT.rglob("*.py"):
        pass

        if motor.lower() in arq.name.lower():
            pass

            try:
                pass

                texto = arq.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                json_dump = texto.count(
                    "json.dump"
                )

                json_write = (
                    texto.count(".write(")
                )

                json_path = (
                    texto.count(".json")
                )

                score = (
                    json_dump
                    +
                    json_write
                    +
                    json_path
                )

                encontrados.append({

                    "arquivo":
                        str(arq),

                    "bytes":
                        arq.stat().st_size,

                    "json_dump":
                        json_dump,

                    "write":
                        json_write,

                    "json_refs":
                        json_path,

                    "score":
                        score

                })

            except:
                pass

    if encontrados:
        pass

        RESULTADO[
            "motores"
        ].append({

            "motor":
                motor,

            "instancias":
                encontrados

        })

print(
    "ANALISANDO JSONS RECENTES...\n"
)

agora = datetime.now()

for arq in ROOT.rglob("*.json"):
    pass

    try:
        pass

        modificado = datetime.fromtimestamp(
            arq.stat().st_mtime
        )

        idade_horas = (
            agora - modificado
        ).total_seconds() / 3600

        if idade_horas <= 168:
            pass

            RESULTADO[
                "json_recentes"
            ].append({

                "arquivo":
                    str(arq),

                "bytes":
                    arq.stat().st_size,

                "idade_horas":
                    round(
                        idade_horas,
                        2
                    )

            })

    except:
        pass

ranking = []

for grupo in RESULTADO["motores"]:
    pass

    score_total = 0

    for item in grupo["instancias"]:
        pass

        score_total += item["score"]

    ranking.append({

        "motor":
            grupo["motor"],

        "score":
            score_total

    })

RESULTADO[
    "ranking_produtores"
] = sorted(

    ranking,

    key=lambda x: x["score"],

    reverse=True

)

RESULTADO[
    "json_recentes"
] = sorted(

    RESULTADO[
        "json_recentes"
    ],

    key=lambda x: x["idade_horas"]

)

SAIDA = (
    ROOT /
    "IOTEC_DATA_PRODUCER_REPORT.json"
)

with open(
    SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        RESULTADO,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nDATA PRODUCER AUDIT\n")

print(
    "MOTORES ANALISADOS:",
    len(
        RESULTADO[
            "motores"
        ]
    )
)

print(
    "JSONS RECENTES:",
    len(
        RESULTADO[
            "json_recentes"
        ]
    )
)

print(
    "\nTOP PRODUTORES:\n"
)

for item in RESULTADO[
    "ranking_produtores"
][:20]:

    print(
        item["motor"],
        "-> SCORE",
        item["score"]
    )

print(
    "\nTOP JSONS RECENTES:\n"
)

for item in RESULTADO[
    "json_recentes"
][:20]:

    print(
        Path(
            item["arquivo"]
        ).name,
        "-",
        item["idade_horas"],
        "horas"
    )

print(
    "\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:"
)

print(SAIDA)


