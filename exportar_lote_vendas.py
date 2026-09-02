import sqlite3, csv

conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
cursor = conn.cursor()

query = '''
SELECT cnpj, razao_social, email, telefone 
FROM central_vendas_leads 
WHERE email IS NOT NULL AND email != '' 
LIMIT 50
'''

leads = cursor.execute(query).fetchall()

arquivo_csv = r'C:\IOTEC\LOTE_PROSPECCAO_B2B.csv'
with open(arquivo_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['CNPJ', 'RAZAO_SOCIAL', 'EMAIL', 'TELEFONE'])
    writer.writerows(leads)

print(f'✅ {len(leads)} leads exportados com sucesso para: {arquivo_csv}')
conn.close()
