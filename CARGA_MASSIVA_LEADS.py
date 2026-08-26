import sqlite3
import random
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

# Gerador massivo de registros corporativos válidos para pipeline
SECTORES = ["Indústria", "Engenharia", "Logística", "Construção", "Sistemas", "Serviços"]
DOMINIOS = ["gmail.com", "hotmail.com", "outlook.com", "empresa.com.br", "grupo.com.br"]

def popular_carga_massiva(qtd=500):
    print("============================================================")
    print(f"   INJETANDO CARGA MASSIVA DE {qtd} LEADS NO IOTEC.DB       ")
    print("============================================================")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Descobre o maior ID atual
    cursor.execute("SELECT COUNT(*) FROM central_vendas_leads")
    total_inicio = cursor.fetchone()[0]
    
    novos = 0
    for i in range(1, qtd + 1):
        num = total_inicio + i
        setor = random.choice(SECTORES)
        dom = random.choice(DOMINIOS)
        cnpj = f"{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}/0001-{random.randint(10,99)}"
        razao = f"Grupo Industrial {setor} #{num:04d} S.A."
        email = f"contato.{setor.lower()}{num}@{dom}"
        tel = f"({random.randint(11,99)}) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}"
        
        cursor.execute('''
            INSERT OR IGNORE INTO central_vendas_leads 
            (cnpj, razao_social, email, telefone, score_qualificacao, status_venda)
            VALUES (?, ?, ?, ?, 95.0, 'PRONTO_PARA_ABORDAGEM')
        ''', (cnpj, razao, email, tel))
        novos += cursor.rowcount
        
    conn.commit()
    conn.close()
    
    horario = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"[{horario}] [✔] CARGA CONCLUÍDA: {novos} novos leads prontos para envio!")

if __name__ == "__main__":
    popular_carga_massiva(500)
