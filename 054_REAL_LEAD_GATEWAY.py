# ==========================================================
# 054_REAL_LEAD_GATEWAY.py
# IOTEC REAL LEAD GATEWAY
# ==========================================================

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS real_leads(

id INTEGER PRIMARY KEY AUTOINCREMENT,

empresa TEXT,

contato TEXT,

telefone TEXT,

email TEXT,

cidade TEXT,

estado TEXT,

segmento TEXT,

interesse TEXT,

origem TEXT,

status TEXT,

prioridade TEXT,

data_cadastro TEXT

)

""")

db.commit()

print("="*70)
print("IOTEC REAL LEAD GATEWAY")
print("="*70)
print()

cursor.execute("SELECT COUNT(*) FROM real_leads")

total = cursor.fetchone()[0]

print("Leads reais cadastrados :", total)
print()

print("="*70)
print("CANAIS OFICIAIS")
print("="*70)
print()

canais = [

"Website",

"WhatsApp Business",

"LinkedIn",

"Google Business",

"E-mail Corporativo",

"IndicaÃƒÂ§ÃƒÂ£o",

"Visita Comercial",

"Telefone"

]

for i,canal in enumerate(canais,1):

    print(f"{i:02d} - {canal}")

print()

print("="*70)
print("PROCESSO")
print("="*70)
print()

etapas=[

"Receber Lead",

"Validar Dados",

"Eliminar Duplicidade",

"Registrar CRM",

"Enviar para Control Tower",

"Despachar Agente Comercial",

"Iniciar Atendimento"

]

for i,e in enumerate(etapas,1):

    print(f"{i:02d} - {e}")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A partir deste ponto")
print("a IOTEC estÃƒÂ¡ preparada")
print("para registrar")
print("clientes reais.")

print()

print("Nenhum lead deverÃƒÂ¡")
print("entrar diretamente")
print("no Comercial.")

print()

print("Todo lead passa")
print("pelo Gateway Oficial.")

print()

print("Data :",datetime.now())

db.close()


