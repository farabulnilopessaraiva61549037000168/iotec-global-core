# ==========================================================
# 053_CLIENT_ORCHESTRATOR_ENGINE.py
# IOTEC CLIENT ORCHESTRATOR
# ==========================================================

import sqlite3

DB="iotec_kernel.db"

db=sqlite3.connect(DB, timeout=30)
cursor=db.cursor()

# ==========================================================
# FILA DE ATENDIMENTO
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS client_queue(

id INTEGER PRIMARY KEY AUTOINCREMENT,

nome TEXT,

empresa TEXT,

origem TEXT,

objetivo TEXT,

categoria TEXT,

prioridade TEXT,

status TEXT,

ecossistema_destino TEXT,

agente_designado TEXT,

data_entrada TEXT

)

""")

db.commit()

print("="*70)
print("IOTEC CLIENT ORCHESTRATOR")
print("="*70)
print()

print("PORTA OFICIAL DE ENTRADA DA IOTEC")
print()

CATEGORIAS=[

("CONSULTORIA","COMERCIAL"),

("AUTOMAÃƒâ€¡ÃƒÆ'O","COMERCIAL"),

("SOFTWARE","COMERCIAL"),

("ROBÃƒâ€œTICA","COMERCIAL"),

("PERÃƒÂCIA DIGITAL","COMERCIAL"),

("SUPORTE","CRM"),

("FINANCEIRO","FINANCEIRO"),

("PARCERIA","PRESIDÃƒÅ NCIA")

]

print("="*70)
print("ROTAS DE ATENDIMENTO")
print("="*70)
print()

for categoria,destino in CATEGORIAS:

    print(f"{categoria:<20} ---> {destino}")

print()

print("="*70)
print("FLUXO OFICIAL")
print("="*70)
print()

fluxo=[

"Cliente chega",

"RecepÃƒÂ§ÃƒÂ£o",

"Triagem",

"IdentificaÃƒÂ§ÃƒÂ£o",

"Escolha da categoria",

"Control Tower",

"Mission Dispatch",

"Agente",

"Ecossistema",

"Produto",

"Pagamento",

"ProduÃƒÂ§ÃƒÂ£o",

"Qualidade",

"Entrega",

"PÃƒÂ³s-venda"

]

for i,item in enumerate(fluxo,1):

    print(f"{i:02d} - {item}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A IOTEC agora possui")
print("uma porta oficial")
print("para receber clientes.")

print()

print("Todo atendimento")
print("deverÃƒÂ¡ comeÃƒÂ§ar")
print("neste Orquestrador.")

db.close()


