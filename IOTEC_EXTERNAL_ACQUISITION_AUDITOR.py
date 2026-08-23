import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
import json
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\IOTEC")

PALAVRAS_AQUISICAO = {

    "requests",
    "httpx",
    "urllib",
    "aiohttp",

    "api",
    "apis",

    "scraping",
    "scraper",

    "search",

    "google",

    "bing",

    "duckduckgo",

    "lead",

    "empresa",

    "cliente",

    "cnpj",

    "business",

    "market",

    "acquisition",

    "source",

    "sources",

    "discovery",

    "crawler",

    "collect",

    "collector"
}

resultado = {

    "motores_aquisicao": [],

    "ranking": [],

    "estatisticas": {}
}

arquivos = list(
    ROOT.rglob("*.py")
)

for arq in arquivos:
    pass

    try:
        pass

        texto = arq.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        score = 0

        encontrados = []

        texto_lower = texto.lower()

        for palavra in PALAVRAS_AQUISICAO:
            pass

            if palavra in texto_lower:
                pass

                score += 1

                encontrados.append(
                    palavra
                )

        if score > 0:
            pass

            resultado[
                "motores_aquisicao"
            ].append({

                "arquivo":
                    str(arq),

                "score":
                    score,

                "palavras":
                    encontrados

            })

    except:
        pass

resultado[
    "ranking"
] = sorted(

    resultado[
        "motores_aquisicao"
    ],

    key=lambda x: x["score"],

    reverse=True

)

resultado[
    "estatisticas"
] = {

    "arquivos_python":
        len(arquivos),

    "motores_aquisicao":
        len(
            resultado[
                "motores_aquisicao"
            ]
        )
}

saida = ROOT / (
    "IOTEC_EXTERNAL_"
    "ACQUISITION_REPORT.json"
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

print(
    "\nEXTERNAL ACQUISITION AUDIT\n"
)

print(
    "ARQUIVOS PYTHON:",
    resultado[
        "estatisticas"
    ]["arquivos_python"]
)

print(
    "MOTORES DE AQUISIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:",
    resultado[
        "estatisticas"
    ]["motores_aquisicao"]
)

print(
    "\nTOP 20:\n"
)

for item in resultado[
    "ranking"
][:20]:

    print(
        item["score"],
        "->",
        Path(
            item["arquivo"]
        ).name
    )

print(
    "\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:"
)

print(saida)




