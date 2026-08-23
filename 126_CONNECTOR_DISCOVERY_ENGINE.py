# ==============================================================================
# 126_CONNECTOR_DISCOVERY_ENGINE.py
# IOTEC CONNECTOR DISCOVERY ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CONNECTOR DISCOVERY ENGINE")
print("CATÃƒÂLOGO CORPORATIVO DE CONECTORES")
print("="*90)
print()

CAPACIDADES = {

    "SITE":[

        {
            "nome":"GOOGLE_MAPS",
            "status":"OFFLINE",
            "prioridade":1
        },

        {
            "nome":"OPEN_CORPORATES",
            "status":"FUTURO",
            "prioridade":2
        },

        {
            "nome":"BING_SEARCH",
            "status":"FUTURO",
            "prioridade":3
        }

    ],

    "ENDERECO":[

        {
            "nome":"OPENSTREETMAP",
            "status":"ONLINE",
            "prioridade":1
        },

        {
            "nome":"GOOGLE_MAPS",
            "status":"OFFLINE",
            "prioridade":2
        }

    ],

    "EMAIL":[

        {
            "nome":"SITE_OFICIAL",
            "status":"FUTURO",
            "prioridade":1
        },

        {
            "nome":"OPEN_CORPORATES",
            "status":"FUTURO",
            "prioridade":2
        }

    ],

    "TELEFONE":[

        {
            "nome":"SITE_OFICIAL",
            "status":"FUTURO",
            "prioridade":1
        },

        {
            "nome":"GOOGLE_MAPS",
            "status":"OFFLINE",
            "prioridade":2
        }

    ],

    "LINKEDIN":[

        {
            "nome":"LINKEDIN_CONNECTOR",
            "status":"FUTURO",
            "prioridade":1
        }

    ],

    "CNPJ":[

        {
            "nome":"RECEITA_PUBLICA",
            "status":"FUTURO",
            "prioridade":1
        }

    ],

    "DIRETORES":[

        {
            "nome":"OPEN_CORPORATES",
            "status":"FUTURO",
            "prioridade":1
        }

    ]

}

print("="*90)
print("COBERTURA DAS CAPACIDADES")
print("="*90)
print()

TOTAL=0
ONLINE=0

for capacidade,lista in CAPACIDADES.items():

    print(capacidade)

    print("-"*60)

    for item in lista:

        TOTAL+=1

        if item["status"]=="ONLINE":
            ONLINE+=1

        print(

            f'{item["prioridade"]}. '

            f'{item["nome"]:25} '

            f'{item["status"]}'

        )

    print()

COBERTURA = round((ONLINE/TOTAL)*100,2)

print("="*90)
print("INDICADORES")
print("="*90)
print()

print("Capacidades........",len(CAPACIDADES))
print("Conectores.........",TOTAL)
print("Online.............",ONLINE)
print("Cobertura..........",f"{COBERTURA}%")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("A IOTEC")
print("nÃƒÂ£o depende")
print("de APIs.")

print()

print("A IOTEC")
print("mantÃƒÂ©m")
print("um catÃƒÂ¡logo")
print("de capacidades.")

print()

print("Sempre existe")
print("uma segunda")
print("alternativa.")

print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CONNECTOR_DISCOVERY_ENGINE",

    "version":"1.0",

    "capacidade_total":len(CAPACIDADES),

    "conectores_total":TOTAL,

    "online":ONLINE,

    "cobertura":COBERTURA,

    "catalogo":CAPACIDADES

}

with open(

    "IOTEC_CONNECTOR_CATALOG.json",

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
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CONNECTOR_CATALOG.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CONNECTOR DISCOVERY OPERACIONAL.")

