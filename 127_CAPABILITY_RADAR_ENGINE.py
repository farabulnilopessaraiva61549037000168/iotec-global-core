# ==============================================================================
# 127_CAPABILITY_RADAR_ENGINE.py
# IOTEC CAPABILITY RADAR ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CAPABILITY RADAR ENGINE")
print("RADAR CORPORATIVO DE CAPACIDADES")
print("="*90)
print()

ARQUIVO="IOTEC_CONNECTOR_CATALOG.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("CatÃƒÂ¡logo nÃƒÂ£o encontrado.")
    raise SystemExit()

catalogo=banco["catalogo"]

print("="*90)
print("RADAR")
print("="*90)
print()

resumo=[]

for capacidade,lista in catalogo.items():

    total=len(lista)

    online=0
    offline=0
    futuro=0

    for item in lista:

        status=item["status"]

        if status=="ONLINE":
            online+=1

        elif status=="OFFLINE":
            offline+=1

        else:
            futuro+=1

    cobertura=round((online/total)*100,1)

    resumo.append({

        "capacidade":capacidade,
        "total":total,
        "online":online,
        "offline":offline,
        "futuro":futuro,
        "cobertura":cobertura

    })

    barra="Ã¢â€"Ë†"*int(cobertura/5)

    print(f"{capacidade:15} {barra:20} {cobertura}%")

print()

print("="*90)
print("PRIORIDADES")
print("="*90)
print()

for item in sorted(resumo,key=lambda x:x["cobertura"]):

    if item["cobertura"]==0:

        print(f"Ã°Å¸â€Â´ {item['capacidade']}")

    elif item["cobertura"]<50:

        print(f"Ã°Å¸Å¸Â¡ {item['capacidade']}")

    else:

        print(f"Ã°Å¸Å¸Â¢ {item['capacidade']}")

print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CAPABILITY_RADAR",

    "version":"1.0",

    "capacidades":resumo

}

with open(

    "IOTEC_CAPABILITY_RADAR.json",

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

print("O Kernel observa")
print("continuamente")
print("a cobertura")
print("das capacidades.")

print()

print("As prioridades")
print("sÃƒÂ£o definidas")
print("pelas lacunas")
print("do ecossistema.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CAPABILITY_RADAR.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CAPABILITY RADAR OPERACIONAL.")

