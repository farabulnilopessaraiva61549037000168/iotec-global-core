import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC STRATEGIC COMMAND CENTER
# ==========================================================

from datetime import datetime

print("=" * 70)
print("IOTEC STRATEGIC COMMAND CENTER")
print("=" * 70)

print()
print("DATA:")
print(datetime.now())

print()
print("=" * 70)
print("MISSAO")
print("=" * 70)

print("""
TRANSFORMAR CAPACIDADES
EM RECEITA RECORRENTE.

MAPEAR.

ORGANIZAR.

INTEGRAR.

PUBLICAR.

NEGOCIAR.

ENTREGAR.

ESCALAR.
""")

# ==========================================================
# PILARES
# ==========================================================

print()
print("=" * 70)
print("PILARES DA IOTEC")
print("=" * 70)

pilares = [

    "CAPACIDADES",
    "PRODUTOS",
    "PUBLICACAO",
    "INTEGRACOES",
    "CLIENTES",
    "NEGOCIACOES",
    "CONTRATOS",
    "RECEITA",
    "RECORRENCIA",
    "GOVERNANCA"

]

for p in pilares:

    print("-", p)

# ==========================================================
# INVENTARIO
# ==========================================================

print()
print("=" * 70)
print("PERGUNTAS DO NUCLEO")
print("=" * 70)

perguntas = [

    "O QUE EXISTE?",

    "ONDE ESTA?",

    "QUEM USA?",

    "GERA RECEITA?",

    "ESTA COMPLETO?",

    "ESTA CONECTADO?",

    "ESTA SENDO DIVULGADO?",

    "POSSUI PAGAMENTO?",

    "POSSUI ENTREGA?",

    "POSSUI CLIENTE?"
]

for pergunta in perguntas:

    print("-", pergunta)

# ==========================================================
# INTEGRACOES PRIORITARIAS
# ==========================================================

print()
print("=" * 70)
print("INTEGRACOES PRIORITARIAS")
print("=" * 70)

integracoes = [

    {
        "nome":"GOOGLE_MAPS",
        "objetivo":"MAPEAR EMPRESAS E OPORTUNIDADES",
        "prioridade":"MAXIMA"
    },

    {
        "nome":"LINKEDIN",
        "objetivo":"MAPEAR DECISORES E CONTATOS",
        "prioridade":"MAXIMA"
    },

    {
        "nome":"YOUTUBE",
        "objetivo":"AUTORIDADE E DEMONSTRACAO",
        "prioridade":"MAXIMA"
    },

    {
        "nome":"INSTAGRAM",
        "objetivo":"VISIBILIDADE E ENGAJAMENTO",
        "prioridade":"MAXIMA"
    }

]

for item in integracoes:

    print()
    print("INTEGRACAO:", item["nome"])
    print("OBJETIVO:", item["objetivo"])
    print("PRIORIDADE:", item["prioridade"])

# ==========================================================
# RECEITA
# ==========================================================

print()
print("=" * 70)
print("INTELIGENCIA DE RECEITA")
print("=" * 70)

print("""

NAO PROCURAR DINHEIRO.

PROCURAR:

MERCADOS

DEMANDAS

PROBLEMAS

COMPRADORES

ORCAMENTOS

CONTRATOS

RELACIONAMENTOS

RECORRENCIA

""")

# ==========================================================
# PRODUTOS
# ==========================================================

print()
print("=" * 70)
print("VALIDACAO DE PRODUTOS")
print("=" * 70)

print("""

TODO PRODUTO DEVE POSSUIR:

DESCRICAO

PRECO

ENTREGA

DEMONSTRACAO

FORMULARIO

PAGAMENTO

SUPORTE

RENOVACAO

""")

# ==========================================================
# PUBLICACAO
# ==========================================================

print()
print("=" * 70)
print("PUBLICACAO")
print("=" * 70)

print("""

TODO PRODUTO DEVE GERAR:

ARTIGO

VIDEO

IMAGEM

APRESENTACAO

LANDING PAGE

FORMULARIO

""")

# ==========================================================
# ESTACOES DO MERCADO
# ==========================================================

print()
print("=" * 70)
print("ESTACOES DO MERCADO")
print("=" * 70)

print("""

O NUCLEO DEVE MONITORAR:

TENDENCIAS

LICITACOES

ORCAMENTOS

CALENDARIOS

EVENTOS

MOVIMENTACOES

MERCADOS

""")

# ==========================================================
# MAPA DE VALOR
# ==========================================================

print()
print("=" * 70)
print("MAPA DE VALOR")
print("=" * 70)

print("""

NAO AVALIAR CODIGOS.

AVALIAR:

CAPACIDADES

IMPACTO

UTILIDADE

ESCALA

AUTOMACAO

MERCADO

RECORRENCIA

""")

# ==========================================================
# ORDEM MOR
# ==========================================================

print()
print("=" * 70)
print("ORDEM MOR")
print("=" * 70)

print("""

OBSERVAR

MAPEAR

CLASSIFICAR

INTEGRAR

PUBLICAR

CAPTAR

NEGOCIAR

CONTRATAR

RECEBER

RENOVAR

ESCALAR

""")

# ==========================================================
# PROXIMOS PASSOS
# ==========================================================

print()
print("=" * 70)
print("PROXIMOS PASSOS PRIORITARIOS")
print("=" * 70)

acoes = [

    "MAPEAR TODOS OS PRODUTOS",

    "MAPEAR TODAS AS INTERFACES",

    "MAPEAR TODAS AS TORRES",

    "IDENTIFICAR O QUE GERA RECEITA",

    "IDENTIFICAR O QUE ESTA PARADO",

    "CONECTAR GOOGLE MAPS",

    "CONECTAR LINKEDIN",

    "CONECTAR YOUTUBE",

    "CONECTAR INSTAGRAM",

    "IMPLEMENTAR PAGAMENTOS",

    "IMPLEMENTAR AREA DO CLIENTE",

    "IMPLEMENTAR PREVISAO DE RECEITA"

]

for acao in acoes:

    print("-", acao)

print()
print("STRATEGIC COMMAND CENTER ATIVO")



