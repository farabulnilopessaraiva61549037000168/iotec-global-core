# ==========================================================
# IOTEC SOURCE ENGINE
# ==========================================================

import requests
import urllib.parse

from WEBSITE_FINDER import search as find_website

HEADERS = {

    "User-Agent": "IOTEC Source Engine"

}


class SourceEngine:

    # ======================================================

    @staticmethod
    def clean_name(company):

        remover = [

            "RegiÃƒÂ£o Nordeste",
            "Brasil",
            "CearÃƒÂ¡",
            "Fortaleza",
            "Centro",
            "Pici",
            "Paupina"

        ]

        nome = company

        for item in remover:

            nome = nome.replace(item, "")

        return nome.split(",")[0].strip()

    # ======================================================

    @staticmethod
    def openstreetmap(company):

        nome = SourceEngine.clean_name(company)

        try:

            r = requests.get(

                "https://nominatim.openstreetmap.org/search",

                params={

                    "q": nome,

                    "format": "jsonv2",

                    "limit": 1,

                    "addressdetails": 1

                },

                headers=HEADERS,

                timeout=20

            )

            if r.status_code != 200:

                return {}

            dados = r.json()

            if not dados:

                return {}

            d = dados[0]

            return {

                "source": "OpenStreetMap",

                "display_name": d.get("display_name",""),

                "latitude": d.get("lat",""),

                "longitude": d.get("lon",""),
# ==========================================================
# IOTEC SOURCE ENGINE
# PARTE 1
# ==========================================================

import requests
import urllib.parse

from WEBSITE_FINDER import search as find_website


HEADERS = {

    "User-Agent": "IOTEC Source Engine"

}


class SourceEngine:


    # ======================================================

    @staticmethod
    def clean_name(company):

        remover = [

            "RegiÃƒÂ£o Nordeste",
            "Brasil",
            "CearÃƒÂ¡",
            "Fortaleza",
            "Centro",
            "Pici",
            "Paupina",
            "Rua",
            "Avenida",
            "Av.",
            "Travessa"

        ]

        nome = company

        for item in remover:

            nome = nome.replace(item, "")

        nome = nome.split(",")[0].strip()

        return nome


    # ======================================================

    @staticmethod
    def openstreetmap(company):

        nome = SourceEngine.clean_name(company)

        url = "https://nominatim.openstreetmap.org/search"

        params = {

            "q": nome,

            "format": "jsonv2",

            "limit": 1,

            "addressdetails": 1

        }

        try:

            resposta = requests.get(

                url,

                params=params,

                headers=HEADERS,

                timeout=30

            )

            if resposta.status_code != 200:

                return {}

            dados = resposta.json()

            if len(dados) == 0:

                return {}

            item = dados[0]

            return {

                "source": "OpenStreetMap",

                "display_name": item.get("display_name", ""),

                "latitude": item.get("lat", ""),

                "longitude": item.get("lon", ""),

                "osm_class": item.get("class", ""),

                "osm_type": item.get("type", ""),

                "importance": item.get("importance", ""),

                "place_id": item.get("place_id", "")

            }

        except Exception:

            return {}
                "osm_class": d.get("class",""),

                "osm_type": d.get("type","")

            }

        except Exception:

            return {}

