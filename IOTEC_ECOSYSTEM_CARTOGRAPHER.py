import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ECOSYSTEM CARTOGRAPHER
# ==========================================================

from datetime import datetime

print("=" * 60)
print("IOTEC ECOSYSTEM CARTOGRAPHER")
print("=" * 60)

print()
print("DATA:")
print(datetime.now())

print()
print("=" * 60)
print("MISSAO")
print("=" * 60)

print("""
MAPEAR O ECOSSISTEMA IOTEC.

LOCALIZAR TODOS OS FRAGMENTOS.

IDENTIFICAR VALOR.

IDENTIFICAR RECEITA.

IDENTIFICAR ABANDONO.

IDENTIFICAR OPORTUNIDADES.
""")

# ==========================================================
# TORRES
# ==========================================================

torres = [

    {
        "nome":"COMERCIAL",
        "status":"ATIVA",
        "receita":True
    },

    {
        "nome":"GOOGLE_MAPS",
        "status":"PENDENTE_INTEGRACAO",
        "receita":False
    },

    {
        "nome":"LINKEDIN",
        "status":"PENDENTE_INTEGRACAO",
        "receita":False
    },

    {
        "nome":"PUBLICACAO",
        "status":"PARCIAL",
        "receita":True
    },

    {
        "nome":"PIPELINE",
        "status":"ATIVA",
        "receita":True
    },

    {
        "nome":"INTELIGENCIA_FINANCEIRA",
        "status":"EM_EXPANSAO",
        "receita":True
    }
]

print()
print("=" * 60)
print("TORRES")
print("=" * 60)

for torre in torres:

    print()
    print("NOME:", torre["nome"])
    print("STATUS:", torre["status"])
    print("GERA_RECEITA:", torre["receita"])

# ==========================================================
# CLASSIFICACAO
# ==========================================================

print()
print("=" * 60)
print("CLASSIFICACAO OPERACIONAL")
print("=" * 60)

print("""
NIVEL 1
RECEITA DIRETA

NIVEL 2
SUPORTE A RECEITA

NIVEL 3
OPERACIONAL

NIVEL 4
EXPERIMENTAL

NIVEL 5
ARQUIVO HISTORICO
""")

# ==========================================================
# PERGUNTAS
# ==========================================================

print()
print("=" * 60)
print("PERGUNTAS OBRIGATORIAS")
print("=" * 60)

perguntas = [

    "O QUE EXISTE?",

    "ONDE ESTA?",

    "EM QUE ESTADO ESTA?",

    "QUEM USA?",

    "QUEM COMPRA?",

    "GERA RECEITA?",

    "QUANTO FATURA?",

    "ESTA CONECTADO A DADOS REAIS?",

    "PRECISA DE API?",

    "PRECISA DE PUBLICACAO?",

    "PRECISA DE CLIENTES?",

    "PRECISA DE MANUTENCAO?"
]

for pergunta in perguntas:

    print("-", pergunta)

# ==========================================================
# DETECTORISMO
# ==========================================================

print()
print("=" * 60)
print("DETECTORISMO")
print("=" * 60)

detectores = [

    "DETECTOR_DE_RECEITA",

    "DETECTOR_DE_MERCADOS",

    "DETECTOR_DE_CLIENTES",

    "DETECTOR_DE_DEMANDAS",

    "DETECTOR_DE_PROBLEMAS",

    "DETECTOR_DE_NEGOCIACOES",

    "DETECTOR_DE_RENOVACOES",

    "DETECTOR_DE_TENDENCIAS",

    "DETECTOR_DE_OPORTUNIDADES"
]

for detector in detectores:

    print("-", detector)

# ==========================================================
# FILOSOFIA
# ==========================================================

print()
print("=" * 60)
print("FILOSOFIA")
print("=" * 60)

print("""
NAO PROCURAR DINHEIRO.

PROCURAR:

MERCADOS

PROBLEMAS

DEMANDAS

ORCAMENTOS

CLIENTES

CONTRATOS

RELACIONAMENTOS

RECORRENCIA
""")

# ==========================================================
# COORDENADAS ECONOMICAS
# ==========================================================

print()
print("=" * 60)
print("COORDENADAS ECONOMICAS")
print("=" * 60)

print("""
MERCADO
+
DEMANDA
+
ORCAMENTO
+
PROBABILIDADE
+
RECORRENCIA

=

POTENCIAL ECONOMICO
""")

# ==========================================================
# ORDEM MOR
# ==========================================================

print()
print("=" * 60)
print("ORDEM MOR")
print("=" * 60)

print("""
OBSERVAR

MAPEAR

CLASSIFICAR

GOVERNAR

NEGOCIAR

CONTRATAR

RECEBER

RENOVAR

ESCALAR
""")

print()
print("ECOSYSTEM CARTOGRAPHER ATIVO")



