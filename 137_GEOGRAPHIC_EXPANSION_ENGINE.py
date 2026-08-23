import json
import os
import uuid
from datetime import datetime

OUTPUT = "IOTEC_WORLD_MAP.json"

# ==========================================================
# MAPA ECONÃƒâ€MICO INICIAL
# ==========================================================

WORLD = {

    "Brasil":{

        "CearÃƒÂ¡":[

            "Fortaleza",

            "Sobral",

            "Juazeiro do Norte",

            "QuixadÃƒÂ¡",

            "MaracanaÃƒÂº"

        ],

        "SÃƒÂ£o Paulo":[

            "SÃƒÂ£o Paulo",

            "Campinas",

            "Santos"

        ]

    },

    "Portugal":{

        "Lisboa":[

            "Lisboa"

        ]

    },

    "Estados Unidos":{

        "Florida":[

            "Miami",

            "Orlando"

        ],

        "Texas":[

            "Houston",

            "Dallas"

        ]

    }

}

SECTORS=[

    "ConstruÃƒÂ§ÃƒÂ£o",

    "Arquitetura",

    "Engenharia",

    "EducaÃƒÂ§ÃƒÂ£o",

    "SaÃƒÂºde",

    "IndÃƒÂºstria",

    "Tecnologia",

    "AgronegÃƒÂ³cio"

]

tree=[]

# ==========================================================

for country,states in WORLD.items():

    for state,cities in states.items():

        for city in cities:

            for sector in SECTORS:

                tree.append({

                    "node_id":str(uuid.uuid4())[:8],

                    "country":country,

                    "state":state,

                    "city":city,

                    "sector":sector,

                    "coverage":0,

                    "companies":0,

                    "contacts":0,

                    "customers":0,

                    "revenue":0,

                    "status":"PENDENTE"

                })

# ==========================================================

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        tree,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================

print("="*90)
print("IOTEC GEOGRAPHIC EXPANSION ENGINE")
print("="*90)
print()

print("NÃƒâ€œS GERADOS :",len(tree))
print()

print("="*90)
print("EXEMPLOS")
print("="*90)
print()

for item in tree[:15]:

    print(

        item["country"],

        "-",

        item["city"],

        "-",

        item["sector"]

    )

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Construir")
print("o mapa")
print("econÃƒÂ´mico")
print("mundial")
print("da")
print("IOTEC.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print(datetime.now())

print()

print("GEOGRAPHIC EXPANSION ENGINE OPERACIONAL.")

