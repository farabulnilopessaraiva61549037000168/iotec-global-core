# ==============================================================================
# 106_OPENSTREETMAP_CONNECTOR.py
# IOTEC OPENSTREETMAP CONNECTOR
# ==============================================================================

import requests
import json
from datetime import datetime

URL = "https://nominatim.openstreetmap.org/search"

HEADERS = {

    "User-Agent": "IOTEC Discovery Center/1.0"

}

# ------------------------------------------------------------------------

def pesquisar(consulta, limite=20):

    resposta = requests.get(

        URL,

        headers=HEADERS,

        params={

            "q": consulta,

            "format": "jsonv2",

            "limit": limite,

            "addressdetails": 1

        },

        timeout=30

    )

    resposta.raise_for_status()

    dados = resposta.json()

    empresas = []

    for item in dados:

        empresas.append({

            "nome": item.get("display_name", ""),

            "latitude": item.get("lat"),

            "longitude": item.get("lon"),

            "origem": "OpenStreetMap"

        })

    return empresas

# ------------------------------------------------------------------------

print("=" * 90)
print("IOTEC OPENSTREETMAP CONNECTOR")
print("=" * 90)
print()

consulta = "engenharia Fortaleza"

print("Consulta:", consulta)
print()

try:

    empresas = pesquisar(consulta)

    print("Resultados encontrados:", len(empresas))
    print()

    for empresa in empresas:

        print("=" * 60)

        print("Nome:")
        print(empresa["nome"])
        print()

        print("Latitude :", empresa["latitude"])
        print("Longitude:", empresa["longitude"])
        print()

    with open(

        "IOTEC_OPENSTREETMAP_RESULTS.json",

        "w",

        encoding="utf8"

    ) as f:

        json.dump(

            {

                "generated_at": datetime.now().isoformat(),

                "consulta": consulta,

                "resultados": empresas

            },

            f,

            indent=4,

            ensure_ascii=False

        )

    print("=" * 90)
    print("ARQUIVO GERADO")
    print("=" * 90)
    print()

    print("IOTEC_OPENSTREETMAP_RESULTS.json")

except Exception as erro:

    print()

    print("ERRO")

    print(erro)


