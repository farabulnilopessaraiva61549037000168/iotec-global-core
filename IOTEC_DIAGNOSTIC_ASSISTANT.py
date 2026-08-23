title("ROOT CAUSE ANALYSIS")

try:

    conn = sqlite3.connect(CRM_DB)
    cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

    print("PASSO 1/6  Verificando Leads...")
    leads = cur.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    print(f"OK ({leads})")

    print("PASSO 2/6  Verificando Opportunities...")
    opp = cur.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"OK ({opp})")

    print("PASSO 3/6  Verificando Pipeline...")
    pipe = cur.execute("SELECT COUNT(*) FROM pipeline").fetchone()[0]
    print(f"OK ({pipe})")

    print("PASSO 4/6  Estados do Pipeline")
    estados = cur.execute("""
        SELECT status,
               COUNT(*)
        FROM pipeline
        GROUP BY status
    """).fetchall()

    for status, qtd in estados:
        print(f"   {status:<25} {qtd}")

    print()

    print("PASSO 5/6  Payment Status")

    pagamentos = cur.execute("""
        SELECT
            IFNULL(payment_status,'NULL'),
            COUNT(*)
        FROM pipeline
        GROUP BY payment_status
    """).fetchall()

    for status, qtd in pagamentos:
        print(f"   {status:<25} {qtd}")

    print()

    aguardando = cur.execute("""
        SELECT COUNT(*)
        FROM pipeline
        WHERE status='PAGAMENTO_PENDENTE'
    """).fetchone()[0]

    print("PASSO 6/6  Resultado")

    if aguardando == 0:

        print()
        print("GARGALO ENCONTRADO")
        print("------------------------------")
        print("PAYMENT_ENGINE nÃƒÂ£o possui")
        print("nenhum registro para processar.")
        print()
        print("CAUSA")
        print("O PAYMENT_ENGINE procura")
        print("status='PAGAMENTO_PENDENTE'")
        print("e atualmente existem:")
        print()

        for status, qtd in estados:
            print(f" - {status}: {qtd}")

    else:

        print("PAYMENT_ENGINE possui registros para processar.")

    conn.close()

except Exception as erro:

    print("[ERRO]", erro)

