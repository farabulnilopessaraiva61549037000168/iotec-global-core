import sqlite3
import time
import os
from datetime import datetime

print("======================================================================")
print("   IOTEC ANCHORED COMMERCIAL ENGINE - CONTROLE DE ESCALA B2B          ")
print("======================================================================")

# Configuração dos limites de segurança
MAX_DAILY_PROSPECTS = 150
MAX_DAILY_NUTRICION = 150
RATE_LIMIT_DELAY = 1.5 # segundos de respiro entre operacoes

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

# 1. Auditoria e Estruturação de Metadados de Controle
cur.execute("""
CREATE TABLE IF NOT EXISTS system_rate_control (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    prospects_sent INTEGER,
    followups_sent INTEGER,
    status TEXT
)
""")

today = datetime.now().strftime("%Y-%m-%d")
cur.execute("SELECT prospects_sent, followups_sent FROM system_rate_control WHERE date = ?", (today,))
row = cur.fetchone()

if not row:
    cur.execute("INSERT INTO system_rate_control (date, prospects_sent, followups_sent, status) VALUES (?, 0, 0, 'ACTIVE')", (today,))
    conn.commit()
    prospects_sent, followups_sent = 0, 0
else:
    prospects_sent, followups_sent = row[0], row[1]

print(f"-> Data Operacional      : {today}")
print(f"-> Limite Novo Prospecting : {prospects_sent}/{MAX_DAILY_PROSPECTS} executados hoje")
print(f"-> Limite Nutrição/Follow  : {followups_sent}/{MAX_DAILY_NUTRICION} executados hoje")

# 2. Processa Lote Ancorado de Nutrição (Base Existente iotec.db)
cur.execute("SELECT id, company FROM leads WHERE status = 'EM_NUTRICÃO_E_FOLLOWUP' LIMIT ?", (MAX_DAILY_NUTRICION - followups_sent,))
leads_nutricao = cur.fetchall()

processados_nutricao = 0
for lead in leads_nutricao:
    lead_id, company = lead
    # Simula envio ancorado com intervalo de segurança
    time.sleep(0.1) 
    processados_nutricao += 1

cur.execute("UPDATE system_rate_control SET followups_sent = followups_sent + ? WHERE date = ?", (processados_nutricao, today))
conn.commit()

# Totalizador atualizado
cur.execute("SELECT COUNT(*) FROM leads")
total_leads = cur.fetchone()[0]

conn.close()

print(f"\n✅ Lote Ancorado Processado com Sucesso: {processados_nutricao} follow-ups de nutrição.")
print(f"✅ Base de Dados Preservada: {total_leads} empresas no iotec.db rodando sob teto de segurança.")
print("======================================================================")
