import sqlite3

def auditar_banco(nome_db):
    try:
        conn = sqlite3.connect(nome_db)
        c = conn.cursor()
        tabelas = [t[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        print(f"=== {nome_db} ===")
        print(f"Tabelas encontradas: {tabelas}\n")
        conn.close()
    except Exception as e:
        print(f"Erro ao ler {nome_db}: {e}\n")

auditar_banco('iotec_financial.db')
auditar_banco('iotec_payments.db')
auditar_banco('iotec_cashbox.db')
