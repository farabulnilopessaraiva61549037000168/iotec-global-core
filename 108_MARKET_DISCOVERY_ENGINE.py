# ==============================================================================
# 108_MARKET_DISCOVERY_ENGINE.py
# IOTEC MARKET DISCOVERY ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC MARKET DISCOVERY ENGINE")
print("MOTOR DE DESCOBERTA DE MERCADO")
print("="*90)
print()

ARQUIVO="IOTEC_ENTITY_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Banco nÃƒÂ£o encontrado.")
    raise SystemExit()

print("Analisando mercado...")
print()

OPORTUNIDADES=[]

PALAVRAS_EMPRESA=[

"engenharia",
"ltda",
"eireli",
"s.a",
"consultoria",
"tecnologia",
"industrial",
"construtora",
"serviÃƒÂ§os",
"solutions",
"group"

]

PALAVRAS_DESCARTAR=[

"departamento",
"curso",
"laboratÃƒÂ³rio",
"laboratorio",
"campus",
"universidade",
"centro acadÃƒÂªmico",
"grupo"

]

for entidade in banco["entidades"]:

    nome=entidade["nome"].lower()

    score=0

    motivos=[]

    for palavra in PALAVRAS_EMPRESA:

        if palavra in nome:

            score+=20

            motivos.append(palavra)

    for palavra in PALAVRAS_DESCARTAR:

        if palavra in nome:

            score-=40

    if score<0:

        score=0

    entidade["score"]=score

    if score>=20:

        entidade["status"]="OPORTUNIDADE"

        OPORTUNIDADES.append(entidade)

    else:

        entidade["status"]="OBSERVAÃƒâ€¡ÃƒÆ'O"

print("="*90)
print("RANKING")
print("="*90)
print()

OPORTUNIDADES.sort(

key=lambda x:x["score"],

reverse=True

)

for empresa in OPORTUNIDADES:

    estrelas="Ã¢Ëœâ€¦"*min(5,max(1,empresa["score"]//20))

    print(f"{estrelas:5} {empresa['score']:3}  {empresa['nome']}")

print()

saida={

"generated_at":datetime.now().isoformat(),

"total":len(OPORTUNIDADES),

"empresas":OPORTUNIDADES

}

with open(

"IOTEC_MARKET_DATABASE.json",

"w",

encoding="utf8"

) as f:

    json.dump(

saida,

f,

indent=4,

ensure_ascii=False

)

print("="*90)
print("RESUMO")
print("="*90)
print()

print("Entidades analisadas....",len(banco["entidades"]))
print("Oportunidades...........",len(OPORTUNIDADES))

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("Nem toda entidade")
print("ÃƒÂ© um cliente.")

print()

print("O Kernel aprende")
print("a separar")

print("Conhecimento.")

print("Mercado.")

print("Oportunidades.")

print("Receita.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_MARKET_DATABASE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("MARKET DISCOVERY OPERACIONAL.")


