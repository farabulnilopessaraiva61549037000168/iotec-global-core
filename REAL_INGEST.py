import json
import sqlite3
from datetime import datetime

print("==================================================")
print("   IOTEC REAL PROSPECTION ENGINE (INGESTAO TOTAL)  ")
print("==================================================")

with open("IOTEC_REAL_COMPANIES.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Identifica se o JSON e lista ou dicionario aninhado
if isinstance(data, dict):
    # Procura a primeira chave que seja uma lista de empresas
    items = []
    for k, v in data.items():
        if isinstance(v, list):
            items = v
            break
else:
    items = data

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

# Garantir tabela pronta
cur.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol TEXT,
    timestamp TEXT,
    name TEXT,
    company TEXT,
    status TEXT,
    priority TEXT
)
""")

# Opcional: Limpar demos e mocks fakes antigos
cur.execute("DELETE FROM leads WHERE company LIKE '%DEMONSTRACAO%' OR company LIKE '%ALFA%'")

inseridos = 0
for emp in items:
    # Extrai o nome independente do formato retornado
    nome = ""
    if isinstance(emp, dict):
        nome = emp.get("display_name") or emp.get("name") or emp.get("nome") or emp.get("titulo") or ""
    elif isinstance(emp, str):
        nome = emp
        
    if nome:
        nome_curto = nome.split(",")[0].strip()
        protocolo = f"PROT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{inseridos+1}"
        
        cur.execute("""
            INSERT INTO leads (protocol, timestamp, name, company, status, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (protocolo, str(datetime.now()), nome_curto, nome, "NOVO_PROSPECT_REAL", "ALTA"))
        print(f"✅ REAL REGISTRADO: {nome_curto}")
        inseridos += 1

conn.commit()
conn.close()

print(f"\n[SUCESSO] {inseridos} EMPRESAS REAIS CARREGADAS NO IOTEC.DB!")
print("==================================================")
