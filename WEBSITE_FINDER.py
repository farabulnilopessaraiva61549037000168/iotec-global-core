# ==========================================================
# C:\IOTEC\WEBSITE_FINDER.py
# IOTEC WEBSITE FINDER
# ==========================================================

import requests
import urllib.parse
import re

HEADERS = {
    "User-Agent": "IOTEC Website Finder"
}


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


def search(company):

    nome = clean_name(company)

    url = "https://html.duckduckgo.com/html/"

    try:

        r = requests.post(

            url,

            data={"q": nome},

            headers=HEADERS,

            timeout=30

        )

        if r.status_code != 200:

            return None

        html = r.text

        links = re.findall(

            r'nofollow" class="result__a" href="(.*?)"',

            html

        )

        if len(links) == 0:

            return None

        return links[0]

    except Exception:

        return None


# ==========================================================

if __name__ == "__main__":

    empresa = "Makro Engenharia"

    print("="*70)
    print("IOTEC WEBSITE FINDER")
    print("="*70)
    print()

    site = search(empresa)

    if site:

        print("Website encontrado")
        print(site)

    else:

        print("Nenhum website encontrado.")

