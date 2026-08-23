import sqlite3

CRM_DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

print()
print("="*70)
print("FLOW ANALYZER")
print("="*70)

conn = sqlite3.connect(CRM_DB)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ---------- LEADS ----------
leads = cur.execute("SELECT COUNT(*) FROM leads").fetchone()[0]

# ---------- OPPORTUNITIES ----------
opp = cur.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]

# ---------- PIPELINE ----------
pipe = cur.execute("SELECT COUNT(*) FROM pipeline").fetchone()[0]

print()
print("ESTRUTURA")

print(f"Leads................. {leads}")
print(f"Opportunities......... {opp}")
print(f"Pipeline.............. {pipe}")

print()

print("PIPELINE STATUS")

for row in cur.execute("""
SELECT
IFNULL(status,'NULL'),
COUNT(*)
FROM pipeline
GROUP BY status
ORDER BY COUNT(*) DESC
"""):
    print(f"{row[0]:30} {row[1]}")

print()

print("PAYMENT STATUS")

for row in cur.execute("""
SELECT
IFNULL(payment_status,'NULL'),
COUNT(*)
FROM pipeline
GROUP BY payment_status
ORDER BY COUNT(*) DESC
"""):
    print(f"{row[0]:30} {row[1]}")

print()

print("="*70)
print("ROOT CAUSE")
print("="*70)

proposta = cur.execute("""
SELECT COUNT(*)
FROM pipeline
WHERE status='PROPOSTA_ENVIADA'
""").fetchone()[0]

pag_pendente = cur.execute("""
SELECT COUNT(*)
FROM pipeline
WHERE status='PAGAMENTO_PENDENTE'
""").fetchone()[0]

aguardando = cur.execute("""
SELECT COUNT(*)
FROM pipeline
WHERE payment_status='AGUARDANDO_PAGAMENTO'
""").fetchone()[0]

recebido = cur.execute("""
SELECT COUNT(*)
FROM pipeline
WHERE payment_status='PAGAMENTO_RECEBIDO'
""").fetchone()[0]

if proposta > 0 and pag_pendente == 0:

    print()
    print("GARGALO DETECTADO")
    print("------------------------------")
    print("Existem propostas enviadas")
    print("mas nenhuma entrou em")
    print("PAGAMENTO_PENDENTE.")
    print()
    print("Arquivo provÃ¡vel:")
    print("PAYMENT_ENGINE.py")
    print()
    print("Prioridade: ALTA")

elif aguardando > 0:

    print()
    print("Existem pagamentos aguardando confirmaÃ§Ã£o.")

elif recebido > 0:

    print()
    print("Existem pagamentos recebidos.")

else:

    print()
    print("Nenhum gargalo encontrado.")

conn.close()


