# ==========================================================
# 064_ENTERPRISE_OPERATING_SYSTEM.py
# IOTEC ENTERPRISE OPERATING SYSTEM
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS enterprise_layers(

id INTEGER PRIMARY KEY AUTOINCREMENT,

codigo TEXT,

nome TEXT,

missao TEXT,

criticidade INTEGER,

status TEXT

)

""")

db.commit()

CAMADAS=[

("EOS001",
"GOVERNANÃƒâ€¡A",
"Controlar toda a empresa.",
10),

("EOS002",
"INTELIGÃƒÅ NCIA",
"Descobrir oportunidades reais de mercado.",
10),

("EOS003",
"ESTRATÃƒâ€°GIA",
"Transformar inteligÃƒÂªncia em campanhas.",
10),

("EOS004",
"EXECUÃƒâ€¡ÃƒÆ'O",
"Executar campanhas comerciais.",
10),

("EOS005",
"MONITORAMENTO",
"Observar continuamente todos os ecossistemas.",
9),

("EOS006",
"EXECUTIVE COCKPIT",
"Permitir gestÃƒÂ£o humana da plataforma.",
9),

("EOS007",
"CAMPANHAS",
"Gerenciar campanhas de curto, mÃƒÂ©dio e longo prazo.",
9),

("EOS008",
"APRENDIZADO",
"Aprender continuamente com cada operaÃƒÂ§ÃƒÂ£o.",
8)

]

for codigo,nome,missao,criticidade in CAMADAS:

    cursor.execute("""

    INSERT INTO enterprise_layers(

    codigo,

    nome,

    missao,

    criticidade,

    status

    )

    VALUES(?,?,?,?,?)

    """,(

    codigo,

    nome,

    missao,

    criticidade,

    "ATIVO"

    ))

db.commit()

print("="*70)
print("IOTEC ENTERPRISE OPERATING SYSTEM")
print("="*70)
print()

print("CAMADAS EMPRESARIAIS")
print()

print("="*70)

for codigo,nome,missao,criticidade in CAMADAS:

    print()

    print(codigo)

    print(nome)

    print("Criticidade :",criticidade)

    print("MissÃƒÂ£o :",missao)

    print("-"*60)

print()

print("="*70)
print("FLUXO CORPORATIVO")
print("="*70)
print()

fluxo=[

"InteligÃƒÂªncia",

"EstratÃƒÂ©gia",

"Campanha",

"Diretores",

"Equipes",

"Cliente",

"Proposta",

"NegociaÃƒÂ§ÃƒÂ£o",

"Pagamento",

"ProduÃƒÂ§ÃƒÂ£o",

"Entrega",

"PÃƒÂ³s-venda",

"Aprendizado"

]

for i,item in enumerate(fluxo,1):

    print(f"{i:02d} - {item}")

print()

print("="*70)
print("TIPOS DE CAMPANHA")
print("="*70)
print()

tipos=[

"24 HORAS",

"72 HORAS",

"7 DIAS",

"15 DIAS",

"30 DIAS",

"90 DIAS",

"180 DIAS",

"365 DIAS"

]

for t in tipos:

    print("Ã¢â‚¬Â¢",t)

print()

print("="*70)
print("MISSÃƒÆ'O DA PRESIDÃƒÅ NCIA")
print("="*70)
print()

print("A IOTEC passa a operar")
print("como um Sistema")
print("Operacional Empresarial.")

print()

print("Toda implementaÃƒÂ§ÃƒÂ£o")
print("deverÃƒÂ¡ fortalecer")
print("uma destas camadas.")

db.close()


