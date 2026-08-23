import sqlite3

CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

FLOW = {
    "EM_ANALISE": "PROPOSTA_ENVIADA",
    "PROPOSTA_ENVIADA": "PAGAMENTO_PENDENTE",
    "PAGAMENTO_PENDENTE": "AGUARDANDO_PAGAMENTO",
    "AGUARDANDO_PAGAMENTO": "PAGAMENTO_RECEBIDO",
    "PAGAMENTO_RECEBIDO": "CLIENTE_ATIVO"
}

RESPONSAVEL = {
    "PROPOSTA_ENVIADA": "PROPOSAL_ENGINE.py",
    "PAGAMENTO_PENDENTE": "APPROVE_PROPOSAL.py",
    "AGUARDANDO_PAGAMENTO": "PAYMENT_ENGINE.py",
    "PAGAMENTO_RECEBIDO": "CONFIRM_PAYMENT.py",
    "CLIENTE_ATIVO": "CONFIRM_INVOICE30.py / CONFIRM_INVOICE70.py"
}

print("=" * 70)
print("PIPELINE EXECUTION AUDITOR")
print("=" * 70)

conn = sqlite3.connect(CRM_DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""
SELECT
    opportunity_id,
    status,
    payment_status
FROM pipeline
ORDER BY opportunity_id
""").fetchall()

gargalos = 0

for row in rows:

    status = row["status"]
    payment = row["payment_status"]

    print()
    print("-" * 70)
    print(f"Opportunity : {row['opportunity_id']}")
    print(f"Status      : {status}")
    print(f"Pagamento   : {payment}")

    if status in FLOW:

        esperado = FLOW[status]

        print(f"PrÃ³ximo     : {esperado}")

        if esperado == "PAGAMENTO_PENDENTE":

            if payment is None:

                gargalos += 1

                print("RESULTADO   : GARGALO")
                print(f"Arquivo     : {RESPONSAVEL[esperado]}")
                print("Motivo      : Ainda nÃ£o iniciou o fluxo de pagamento.")

        elif esperado == "AGUARDANDO_PAGAMENTO":

            if payment != "AGUARDANDO_PAGAMENTO":

                gargalos += 1

                print("RESULTADO   : GARGALO")
                print(f"Arquivo     : {RESPONSAVEL[esperado]}")
                print("Motivo      : Link de pagamento ainda nÃ£o gerado.")

        elif esperado == "PAGAMENTO_RECEBIDO":

            if payment != "PAGAMENTO_RECEBIDO":

                gargalos += 1

                print("RESULTADO   : GARGALO")
                print(f"Arquivo     : {RESPONSAVEL[esperado]}")
                print("Motivo      : Pagamento ainda nÃ£o confirmado.")

        else:

            print("RESULTADO   : OK")

    else:

        print("RESULTADO   : Estado final ou desconhecido.")

print()
print("=" * 70)
print("RESUMO")
print("=" * 70)
print(f"Gargalos encontrados : {gargalos}")

conn.close()


