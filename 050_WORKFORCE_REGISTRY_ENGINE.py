# ==========================================================
# 050_WORKFORCE_REGISTRY_ENGINE.py
# IOTEC WORKFORCE REGISTRY
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS workforce(

id INTEGER PRIMARY KEY AUTOINCREMENT,

codigo TEXT UNIQUE,

nome TEXT,

ecossistema TEXT,

especialidade TEXT,

nivel INTEGER,

status TEXT,

missoes INTEGER,

capacidade INTEGER,

responsavel TEXT

)

""")

db.commit()

AGENTES=[

("AGT-001","Hunter Alpha",
"COMERCIAL",
"ProspecÃƒÂ§ÃƒÂ£o de Empresas",
10,
"LIVRE",
0,
100,
"Diretor Comercial"),

("AGT-002","Negotiator Prime",
"COMERCIAL",
"NegociaÃƒÂ§ÃƒÂ£o",
10,
"LIVRE",
0,
100,
"Diretor Comercial"),

("AGT-003","Financial Guardian",
"FINANCEIRO",
"Recebimentos",
10,
"LIVRE",
0,
100,
"Diretor Financeiro"),

("AGT-004","Production Master",
"PRODUÃƒâ€¡ÃƒÆ'O",
"ProduÃƒÂ§ÃƒÂ£o",
9,
"LIVRE",
0,
100,
"Diretor ProduÃƒÂ§ÃƒÂ£o"),

("AGT-005","Quality Sentinel",
"QUALIDADE",
"ValidaÃƒÂ§ÃƒÂ£o",
9,
"LIVRE",
0,
100,
"Diretor Qualidade"),

("AGT-006","CRM Keeper",
"CRM",
"Relacionamento",
8,
"LIVRE",
0,
100,
"Diretor CRM"),

("AGT-007","Intelligence Oracle",
"INTELIGÃƒÅ NCIA",
"AnÃƒÂ¡lise EstratÃƒÂ©gica",
9,
"LIVRE",
0,
100,
"Chief Intelligence Officer"),

("AGT-008","Architect Guardian",
"ARQUITETURA",
"Arquitetura",
10,
"LIVRE",
0,
100,
"Arquiteto Chefe"),

("AGT-009","AI Coordinator",
"IA",
"CoordenaÃƒÂ§ÃƒÂ£o de Agentes",
9,
"LIVRE",
0,
100,
"Diretor IA"),

("AGT-010","Executive Messenger",
"PRESIDÃƒÅ NCIA",
"CoordenaÃƒÂ§ÃƒÂ£o Executiva",
10,
"LIVRE",
0,
100,
"Presidente")

]

novos=0

for agente in AGENTES:

    cursor.execute("""

    SELECT id

    FROM workforce

    WHERE codigo=?

    """,(agente[0],))

    if cursor.fetchone() is None:

        cursor.execute("""

        INSERT INTO workforce(

        codigo,

        nome,

        ecossistema,

        especialidade,

        nivel,

        status,

        missoes,

        capacidade,

        responsavel

        )

        VALUES(?,?,?,?,?,?,?,?,?)

        """,agente)

        novos+=1

db.commit()

print("="*70)
print("IOTEC WORKFORCE REGISTRY")
print("="*70)
print()

cursor.execute("""

SELECT

codigo,

nome,

ecossistema,

especialidade,

status

FROM workforce

ORDER BY ecossistema,nivel DESC

""")

for codigo,nome,eco,esp,status in cursor.fetchall():

    print(f"{codigo:<10}{nome:<24}{eco:<18}{status}")

print()

print("="*70)
print("INDICADORES")
print("="*70)
print()

cursor.execute("SELECT COUNT(*) FROM workforce")
print("Agentes cadastrados :",cursor.fetchone()[0])

cursor.execute("""

SELECT COUNT(*)

FROM workforce

WHERE status='LIVRE'

""")

print("Agentes livres..... :",cursor.fetchone()[0])

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A Torre de Controle")
print("agora conhece")
print("sua forÃƒÂ§a de trabalho.")

print()

print("PrÃƒÂ³xima etapa:")

print()

print("Distribuir missÃƒÂµes")
print("automaticamente")
print("para os melhores agentes.")

db.close()


