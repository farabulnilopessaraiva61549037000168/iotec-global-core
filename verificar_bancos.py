import sqlite3, os

dbs = [f for f in os.listdir(r'C:\IOTEC') if f.endswith('.db')]
print('=== BANCOS DE DADOS ENCONTRADOS ===')
print(dbs)

for db in dbs:
    path = os.path.join(r'C:\IOTEC', db)
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        tables = [t[0] for t in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        print(f'\n---> BANCO: {db}')
        for t in tables:
            count = cursor.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            print(f'     Tabela [{t}]: {count} registros')
        conn.close()
    except Exception as e:
        print(f'Erro ao ler {db}: {e}')
