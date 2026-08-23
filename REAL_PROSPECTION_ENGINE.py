import json
import sqlite3
from datetime import datetime

print("==================================================")
print("   IOTEC REAL PROSPECTION ENGINE (100% DADOS REAIS)")
print("==================================================")

with open("IOTEC_REAL_COMPANIES.json", "r", encoding="utf-8") as f:
    empresas_reais = json.load(f)

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

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

inseridos = 0
for emp in empresas_reais:
    # Captura o nome da empresa considerando os diferentes formatos do OpenStreetMap
    nome_empresa = emp.get("display_name") or emp.get("name") or emp.get("nome") or ""
    
    if nome_empresa:
        # Pega a primeira parte do nome formatado
        nome_curto = nome_empresa.split(",")[0].strip()
        protocolo = f"PROT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{inseridos+1}"
        
        cur.execute("""
            INSERT INTO leads (protocol, timestamp, name, company, status, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (protocolo, str(datetime.now()), nome_curto, nome_empresa, "NOVO_PROSPECT_REAL", "ALTA"))
        print(f"✅ EMPRESA REAL CARREGADA: {nome_curto}")
        inseridos += 1

conn.commit()
conn.close()

print(f"\n[TOTAL] {inseridos} EMPRESAS REAIS GRAVADAS NO BANCO 'iotec.db'!")
print("==================================================")
