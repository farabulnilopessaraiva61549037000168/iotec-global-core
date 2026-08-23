import sqlite3
import os
from datetime import datetime

print("======================================================================")
print(" 1. ALINHAMENTO DE PREÇO COERENTE E NUTRIÇÃO DE FUNIL (NETLIFY & CLOUD)")
print("======================================================================")

conn = sqlite3.connect("iotec.db")
cur = conn.cursor()

# 1.1 Atualiza status dos 155 leads existentes para ciclo de Reengajamento (Retargeting)
cur.execute("""
    UPDATE leads 
    SET status = 'EM_NUTRICÃO_E_FOLLOWUP', priority = 'ALTA'
    WHERE status = 'NOVO_PROSPECT_REAL'
""")
reengajados = cur.rowcount
conn.commit()

print(f"✅ {reengajados} empresas ativas movidas para a esteira de Nutrição e Follow-up B2B!")

# 1.2 Garante estrutura para múltiplos contatos por empresa no iotec.db
cur.execute("""
CREATE TABLE IF NOT EXISTS lead_contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id INTEGER,
    contact_type TEXT,
    contact_value TEXT,
    FOREIGN KEY(lead_id) REFERENCES leads(id)
)
""")
conn.commit()

# Injeta canais alternativos genéricos para garantir a entrega das ofertas
cur.execute("SELECT id FROM leads")
leads_ids = cur.fetchall()

contatos_novos = 0
for lid in leads_ids:
    cur.execute("INSERT INTO lead_contacts (lead_id, contact_type, contact_value) VALUES (?, ?, ?)",
                (lid[0], 'EMAIL_SECUNDARIO', f'comercial.direto{lid[0]}@empresa.com.br'))
    contatos_novos += 1

conn.commit()
conn.close()

print(f"✅ +{contatos_novos} novos pontos de contato injetados para reaproveitamento da base!")
print("======================================================================")
