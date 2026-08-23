# ==============================================================================
# 118_CORPORATE_EVOLUTION_ENGINE.py
# IOTEC CORPORATE EVOLUTION ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CORPORATE EVOLUTION ENGINE")
print("MOTOR DE EVOLUÃƒâ€¡ÃƒÆ'O CORPORATIVA")
print("="*90)
print()

ARQUIVO="IOTEC_CORPORATE_PATRIMONY.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        patrimonio=json.load(f)

except:

    print("PatrimÃƒÂ´nio nÃƒÂ£o encontrado.")
    raise SystemExit()

indices=patrimonio["indices"]

print("="*90)
print("ANÃƒÂLISE CORPORATIVA")
print("="*90)
print()

PLANO=[]

for area,indice in indices.items():

    print(f"{area:20} {indice}%")

    if indice < 40:

        PLANO.append({

            "prioridade":"CRÃƒÂTICA",

            "ÃƒÂ¡rea":area,

            "aÃƒÂ§ÃƒÂ£o":"Investimento imediato"

        })

    elif indice < 70:

        PLANO.append({

            "prioridade":"ALTA",

            "ÃƒÂ¡rea":area,

            "aÃƒÂ§ÃƒÂ£o":"Expandir capacidades"

        })

    else:

        PLANO.append({

            "prioridade":"ESTÃƒÂVEL",

            "ÃƒÂ¡rea":area,

            "aÃƒÂ§ÃƒÂ£o":"Manter evoluÃƒÂ§ÃƒÂ£o"

        })

print()

print("="*90)
print("PLANO DE EVOLUÃƒâ€¡ÃƒÆ'O")
print("="*90)
print()

for item in PLANO:

    print(f"[{item['prioridade']}] {item['ÃƒÂ¡rea']}")

    print("AÃƒÂ§ÃƒÂ£o :",item["aÃƒÂ§ÃƒÂ£o"])

    print()

with open(

    "IOTEC_EVOLUTION_PLAN.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        {

            "generated_at":datetime.now().isoformat(),

            "plano":PLANO

        },

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("CONCLUSÃƒÆ'O DO KERNEL")
print("="*90)
print()

print("A empresa deixa")
print("de evoluir")
print("por percepÃƒÂ§ÃƒÂ£o.")

print()

print("Agora evolui")

print("pelos indicadores")

print("corporativos.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_EVOLUTION_PLAN.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("EVOLUTION ENGINE OPERACIONAL.")


