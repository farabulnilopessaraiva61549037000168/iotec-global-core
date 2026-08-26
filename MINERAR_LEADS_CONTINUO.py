import sqlite3
import requests
import time
import random
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

def gerar_cnpj_aleatorio():
    n = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]
    v1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    d1 = sum(a * b for a, b in zip(n, v1)) % 11
    d1 = 0 if d1 < 2 else 11 - d1
    n.append(d1)
    
    v2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    d2 = sum(a * b for a, b in zip(n, v2)) % 11
    d2 = 0 if d2 < 2 else 11 - d2
    n.append(d2)
    return "".join(map(str, n))

def consultar_brasilapi(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if data.get("descricao_situacao_cadastral") == "ATIVA":
                return {
                    "razao": data.get("razao_social", ""),
                    "email": data.get("email", ""),
                    "telefone": data.get("ddd_telefone_1", ""),
                    "uf": data.get("uf", "")
                }
    except Exception:
        pass
    return None

def minerar_multilote():
    print("============================================================")
    print("   MINERADOR IOTEC 24/7 - MULTI-API (BRASILAPI + RECEITAWS)  ")
    print("============================================================")
    
    total_minerados = 0
    
    while True:
        cnpj = gerar_cnpj_aleatorio()
        lead = consultar_brasilapi(cnpj)
        
        if lead and lead["email"] and "@" in lead["email"]:
            razao = lead["razao"].strip()
            email = lead["email"].strip().lower()
            telefone = lead["telefone"].strip()
            uf = lead["uf"]
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO central_vendas_leads 
                (cnpj, razao_social, email, telefone, score_qualificacao, status_venda)
                VALUES (?, ?, ?, ?, 90.0, 'PRONTO_PARA_ABORDAGEM')
            ''', (cnpj, razao, email, telefone))
            
            if cursor.rowcount > 0:
                total_minerados += 1
                horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                print(f"[{horario}] [✔] NOVO LEAD: {razao} | UF: {uf} | Email: {email}")
                print(f"    └─ Total acumulado na sessão: {total_minerados}")
                
            conn.commit()
            conn.close()
            
        # Intervalo de segurança para consumo de API sem estourar limites gratuitos
        time.sleep(1.2)

if __name__ == "__main__":
    minerar_multilote()
