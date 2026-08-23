import sqlite3
import datetime
import uuid

db_path = "iotec_financial.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar tabela de auditoria real se nao existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS real_transactions (
    id TEXT PRIMARY KEY,
    invoice_id TEXT,
    amount REAL,
    pix_key TEXT,
    status TEXT,
    payment_type TEXT,
    timestamp TEXT
)
""")

trans_id = f"REAL-PIX-{uuid.uuid4().hex[:8].upper()}"
invoice_id = "FAT-REAL-001"
amount = 29.90
pix_key = "a4b216a6-852e-4937-b796-fe7c27730595"
now = datetime.datetime.now().isoformat()

cursor.execute("""
INSERT INTO real_transactions (id, invoice_id, amount, pix_key, status, payment_type, timestamp)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (trans_id, invoice_id, amount, pix_key, "PENDING_CONFIRMATION", "MANUAL_PIX", now))

conn.commit()
conn.close()

print("="*60)
print("AGENTE INTERNO IOTEC - REGISTRO DE COBRANÇA REAL")
print("="*60)
print(f"ID TRANSAÇÃO : {trans_id}")
print(f"FATURA       : {invoice_id}")
print(f"VALOR REAL   : R$ {amount:.2f}")
print(f"CHAVE PIX    : {pix_key}")
print(f"STATUS       : PENDING_CONFIRMATION (Aguardando PIX Real)")
print("="*60)
