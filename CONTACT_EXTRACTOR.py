# ==========================================================
# C:\IOTEC\CONTACT_EXTRACTOR.py
# IOTEC CONTACT EXTRACTOR
# ==========================================================

import re
import requests

HEADERS = {
    "User-Agent": "IOTEC Contact Extractor"
}


# ==========================================================

def extract(url):

    resultado = {

        "website": url,

        "emails": [],

        "phones": [],

        "linkedin": "",

        "instagram": "",

        "facebook": "",

        "youtube": ""

    }

    try:

        r = requests.get(

            url,

            headers=HEADERS,

            timeout=30

        )

    except:

        return resultado

    html = r.text

    # ------------------------------------------------------
    # EMAILS
    # ------------------------------------------------------

    emails = re.findall(

        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',

        html

    )

    resultado["emails"] = sorted(set(emails))

    # ------------------------------------------------------
    # TELEFONES
    # ------------------------------------------------------

    telefones = re.findall(

        r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}',

        html

    )

    resultado["phones"] = sorted(set(telefones))

    # ------------------------------------------------------
    # LINKEDIN
    # ------------------------------------------------------

    m = re.search(

        r'https?://(?:www\.)?linkedin\.com[^"']+',

        html,

        re.I

    )

    if m:

        resultado["linkedin"] = m.group(0)

    # ------------------------------------------------------
    # INSTAGRAM
    # ------------------------------------------------------

    m = re.search(

        r'https?://(?:www\.)?instagram\.com[^"']+',

        html,

        re.I

    )

    if m:

        resultado["instagram"] = m.group(0)

    # ------------------------------------------------------
    # FACEBOOK
    # ------------------------------------------------------

    m = re.search(

        r'https?://(?:www\.)?facebook\.com[^"']+',

        html,

        re.I

    )

    if m:

        resultado["facebook"] = m.group(0)

    # ------------------------------------------------------
    # YOUTUBE
    # ------------------------------------------------------

    m = re.search(

        r'https?://(?:www\.)?youtube\.com[^"']+',

        html,

        re.I

    )

    if m:

        resultado["youtube"] = m.group(0)

    return resultado


# ==========================================================

if __name__ == "__main__":

    url = "https://makroengenharia.com.br/"

    print("="*70)
    print("IOTEC CONTACT EXTRACTOR")
    print("="*70)
    print()

    dados = extract(url)

    for k,v in dados.items():

        print(k)

        print(v)

        print()

