import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import re
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

PADROES = {

    "requests_get": r"requests\.get\s*\(",
    "requests_post": r"requests\.post\s*\(",

    "httpx_get": r"httpx\.get\s*\(",
    "httpx_post": r"httpx\.post\s*\(",

    "aiohttp": r"aiohttp",

    "selenium": r"selenium",
    "webdriver": r"webdriver",

    "beautifulsoup": r"BeautifulSoup",
    "scrapy": r"scrapy",

    "api_key": r"api[_\-]?key",
    "token": r"token",
    "bearer": r"bearer",

    "authorization": r"authorization",

    "socket": r"socket",

    "websocket": r"websocket",

    "urllib": r"urllib",

    "ftp": r"ftp",

    "graphql": r"graphql"
}

resultado = {
    "motores": [],
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

        for nome, padrao in PADROES.items():
            pass

            if re.search(
                padrao,
                texto,
                re.IGNORECASE
            ):

                score += 1

                encontrados.append(nome)

        if score > 0:
            pass

            resultado["motores"].append({

                "arquivo":
                    str(arq),

                "score":
                    score,

                "conectores":
                    encontrados

            })

    except:
        pass

resultado["motores"] = sorted(

    resultado["motores"],

    key=lambda x: x["score"],

    reverse=True

)

resultado["estatisticas"] = {

    "arquivos_python":
        len(arquivos),

    "motores_conectividade":
        len(
            resultado["motores"]
        )
}

saida = (
    ROOT /
    "IOTEC_REAL_CONNECTIVITY_REPORT.json"
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
    "\nREAL CONNECTIVITY AUDIT\n"
)

print(
    "ARQUIVOS PYTHON:",
    resultado[
        "estatisticas"
    ]["arquivos_python"]
)

print(
    "MOTORES COM CONECTIVIDADE:",
    resultado[
        "estatisticas"
    ]["motores_conectividade"]
)

print(
    "\nTOP 50:\n"
)

for item in resultado[
    "motores"
][:50]:

    print(
        item["score"],
        "->",
        Path(
            item["arquivo"]
        ).name
    )

    print(
        "   ",
        ", ".join(
            item["conectores"]
        )
    )

print(
    "\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:"
)

print(saida)




