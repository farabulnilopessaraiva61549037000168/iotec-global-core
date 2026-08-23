import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC SIGNAL PRIORITY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "CLASSIFICAR SINAIS POR "
    "IMPACTO, URGENCIA E "
    "POTENCIAL ECONOMICO"
)

sinais = [

    {
        "nome": "ESTIAGEM_CEARA",
        "impacto": 10,
        "urgencia": 10,
        "orcamento": 9
    },

    {
        "nome": "ENCHENTE_REGIONAL",
        "impacto": 8,
        "urgencia": 8,
        "orcamento": 7
    },

    {
        "nome": "QUEDA_DE_PRODUCAO",
        "impacto": 7,
        "urgencia": 6,
        "orcamento": 8
    }
]

print("")
print("===================================")
print("SINAIS ANALISADOS")
print("===================================")

ranking = []

for sinal in sinais:
    pass

    score = (
        sinal["impacto"]
        *
        sinal["urgencia"]
        *
        sinal["orcamento"]
    )

    ranking.append(
        {
            "nome": sinal["nome"],
            "score": score
        }
    )

ranking.sort(
    key=lambda x: x["score"],
    reverse=True
)

for item in ranking:
    pass

    print("")
    print("SINAL:")
    print(item["nome"])

    print("PRIORIDADE:")
    print(item["score"])

print("")
print("===================================")
print("LOGICA")
print("===================================")

print("FONTE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("SINAL")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("IMPACTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("URGENCIA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("ORCAMENTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRIORIDADE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PRODUTO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("PERGUNTA CENTRAL:")

print(
    "QUAL O PROBLEMA MAIS "
    "IMPORTANTE PARA ATUAR AGORA?"
)

print("")
print("ORDEM MOR:")

print(
    "ATACAR PRIMEIRO OS "
    "PROBLEMAS COM MAIOR "
    "IMPACTO E MAIOR "
    "POTENCIAL DE MERCADO."
)

print("")
print("NUCLEO DE PRIORIZACAO ATIVO")


