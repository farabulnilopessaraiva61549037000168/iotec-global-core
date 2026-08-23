# ==========================================================
# 078_EXPERIENCE_ARCHAEOLOGIST.py
# IOTEC EXPERIENCE ARCHAEOLOGIST
# ==========================================================

from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
import json

ROOT = Path("C:/IOTEC")

print("="*70)
print("IOTEC EXPERIENCE ARCHAEOLOGIST")
print("="*70)
print()

print("Escavando patrimonio HTML...")
print()

PALAVRAS = {

    "Cockpit":[
        "cockpit","executive","presidencia",
        "painel","command center","control tower"
    ],

    "Dashboard":[
        "dashboard","grafico","chart","metric",
        "indicador","analytics"
    ],

    "Portal":[
        "portal","home","inicio","welcome",
        "empresa","institutional"
    ],

    "Landing Page":[
        "landing","hero","saiba mais",
        "conheca","conhecer","solucao"
    ],

    "Cliente":[
        "cliente","customer",
        "cadastro","contato"
    ],

    "Financeiro":[
        "paypal","pix","pagamento",
        "checkout","payment","invoice"
    ],

    "CRM":[
        "crm","lead","pipeline",
        "prospect"
    ],

    "Login":[
        "login","senha","password",
        "entrar","signin"
    ],

    "Catalogo":[
        "catalogo","catalog",
        "portfolio","produto","produto"
    ]

}

resultado=[]
contador=Counter()

total=0

for html in ROOT.rglob("*.html"):

    total+=1

    categoria="Indefinido"

    try:

        texto=html.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        soup=BeautifulSoup(texto,"html.parser")

        conteudo=(

            soup.get_text(" ",strip=True)

        ).lower()

        maior=0

        for nome,palavras in PALAVRAS.items():

            score=0

            for palavra in palavras:

                score+=conteudo.count(palavra.lower())

            if score>maior:

                maior=score
                categoria=nome

        contador[categoria]+=1

        resultado.append({

            "arquivo":html.name,
            "categoria":categoria,
            "score":maior,
            "caminho":str(html)

        })

    except:

        pass

print("="*70)
print("ARQUEOLOGIA CONCLUIDA")
print("="*70)
print()

print("HTML analisados :",total)
print()

for nome,qtd in contador.most_common():

    print(f"{nome:<20}{qtd}")

print()

with open(

    "IOTEC_EXPERIENCE_ARCHAEOLOGY.json",

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

print("IOTEC_EXPERIENCE_ARCHAEOLOGY.json")

print()

print("="*70)
print("MISSAO")
print("="*70)
print()

print("O Kernel passa")
print("a compreender")
print("o patrimonio")
print("visual da empresa.")


