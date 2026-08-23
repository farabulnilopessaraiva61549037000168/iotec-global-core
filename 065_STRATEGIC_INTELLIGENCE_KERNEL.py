# ==========================================================
# 065_STRATEGIC_INTELLIGENCE_KERNEL.py
# IOTEC STRATEGIC INTELLIGENCE KERNEL
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS strategic_targets(

id INTEGER PRIMARY KEY AUTOINCREMENT,

empresa TEXT,

segmento TEXT,

cidade TEXT,

estado TEXT,

pais TEXT,

porte TEXT,

faturamento_estimado TEXT,

poder_compra INTEGER,

compatibilidade INTEGER,

valor_estrategico INTEGER,

probabilidade INTEGER,

campanha TEXT,

status TEXT,

fonte TEXT,

observacoes TEXT

)

""")

db.commit()

print("="*70)
print("IOTEC STRATEGIC INTELLIGENCE KERNEL")
print("="*70)
print()

print("MISSÃƒÆ'O")
print()

print("Encontrar empresas")
print("que realmente")
print("merecem atenÃƒÂ§ÃƒÂ£o.")
print()

print("="*70)
print("CRITÃƒâ€°RIOS DE ANÃƒÂLISE")
print("="*70)
print()

criterios=[

"Segmento",

"Porte",

"LocalizaÃƒÂ§ÃƒÂ£o",

"Poder de compra",

"Compatibilidade",

"Valor estratÃƒÂ©gico",

"Probabilidade de fechamento",

"Necessidade estimada",

"Origem da oportunidade"

]

for i,item in enumerate(criterios,1):

    print(f"{i:02d} - {item}")

print()

print("="*70)
print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")
print("="*70)
print()

print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ PRIORIDADE MÃƒÂXIMA")
print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦  PRIORIDADE ALTA")
print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦   PRIORIDADE MÃƒâ€°DIA")
print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦    PRIORIDADE BAIXA")
print("Ã¢Ëœâ€¦     OBSERVAÃƒâ€¡ÃƒÆ'O")

print()

print("="*70)
print("DESTINOS POSSÃƒÂVEIS")
print("="*70)
print()

destinos=[

"Tecnologia",

"IndÃƒÂºstrias",

"Hospitais",

"Prefeituras",

"Universidades",

"Escolas",

"EscritÃƒÂ³rios",

"Construtoras",

"AgronegÃƒÂ³cio",

"ComÃƒÂ©rcio"

]

for item in destinos:

    print("Ã¢â‚¬Â¢",item)

print()

print("="*70)
print("FONTES FUTURAS")
print("="*70)
print()

fontes=[

"Google Maps",

"LinkedIn",

"Sites Corporativos",

"Receita PÃƒÂºblica",

"Bases PÃƒÂºblicas",

"IndicaÃƒÂ§ÃƒÂµes",

"CRM",

"Campanhas anteriores"

]

for item in fontes:

    print("Ã¢â‚¬Â¢",item)

print()

print("="*70)
print("MISSÃƒÆ'O DA PRESIDÃƒÅ NCIA")
print("="*70)
print()

print("Nenhuma empresa")
print("entra em campanha")
print("sem anÃƒÂ¡lise")
print("estratÃƒÂ©gica.")

print()

print("O Kernel passa")
print("a produzir")
print("alvos qualificados.")

db.close()


