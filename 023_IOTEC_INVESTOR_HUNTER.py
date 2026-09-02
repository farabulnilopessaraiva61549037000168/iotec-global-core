import sqlite3
import json
from datetime import datetime

# 1. Conexao com o Banco do Nucleo
conn = sqlite3.connect(r'C:\IOTEC\iotec_kernel.db')
cursor = conn.cursor()

# 2. Tabela de Inteligencia de Investidores
cursor.execute('''
CREATE TABLE IF NOT EXISTS iotec_investor_leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_fundo_anjo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    tese TEXT,
    foco_geografico TEXT,
    contato_email TEXT,
    status TEXT DEFAULT 'Mapeado',
    data_criacao DATETIME
)
''')

# 3. Tabela do Escritorio Virtual (Triagem da Sala de Atendimento)
cursor.execute('''
CREATE TABLE IF NOT EXISTS iotec_investor_virtual_room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    whatsapp_jid TEXT NOT NULL UNIQUE,
    nome TEXT,
    perfil TEXT, -- 'Curioso', 'Investidor Anjo', 'Fundo VC'
    ticket_pretendido TEXT,
    nda_aceito INTEGER DEFAULT 0,
    data_atendimento DATETIME
)
''')

# 4. Insercao de Teses e Bases Estrategicas
perfis = [
    ('Bossa Invest', 'Micro-VC', 'SaaS B2B, Fintech', 'Brasil / EUA', 'ri@bossainvest.com'),
    ('Delaware Angels Network', 'Anjo', 'Holding Delaware, Dolar', 'EUA / LATAM', 'delaware@angels.com'),
    ('BNB Inovacao', 'Corporate Banking', 'Infraestrutura Tecnologica', 'Brasil', 'inovacao@bnb.gov.br'),
    ('GAVEA Angels', 'Anjo', 'Startups Early Stage', 'Brasil', 'contato@gaveaangels.org.br')
]

for nome, tipo, tese, geo, email in perfis:
    cursor.execute('''
    INSERT INTO iotec_investor_leads (nome_fundo_anjo, tipo, tese, foco_geografico, contato_email, data_criacao)
    SELECT ?, ?, ?, ?, ?, ? WHERE NOT EXISTS (
        SELECT 1 FROM iotec_investor_leads WHERE nome_fundo_anjo = ?
    )
    ''', (nome, tipo, tese, geo, email, datetime.now(), nome))

conn.commit()
conn.close()
print('[IOTEC PYTHON] Banco de dados e tabelas do Virtual Investor Room inicializados.')
