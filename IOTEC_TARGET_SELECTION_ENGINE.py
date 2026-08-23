import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC TARGET SELECTION ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "PRIORIZAR ALVOS COM MAIOR "
    "POTENCIAL DE CONTRATACAO"
)

alvos = [

    {
        "nome":"PREFEITURA_A",
        "problema":"ESTIAGEM",
        "impacto":10,
        "orcamento":9,
        "urgencia":10,
        "acesso":7
    },

    {
        "nome":"COOPERATIVA_B",
        "problema":"ESTIAGEM",
        "impacto":8,
        "orcamento":7,
        "urgencia":8,
        "acesso":8
    },

    {
        "nome":"INDUSTRIA_C",
        "problema":"LOGISTICA",
        "impacto":9,
        "orcamento":10,
        "urgencia":7,
        "acesso":6
    },

    {
        "nome":"EMPRESA_D",
        "problema":"GESTAO_FINANCEIRA",
        "impacto":7,
        "orcamento":8,
        "urgencia":6,
        "acesso":9
    }
]

for alvo in alvos:
    pass

    score = (

        alvo["impacto"] +
        alvo["orcamento"] +
        alvo["urgencia"] +
        alvo["acesso"]

    )

    alvo["score"] = score

ranking = sorted(
    alvos,
    key=lambda x: x["score"],
    reverse=True
)

print("")
print("===================================")
print("RANKING DE ALVOS")
print("===================================")

posicao = 1

for alvo in ranking:
    pass

    print("")
    print(f"#{posicao}")

    print("ALVO:")
    print(alvo["nome"])

    print("PROBLEMA:")
    print(alvo["problema"])

    print("IMPACTO:")
    print(alvo["impacto"])

    print("ORCAMENTO:")
    print(alvo["orcamento"])

    print("URGENCIA:")
    print(alvo["urgencia"])

    print("ACESSO:")
    print(alvo["acesso"])

    print("SCORE:")
    print(alvo["score"])

    posicao += 1

print("")
print("===================================")
print("FORMULA")
print("===================================")

print("IMPACTO")
print("+")
print("ORCAMENTO")
print("+")
print("URGENCIA")
print("+")
print("ACESSO")
print("=")
print("PRIORIDADE")

print("")
print("===================================")
print("MISSAO COMERCIAL")
print("===================================")

print(
    "ATACAR PRIMEIRO OS ALVOS "
    "COM MAIOR SCORE."
)

print("")
print("PERGUNTAS DO NUCLEO:")

perguntas = [

    "QUEM TEM MAIOR DOR?",
    "QUEM TEM ORCAMENTO?",
    "QUEM TEM URGENCIA?",
    "QUEM E MAIS ACESSIVEL?",
    "QUEM TEM MAIOR CHANCE DE FECHAMENTO?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("ORDEM MOR:")
print(
    "NAO PROSPECTAR TODOS. "
    "PROSPECTAR PRIMEIRO "
    "OS MELHORES ALVOS."
)

print("")
print("TARGET SELECTION ENGINE ATIVO")




