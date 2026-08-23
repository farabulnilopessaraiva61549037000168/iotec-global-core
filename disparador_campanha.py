import csv
import sqlite3
import datetime
import time

DB_PATH = r"C:\IOTEC\data_store.db"
CSV_PATH = r"C:\IOTEC\lista_prospeccao_iotec.csv"

# 1. CRIAR BASE INICIAL DE PROSPECÇÃO B2B (CSV)
leads_exemplo = [
    ["Empresa / Grupo", "Perfil / Setor", "Frente de Ataque", "Contato / Cargo", "E-mail / Canal", "Status"],
    ["Wilson Sons Logistics", "Operador Logístico / Porto", "Enterprise (R$ 4.500/mês)", "Diretor de Coméx", "comex@wilsonsons.com.br", "PRONTO"],
    ["Pinho Logística", "Despachante Aduaneiro", "Parceiros (15% Comissão)", "Sócio Operacional", "contato@pinhologistica.com.br", "PRONTO"],
    ["Asia Shipping", "Agenciamento Marítimo", "Enterprise (R$ 4.500/mês)", "Head de Tax & Fiscal", "tax@asiashipping.com.br", "PRONTO"],
    ["Contabilizei Corporativo", "Contabilidade B2B", "Parceiros (15% Comissão)", "Gerente de Parcerias", "parceiros@contabilizei.com.br", "PRONTO"],
    ["Importadora & Indústria Química", "Importador Direto", "Certidão NCM (R$ 250,00)", "Controller Fiscal", "fiscal@importquimica.com.br", "PRONTO"]
]

with open(CSV_PATH, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerows(leads_exemplo)

print(f"✅ Lista de Leads gerada com sucesso em: {CSV_PATH}")

# 2. REGISTRAR A CAMPANHA DE DISPARO NO BANCO DE DADOS SQLITE
def registrar_campanha_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campanhas_prospeccao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            empresa TEXT,
            frente TEXT,
            canal TEXT,
            status TEXT
        )
    """)
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for lead in leads_exemplo[1:]:
        cursor.execute("""
            INSERT INTO campanhas_prospeccao (timestamp, empresa, frente, canal, status)
            VALUES (?, ?, ?, ?, ?)
        """, (now_str, lead[0], lead[2], lead[4], "DISPARADO"))
        
    conn.commit()
    conn.close()
    print("🚀 Todos os disparos foram registrados na tabela 'campanhas_prospeccao' do SQLite!")

registrar_campanha_banco()