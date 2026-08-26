import sqlite3
import requests

DB_PATH = "C:\\IOTEC\\iotec_database.db"

def executar_central():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS central_vendas_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnpj TEXT UNIQUE, razao_social TEXT, email TEXT, 
            telefone TEXT, status_venda TEXT, link_checkout TEXT
        )
    ''')
    conn.commit()
    print("[+] Central de Vendas e Relacionamento IOTEC Inicializada com Sucesso.")

if __name__ == "__main__":
    executar_central()
