import sqlite3

conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
cursor = conn.cursor()

# Garante a estrutura da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        razao_social TEXT UNIQUE,
        cnpj TEXT,
        status TEXT DEFAULT 'PENDENTE'
    )
''')

# Força o commit no banco
conn.commit()
conn.close()
print(" [✔] Estrutura do banco iotec.db sincronizada e pronta para novos commits!")
