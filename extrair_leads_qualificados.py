import sqlite3

conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
cursor = conn.cursor()

print('=== LEADS QUALIFICADOS PARA ABORDAGEM B2B ===\n')
try:
    cols = [col[1] for col in cursor.execute("PRAGMA table_info(leads_qualificados);").fetchall()]
    print("Colunas encontradas:", cols)
    
    rows = cursor.execute("SELECT * FROM leads_qualificados LIMIT 15;").fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("Erro ao ler tabela:", e)

conn.close()
