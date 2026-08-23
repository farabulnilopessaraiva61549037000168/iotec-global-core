import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_ENGINE_FORENSICS.py

import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ALVOS = [
    "IOTEC_WEB_OBSERVER.py",
    "SIGNAL_MAPPER.py",
    "CREATIVE_EXPLORER.py",
    "IOTEC_AUDITOR_PAYPAL.py",
    "paypal_server.py",
    "TOKEN.py",
    "token.py",
    "Specter.Fortress.py"
]

PADROES = {

    "requests_get":
        r"requests\.get\s*\(",

    "requests_post":
        r"requests\.post\s*\(",

    "requests_put":
        r"requests\.put\s*\(",

    "requests_delete":
        r"requests\.delete\s*\(",

    "httpx":
        r"httpx",

    "aiohttp":
        r"aiohttp",

    "beautifulsoup":
        r"BeautifulSoup",

    "selenium":
        r"selenium",

    "webdriver":
        r"webdriver",

    "scrapy":
        r"scrapy",

    "api_key":
        r"api[_\-]?key",

    "token":
        r"token",

    "bearer":
        r"bearer",

    "authorization":
        r"authorization",

    "json_dump":
        r"json\.dump",

    "json_load":
        r"json\.load",

    "sqlite":
        r"sqlite3",

    "csv":
        r"csv\.",

    "url":
        r"https?://",

    "socket":
        r"socket",

    "websocket":
        r"websocket"
}

RELATORIO = {
    "gerado_em": str(datetime.now()),
    "motores": [],
    "resumo": {}
}

total_encontrados = 0

for alvo in ALVOS:
    pass

    encontrados = list(
        ROOT.rglob(alvo)
    )

    for arquivo in encontrados:
        pass

        try:
            pass

            texto = arquivo.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            info = {
                "arquivo": str(arquivo),
                "nome": arquivo.name,
                "bytes": arquivo.stat().st_size,
                "modificado": datetime.fromtimestamp(
                    arquivo.stat().st_mtime
                ).isoformat(),
                "assinaturas": {},
                "urls_encontradas": [],
                "score": 0
            }

            for nome, padrao in PADROES.items():
                pass

                ocorrencias = len(
                    re.findall(
                        padrao,
                        texto,
                        re.IGNORECASE
                    )
                )

                if ocorrencias > 0:
                    pass

                    info["assinaturas"][
                        nome
                    ] = ocorrencias

                    info["score"] += ocorrencias

            urls = re.findall(
                r"https?://[^\s'"<>]+",
                texto,
                re.IGNORECASE
            )

            info[
                "urls_encontradas"
            ] = list(
                set(urls)
            )[:50]

            RELATORIO[
                "motores"
            ].append(info)

            total_encontrados += 1

        except Exception as erro:
            pass

            RELATORIO[
                "motores"
            ].append({

                "arquivo":
                    str(arquivo),

                "erro":
                    str(erro)

            })

RELATORIO[
    "motores"
] = sorted(

    RELATORIO[
        "motores"
    ],

    key=lambda x: x.get(
        "score",
        0
    ),

    reverse=True

)

RELATORIO[
    "resumo"
] = {

    "motores_inspecionados":
        total_encontrados,

    "motores_com_score":
        len(
            RELATORIO[
                "motores"
            ]
        )
}

SAIDA = (
    ROOT /
    "IOTEC_ENGINE_FORENSICS_REPORT.json"
)

with open(
    SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        RELATORIO,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nENGINE FORENSICS\n")

print(
    "MOTORES:",
    RELATORIO[
        "resumo"
    ][
        "motores_inspecionados"
    ]
)

print("\nTOP MOTORES:\n")

for motor in RELATORIO[
    "motores"
][:20]:

    print(
        motor.get(
            "nome",
            "?"
        ),
        "-> SCORE",
        motor.get(
            "score",
            0
        )
    )

    if motor.get(
        "assinaturas"
    ):

        print(
            "ASSINATURAS:",
            ", ".join(
                motor[
                    "assinaturas"
                ].keys()
            )
        )

print(
    "\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:"
)

print(SAIDA)


