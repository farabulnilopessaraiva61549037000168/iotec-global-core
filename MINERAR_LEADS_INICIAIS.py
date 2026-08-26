import sqlite3
import requests

DB_PATH = "C:\\IOTEC\\iotec.db"

CNPJS_PARA_MINERAR = [
    "00000000000191", # Banco do Brasil
    "33000167000101", # Petrobras
    "60701190000104", # Itaú
    "02558157000162"  # Telefônica / Vivo
]

def minerar_lote_inicial():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS central_vendas_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnpj TEXT UNIQUE,
            razao_social TEXT,
            email TEXT,
            telefone TEXT,
            score_qualificacao REAL,
            status_venda TEXT DEFAULT 'MINERADO',
            link_checkout TEXT,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("[*] Conectando ao iotec.db e minerando dados nas APIs publicas...\n")
    
    for cnpj in CNPJS_PARA_MINERAR:
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if data.get("situacao") == "ATIVA":
                    razao = data.get("nome", "EMPRESA")
                    email = data.get("email", "")
                    telefone = data.get("telefone", "")
                    
                    cursor.execute('''
                        INSERT OR REPLACE INTO central_vendas_leads 
                        (cnpj, razao_social, email, telefone, score_qualificacao, status_venda)
                        VALUES (?, ?, ?, ?, 95.0, 'PRONTO_PARA_ABORDAGEM')
                    ''', (cnpj, razao, email, telefone))
                    
                    print(f"[✔] Minerado: {razao} | Tel: {telefone} | Email: {email}")
        except Exception as e:
            print(f"[-] Erro ao buscar CNPJ {cnpj}: {e}")
            
    conn.commit()
    
    cursor.execute("SELECT COUNT(*) FROM central_vendas_leads")
    total = cursor.fetchone()[0]
    print(f"\n[+] Operacao concluida! Total de leads ativos no iotec.db: {total}")
    conn.close()

if __name__ == "__main__":
    minerar_lote_inicial()
