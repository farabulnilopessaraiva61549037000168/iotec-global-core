# ==========================================================
# 110_GOOGLE_MAPS_CONNECTOR.py
# IOTEC GOOGLE MAPS CONNECTOR
# ==========================================================

import requests

API_KEY = "COLE_AQUI_A_MESMA_CHAVE_DO_GOOGLE_MAPS"

BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"


def pesquisar_empresas(consulta):

    resposta = requests.get(

        BASE_URL,

        params={

            "query": consulta,

            "key": API_KEY

        },

        timeout=30

    )

    resposta.raise_for_status()

    dados = resposta.json()

    if dados.get("status") != "OK":

        print(dados)

        return []

    empresas = []

    for item in dados.get("results", []):

        empresas.append({

            "nome": item.get("name", ""),

            "endereco": item.get("formatted_address", ""),

            "avaliacao": item.get("rating", ""),

            "latitude": item.get("geometry", {})
                             .get("location", {})
                             .get("lat"),

            "longitude": item.get("geometry", {})
                              .get("location", {})
                              .get("lng"),

            "place_id": item.get("place_id", "")

        })

    return empresas


