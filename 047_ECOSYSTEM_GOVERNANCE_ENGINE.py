# ==========================================================
# 047_ECOSYSTEM_GOVERNANCE_ENGINE.py
# IOTEC ECOSYSTEM GOVERNANCE ENGINE
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS ecosystems(

id INTEGER PRIMARY KEY AUTOINCREMENT,

codigo TEXT UNIQUE,

nome TEXT,

responsavel TEXT,

missao TEXT,

fronteira TEXT,

status TEXT,

criticidade INTEGER

)

""")

db.commit()

ECOSSISTEMAS=[

("ECO001","PRESIDÃƒÅ NCIA",
"Presidente",
"Governar toda a IOTEC",
"GLOBAL",
"ATIVO",
10),

("ECO002","COMERCIAL",
"Diretor Comercial",
"Gerar Receita",
"CLIENTES",
"ATIVO",
10),

("ECO003","FINANCEIRO",
"Diretor Financeiro",
"Receber pagamentos",
"PAGAMENTOS",
"ATIVO",
10),

("ECO004","PRODUÃƒâ€¡ÃƒÆ'O",
"Diretor ProduÃƒÂ§ÃƒÂ£o",
"Produzir Produtos",
"ENTREGA",
"ATIVO",
9),

("ECO005","INTELIGÃƒÅ NCIA",
"Chief Intelligence Officer",
"Descobrir conhecimento",
"DADOS",
"ATIVO",
9),

("ECO006","ARQUITETURA",
"Arquiteto Chefe",
"Organizar Plataforma",
"CORE",
"ATIVO",
10),

("ECO007","IA",
"Diretor IA",
"Coordenar Agentes",
"AGENTES",
"ATIVO",
8),

("ECO008","CRM",
"Diretor CRM",
"Relacionamento",
"CLIENTES",
"ATIVO",
8),

("ECO009","JURÃƒÂDICO",
"Diretor JurÃƒÂ­dico",
"Contratos",
"DOCUMENTOS",
"ATIVO",
8),

("ECO010","QUALIDADE",
"Diretor Qualidade",
"Validar Produtos",
"VALIDAÃƒâ€¡ÃƒÆ'O",
"ATIVO",
9)

]

novos=0

for eco in ECOSSISTEMAS:

    cursor.execute("""

    SELECT id

    FROM ecosystems

    WHERE codigo=?

    """,(eco[0],))

    if cursor.fetchone() is None:

        cursor.execute("""

        INSERT INTO ecosystems(

        codigo,

        nome,

        responsavel,

        missao,

        fronteira,

        status,

        criticidade

        )

        VALUES(?,?,?,?,?,?,?)

        """,eco)

        novos+=1

db.commit()

print("="*70)
print("IOTEC ECOSYSTEM GOVERNANCE")
print("="*70)
print()

cursor.execute("""

SELECT

codigo,

nome,

responsavel,

criticidade

FROM ecosystems

ORDER BY criticidade DESC

""")

for codigo,nome,resp,crit in cursor.fetchall():

    print(f"{codigo:<8}{nome:<20} Criticidade:{crit}")
    print("ResponsÃƒÂ¡vel:",resp)
    print("-"*60)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("Ecossistemas registrados :",novos)
print()

print("A IOTEC agora possui")
print("uma estrutura oficial")
print("de governanÃƒÂ§a.")

print()

print("PrÃƒÂ³xima etapa:")

print()

print("Criar os Agentes")
print("de Fronteira.")
print()

db.close()


