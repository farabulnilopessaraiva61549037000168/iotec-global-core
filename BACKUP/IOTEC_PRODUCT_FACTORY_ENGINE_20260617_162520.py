import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC PRODUCT FACTORY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "TRANSFORMAR OPORTUNIDADES "
    "EM PRODUTOS COMERCIAIS"
)

oportunidades = {

    "ESTIAGEM": {

        "compradores": [

            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SECRETARIAS_ESTADUAIS",
            "COOPERATIVAS"
        ],

        "produtos": [

            {
                "nome": "MAPA_DE_RISCO",
                "valor": 2490
            },

            {
                "nome": "PLANO_DE_CONTINGENCIA",
                "valor": 4900
            },

            {
                "nome": "ANALISE_DE_CENARIOS",
                "valor": 8900
            },

            {
                "nome": "PAINEL_EXECUTIVO",
                "valor": 12900
            }
        ]
    },

    "ENCHENTE": {

        "compradores": [

            "PREFEITURAS",
            "DEFESA_CIVIL",
            "SEGURADORAS"
        ],

        "produtos": [

            {
                "nome": "MAPA_DE_VULNERABILIDADE",
                "valor": 2490
            },

            {
                "nome": "PLANO_DE_EMERGENCIA",
                "valor": 4900
            }
        ]
    }
}

print("")
print("===================================")
print("CATALOGO GERADO")
print("===================================")

receita_total = 0

for oportunidade, dados in oportunidades.items():
    pass

    print("")
    print("OPORTUNIDADE:")
    print(oportunidade)

    print("")
    print("COMPRADORES:")

    for comprador in dados["compradores"]:
        pass

        print("-", comprador)

    print("")
    print("PRODUTOS:")

    subtotal = 0

    for produto in dados["produtos"]:
        pass

        print(
            f"- {produto['nome']} "
            f"R$ {produto['valor']:,.2f}"
        )

        subtotal += produto["valor"]

    receita_total += subtotal

    print("")
    print(
        "POTENCIAL DE PORTFOLIO:"
    )

    print(
        f"R$ {subtotal:,.2f}"
    )

print("")
print("===================================")
print("FORMULA INDUSTRIAL")
print("===================================")

print("FONTE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("SINAL")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("OPORTUNIDADE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("FATURA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("===================================")
print("PERGUNTAS DO NUCLEO")
print("===================================")

perguntas = [

    "QUAL PROBLEMA FOI DETECTADO?",

    "QUAIS PRODUTOS PODEM NASCER?",

    "QUEM COMPRA?",

    "QUAL O PRECO?",

    "QUAL O FATURAMENTO POSSIVEL?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("===================================")
print("RECEITA POTENCIAL")
print("===================================")

print(
    f"R$ {receita_total:,.2f}"
)

print("")
print("ORDEM MOR:")

print(
    "TODO PROBLEMA RELEVANTE "
    "DEVE GERAR PRODUTOS, "
    "PROPOSTAS E RECEITA."
)

print("")
print("FABRICA DE PRODUTOS ATIVA")


