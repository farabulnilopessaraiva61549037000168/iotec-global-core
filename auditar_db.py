import sqlite3
import os

db_path = r'C:\IOTEC\iotec.db'

if os.path.exists(db_path):
    print('==================================================')
    print('         AUDITORIA DE BANCO DE DADOS IOTEC.DB     ')
    print('==================================================')
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print('[?] BANCO LOCALIZADO. Tabelas encontradas:')
        
        total_geral = 0
        for t in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {t[0]}")
            qtd = cursor.fetchone()[0]
            total_geral += qtd
            print(f'  - Tabela: {t[0]} | Registros: {qtd}')
            
        print('--------------------------------------------------')
        print(f'TOTAL DE REGISTROS NO BANCO: {total_geral}')
        conn.close()
    except Exception as e:
        print(f'[!] Erro ao ler banco: {e}')
else:
    print('[!] O arquivo C:\\IOTEC\\iotec.db nao foi localizado.')
