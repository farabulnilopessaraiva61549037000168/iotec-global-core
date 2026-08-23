# ==========================================================
# 079_VISUAL_GENOME_ENGINE.py
# IOTEC VISUAL GENOME ENGINE
# ==========================================================

from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json

ROOT = Path("C:/IOTEC")

print("="*70)
print("IOTEC VISUAL GENOME ENGINE")
print("="*70)
print()

print("Analisando DNA visual...")
print()

FEATURES = {

    "navbar":[
        "navbar","menu","navigation"
    ],

    "sidebar":[
        "sidebar","menu-lateral"
    ],

    "table":[
        "<table","datatable"
    ],

    "form":[
        "<form","input","textarea","select"
    ],

    "button":[
        "<button","btn","submit"
    ],

    "card":[
        "card","panel","widget"
    ],

    "chart":[
        "chart","plotly","canvas","apex","echarts"
    ],

    "login":[
        "password","login","signin"
    ],

    "payment":[
        "paypal","checkout","payment","pix"
    ],

    "map":[
        "google.maps","leaflet","mapbox"
    ]

}

resultado=[]

estatisticas=Counter()

for html in ROOT.rglob("*.html"):

    try:

        texto=html.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()

        soup=BeautifulSoup(texto,"html.parser")

        score=0

        dna={}

        for feature,palavras in FEATURES.items():

            valor=0

            for palavra in palavras:

                valor+=texto.count(palavra)

            dna[feature]=valor

            score+=valor

            if valor>0:
                estatisticas[feature]+=1

        if score>=80:

            nivel="Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦"

        elif score>=40:

            nivel="Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦"

        elif score>=20:

            nivel="Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦"

        elif score>=10:

            nivel="Ã¢Ëœâ€¦Ã¢Ëœâ€¦"

        else:

            nivel="Ã¢Ëœâ€¦"

        resultado.append({

            "arquivo":html.name,

            "score":score,

            "nivel":nivel,

            "dna":dna,

            "caminho":str(html)

        })

    except:

        pass

resultado.sort(
    key=lambda x:x["score"],
    reverse=True
)

print("="*70)
print("TOP 30 INTERFACES")
print("="*70)
print()

for item in resultado[:30]:

    print(f'{item["score"]:5}  {item["nivel"]}  {item["arquivo"]}')

print()

print("="*70)
print("GENOMA VISUAL")
print("="*70)
print()

for nome,qtd in estatisticas.most_common():

    print(f"{nome:<20}{qtd}")

print()

with open(

    "IOTEC_VISUAL_GENOME.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        resultado,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*70)
print("ARQUIVO GERADO")
print("="*70)
print()

print("IOTEC_VISUAL_GENOME.json")

print()

print("="*70)
print("MISSAO")
print("="*70)
print()

print("O Kernel agora")
print("conhece as")
print("interfaces")
print("mais completas")
print("da empresa.")


