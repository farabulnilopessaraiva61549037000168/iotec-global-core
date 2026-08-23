import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC PRODUCT CURATOR ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "TRANSFORMAR CAPACIDADES TECNICAS "
    "EM PRODUTOS COMERCIAIS"
)

capacidades = [

    {
        "capacidade":"MODELAGEM_MATEMATICA",
        "compradores":[
            "INDUSTRIAS",
            "AGRONEGOCIO",
            "LOGISTICA"
        ],
        "produto":
        "ANALISE_DE_CENARIOS",
        "ticket":4900
    },

    {
        "capacidade":"CLIMA",
        "compradores":[
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "COOPERATIVAS"
        ],
        "produto":
        "MAPA_DE_RISCO",
        "ticket":2490
    },

    {
        "capacidade":"INTELIGENCIA_COMERCIAL",
        "compradores":[
            "EMPRESAS",
            "COMERCIOS"
        ],
        "produto":
        "PAINEL_EXECUTIVO",
        "ticket":4900
    },

    {
        "capacidade":"AUDITORIA",
        "compradores":[
            "EMPRESAS",
            "ORGAOS_PUBLICOS"
        ],
        "produto":
        "DIAGNOSTICO_ESTRATEGICO",
        "ticket":2990
    },

    {
        "capacidade":"GESTAO_PUBLICA",
        "compradores":[
            "PREFEITURAS",
            "SECRETARIAS"
        ],
        "produto":
        "PLANO_DE_CONTINGENCIA",
        "ticket":8900
    }
]

print("")
print("===================================")
print("CARDAPIO ESTRATEGICO")
print("===================================")

receita_potencial = 0

for item in capacidades:
    pass

    print("")
    print("CAPACIDADE:")
    print(item["capacidade"])

    print("")
    print("COMPRADORES:")

    for comprador in item["compradores"]:
        pass

        print("-", comprador)

    print("")
    print("PRODUTO:")
    print(item["produto"])

    print("")
    print("TICKET:")
    print(
        f'R$ {item["ticket"]:,.2f}'
    )

    receita_potencial += item["ticket"]

print("")
print("===================================")
print("FORMULA DO CHEF")
print("===================================")

print("CAPACIDADE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("COMPRADOR")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("===================================")
print("PERGUNTAS OBRIGATORIAS")
print("===================================")

perguntas = [

    "QUEM SOFRE COM O PROBLEMA?",
    "QUEM TEM ORCAMENTO?",
    "QUEM DECIDE?",
    "QUAL O IMPACTO?",
    "QUAL O CUSTO DE NAO AGIR?",
    "QUAL PRODUTO RESOLVE?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("===================================")
print("RECEITA POTENCIAL DO CARDAPIO")
print("===================================")

print(
    f'R$ {receita_potencial:,.2f}'
)

print("")
print("ORDEM MOR:")
print(
    "NAO VENDER CODIGO. "
    "VENDER SOLUCOES."
)

print("")
print("CHEF ESTRATEGICO ATIVO")




