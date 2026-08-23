import json
import sqlite3
from datetime import datetime

print("==================================================")
print("   INSPEÇÃO E INGESTÃO DE EMPRESAS REAIS         ")
print("==================================================")

with open("IOTEC_REAL_COMPANIES.json", "r", encoding="utf-8") as f:
    raw = f.read()

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

# Garantir tabela pronta no banco oficial
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

# Expurga registros antigos de teste/demonstração
cur.execute("DELETE FROM leads WHERE company LIKE '%DEMONSTRA%' OR name LIKE '%DEMONSTRA%'")

inseridos = 0

try:
    data = json.loads(raw)
    
    # Se for uma lista de itens
    if isinstance(data, list):
        lista = data
    # Se for um dicionário, busca a lista em qualquer uma das chaves
    elif isinstance(data, dict):
        lista = []
        for val in data.values():
            if isinstance(val, list):
                lista.extend(val)
    else:
        lista = []

    for item in lista:
        nome_completo = ""
        if isinstance(item, dict):
            nome_completo = item.get("display_name") or item.get("name") or item.get("nome") or item.get("empresa") or ""
        elif isinstance(item, str):
            nome_completo = item

        if nome_completo and len(nome_completo.strip()) > 2:
            nome_curto = nome_completo.split(",")[0].strip()
            protocolo = f"PROT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{inseridos+1}"
            
            cur.execute("""
                INSERT INTO leads (protocol, timestamp, name, company, status, priority)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (protocolo, str(datetime.now()), nome_curto, nome_completo, "NOVO_PROSPECT_REAL", "ALTA"))
            
            print(f"✅ REGISTRADO REAL: {nome_curto}")
            inseridos += 1

except Exception as e:
    print(f"Erro na conversão direta de JSON: {e}")
    # Backup: se for texto puro formatado linha a linha
    lines = [line.strip() for line in raw.split('\n') if line.strip() and not line.startswith('{') and not line.startswith('[')]
    for line in lines:
        protocolo = f"PROT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{inseridos+1}"
        cur.execute("""
            INSERT INTO leads (protocol, timestamp, name, company, status, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (protocolo, str(datetime.now()), line.split(',')[0], line, "NOVO_PROSPECT_REAL", "ALTA"))
        print(f"✅ REGISTRADO REAL (TEXTO): {line.split(',')[0]}")
        inseridos += 1

conn.commit()
conn.close()

print(f"\n[FINAL] {inseridos} EMPRESAS REAIS INJETADAS EM IOTEC.DB")
print("==================================================")
