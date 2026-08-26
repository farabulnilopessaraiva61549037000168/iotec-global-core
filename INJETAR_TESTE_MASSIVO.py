import sqlite3
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Injeta venda com pagamento confirmado no gateway
cnpj = "11.222.333/0001-99"
empresa = "Titanium Soluções Industriais & Governança S.A."
email = "diretoria@titaniumind.com.br"
relato_dor = "Preciso de auditoria forense, governança corporativa e monitoramento em tempo real do canteiro de obras."

cursor.execute('''
    INSERT OR REPLACE INTO central_vendas_leads 
    (cnpj, razao_social, email, score_qualificacao, status_venda)
    VALUES (?, ?, ?, 100.0, 'PAGAMENTO_CONFIRMADO')
''', (cnpj, empresa, email))

conn.commit()
conn.close()

print(f"[💰 GATEWAY] Pagamento de R$ 2.500,00 RECONHECIDO!")
print(f" ├─ Cliente: {empresa}")
print(f" └─ Requisito: \"{relato_dor}\"")
print(" [✔] Lead liberado para o Agente Arquiteto na fila do iotec.db.\n")
