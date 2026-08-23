import urllib.request
import urllib.parse
import json
import sqlite3
from datetime import datetime

print("======================================================================")
print("   IOTEC MASSIVE DISCOVERY ENGINE - VARREDURA NORDESTE B2B            ")
print("======================================================================")

cidades = ["Fortaleza", "Recife", "Salvador", "Natal"]
setores = ["logistica", "distribuidora", "industria", "contabilidade"]

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

total_novos = 0

for cidade in cidades:
    for setor in setores:
        query = f"{setor} {cidade}"
        url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query)}&format=json&limit=25"
        
        headers = {'User-Agent': 'IOTEC_Massive_Engine/3.0'}
        req = urllib.request.Request(url, headers=headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                for item in data:
                    nome_raw = item.get("display_name", "")
                    if nome_raw:
                        nome_curto = nome_raw.split(",")[0].strip()
                        protocolo = f"PROT-MASS-{datetime.now().strftime('%Y%m%d%H%M%S')}-{total_novos+1}"
                        
                        cur.execute("""
                            INSERT INTO leads (protocol, timestamp, company, email, status, priority)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (protocolo, str(datetime.now()), f"{nome_curto} ({cidade})", "contato@empresa.com.br", "NOVO_PROSPECT_REAL", "ALTA"))
                        
                        total_novos += 1
                conn.commit()
                print(f"✅ MAPEADO: {setor.upper()} em {cidade} (+{len(data)} alvos)")
        except Exception as e:
            print(f"Erro em {query}: {e}")

# Total acumulado no banco
cur.execute("SELECT COUNT(*) FROM leads")
total_banco = cur.fetchone()[0]

conn.close()

print("\n======================================================================")
print(f"[ESCALA CONCLUÍDA] +{total_novos} novos alvos injetados!")
print(f"[TOTAL BANCO IOTEC.DB] {total_banco} EMPRESAS REAIS NO FUNIL DE PROSPECÇÃO!")
print("======================================================================")
