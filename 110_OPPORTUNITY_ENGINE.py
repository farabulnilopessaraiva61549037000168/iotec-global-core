# ==============================================================================
# 110_OPPORTUNITY_ENGINE.py
# IOTEC OPPORTUNITY ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC OPPORTUNITY ENGINE")
print("MOTOR DE OPORTUNIDADES")
print("="*90)
print()

ARQUIVO="IOTEC_COMMERCIAL_EVIDENCE_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Banco comercial nÃƒÂ£o encontrado.")
    raise SystemExit()

# ---------------------------------------------------------------------
# PRODUTOS DA IOTEC
# ---------------------------------------------------------------------

PRODUTOS=[

{
    "nome":"Executive Skin",
    "segmentos":["engenharia","construtora","indÃƒÂºstria","tecnologia"],
    "valor":"ALTO"
},

{
    "nome":"Commercial Intelligence",
    "segmentos":["engenharia","consultoria","serviÃƒÂ§os"],
    "valor":"ALTO"
},

{
    "nome":"Business Analytics",
    "segmentos":["engenharia","hospital","prefeitura","escola"],
    "valor":"MÃƒâ€°DIO"
},

{
    "nome":"Experience Warehouse",
    "segmentos":["todos"],
    "valor":"ALTO"
},

{
    "nome":"Visual Genome",
    "segmentos":["todos"],
    "valor":"MÃƒâ€°DIO"
}

]

OPORTUNIDADES=[]

print("Analisando compatibilidade...")
print()

for empresa in banco["empresas"]:

    nome=empresa["nome"].lower()

    produtos=[]

    score=empresa["score"]

    if "engenharia" in nome:

        produtos.extend([

            "Executive Skin",
            "Commercial Intelligence",
            "Business Analytics"

        ])

        score+=40

    if "tecnologia" in nome:

        produtos.append("Experience Warehouse")
        score+=20

    if score>=80:

        prioridade="ALTÃƒÂSSIMA"

    elif score>=60:

        prioridade="ALTA"

    elif score>=40:

        prioridade="MÃƒâ€°DIA"

    else:

        prioridade="BAIXA"

    oportunidade={

        "empresa":empresa["nome"],

        "score":score,

        "prioridade":prioridade,

        "produtos":produtos,

        "status":"AGUARDANDO CONTATO"

    }

    OPORTUNIDADES.append(oportunidade)

OPORTUNIDADES.sort(

key=lambda x:x["score"],

reverse=True

)

print("="*90)
print("OPORTUNIDADES")
print("="*90)
print()

for op in OPORTUNIDADES:

    estrelas="Ã¢Ëœâ€¦"*min(5,max(1,op["score"]//20))

    print(f"{estrelas:5} {op['score']:3} {op['prioridade']:12} {op['empresa']}")

    print("Produtos:")

    for p in op["produtos"]:

        print("   Ã¢Å"â€œ",p)

    print()

saida={

"generated_at":datetime.now().isoformat(),

"total":len(OPORTUNIDADES),

"oportunidades":OPORTUNIDADES

}

with open(

"IOTEC_OPPORTUNITY_DATABASE.json",

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
print("MISSÃƒÆ'O")
print("="*90)
print()

print("O Kernel deixa")
print("de procurar")

print("empresas.")

print()

print("Agora procura")

print("oportunidades")

print("de negÃƒÂ³cio.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_OPPORTUNITY_DATABASE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Oportunidades......",len(OPORTUNIDADES))
print("Data...............",datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("OPPORTUNITY ENGINE OPERACIONAL.")


