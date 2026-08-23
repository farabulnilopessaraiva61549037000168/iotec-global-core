import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC CONVERSION INTELLIGENCE ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "MEDIR O QUE ESTA "
    "GERANDO LEADS, "
    "PROPOSTAS E RECEITA"
)

ativos = [

    {
        "nome":"VIDEO_ESTIAGEM",
        "canal":"LINKEDIN",
        "visitas":500,
        "leads":12,
        "propostas":4,
        "contratos":1,
        "receita":8900
    },

    {
        "nome":"PAINEL_EXECUTIVO",
        "canal":"SITE",
        "visitas":300,
        "leads":20,
        "propostas":10,
        "contratos":3,
        "receita":14700
    },

    {
        "nome":"MAPA_DE_RISCO",
        "canal":"PORTAL",
        "visitas":200,
        "leads":8,
        "propostas":3,
        "contratos":1,
        "receita":2490
    }
]

print("")
print("===================================")
print("ATIVOS ANALISADOS")
print("===================================")

melhor_receita = 0
melhor_produto = ""

melhor_conversao = 0
melhor_conteudo = ""

for ativo in ativos:
    pass

    visitas = ativo["visitas"]
    leads = ativo["leads"]
    contratos = ativo["contratos"]

    conversao = 0

    if visitas > 0:
        pass

        conversao = (
            contratos / visitas
        ) * 100

    ativo["conversao"] = conversao

    print("")
    print("ATIVO:")
    print(ativo["nome"])

    print("CANAL:")
    print(ativo["canal"])

    print("VISITAS:")
    print(visitas)

    print("LEADS:")
    print(leads)

    print("PROPOSTAS:")
    print(ativo["propostas"])

    print("CONTRATOS:")
    print(contratos)

    print("RECEITA:")
    print(
        f'R$ {ativo["receita"]:,.2f}'
    )

    print("CONVERSAO:")
    print(
        f'{conversao:.2f}%'
    )

    if ativo["receita"] > melhor_receita:
        pass

        melhor_receita = ativo["receita"]
        melhor_produto = ativo["nome"]

    if conversao > melhor_conversao:
        pass

        melhor_conversao = conversao
        melhor_conteudo = ativo["nome"]

print("")
print("===================================")
print("INTELIGENCIA DE CONVERSAO")
print("===================================")

print("")
print("MELHOR GERADOR DE RECEITA:")
print(melhor_produto)

print("")
print("MAIOR RECEITA:")
print(
    f'R$ {melhor_receita:,.2f}'
)

print("")
print("MELHOR CONVERSAO:")
print(melhor_conteudo)

print("")
print("TAXA:")
print(
    f'{melhor_conversao:.2f}%'
)

print("")
print("===================================")
print("FORMULA")
print("===================================")

print("CONTEUDO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("VISITA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("LEAD")
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

    "QUAL CONTEUDO ATRAI MAIS?",
    "QUAL CANAL ATRAI MAIS?",
    "QUAL PRODUTO VENDE MAIS?",
    "QUAL PRODUTO FATURA MAIS?",
    "QUAL PRODUTO CONVERTE MELHOR?",
    "ONDE INVESTIR MAIS?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "MEDIR. COMPARAR. "
    "APRENDER. OTIMIZAR."
)

print("")
print("CONVERSION INTELLIGENCE ATIVA")




