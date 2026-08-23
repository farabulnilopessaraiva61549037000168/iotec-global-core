import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC MARKET DISCOVERY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "IDENTIFICAR PROBLEMAS, "
    "COMPRADORES E PRODUTOS "
    "COM POTENCIAL DE RECEITA"
)

problemas = {

    "ESTIAGEM": {
        "compradores": [
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SECRETARIAS_ESTADUAIS",
            "COOPERATIVAS"
        ],
        "produtos": [
            "PLANO_DE_CONTINGENCIA",
            "MAPA_DE_RISCO",
            "ANALISE_DE_CENARIOS"
        ]
    },

    "ENCHENTE": {
        "compradores": [
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SEGURADORAS"
        ],
        "produtos": [
            "MAPA_DE_VULNERABILIDADE",
            "PLANO_DE_EMERGENCIA"
        ]
    },

    "LOGISTICA": {
        "compradores": [
            "INDUSTRIAS",
            "TRANSPORTADORAS",
            "COMERCIOS"
        ],
        "produtos": [
            "OTIMIZACAO_DE_ROTAS",
            "PAINEL_EXECUTIVO"
        ]
    }
}

print("")
print("===================================")
print("MERCADOS IDENTIFICADOS")
print("===================================")

for problema, dados in problemas.items():
    pass

    print("")
    print("PROBLEMA:")
    print(problema)

    print("")
    print("COMPRADORES:")

    for comprador in dados["compradores"]:
        print("-", comprador)

    print("")
    print("PRODUTOS:")

    for produto in dados["produtos"]:
        print("-", produto)

print("")
print("===================================")
print("LOGICA DE MERCADO")
print("===================================")

print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("IMPACTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("COMPRADOR")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("ORCAMENTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("PERGUNTAS OBRIGATORIAS")

perguntas = [

    "QUEM SOFRE COM O PROBLEMA?",

    "QUEM TEM ORCAMENTO?",

    "QUEM DECIDE?",

    "QUAL O CUSTO DE NAO AGIR?",

    "QUAL O CUSTO DE AGIR?",

    "QUAL PRODUTO RESOLVE?"
]

for pergunta in perguntas:
    print("-", pergunta)

print("")
print("ORDEM MOR:")

print(
    "TODO PROBLEMA COM IMPACTO, "
    "COMPRADOR E ORCAMENTO "
    "PODE GERAR RECEITA."
)

print("")
print("NUCLEO DE DESCOBERTA DE MERCADO ATIVO")


