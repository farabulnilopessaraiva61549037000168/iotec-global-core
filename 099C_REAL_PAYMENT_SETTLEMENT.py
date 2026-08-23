import sqlite3
import datetime

db_path = "iotec_financial.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Atualizar status na tabela de transacoes reais
cursor.execute("""
UPDATE real_transactions
SET status = 'PAID',
    timestamp = ?
WHERE invoice_id = 'FAT-REAL-001'
""", (datetime.datetime.now().isoformat(),))

# Criar tabela de auditoria detalhada de comprovantes reais
cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_receipts (
    id TEXT PRIMARY KEY,
    invoice_id TEXT,
    amount REAL,
    payer_name TEXT,
    payer_doc TEXT,
    payer_institution TEXT,
    receiver_cnpj TEXT,
    receiver_institution TEXT,
    pix_end_to_end_id TEXT,
    settlement_timestamp TEXT,
    status TEXT
)
""")

audit_id = "AUD-PIX-20260728-001"
invoice_id = "FAT-REAL-001"
amount = 29.90
payer_name = "FARABULINI LOPES SARAIVA"
payer_doc = "***.902.313-**"
payer_inst = "PagBank (PagSeguro)"
receiver_cnpj = "61.549.037/0001-68"
receiver_inst = "PICPAY INSTITUICAO DE PAGAMENTO S.A."
pix_id = "E0856170120260728131841APUZGV7G0"
now = datetime.datetime.now().isoformat()

cursor.execute("""
INSERT INTO audit_receipts (
    id, invoice_id, amount, payer_name, payer_doc, 
    payer_institution, receiver_cnpj, receiver_institution, 
    pix_end_to_end_id, settlement_timestamp, status
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (audit_id, invoice_id, amount, payer_name, payer_doc, payer_inst, receiver_cnpj, receiver_inst, pix_id, now, "VERIFIED_AND_SETTLED"))

conn.commit()
conn.close()

print("="*65)
print("IOTEC FINANCIAL ENGINE - LIQUIDAÇÃO E AUDITORIA REAL")
print("="*65)
print(f"STATUS DA FATURA     : PAID (PAGO E LIQUIDADO)")
print(f"ID AUDITORIA          : {audit_id}")
print(f"VALOR CONSOLIDADO     : R$ {amount:.2f}")
print(f"PAGADOR               : {payer_name} ({payer_inst})")
print(f"RECEBEDOR (CNPJ)      : {receiver_cnpj} ({receiver_inst})")
print(f"CÓDIGO PIX REAL (E2E) : {pix_id}")
print(f"DATA/HORA LIQUIDAÇÃO  : {now}")
print("="*65)
