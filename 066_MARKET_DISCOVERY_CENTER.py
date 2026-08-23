# ==========================================================
# 066_MARKET_DISCOVERY_CENTER.py
# IOTEC MARKET DISCOVERY CENTER
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS market_sources(

id INTEGER PRIMARY KEY AUTOINCREMENT,

codigo TEXT,

nome TEXT,

tipo TEXT,

objetivo TEXT,

prioridade INTEGER,

status TEXT

)

""")

db.commit()

FONTES=[

("SRC001",
"Google Maps",
"LOCAL",
"Encontrar empresas por localizaÃƒÂ§ÃƒÂ£o.",
10),

("SRC002",
"LinkedIn",
"CORPORATIVO",
"Encontrar empresas e profissionais.",
10),

("SRC003",
"Sites Corporativos",
"WEB",
"Descobrir serviÃƒÂ§os e contatos.",
9),

("SRC004",
"Receita PÃƒÂºblica",
"GOVERNO",
"Consultar dados pÃƒÂºblicos.",
9),

("SRC005",
"Bases PÃƒÂºblicas",
"DADOS",
"Encontrar oportunidades pÃƒÂºblicas.",
9),

("SRC006",
"CRM",
"INTERNO",
"Aprender com clientes existentes.",
8),

("SRC007",
"Campanhas Anteriores",
"HISTÃƒâ€œRICO",
"Reutilizar inteligÃƒÂªncia obtida.",
8),

("SRC008",
"Google Business",
"LOCAL",
"Descobrir empresas por segmento.",
9)

]

for codigo,nome,tipo,objetivo,prioridade in FONTES:

    cursor.execute("""

    INSERT INTO market_sources(

    codigo,

    nome,

    tipo,

    objetivo,

    prioridade,

    status

    )

    VALUES(?,?,?,?,?,?)

    """,(

    codigo,

    nome,

    tipo,

    objetivo,

    prioridade,

    "ATIVO"

    ))

db.commit()

print("="*70)
print("IOTEC MARKET DISCOVERY CENTER")
print("="*70)
print()

print("FONTES ESTRATÃƒâ€°GICAS")
print()

for codigo,nome,tipo,objetivo,prioridade in FONTES:

    print(f"{codigo}")
    print(nome)
    print("Tipo.......:",tipo)
    print("Prioridade.:",prioridade)
    print("Objetivo...:",objetivo)
    print("-"*60)

print()

print("="*70)
print("PIPELINE DA INTELIGÃƒÅ NCIA")
print("="*70)
print()

pipeline=[

"Descobrir empresa",

"Coletar informaÃƒÂ§ÃƒÂµes",

"Validar qualidade",

"Calcular potencial",

"Classificar",

"Criar dossiÃƒÂª",

"Enviar para EstratÃƒÂ©gia",

"Preparar Campanha"

]

for i,item in enumerate(pipeline,1):

    print(f"{i:02d} - {item}")

print()

print("="*70)
print("MISSÃƒÆ'O DA PRESIDÃƒÅ NCIA")
print("="*70)
print()

print("Toda inteligÃƒÂªncia")
print("de mercado deverÃƒÂ¡")
print("nascer neste Centro.")

print()

print("Nenhuma campanha")
print("comeÃƒÂ§a sem passar")
print("pelo Discovery Center.")

db.close()


