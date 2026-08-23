$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "============================================================"
Write-Host " IOTEC RECOVERY - COVERAGE SYNCHRONIZER"
Write-Host "============================================================"
Write-Host ""

$pythonFile = "139_COVERAGE_SYNCHRONIZER.py"

if(Test-Path $pythonFile){

    Copy-Item `
        $pythonFile `
        "$pythonFile.bak" `
        -Force

    Write-Host "Backup criado."
}

@'
import json
import os
from datetime import datetime

WORLD_MAP_FILE = "IOTEC_WORLD_MAP.json"
COMPANY_FILE = "IOTEC_COMPANY_DATABASE.json"

# ==========================================================

def load_json(file):

    if not os.path.exists(file):
        return []

    try:

        with open(file,"r",encoding="utf-8") as f:

            data=json.load(f)

            if isinstance(data,list):
                return data

            return []

    except Exception:

        return []

# ==========================================================

world = load_json(WORLD_MAP_FILE)

companies = load_json(COMPANY_FILE)

# ==========================================================

for node in world:

    node["companies"]=0

    node["coverage"]=0

# ==========================================================

matched = 0

for company in companies:

    city = str(
        company.get("city","")
    ).strip().lower()

    segmento = str(
        company.get("segmento","")
    ).strip().upper()

    sector = None

    if "ENGENHARIA" in segmento:
        sector="Engenharia"

    elif "ARQUITETURA" in segmento:
        sector="Arquitetura"

    elif "CONSTRU" in segmento:
        sector="Construção"

    elif "EDUC" in segmento:
        sector="Educação"

    elif "SAÚDE" in segmento or "SAUDE" in segmento:
        sector="Saúde"

    elif "TECNOLOGIA" in segmento:
        sector="Tecnologia"

    elif "INDÚSTRIA" in segmento or "INDUSTRIA" in segmento:
        sector="Indústria"

    elif "AGRO" in segmento:
        sector="Agronegócio"

    if sector is None:
        continue

    for node in world:

        if (
            node["city"].strip().lower()==city
            and
            node["sector"]==sector
        ):

            node["companies"]+=1

            matched+=1

            break

# ==========================================================

MAX_COMPANIES = 50

for node in world:

    cov = (
        node["companies"] /
        MAX_COMPANIES
    )*100

    if cov>100:
        cov=100

    node["coverage"]=round(cov,1)

# ==========================================================

with open(
    WORLD_MAP_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        world,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================

ranking = sorted(
    world,
    key=lambda x:x["coverage"],
    reverse=True
)

print("="*90)
print("IOTEC COVERAGE SYNCHRONIZER")
print("="*90)
print()

print("Empresas analisadas :",len(companies))
print("Empresas sincronizadas :",matched)
print()

print("="*90)
print("TOP COBERTURA")
print("="*90)
print()

for node in ranking:

    if node["companies"]==0:
        continue

    print(
        f'{node["country"]} | '
        f'{node["city"]} | '
        f'{node["sector"]}'
    )

    print(
        "Empresas :",
        node["companies"]
    )

    print(
        "Cobertura:",
        f'{node["coverage"]}%'
    )

    print()

print("="*90)
print("RESUMO")
print("="*90)

covered = sum(
    1
    for n in world
    if n["companies"]>0
)

print("Nós econômicos :",len(world))
print("Nós cobertos   :",covered)

print("Data :",datetime.now())

print()

print("COVERAGE SYNCHRONIZER OPERACIONAL")
'@ | Set-Content `
        $pythonFile `
        -Encoding UTF8

Write-Host ""
Write-Host "Arquivo reconstruído."
Write-Host ""

python $pythonFile

Write-Host ""
Write-Host "============================================================"
Write-Host " FINALIZADO "
Write-Host "============================================================"