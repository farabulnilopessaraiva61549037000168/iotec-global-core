import json
import sqlite3
from datetime import datetime

print("==================================================")
print("   IOTEC - FINALIZANDO A CARGA DE LEADS REAIS    ")
print("==================================================")

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

# 1. Recria a tabela com o schema exato do iotec.db
cur.execute("DROP TABLE IF EXISTS leads")
cur.execute("""
CREATE TABLE leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol TEXT,
    timestamp TEXT,
    company TEXT,
    email TEXT,
    status TEXT,
    priority TEXT
)
""")

# 2. Carrega os dados reais minerados do OpenStreetMap
with open("IOTEC_REAL_COMPANIES.json", "r", encoding="utf-8") as f:
    raw = f.read()

data = json.loads(raw)
items = data if isinstance(data, list) else data.get("resultados", [])

inseridos = 0
for item in items:
    nome = item.get("display_name") or item.get("name") or str(item)
    if nome and len(nome.strip()) > 3:
        nome_curto = nome.split(",")[0].strip()
        protocolo = f"PROT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{inseridos+1}"
        
        cur.execute("""
            INSERT INTO leads (protocol, timestamp, company, email, status, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (protocolo, str(datetime.now()), nome_curto, "contato@empresa.com.br", "NOVO_PROSPECT_REAL", "ALTA"))
        print(f"✅ REGISTRADO NO BANCO: {nome_curto}")
        inseridos += 1

conn.commit()
conn.close()

print(f"\n[SUCESSO DEFINITIVO] {inseridos} EMPRESAS REAIS PRONTAS EM IOTEC.DB!")
print("==================================================")
