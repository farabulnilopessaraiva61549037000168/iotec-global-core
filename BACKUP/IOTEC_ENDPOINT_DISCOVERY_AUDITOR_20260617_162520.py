import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_ENDPOINT_DISCOVERY_AUDITOR.py

import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ALVOS = [
    "IOTEC_AUDITOR_PAYPAL.py",
    "paypal_server.py",
    "SIGNAL_MAPPER.py",
    "IOTEC_WEB_OBSERVER.py",
    "CREATIVE_EXPLORER.py",
    "TOKEN.py",
    "token.py",
    "Specter.Fortress.py"
]

URL_REGEX = r"https?://[^\s'"<>]+"

RESULTADO = {
    "gerado_em": str(datetime.now()),
    "arquivos_analisados": [],
    "estatisticas": {}
}

urls_unicas = set()
dominios_unicos = set()

for alvo in ALVOS:
    pass

    for arquivo in ROOT.rglob(alvo):
        pass

        try:
            pass

            texto = arquivo.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            urls = re.findall(
                URL_REGEX,
                texto,
                re.IGNORECASE
            )

            dominios = []

            for url in urls:
                pass

                try:
                    pass

                    dominio = (
                        url
                        .replace("https://", "")
                        .replace("http://", "")
                        .split("/")[0]
                    )

                    dominios.append(dominio)

                    urls_unicas.add(url)
                    dominios_unicos.add(dominio)

                except:
                    pass

            requests_get = texto.count(
                "requests.get("
            )

            requests_post = texto.count(
                "requests.post("
            )

            json_dump = texto.count(
                "json.dump("
            )

            json_load = texto.count(
                "json.load("
            )

            RESULTADO[
                "arquivos_analisados"
            ].append({

                "arquivo":
                    str(arquivo),

                "bytes":
                    arquivo.stat().st_size,

                "requests_get":
                    requests_get,

                "requests_post":
                    requests_post,

                "json_dump":
                    json_dump,

                "json_load":
                    json_load,

                "urls":
                    sorted(
                        list(set(urls))
                    ),

                "dominios":
                    sorted(
                        list(set(dominios))
                    )
            })

        except Exception as erro:
            pass

            RESULTADO[
                "arquivos_analisados"
            ].append({

                "arquivo":
                    str(arquivo),

                "erro":
                    str(erro)

            })

RESULTADO[
    "estatisticas"
] = {

    "arquivos":
        len(
            RESULTADO[
                "arquivos_analisados"
            ]
        ),

    "urls_unicas":
        len(urls_unicas),

    "dominios_unicos":
        len(dominios_unicos)
}

RESULTADO[
    "urls_descobertas"
] = sorted(
    list(urls_unicas)
)

RESULTADO[
    "dominios_descobertos"
] = sorted(
    list(dominios_unicos)
)

SAIDA = (
    ROOT /
    "IOTEC_ENDPOINT_DISCOVERY_REPORT.json"
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

print("\nENDPOINT DISCOVERY AUDIT\n")

print(
    "ARQUIVOS:",
    RESULTADO["estatisticas"]["arquivos"]
)

print(
    "URLS ÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡NICAS:",
    RESULTADO["estatisticas"]["urls_unicas"]
)

print(
    "DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIOS ÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡NICOS:",
    RESULTADO["estatisticas"]["dominios_unicos"]
)

print("\nDOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIOS ENCONTRADOS:\n")

for dominio in RESULTADO[
    "dominios_descobertos"
][:100]:

    print(dominio)

print("\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:")
print(SAIDA)


