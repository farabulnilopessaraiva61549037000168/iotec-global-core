import json
import os
from datetime import datetime

INPUT = "IOTEC_CRM_DATABASE.json"
OUTPUT = "IOTEC_QUALIFIED_LEADS.json"

# ==========================================================
# PALAVRAS-CHAVE
# ==========================================================

COMPANIES = [

    "engenharia",
    "construtora",
    "empreiteira",
    "consultoria",
    "tecnologia",
    "software",
    "industrial",
    "indÃƒÂºstria",
    "hospital",
    "clÃƒÂ­nica",
    "empresa",
    "corp",
    "ltda",
    "s.a",
    "sa"

]

LOW_PRIORITY = [

    "universidade",
    "campus",
    "departamento",
    "centro acadÃƒÂªmico",
    "grupo",
    "laboratÃƒÂ³rio",
    "area de convivencia",
    "ÃƒÂ¡rea de convivÃƒÂªncia",
    "curso",
    "bloco",
    "biblioteca"

]


# ==========================================================

def classify(name):

    texto = name.lower()

    score = 50

    tipo = "OUTRO"

    comprador = False

    for palavra in COMPANIES:

        if palavra in texto:

            score += 35

            tipo = "EMPRESA"

            comprador = True

    for palavra in LOW_PRIORITY:

        if palavra in texto:

            score -= 45

            tipo = "NÃƒÆ'O PRIORITÃƒÂRIO"

            comprador = False

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    if score >= 90:
        prioridade = "MÃƒÂXIMA"

    elif score >= 75:
        prioridade = "ALTA"

    elif score >= 50:
        prioridade = "MÃƒâ€°DIA"

    else:
        prioridade = "BAIXA"

    return tipo, comprador, score, prioridade


# ==========================================================

if not os.path.exists(INPUT):

    print("CRM inexistente.")
    raise SystemExit()


with open(INPUT, "r", encoding="utf-8") as f:

    crm = json.load(f)


resultado = []

for lead in crm:

    tipo, comprador, score, prioridade = classify(

        lead["company"]

    )

    registro = lead.copy()

    registro["organization_type"] = tipo

    registro["potential_buyer"] = comprador

    registro["lead_quality_score"] = score

    registro["lead_priority"] = prioridade

    resultado.append(registro)


resultado.sort(

    key=lambda x: x["lead_quality_score"],

    reverse=True

)


with open(

    OUTPUT,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        resultado,

        f,

        indent=4,

        ensure_ascii=False

    )


# ==========================================================

print("="*90)
print("IOTEC LEAD QUALITY ENGINE")
print("="*90)
print()

print("LEADS ANALISADOS :",len(resultado))
print()

print("="*90)
print("TOP 10")
print("="*90)
print()

for lead in resultado[:10]:

    print(lead["company"])

    print("Tipo........:",lead["organization_type"])

    print("Comprador...:",lead["potential_buyer"])

    print("Score.......:",lead["lead_quality_score"])

    print("Prioridade..:",lead["lead_priority"])

    print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Separar")

print("empresas")

print("de")

print("organizaÃƒÂ§ÃƒÂµes")

print("que")

print("nÃƒÂ£o")

print("representam")

print("clientes")

print("prioritÃƒÂ¡rios.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("O Comercial")

print("passa")

print("a concentrar")

print("esforÃƒÂ§os")

print("nas organizaÃƒÂ§ÃƒÂµes")

print("com maior")

print("potencial")

print("de negÃƒÂ³cio.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

empresas = sum(

    1 for x in resultado

    if x["potential_buyer"]

)

print("Compradores Potenciais :",empresas)

print("Total de Leads :",len(resultado))

print("Data :",datetime.now())

print()

print("LEAD QUALITY ENGINE OPERACIONAL.")

