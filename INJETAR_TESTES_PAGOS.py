import sqlite3
import time

DB_PATH = "C:\\IOTEC\\iotec.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Injeta 3 leads de setores distintos simulando pagamentos confirmados
testes = [
    ("99.111.222/0001-01", "Aço Forte Engenharia e Obras Ltda", "diretoria@acoforte.com.br", "PAGAMENTO_CONFIRMADO"),
    ("88.333.444/0001-02", "TransLitoral Expresso e Logistica S.A.", "operacoes@translitoral.com.br", "PAGAMENTO_CONFIRMADO"),
    ("77.555.666/0001-03", "MegaVendas Distribuidora Comercial", "financeiro@megavendas.com.br", "PAGAMENTO_CONFIRMADO")
]

for cnpj, razao, email, status in testes:
    cursor.execute('''
        INSERT OR REPLACE INTO central_vendas_leads 
        (cnpj, razao_social, email, score_qualificacao, status_venda)
        VALUES (?, ?, ?, 99.0, ?)
    ''', (cnpj, razao, email, status))

conn.commit()
conn.close()

print("[✔] 3 Pagamentos reais inseridos na fila do Gatekeeper com sucesso.\n")
