import json
import time
import requests
from datetime import datetime

# ==========================================================
# IOTEC OPENSTREETMAP DISCOVERY ENGINE
# ==========================================================

USER_AGENT = "IOTEC Discovery Engine 1.0"

HEADERS = {
    "User-Agent": USER_AGENT
}

URL = "https://nominatim.openstreetmap.org/search"


# ----------------------------------------------------------
# Pesquisa empresas
# ----------------------------------------------------------

def pesquisar(query):

    parametros = {
        "q": query,
        "format": "jsonv2",
        "limit": 20,
        "addressdetails": 1
    }

    resposta = requests.get(
        URL,
        params=parametros,
        headers=HEADERS,
        timeout=30
    )

    resposta.raise_for_status()

    return resposta.json()


# ----------------------------------------------------------
# PadronizaÃƒÂ§ÃƒÂ£o
# ----------------------------------------------------------

def padronizar(resultado):

    endereco = resultado.get("address", {})

    return {

        "company_name": resultado.get("display_name",""),

        "latitude": resultado.get("lat",""),

        "longitude": resultado.get("lon",""),

        "city": endereco.get(
            "city",
            endereco.get(
                "town",
                endereco.get(
                    "municipality",""
                )
            )
        ),

        "state": endereco.get("state",""),

        "country": endereco.get("country",""),

        "source": "OpenStreetMap"

    }


# ----------------------------------------------------------
# Principal
# ----------------------------------------------------------

def main():

    consulta = "engenharia Fortaleza"

    print("="*80)
    print("IOTEC OPENSTREETMAP DISCOVERY ENGINE")
    print("="*80)
    print()

    print("Consulta:")
    print(consulta)
    print()

    dados = pesquisar(consulta)

    empresas = []

    for item in dados:

        empresas.append(
            padronizar(item)
        )

    with open(

        "IOTEC_REAL_COMPANIES.json",

        "w",

        encoding="utf-8"

    ) as arquivo:

        json.dump(

            empresas,

            arquivo,

            indent=4,

            ensure_ascii=False

        )

    print("Resultados:",len(empresas))
    print()

    for empresa in empresas[:10]:

        print("-"*60)
        print(empresa["company_name"])
        print(empresa["city"])
        print()

    print("="*80)
    print("ARQUIVO GERADO")
    print("="*80)

    print()

    print("IOTEC_REAL_COMPANIES.json")

    print()

    print("STATUS")

    print("DISCOVERY OPERACIONAL")

    print(datetime.now())



if __name__ == "__main__":

    main()

