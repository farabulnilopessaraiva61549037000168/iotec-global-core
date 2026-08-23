# ==========================================================
# 067_INTELLIGENCE_MISSION_PLANNER.py
# IOTEC INTELLIGENCE MISSION PLANNER
# ==========================================================

import sqlite3
from datetime import datetime

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

# ==========================================================
# MISSÃƒâ€¢ES DE INTELIGÃƒÅ NCIA
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS intelligence_missions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

codigo TEXT,

nome TEXT,

segmento TEXT,

cidade TEXT,

estado TEXT,

pais TEXT,

porte_minimo TEXT,

porte_maximo TEXT,

objetivo TEXT,

prioridade INTEGER,

origem TEXT,

status TEXT,

data_criacao TEXT

)

""")

db.commit()

MISSOES=[

(

"MS001",

"Tecnologia Fortaleza",

"Tecnologia",

"Fortaleza",

"CE",

"Brasil",

"MÃƒÂ©dio",

"Grande",

"Encontrar empresas para soluÃƒÂ§ÃƒÂµes de IA.",

10,

"PresidÃƒÂªncia"

),

(

"MS002",

"Prefeituras CearÃƒÂ¡",

"Governo",

"*",

"CE",

"Brasil",

"Pequeno",

"Grande",

"Projetos de transformaÃƒÂ§ÃƒÂ£o digital.",

9,

"PresidÃƒÂªncia"

),

(

"MS003",

"Hospitais Nordeste",

"SaÃƒÂºde",

"*",

"*",

"Brasil",

"MÃƒÂ©dio",

"Grande",

"AutomaÃƒÂ§ÃƒÂ£o e InteligÃƒÂªncia.",

9,

"PresidÃƒÂªncia"

),

(

"MS004",

"IndÃƒÂºstrias",

"IndÃƒÂºstria",

"*",

"*",

"Brasil",

"MÃƒÂ©dio",

"Grande",

"Projetos corporativos.",

8,

"PresidÃƒÂªncia"

)

]

for m in MISSOES:

    cursor.execute("""

    INSERT INTO intelligence_missions(

    codigo,

    nome,

    segmento,

    cidade,

    estado,

    pais,

    porte_minimo,

    porte_maximo,

    objetivo,

    prioridade,

    origem,

    status,

    data_criacao

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,(

    m[0],

    m[1],

    m[2],

    m[3],

    m[4],

    m[5],

    m[6],

    m[7],

    m[8],

    m[9],

    m[10],

    "AGUARDANDO",

    datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

db.commit()

print("="*70)
print("IOTEC INTELLIGENCE MISSION PLANNER")
print("="*70)
print()

print("MISSÃƒâ€¢ES CADASTRADAS")
print()

cursor.execute("""

SELECT

codigo,

nome,

segmento,

cidade,

estado,

prioridade,

status

FROM intelligence_missions

ORDER BY prioridade DESC

""")

for linha in cursor.fetchall():

    print(f"{linha[0]}  {linha[1]}")
    print(f"Segmento..: {linha[2]}")
    print(f"RegiÃƒÂ£o....: {linha[3]} / {linha[4]}")
    print(f"Prioridade: {linha[5]}")
    print(f"Status....: {linha[6]}")
    print("-"*60)

print()

print("="*70)
print("FLUXO DA MISSÃƒÆ'O")
print("="*70)
print()

fluxo=[

"PresidÃƒÂªncia define objetivo",

"MissÃƒÂ£o EstratÃƒÂ©gica criada",

"Discovery Center recebe",

"Coletores executam",

"Empresas encontradas",

"Kernel EstratÃƒÂ©gico qualifica",

"EstratÃƒÂ©gia monta campanha",

"ExecuÃƒÂ§ÃƒÂ£o inicia prospecÃƒÂ§ÃƒÂ£o"

]

for i,item in enumerate(fluxo,1):

    print(f"{i:02d} - {item}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("Nenhum coletor")
print("pesquisa aleatoriamente.")

print()

print("Toda busca deverÃƒÂ¡")
print("obedecer uma")
print("MissÃƒÂ£o EstratÃƒÂ©gica.")

db.close()


