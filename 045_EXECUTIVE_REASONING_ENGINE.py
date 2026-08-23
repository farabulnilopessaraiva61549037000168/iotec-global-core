# ==========================================================
# 045_EXECUTIVE_REASONING_ENGINE.py
# IOTEC EXECUTIVE REASONING ENGINE
# ==========================================================

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

print("=" * 70)
print("IOTEC EXECUTIVE REASONING ENGINE")
print("=" * 70)
print()

# ----------------------------------------------------------
# Carrega perguntas
# ----------------------------------------------------------

cursor.execute("""
SELECT
    id,
    departamento,
    pergunta
FROM executive_questions
ORDER BY id
""")

perguntas = cursor.fetchall()

total_evidencias = 0

print("PERGUNTAS ANALISADAS")
print()

for pergunta_id, departamento, pergunta in perguntas:

    cursor.execute("""
    SELECT
        COUNT(*)
    FROM executive_evidence
    WHERE pergunta_id=?
    """,(pergunta_id,))

    qtd = cursor.fetchone()[0]

    total_evidencias += qtd

    if qtd >= 1000:
        maturidade = "MUITO ALTA"
        confianca = 95

    elif qtd >= 500:
        maturidade = "ALTA"
        confianca = 85

    elif qtd >= 200:
        maturidade = "MÃƒâ€°DIA"
        confianca = 70

    elif qtd >= 50:
        maturidade = "BAIXA"
        confianca = 50

    else:
        maturidade = "CRÃƒÂTICA"
        confianca = 25

    print("-"*70)
    print(pergunta)
    print()
    print("Departamento :",departamento)
    print("EvidÃƒÂªncias   :",qtd)
    print("Maturidade   :",maturidade)
    print("ConfianÃƒÂ§a    :",f"{confianca}%")

print()

print("="*70)
print("RESUMO EXECUTIVO")
print("="*70)
print()

print("Perguntas........:",len(perguntas))
print("EvidÃƒÂªncias.......:",total_evidencias)

cursor.execute("""

SELECT COUNT(DISTINCT arquivo)

FROM executive_evidence

""")

arquivos = cursor.fetchone()[0]

print("Arquivos usados..:",arquivos)

print()

# ----------------------------------------------------------

print("="*70)
print("PARECER PRELIMINAR")
print("="*70)
print()

print("O Kernel encontrou um grande volume")
print("de evidÃƒÂªncias distribuÃƒÂ­das por toda")
print("a arquitetura.")

print()

print("Isso indica que existe conhecimento")
print("tecnolÃƒÂ³gico consolidado.")

print()

print("A prÃƒÂ³xima etapa nÃƒÂ£o ÃƒÂ© produzir")
print("mais cÃƒÂ³digo.")

print("A prÃƒÂ³xima etapa ÃƒÂ© transformar")
print("essas evidÃƒÂªncias em decisÃƒÂµes.")

print()

# ----------------------------------------------------------
# PERGUNTA MAIS IMPORTANTE
# ----------------------------------------------------------

cursor.execute("""

SELECT id

FROM executive_questions

WHERE pergunta LIKE '%impede a primeira venda%'

""")

linha = cursor.fetchone()

if linha:

    pergunta_id = linha[0]

    cursor.execute("""

    SELECT

    arquivo,

    evidencia

    FROM executive_evidence

    WHERE pergunta_id=?

    ORDER BY arquivo

    LIMIT 30

    """,(pergunta_id,))

    print("="*70)
    print("EVIDÃƒÅ NCIAS RELACIONADAS Ãƒâ‚¬ PRIMEIRA VENDA")
    print("="*70)
    print()

    for arq,evid in cursor.fetchall():

        print(arq)
        print("   ",evid)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("O prÃƒÂ³ximo passo serÃƒÂ¡ abandonar")
print("a anÃƒÂ¡lise baseada em palavras.")

print()

print("O Kernel comeÃƒÂ§arÃƒÂ¡ a analisar")
print("relaÃƒÂ§ÃƒÂµes entre mÃƒÂ³dulos, bancos")
print("de dados e dependÃƒÂªncias.")

print()

print("Data :",datetime.now())

db.close()


