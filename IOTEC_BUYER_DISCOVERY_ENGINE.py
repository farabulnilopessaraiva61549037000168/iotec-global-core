import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC BUYER DISCOVERY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "IDENTIFICAR COMPRADORES "
    "PARA CADA OPORTUNIDADE"
)

mercados = [

    {
        "problema":"ESTIAGEM",

        "compradores":[
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SECRETARIA_RECURSOS_HIDRICOS",
            "COOPERATIVAS"
        ],

        "decisores":[
            "PREFEITO",
            "SECRETARIO",
            "COORDENADOR",
            "DIRETOR"
        ],

        "produto":
        "PLANO_DE_CONTINGENCIA"
    },

    {
        "problema":"ENCHENTE",

        "compradores":[
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SEGURADORAS"
        ],

        "decisores":[
            "PREFEITO",
            "GERENTE_DE_RISCO",
            "COORDENADOR"
        ],

        "produto":
        "MAPA_DE_VULNERABILIDADE"
    },

    {
        "problema":"LOGISTICA",

        "compradores":[
            "TRANSPORTADORAS",
            "INDUSTRIAS",
            "COMERCIOS"
        ],

        "decisores":[
            "DIRETOR",
            "GERENTE_OPERACIONAL"
        ],

        "produto":
        "OTIMIZACAO_DE_ROTAS"
    },

    {
        "problema":"GESTAO_FINANCEIRA",

        "compradores":[
            "EMPRESAS",
            "COOPERATIVAS",
            "INSTITUICOES"
        ],

        "decisores":[
            "CEO",
            "DIRETOR_FINANCEIRO",
            "CONTROLADOR"
        ],

        "produto":
        "PAINEL_EXECUTIVO"
    }
]

print("")
print("===================================")
print("MAPA DE COMPRADORES")
print("===================================")

for mercado in mercados:
    pass

    print("")
    print("PROBLEMA:")
    print(mercado["problema"])

    print("")
    print("PRODUTO:")
    print(mercado["produto"])

    print("")
    print("COMPRADORES:")

    for comprador in mercado["compradores"]:
        print("-", comprador)

    print("")
    print("DECISORES:")

    for decisor in mercado["decisores"]:
        print("-", decisor)

print("")
print("===================================")
print("FORMULA COMERCIAL")
print("===================================")

print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("COMPRADOR")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("DECISOR")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("CONTRATO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("===================================")
print("PERGUNTAS DO NUCLEO")
print("===================================")

perguntas = [

    "QUEM SOFRE COM O PROBLEMA?",
    "QUEM POSSUI ORCAMENTO?",
    "QUEM ASSINA O CONTRATO?",
    "QUEM DECIDE A COMPRA?",
    "QUAL PRODUTO RESOLVE?"
]

for pergunta in perguntas:
    print("-", pergunta)

print("")
print("ORDEM MOR:")
print(
    "TODO PRODUTO PRECISA TER "
    "UM COMPRADOR E UM DECISOR."
)

print("")
print("BUYER DISCOVERY ENGINE ATIVO")




