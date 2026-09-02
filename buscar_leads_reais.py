import sqlite3

conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
cursor = conn.cursor()

def checar_tabela(tabela):
    print(f'=== AMOSTRA DA TABELA: {tabela} ===')
    try:
        cols = [col[1] for col in cursor.execute(f'PRAGMA table_info({tabela});').fetchall()]
        print('Colunas:', cols)
        
        # Busca 5 registros que tenham dados preenchidos
        rows = cursor.execute(f'SELECT * FROM {tabela} LIMIT 5;').fetchall()
        for r in rows:
            print(r)
    except Exception as e:
        print('Erro:', e)
    print('\n')

checar_tabela('central_vendas_leads')
checar_tabela('lead_contacts')

conn.close()
