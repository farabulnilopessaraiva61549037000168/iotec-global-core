# ==========================================================
# C:\IOTEC\SOURCE_CONNECTORS.py
# IOTEC SOURCE CONNECTORS
# ==========================================================

import requests
import urllib.parse

HEADERS = {
    "User-Agent": "IOTEC Source Engine"
}


# ==========================================================
# LIMPEZA
# ==========================================================

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

    for item in remover:

        company = company.replace(item, "")

    return company.split(",")[0].strip()


# ==========================================================
# OPENSTREETMAP
# ==========================================================

def openstreetmap(company):

    nome = clean_name(company)

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

            "display_name": d.get("display_name",""),

            "latitude": d.get("lat",""),

            "longitude": d.get("lon",""),

            "osm_class": d.get("class",""),

            "osm_type": d.get("type",""),

            "source": "OpenStreetMap"

        }

    except:

        return {}


# ==========================================================
# WEBSITE
# ==========================================================

def website(company):

    nome = (

        clean_name(company)

        .lower()

        .replace("engenharia","")

        .replace("arquitetura","")

        .replace("construtora","")

        .replace(" ","")

    )

    candidatos = [

        f"https://{nome}.com.br",

        f"https://www.{nome}.com.br",

        f"https://{nome}.com",

        f"https://www.{nome}.com"

    ]

    for url in candidatos:

        try:

            r = requests.get(

                url,

                headers=HEADERS,

                timeout=6,

                allow_redirects=True

            )

            if r.status_code < 400:

                return url

        except:

            pass

    return ""


# ==========================================================
# GOOGLE
# ==========================================================

def google(company):

    return (

        "https://www.google.com/search?q=" +

        urllib.parse.quote(clean_name(company))

    )


# ==========================================================
# GOOGLE MAPS
# ==========================================================

def maps(company):

    return (

        "https://www.google.com/maps/search/" +

        urllib.parse.quote(clean_name(company))

    )


# ==========================================================
# BING
# ==========================================================

def bing(company):

    return (

        "https://www.bing.com/search?q=" +

        urllib.parse.quote(clean_name(company))

    )


# ==========================================================
# LINKEDIN
# ==========================================================

def linkedin(company):

    return (

        "https://www.linkedin.com/search/results/companies/?keywords=" +

        urllib.parse.quote(clean_name(company))

    )


# ==========================================================
# COLETOR ÃƒÅ¡NICO
# ==========================================================

def collect(company):

    dados = {

        "company_name": company

    }

    dados.update(openstreetmap(company))

    dados["website"] = website(company)

    dados["google"] = google(company)

    dados["maps"] = maps(company)

    dados["bing"] = bing(company)

    dados["linkedin"] = linkedin(company)

    return dados


# ==========================================================

if __name__ == "__main__":

    empresa = "Makro Engenharia"

    print("="*70)
    print("SOURCE CONNECTORS")
    print("="*70)
    print()

    resultado = collect(empresa)

    for k,v in resultado.items():

        print(f"{k:18}",v)

