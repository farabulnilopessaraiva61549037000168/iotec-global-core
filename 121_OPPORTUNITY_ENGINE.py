import json
import os
from datetime import datetime

INPUT_FILE = "IOTEC_COMPANY_DATABASE.json"
OUTPUT_FILE = "IOTEC_OPPORTUNITY_DATABASE.json"

# ==========================================================
# PRODUTOS POR SEGMENTO
# ==========================================================

PRODUCTS = {

    "ENGENHARIA":[

        "Dashboard Executivo",
        "Business Intelligence",
        "Portal Corporativo",
        "DiagnÃƒÂ³stico Digital"

    ],

    "EDUCACAO":[

        "Portal Corporativo",
        "Dashboard Executivo",
        "Business Intelligence"

    ],

    "SAUDE":[

        "Business Intelligence",
        "Monitoramento EstratÃƒÂ©gico"

    ],

    "INDUSTRIA":[

        "Business Intelligence",
        "Auditoria TecnolÃƒÂ³gica",
        "Dashboard Executivo"

    ]

}

# ==========================================================

def calcular_score(segmento):

    segmento = segmento.upper()

    if segmento == "ENGENHARIA":
        return 95

    if segmento == "INDUSTRIA":
        return 90

    if segmento == "SAUDE":
        return 88

    if segmento == "EDUCACAO":
        return 86

    return 70

# ==========================================================

def prioridade(score):

    if score >= 90:
        return "MÃƒÂXIMA"

    if score >= 80:
        return "ALTA"

    if score >= 70:
        return "MÃƒâ€°DIA"

    return "BAIXA"

# ==========================================================

if not os.path.exists(INPUT_FILE):

    print("Arquivo nÃƒÂ£o encontrado:")
    print(INPUT_FILE)
    raise SystemExit()

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    empresas = json.load(f)

oportunidades = []

for empresa in empresas:

    segmento = empresa.get("segmento","GERAL")

    score = calcular_score(segmento)

    produtos = PRODUCTS.get(
        segmento.upper(),
        ["Business Intelligence"]
    )

    oportunidades.append({

        "company":empresa.get("company_name",""),

        "segment":segmento,

        "city":empresa.get("city",""),

        "score":score,

        "priority":prioridade(score),

        "recommended_products":produtos,

        "crm_status":"NOVO LEAD",

        "proposal":"PENDENTE",

        "commercial_action":"AGUARDANDO",

        "created_at":datetime.now().isoformat()

    })

oportunidades.sort(
    key=lambda x:x["score"],
    reverse=True
)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        oportunidades,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*90)
print("IOTEC OPPORTUNITY ENGINE")
print("="*90)
print()

print("OPORTUNIDADES :",len(oportunidades))
print()

print("="*90)
print("TOP 10")
print("="*90)
print()

for item in oportunidades[:10]:

    print(item["company"])
    print("Segmento :",item["segment"])
    print("Score....:",item["score"])
    print("Prioridade:",item["priority"])
    print("Produto Principal :",item["recommended_products"][0])
    print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Transformar")
print("empresas")
print("em oportunidades")
print("comerciais.")

print()

print("Priorizar")
print("quem deve")
print("receber")
print("atenÃƒÂ§ÃƒÂ£o")
print("primeiro.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("As empresas")
print("passam agora")
print("a possuir")
print("prioridade")
print("comercial.")

print()

print("O Comercial")
print("nÃƒÂ£o trabalha")
print("mais por")
print("ordem aleatÃƒÂ³ria.")

print()

print("Ele trabalha")
print("por oportunidade.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Banco de Oportunidades :",len(oportunidades))
print("Data :",datetime.now())
print()

print("OPPORTUNITY ENGINE OPERACIONAL.")

