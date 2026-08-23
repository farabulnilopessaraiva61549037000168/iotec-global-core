# ==========================================================
# 043_IOTEC_INTERROGATOR.py
# IOTEC EXECUTIVE INTERROGATOR
# ==========================================================

import sqlite3

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS executive_questions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    departamento TEXT,

    pergunta TEXT,

    prioridade INTEGER,

    status TEXT DEFAULT 'PENDENTE'

)
""")

PERGUNTAS = [

("IDENTIDADE","Qual ÃƒÂ© a missÃƒÂ£o real da IOTEC?",1),

("IDENTIDADE","Quais produtos realmente existem?",1),

("IDENTIDADE","Quais produtos ainda sÃƒÂ£o apenas ideias?",1),

("COMERCIAL","O que impede a primeira venda?",1),

("COMERCIAL","Qual produto venderia amanhÃƒÂ£?",1),

("COMERCIAL","Existe fluxo completo atÃƒÂ© o pagamento?",1),

("FINANCEIRO","Existe recebimento automÃƒÂ¡tico?",1),

("FINANCEIRO","Existe PIX funcionando?",1),

("PRODUÃƒâ€¡ÃƒÆ'O","Existe entrega automÃƒÂ¡tica?",1),

("PRODUÃƒâ€¡ÃƒÆ'O","Existe controle de qualidade?",1),

("ARQUITETURA","Existem mÃƒÂ³dulos abandonados?",1),

("ARQUITETURA","Existem mÃƒÂ³dulos duplicados?",1),

("ARQUITETURA","Existem dependÃƒÂªncias quebradas?",1),

("IA","Existem agentes sem missÃƒÂ£o?",1),

("IA","Existem agentes sem utilidade?",1),

("EMPRESA","Se vocÃƒÂª fosse Presidente da IOTEC, o que faria primeiro?",1),

("EMPRESA","Quais sÃƒÂ£o os 10 maiores gargalos?",1),

("EMPRESA","Quais setores impedem faturamento?",1),

("EMPRESA","Quais obras estÃƒÂ£o inacabadas?",1),

("EMPRESA","Quais ativos tecnolÃƒÂ³gicos ainda nÃƒÂ£o sÃƒÂ£o utilizados?",1)

]

novas = 0

for departamento, pergunta, prioridade in PERGUNTAS:

    cursor.execute("""

    SELECT id

    FROM executive_questions

    WHERE pergunta=?

    """,(pergunta,))

    if cursor.fetchone() is None:

        cursor.execute("""

        INSERT INTO executive_questions(

        departamento,

        pergunta,

        prioridade

        )

        VALUES(?,?,?)

        """,(departamento,pergunta,prioridade))

        novas += 1

db.commit()

print("="*70)
print("IOTEC EXECUTIVE INTERROGATOR")
print("="*70)
print()

print("Perguntas cadastradas :",novas)

print()

cursor.execute("""

SELECT departamento,

COUNT(*)

FROM executive_questions

GROUP BY departamento

ORDER BY departamento

""")

for dep,qtd in cursor.fetchall():

    print(f"{dep:<20}{qtd}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia agora possui")
print("um banco oficial de perguntas.")
print()

print("PrÃƒÂ³xima etapa:")
print()

print("Fazer o Kernel responder")
print("cada pergunta com evidÃƒÂªncias.")

db.close()


