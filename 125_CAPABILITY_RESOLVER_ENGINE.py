# ==============================================================================
# 125_CAPABILITY_RESOLVER_ENGINE.py
# IOTEC CAPABILITY RESOLVER ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CAPABILITY RESOLVER ENGINE")
print("RESOLVEDOR CORPORATIVO DE CAPACIDADES")
print("="*90)
print()

ARQUIVO="IOTEC_CONNECTOR_ROUTING.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        banco=json.load(f)

except:

    print("Routing nÃƒÂ£o encontrado.")
    raise SystemExit()

EMPRESAS=banco.get("empresas",[])
CONECTORES=banco.get("conectores",[])

CAPACIDADES=[

    "SITE",
    "TELEFONE",
    "EMAIL",
    "ENDEREÃƒâ€¡O",
    "CNPJ",
    "LINKEDIN",
    "DIRETORES"

]

print("="*90)
print("RESOLUÃƒâ€¡ÃƒÆ'O DE CAPACIDADES")
print("="*90)
print()

for empresa in EMPRESAS:

    print("="*70)
    print(empresa["empresa"])
    print()

    empresa["capacidades"]={}

    for capacidade in CAPACIDADES:

        fornecedor=""

        for conector in CONECTORES:

            if conector["status"]!="ONLINE":
                continue

            if capacidade in conector["capacidade"]:

                fornecedor=conector["nome"]
                break

        empresa["capacidades"][capacidade]=fornecedor

        print(f"{capacidade:12} -> {fornecedor if fornecedor else 'SEM FORNECEDOR'}")

    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CAPABILITY_RESOLVER",

    "version":"1.0",

    "empresas":EMPRESAS

}

with open(

    "IOTEC_CAPABILITY_ROUTING.json",

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

print("O Kernel")
print("nÃƒÂ£o procura")
print("APIs.")

print()

print("O Kernel")
print("procura")
print("capacidades.")

print()

print("As capacidades")
print("escolhem")
print("automaticamente")
print("o fornecedor.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CAPABILITY_ROUTING.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CAPABILITY RESOLVER OPERACIONAL.")

