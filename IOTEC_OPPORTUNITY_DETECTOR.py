import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC OPPORTUNITY DETECTOR")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

EVENTOS = [

    "ESTIAGEM",

    "ENCHENTE",

    "CRISE_HIDRICA",

    "AUMENTO_DE_CUSTOS",

    "QUEDA_DE_PRODUCAO",

    "CRESCIMENTO_POPULACIONAL"
]

BASE = {

    "ESTIAGEM": {

        "setores": [
            "AGRICULTURA",
            "PECUARIA",
            "ABASTECIMENTO",
            "TRANSPORTE"
        ],

        "compradores": [
            "PREFEITURAS",
            "DEFESA_CIVIL",
            "COOPERATIVAS"
        ],

        "produtos": [
            "MAPA_DE_RISCO",
            "PLANO_DE_CONTINGENCIA",
            "ANALISE_DE_CENARIOS"
        ]
    },

    "ENCHENTE": {

        "setores": [
            "INFRAESTRUTURA",
            "TRANSPORTE",
            "HABITACAO"
        ],

        "compradores": [
            "PREFEITURAS",
            "SEGURADORAS"
        ],

        "produtos": [
            "MAPA_DE_VULNERABILIDADE",
            "PLANO_DE_EMERGENCIA"
        ]
    }
}

print("")
print("===================================")
print("OPORTUNIDADES DETECTADAS")
print("===================================")

for evento in EVENTOS:
    pass

    if evento not in BASE:
        continue

    dados = BASE[evento]

    print("")
    print("EVENTO:")
    print(evento)

    print("")
    print("SETORES AFETADOS:")

    for setor in dados["setores"]:
        print("-", setor)

    print("")
    print("COMPRADORES:")

    for comprador in dados["compradores"]:
        print("-", comprador)

    print("")
    print("PRODUTOS POSSIVEIS:")

    for produto in dados["produtos"]:
        print("-", produto)

    potencial = (
        len(dados["setores"])
        *
        len(dados["compradores"])
        *
        len(dados["produtos"])
    )

    print("")
    print("INDICE DE OPORTUNIDADE:")
    print(potencial)

print("")
print("===================================")
print("LOGICA DO NUCLEO")
print("===================================")

print("EVENTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("IMPACTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("SETORES")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("COMPRADORES")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTOS")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("PERGUNTA ESTRATEGICA:")

print(
    "QUAIS PROBLEMAS POSSUEM "
    "MAIOR POTENCIAL DE MERCADO?"
)

print("")
print("NUCLEO DETECTOR DE OPORTUNIDADES ATIVO")




