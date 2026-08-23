import json
from datetime import datetime

# ==========================================================
# IOTEC GLOBAL MARKET MAPPER
# ==========================================================

MARKETS = {

    "Brasil":{

        "ConstruÃƒÂ§ÃƒÂ£o":{

            "subsetores":[

                "Construtoras",
                "Empreiteiras",
                "Engenharia Civil",
                "Arquitetura",
                "Urbanismo",
                "Infraestrutura"

            ]

        },

        "EducaÃƒÂ§ÃƒÂ£o":{

            "subsetores":[

                "Escolas",
                "Universidades",
                "Institutos",
                "Secretarias de EducaÃƒÂ§ÃƒÂ£o",
                "Editoras"

            ]

        },

        "SaÃƒÂºde":{

            "subsetores":[

                "Hospitais",
                "ClÃƒÂ­nicas",
                "LaboratÃƒÂ³rios",
                "Operadoras"

            ]

        },

        "IndÃƒÂºstria":{

            "subsetores":[

                "Metalurgia",
                "Alimentos",
                "QuÃƒÂ­mica",
                "Automotiva",
                "Energia"

            ]

        }

    },

    "Estados Unidos":{

        "Technology":{

            "subsetores":[

                "Software",
                "Artificial Intelligence",
                "Cybersecurity",
                "Cloud Computing"

            ]

        },

        "Healthcare":{

            "subsetores":[

                "Hospitals",
                "Medical AI",
                "Medical Devices"

            ]

        }

    },

    "Portugal":{

        "Tecnologia":{

            "subsetores":[

                "Software",
                "Consultoria",
                "Cloud"

            ]

        }

    }

}


# ==========================================================

saida=[]

for pais in MARKETS:

    for setor in MARKETS[pais]:

        saida.append({

            "country":pais,

            "sector":setor,

            "subsectors":MARKETS[pais][setor]["subsetores"],

            "companies":0,

            "products":0,

            "market_score":0,

            "priority":"PENDING"

        })


with open(

    "IOTEC_GLOBAL_MARKET_MAP.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )


print("="*90)
print("IOTEC GLOBAL MARKET MAPPER")
print("="*90)
print()

print("PAÃƒÂSES")

print("-"*90)

for pais in MARKETS:

    print()

    print(pais)

    for setor in MARKETS[pais]:

        print("   >",setor)

print()

print("="*90)
print("MERCADOS MAPEADOS")
print("="*90)
print()

print("Total :",len(saida))

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Organizar")

print("a economia")

print("mundial")

print("em setores")

print("e subsetores.")

print()

print("Cada setor")

print("passarÃƒÂ¡")

print("a receber")

print("empresas")

print("produtos")

print("oportunidades")

print("e indicadores.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print("Boa noite, Presidente.")
print()

print("O Mercado Global")

print("passa a ser")

print("organizado")

print("por paÃƒÂ­ses")

print("setores")

print("e especializaÃƒÂ§ÃƒÂµes.")

print()

print("As prÃƒÂ³ximas")

print("missÃƒÂµes")

print("consistirÃƒÂ£o")

print("em preencher")

print("automaticamente")

print("cada setor")

print("com empresas")

print("reais.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Mercados :",len(saida))

print("Data :",datetime.now())

print()

print("GLOBAL MARKET MAPPER OPERACIONAL.")

