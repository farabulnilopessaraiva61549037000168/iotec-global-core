import json
import os
from datetime import datetime

INPUT_FILE = "IOTEC_OPPORTUNITY_DATABASE.json"
OUTPUT_FILE = "IOTEC_CRM_DATABASE.json"


# ==========================================================
# ESTÃƒÂGIOS DO CRM
# ==========================================================

PIPELINE = [

    "NOVO LEAD",

    "QUALIFICAÃƒâ€¡ÃƒÆ'O",

    "PRIMEIRO CONTATO",

    "DIAGNÃƒâ€œSTICO",

    "PROPOSTA",

    "NEGOCIAÃƒâ€¡ÃƒÆ'O",

    "CONTRATO",

    "CLIENTE"

]


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

    print("Arquivo inexistente:")
    print(INPUT_FILE)

    raise SystemExit()


with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    oportunidades = json.load(f)


crm = []


for oportunidade in oportunidades:

    registro = {

        "company": oportunidade["company"],

        "segment": oportunidade["segment"],

        "city": oportunidade.get("city", ""),

        "score": oportunidade["score"],

        "priority": prioridade(
            oportunidade["score"]
        ),

        "recommended_products":
            oportunidade["recommended_products"],

        "pipeline_stage": PIPELINE[0],

        "assigned_department":
            "Commercial Factory",

        "assigned_agent":
            "Commercial Scientist",

        "next_action":
            "Pesquisar canais oficiais",

        "website": "",

        "email": "",

        "phone": "",

        "linkedin": "",

        "last_contact": "",

        "proposal_status":
            "NÃƒÆ'O GERADA",

        "contract_status":
            "NÃƒÆ'O",

        "customer":
            False,

        "created_at":
            datetime.now().isoformat()

    }

    crm.append(registro)


with open(

    OUTPUT_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        crm,

        f,

        indent=4,

        ensure_ascii=False

    )


# ==========================================================

print("="*90)
print("IOTEC CRM INTELLIGENCE ENGINE")
print("="*90)
print()

print("LEADS GERADOS :",len(crm))
print()

print("="*90)
print("TOP 10")
print("="*90)
print()

for lead in crm[:10]:

    print(lead["company"])

    print("Segmento :",lead["segment"])

    print("Prioridade :",lead["priority"])

    print("Pipeline :",lead["pipeline_stage"])

    print("PrÃƒÂ³xima AÃƒÂ§ÃƒÂ£o :",lead["next_action"])

    print()

print("="*90)
print("PIPELINE")
print("="*90)
print()

for etapa in PIPELINE:

    print(">",etapa)

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Transformar")

print("oportunidades")

print("em relacionamento")

print("comercial.")

print()

print("Nenhuma empresa")

print("permanece")

print("fora")

print("do CRM.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("Todas as")

print("oportunidades")

print("foram inseridas")

print("automaticamente")

print("no CRM.")

print()

print("O Comercial")

print("passa a trabalhar")

print("por prioridades")

print("e etapas")

print("bem definidas.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Leads :",len(crm))

print("Pipeline :",len(PIPELINE),"etapas")

print("Data :",datetime.now())

print()

print("CRM INTELLIGENCE OPERACIONAL.")

