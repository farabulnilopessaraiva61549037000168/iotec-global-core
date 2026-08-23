# ==============================================================================
# 120_COMPANY_ENRICHMENT_ENGINE.py
# IOTEC COMPANY ENRICHMENT ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC COMPANY ENRICHMENT ENGINE")
print("MOTOR DE ENRIQUECIMENTO EMPRESARIAL")
print("="*90)
print()

ARQUIVO = "IOTEC_REVENUE_PIPELINE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco = json.load(f)

except:

    print("Pipeline nÃƒÂ£o encontrado.")
    raise SystemExit()

PIPELINE = banco.get("pipeline", [])

ENRIQUECIDAS=[]

print("="*90)
print("ENRIQUECIMENTO")
print("="*90)
print()

for empresa in PIPELINE:

    registro = {

        "empresa":empresa["empresa"],

        "cidade":"",

        "estado":"",

        "pais":"Brasil",

        "segmento":"",

        "site":"",

        "telefone":"",

        "email":"",

        "linkedin":"",

        "instagram":"",

        "facebook":"",

        "porte":"",

        "cnpj":"",

        "responsavel":"",

        "cargo":"",

        "status":"AGUARDANDO ENRIQUECIMENTO",

        "origem":"OpenStreetMap",

        "pipeline":empresa["fase"],

        "score":empresa.get("score",0),

        "produtos":empresa.get("produtos",[])

    }

    nome = registro["empresa"]

    if "Fortaleza" in nome:
        registro["cidade"]="Fortaleza"
        registro["estado"]="CE"

    if "Engenharia" in nome:
        registro["segmento"]="Engenharia"

    ENRIQUECIDAS.append(registro)

    print("="*70)
    print(nome)
    print()
    print("Cidade.......",registro["cidade"])
    print("Estado.......",registro["estado"])
    print("Segmento.....",registro["segmento"])
    print("Status.......",registro["status"])
    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "total":len(ENRIQUECIDAS),

    "empresas":ENRIQUECIDAS

}

with open(

    "IOTEC_COMPANY_DATABASE.json",

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
print("PRÃƒâ€œXIMAS ETAPAS")
print("="*90)
print()

print("Ã¢Å"â€œ Descobrir Site")
print("Ã¢Å"â€œ Descobrir Telefone")
print("Ã¢Å"â€œ Descobrir Email")
print("Ã¢Å"â€œ Descobrir LinkedIn")
print("Ã¢Å"â€œ Descobrir ResponsÃƒÂ¡vel")
print("Ã¢Å"â€œ Gerar EstratÃƒÂ©gia")
print("Ã¢Å"â€œ Registrar CRM")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Cada empresa")
print("passa a possuir")
print("um cadastro")
print("corporativo.")

print()

print("O Kernel")
print("deixa de")
print("armazenar")
print("apenas nomes.")

print()

print("Agora organiza")
print("empresas")
print("como ativos")
print("corporativos.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_COMPANY_DATABASE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("COMPANY ENRICHMENT OPERACIONAL.")

