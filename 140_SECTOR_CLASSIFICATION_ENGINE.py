import json
import os
from datetime import datetime

INPUT = "IOTEC_COMPANY_DATABASE.json"
OUTPUT = "IOTEC_COMPANY_DATABASE.json"

# ==========================================================
# CARREGAR
# ==========================================================

if not os.path.exists(INPUT):

    print("Banco de empresas inexistente.")
    raise SystemExit()

with open(INPUT,"r",encoding="utf-8") as f:

    companies = json.load(f)

# ==========================================================
# CLASSIFICADOR
# ==========================================================

classified = 0

for company in companies:

    name = company.get("company_name","").upper()

    segmento = company.get("segmento","").upper()

    setor = "OUTROS"
    subsetor = "NÃƒÆ'O CLASSIFICADO"
    especialidade = ""
    comprador = False
    score = 50

    # ------------------------------------------------------

    if "ENGENHARIA" in name:

        setor = "CONSTRUÃƒâ€¡ÃƒÆ'O"

        comprador = True

        score = 85

        especialidade = "ENGENHARIA"

        subsetor = "ESCRITÃƒâ€œRIO DE ENGENHARIA"

    if "CONSTRUTORA" in name:

        setor = "CONSTRUÃƒâ€¡ÃƒÆ'O"

        subsetor = "CONSTRUTORA"

        especialidade = "CONSTRUÃƒâ€¡ÃƒÆ'O CIVIL"

        comprador = True

        score = 95

    if "EMPREITEIRA" in name:

        setor = "CONSTRUÃƒâ€¡ÃƒÆ'O"

        subsetor = "EMPREITEIRA"

        comprador = True

        score = 95

    if "ARQUITET" in name:

        setor = "CONSTRUÃƒâ€¡ÃƒÆ'O"

        subsetor = "ARQUITETURA"

        especialidade = "ARQUITETURA"

        comprador = True

        score = 90

    # ------------------------------------------------------

    if "HOSPITAL" in name:

        setor = "SAÃƒÅ¡DE"

        subsetor = "HOSPITAL"

        comprador = True

        score = 95

    if "CLINICA" in name or "CLÃƒÂNICA" in name:

        setor = "SAÃƒÅ¡DE"

        subsetor = "CLÃƒÂNICA"

        comprador = True

        score = 90

    if "LABORATORIO" in name or "LABORATÃƒâ€œRIO" in name:

        setor = "SAÃƒÅ¡DE"

        subsetor = "LABORATÃƒâ€œRIO"

        comprador = True

        score = 90

    # ------------------------------------------------------

    if "ESCOLA" in name:

        setor = "EDUCAÃƒâ€¡ÃƒÆ'O"

        subsetor = "ESCOLA"

        comprador = True

        score = 80

    if "UNIVERSIDADE" in name:

        setor = "EDUCAÃƒâ€¡ÃƒÆ'O"

        subsetor = "UNIVERSIDADE"

        comprador = True

        score = 85

    if "SECRETARIA" in name:

        setor = "GOVERNO"

        subsetor = "SECRETARIA"

        comprador = True

        score = 90

    # ------------------------------------------------------

    if "INDUSTRIA" in name or "INDÃƒÅ¡STRIA" in name:

        setor = "INDÃƒÅ¡STRIA"

        subsetor = "INDÃƒÅ¡STRIA"

        comprador = True

        score = 95

    # ------------------------------------------------------

    company["setor"] = setor
    company["subsetor"] = subsetor
    company["especialidade"] = especialidade
    company["comprador_potencial"] = comprador
    company["score_comercial"] = score
    company["ultima_classificacao"] = str(datetime.now())

    classified += 1

# ==========================================================
# SALVAR
# ==========================================================

with open(OUTPUT,"w",encoding="utf-8") as f:

    json.dump(
        companies,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# RELATÃƒâ€œRIO
# ==========================================================

print("="*90)
print("IOTEC SECTOR CLASSIFICATION ENGINE")
print("="*90)
print()

print("EMPRESAS CLASSIFICADAS :",classified)
print()

print("="*90)
print("EXEMPLOS")
print("="*90)
print()

for company in companies[:10]:

    print(company["company_name"])

    print("Setor.........:",company["setor"])

    print("Subsetor......:",company["subsetor"])

    print("Comprador.....:",company["comprador_potencial"])

    print("Score.........:",company["score_comercial"])

    print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Transformar")
print("empresas")
print("em")
print("inteligÃƒÂªncia")
print("comercial.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())

print()

print("SECTOR CLASSIFICATION ENGINE OPERACIONAL.")

