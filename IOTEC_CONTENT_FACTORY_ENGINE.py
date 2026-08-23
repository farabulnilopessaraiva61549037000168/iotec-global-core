import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC CONTENT FACTORY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "TRANSFORMAR PROBLEMAS "
    "EM ATIVOS DE CAPTACAO"
)

produtos = [

    {
        "problema":"ESTIAGEM",

        "produto":
        "PLANO_DE_CONTINGENCIA",

        "publico":
        "PREFEITURAS"
    },

    {
        "problema":"ENCHENTE",

        "produto":
        "MAPA_DE_VULNERABILIDADE",

        "publico":
        "DEFESA_CIVIL"
    },

    {
        "problema":"LOGISTICA",

        "produto":
        "OTIMIZACAO_DE_ROTAS",

        "publico":
        "INDUSTRIAS"
    },

    {
        "problema":"GESTAO_FINANCEIRA",

        "produto":
        "PAINEL_EXECUTIVO",

        "publico":
        "EMPRESAS"
    }
]

print("")
print("===================================")
print("FABRICA DE CONTEUDO")
print("===================================")

for item in produtos:
    pass

    print("")
    print("PROBLEMA:")
    print(item["problema"])

    print("PUBLICO:")
    print(item["publico"])

    print("PRODUTO:")
    print(item["produto"])

    print("")
    print("ATIVOS GERAVEIS:")

    ativos = [

        "ARTIGO_TECNICO",
        "RELATORIO_EXECUTIVO",
        "VIDEO_EXPLICATIVO",
        "LANDING_PAGE",
        "FORMULARIO_DIAGNOSTICO",
        "ESTUDO_DE_CASO",
        "INFOGRAFICO",
        "APRESENTACAO_EXECUTIVA"
    ]

    for ativo in ativos:
        pass

        print("-", ativo)

print("")
print("===================================")
print("JORNADA DE CAPTACAO")
print("===================================")

print("PROBLEMA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("CONTEUDO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("INTERESSE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("FORMULARIO")
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
print("MODELO DE PORTAL")
print("===================================")

print("VIDEO DE FUNDO")
print("+")
print("PROBLEMA VISUAL")
print("+")
print("DADOS")
print("+")
print("SOLUCAO")
print("+")
print("FORMULARIO")
print("=")
print("CAPTACAO")

print("")
print("===================================")
print("PERGUNTAS DO NUCLEO")
print("===================================")

perguntas = [

    "QUAL PROBLEMA ESTA SENDO MOSTRADO?",
    "QUEM ESTA SENDO AFETADO?",
    "QUAL O IMPACTO ECONOMICO?",
    "QUAL A SOLUCAO?",
    "QUAL O PRODUTO?",
    "COMO CAPTURAR O LEAD?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "TODO PRODUTO DEVE GERAR "
    "CONTEUDO, TODO CONTEUDO "
    "DEVE GERAR INTERESSE E "
    "TODO INTERESSE DEVE "
    "GERAR LEADS."
)

print("")
print("CONTENT FACTORY ENGINE ATIVO")




