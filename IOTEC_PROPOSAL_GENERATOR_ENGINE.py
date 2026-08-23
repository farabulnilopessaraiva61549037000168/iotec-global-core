import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC PROPOSAL GENERATOR ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "TRANSFORMAR OPORTUNIDADES "
    "EM PROPOSTAS COMERCIAIS"
)

alvos = [

    {
        "cliente":"PREFEITURA_A",

        "problema":"ESTIAGEM",

        "produto":
        "PLANO_DE_CONTINGENCIA",

        "valor":8900,

        "prazo":"30 DIAS",

        "score":36
    },

    {
        "cliente":"INDUSTRIA_C",

        "problema":"LOGISTICA",

        "produto":
        "OTIMIZACAO_DE_ROTAS",

        "valor":12900,

        "prazo":"45 DIAS",

        "score":32
    },

    {
        "cliente":"COOPERATIVA_B",

        "problema":"ESTIAGEM",

        "produto":
        "MAPA_DE_RISCO",

        "valor":2490,

        "prazo":"15 DIAS",

        "score":31
    }
]

alvos = sorted(
    alvos,
    key=lambda x: x["score"],
    reverse=True
)

principal = alvos[0]

print("")
print("===================================")
print("ALVO PRIORITARIO")
print("===================================")

print("CLIENTE:")
print(principal["cliente"])

print("")
print("PROBLEMA:")
print(principal["problema"])

print("")
print("PRODUTO:")
print(principal["produto"])

print("")
print("VALOR:")
print(
    f'R$ {principal["valor"]:,.2f}'
)

print("")
print("PRAZO:")
print(principal["prazo"])

print("")
print("SCORE:")
print(principal["score"])

print("")
print("===================================")
print("PROPOSTA EXECUTIVA")
print("===================================")

print("")
print("OBJETIVO:")

if principal["problema"] == "ESTIAGEM":
    pass

    entregaveis = [

        "MAPA_DE_RISCO",
        "ANALISE_DE_CENARIOS",
        "PLANO_DE_CONTINGENCIA",
        "PAINEL_EXECUTIVO"
    ]

    print(
        "REDUZIR IMPACTOS "
        "DA ESTIAGEM "
        "E MELHORAR A "
        "CAPACIDADE DE RESPOSTA."
    )

elif principal["problema"] == "LOGISTICA":
    pass

    entregaveis = [

        "MAPA_OPERACIONAL",
        "OTIMIZACAO_DE_ROTAS",
        "SIMULACAO_DE_CENARIOS",
        "PAINEL_EXECUTIVO"
    ]

    print(
        "OTIMIZAR CUSTOS "
        "E MELHORAR "
        "A EFICIENCIA LOGISTICA."
    )

else:
    pass

    entregaveis = [

        "DIAGNOSTICO",
        "PAINEL_EXECUTIVO"
    ]

print("")
print("ENTREGAVEIS:")

for item in entregaveis:
    pass

    print("-", item)

print("")
print("INVESTIMENTO:")
print(
    f'R$ {principal["valor"]:,.2f}'
)

print("")
print("PRAZO DE ENTREGA:")
print(principal["prazo"])

print("")
print("===================================")
print("FORMULA COMERCIAL")
print("===================================")

print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("SOLUCAO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTO")
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

    "QUAL O PROBLEMA?",
    "QUAL O IMPACTO?",
    "QUAL A SOLUCAO?",
    "QUEM DECIDE?",
    "QUAL O INVESTIMENTO?",
    "QUAL O PRAZO?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("ORDEM MOR:")
print(
    "TODA OPORTUNIDADE "
    "DEVE VIRAR UMA "
    "PROPOSTA COMERCIAL."
)

print("")
print("PROPOSAL GENERATOR ENGINE ATIVO")




