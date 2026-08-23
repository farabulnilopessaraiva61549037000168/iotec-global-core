# ==============================================================================
# 124_CONNECTOR_HUB.py
# IOTEC CONNECTOR HUB
# HUB CORPORATIVO DE CONECTORES
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CONNECTOR HUB")
print("HUB CORPORATIVO DE CONECTORES")
print("="*90)
print()

ARQUIVO="IOTEC_CONTACT_ENRICHMENT_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Banco corporativo nÃƒÂ£o encontrado.")
    raise SystemExit()

EMPRESAS=banco.get("empresas",[])

CONECTORES=[

    {
        "nome":"GOOGLE_MAPS",
        "status":"OFFLINE",
        "capacidade":[
            "SITE",
            "TELEFONE",
            "ENDEREÃƒâ€¡O",
            "AVALIAÃƒâ€¡Ãƒâ€¢ES"
        ]
    },

    {
        "nome":"OPENSTREETMAP",
        "status":"ONLINE",
        "capacidade":[
            "ENDEREÃƒâ€¡O",
            "LOCALIZAÃƒâ€¡ÃƒÆ'O"
        ]
    },

    {
        "nome":"RECEITA_PUBLICA",
        "status":"FUTURO",
        "capacidade":[
            "CNPJ",
            "RAZÃƒÆ'O SOCIAL"
        ]
    },

    {
        "nome":"OPEN_CORPORATES",
        "status":"FUTURO",
        "capacidade":[
            "EMPRESA",
            "DIRETORES"
        ]
    }

]

print("="*90)
print("CONECTORES DISPONÃƒÂVEIS")
print("="*90)
print()

for c in CONECTORES:

    print(c["nome"])

    print("Status.....",c["status"])

    print("Capacidade.")

    for item in c["capacidade"]:

        print("   Ã¢Å"â€œ",item)

    print()

print("="*90)
print("ROTEAMENTO")
print("="*90)
print()

for empresa in EMPRESAS:

    print("="*70)

    print(empresa["empresa"])

    print()

    escolhido=None

    for c in CONECTORES:

        if c["status"]=="ONLINE":

            escolhido=c

            break

    if escolhido:

        empresa["conector"]=escolhido["nome"]

        empresa["status_conector"]="ATRIBUÃƒÂDO"

        print("Conector........",escolhido["nome"])

    else:

        empresa["conector"]=""

        empresa["status_conector"]="SEM CONECTOR"

        print("Nenhum conector disponÃƒÂ­vel.")

    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CONNECTOR_HUB",

    "version":"1.0",

    "conectores":CONECTORES,

    "empresas":EMPRESAS

}

with open(

    "IOTEC_CONNECTOR_ROUTING.json",

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
print("FILOSOFIA")
print("="*90)
print()

print("O Kernel nunca")
print("depende")
print("de um fornecedor.")

print()

print("O Kernel procura")
print("a capacidade.")

print()

print("Se um conector")
print("falhar,")

print("o prÃƒÂ³ximo")

print("assume")

print("automaticamente.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CONNECTOR_ROUTING.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CONNECTOR HUB OPERACIONAL.")

