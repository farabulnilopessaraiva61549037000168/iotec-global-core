import json
import os
from datetime import datetime

INPUT = "IOTEC_COMPANY_DATABASE.json"

if not os.path.exists(INPUT):

    print("Banco inexistente.")
    raise SystemExit()

with open(INPUT,"r",encoding="utf-8") as f:

    companies = json.load(f)

# ==========================================================
# PALAVRAS-CHAVE
# ==========================================================

RULES = {

    "EMPRESA_PRIVADA":[
        "LTDA",
        "S/A",
        "SA",
        "ME",
        "EPP",
        "ENGENHARIA",
        "CONSTRUTORA",
        "EMPREITEIRA",
        "INDUSTRIA",
        "INDÃƒÅ¡STRIA"
    ],

    "UNIVERSIDADE":[
        "UNIVERSIDADE",
        "UNIVERSITÃƒÂRIO",
        "UNIVERSITARIA",
        "CENTRO UNIVERSITÃƒÂRIO",
        "CAMPUS"
    ],

    "CENTRO_DE_PESQUISA":[
        "LABORATÃƒâ€œRIO",
        "LABORATORIO",
        "PESQUISA",
        "CIENTÃƒÂFICO",
        "CIENTIFICO",
        "GRUPO DE PESQUISA"
    ],

    "CENTRO_ACADEMICO":[
        "CENTRO ACADÃƒÅ MICO",
        "CENTRO ACADEMICO",
        "DIRETÃƒâ€œRIO ACADÃƒÅ MICO",
        "DIRETORIO ACADEMICO"
    ],

    "Ãƒâ€œRGÃƒÆ'O_PÃƒÅ¡BLICO":[
        "SECRETARIA",
        "PREFEITURA",
        "GOVERNO",
        "MINISTÃƒâ€°RIO",
        "MINISTERIO",
        "TRIBUNAL",
        "FÃƒâ€œRUM",
        "FORUM",
        "ASSEMBLEIA",
        "CÃƒâ€šMARA",
        "CAMARA"
    ],

    "LOCAL_TÃƒâ€°CNICO":[
        "ÃƒÂREA DE CONVIVENCIA",
        "AREA DE CONVIVENCIA",
        "BLOCO",
        "DEPARTAMENTO",
        "AUDITÃƒâ€œRIO",
        "AUDITORIO"
    ]

}

# ==========================================================

summary = {}

for company in companies:

    name = company.get("company_name","").upper()

    org_type = "NÃƒÆ'O_CLASSIFICADO"

    for category, words in RULES.items():

        found = False

        for word in words:

            if word in name:

                org_type = category

                found = True

                break

        if found:
            break

    # ======================================================

    if org_type == "EMPRESA_PRIVADA":

        potential = "ALTO"

    elif org_type == "Ãƒâ€œRGÃƒÆ'O_PÃƒÅ¡BLICO":

        potential = "ALTO"

    elif org_type == "UNIVERSIDADE":

        potential = "MÃƒâ€°DIO"

    elif org_type == "CENTRO_DE_PESQUISA":

        potential = "MÃƒâ€°DIO"

    elif org_type == "CENTRO_ACADEMICO":

        potential = "BAIXO"

    elif org_type == "LOCAL_TÃƒâ€°CNICO":

        potential = "NÃƒÆ'O PRIORITÃƒÂRIO"

    else:

        potential = "BAIXO"

    company["organization_type"] = org_type
    company["commercial_potential"] = potential
    company["classification_date"] = str(datetime.now())

    summary.setdefault(org_type,0)
    summary[org_type]+=1

# ==========================================================

with open(INPUT,"w",encoding="utf-8") as f:

    json.dump(
        companies,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================

print("="*90)
print("IOTEC ORGANIZATION CLASSIFIER ENGINE")
print("="*90)
print()

print("EMPRESAS PROCESSADAS :",len(companies))
print()

print("="*90)
print("RESUMO")
print("="*90)
print()

for key,value in sorted(summary.items()):

    print(f"{key:<25} {value}")

print()

print("="*90)
print("EXEMPLOS")
print("="*90)
print()

for company in companies[:10]:

    print(company["company_name"])

    print("Tipo........:",company["organization_type"])

    print("Potencial...:",company["commercial_potential"])

    print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Identificar")
print("a natureza")
print("organizacional")
print("de cada")
print("entidade")
print("descoberta.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())

print()

print("ORGANIZATION CLASSIFIER OPERACIONAL.")

