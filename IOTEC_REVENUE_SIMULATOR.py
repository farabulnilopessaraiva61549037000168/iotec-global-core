import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC REVENUE SIMULATOR")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

produtos = [

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

cenarios = [

    {
        "nome": "CONSERVADOR",
        "clientes": 5
    },

    {
        "nome": "MODERADO",
        "clientes": 20
    },

    {
        "nome": "EXPANSAO",
        "clientes": 50
    },

    {
        "nome": "ESCALA",
        "clientes": 100
    }
]

print("")
print("CATALOGO:")

for produto in produtos:
    pass

    print(
        f"- {produto['nome']} "
        f"R$ {produto['valor']:,.2f}"
    )

print("")
print("===================================")
print("SIMULACOES")
print("===================================")

for cenario in cenarios:
    pass

    print("")
    print("CENARIO:")
    print(cenario["nome"])

    clientes = cenario["clientes"]

    print(
        f"CLIENTES: {clientes}"
    )

    receita = 0

    for produto in produtos:
        pass

        valor = (
            produto["valor"]
            *
            clientes
        )

        receita += valor

        print(
            f"{produto['nome']} -> "
            f"R$ {valor:,.2f}"
        )

    print("")
    print(
        f"RECEITA TOTAL -> "
        f"R$ {receita:,.2f}"
    )

    print(
        f"RECEITA ANUAL -> "
        f"R$ {(receita * 12):,.2f}"
    )

print("")
print("===================================")
print("FORMULA")
print("===================================")

print("PRODUTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("FATURA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PAGAMENTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("PERGUNTAS DO NUCLEO")

perguntas = [

    "QUANTOS CLIENTES?",

    "QUANTAS PROPOSTAS?",

    "QUANTAS FATURAS?",

    "QUANTO FATURA?",

    "QUAL A RECEITA ANUAL?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("ORDEM MOR:")

print(
    "TRANSFORMAR PRODUTOS "
    "EM CONTRATOS E "
    "CONTRATOS EM RECEITA."
)

print("")
print("SIMULADOR DE RECEITA ATIVO")




