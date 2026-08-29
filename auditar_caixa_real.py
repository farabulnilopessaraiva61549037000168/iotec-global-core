import sqlite3

def ler_dados(db_name, tabela):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        qtd = c.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
        print(f"[{db_name}] -> Tabela '{tabela}': {qtd} registros.")
        if qtd > 0:
            registros = c.execute(f"SELECT * FROM {tabela} LIMIT 5").fetchall()
            print(f"   └─ Primeiros registros: {registros}\n")
        else:
            print("   └─ Sem registros no momento.\n")
        conn.close()
    except Exception as e:
        print(f"Erro ao ler {db_name} / {tabela}: {e}\n")

ler_dados('iotec_cashbox.db', 'cashbox')
ler_dados('iotec_financial.db', 'real_transactions')
ler_dados('iotec_financial.db', 'pending_payments')
ler_dados('iotec_payments.db', 'payments')
