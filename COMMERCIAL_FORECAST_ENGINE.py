import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("===================================")
print("COMMERCIAL FORECAST ENGINE")
print("===================================")
print("")

rows = cur.execute("""

SELECT

    company,
    estimated_value,
    lead_score,
    status

FROM commercial_opportunities

""").fetchall()

pipeline_total = 0
receita_provavel = 0

negociacao = 0
pagamento_pendente = 0
proposta_enviada = 0
em_analise = 0

for row in rows:
    pass

    empresa = row[0]
    valor = row[1]
    score = row[2]
    status = row[3]

    pipeline_total += valor

    chance = score

    if status == "NEGOCIACAO":
        chance += 30
        negociacao += valor

    elif status == "PAGAMENTO_PENDENTE":
        chance += 40
        pagamento_pendente += valor

    elif status == "PROPOSTA_ENVIADA":
        chance += 20
        proposta_enviada += valor

    elif status == "EM_ANALISE":
        chance += 10
        em_analise += valor

    if chance > 100:
        chance = 100

    receita_provavel += valor * (chance / 100)

conversao = 0

if pipeline_total > 0:
    conversao = (
        receita_provavel /
        pipeline_total
    ) * 100

print("PIPELINE TOTAL:")
print(f"R$ {pipeline_total:,.2f}")
print("")

print("RECEITA PROVAVEL:")
print(f"R$ {receita_provavel:,.2f}")
print("")

print("NEGOCIACAO:")
print(f"R$ {negociacao:,.2f}")
print("")

print("PAGAMENTO PENDENTE:")
print(f"R$ {pagamento_pendente:,.2f}")
print("")

print("PROPOSTA ENVIADA:")
print(f"R$ {proposta_enviada:,.2f}")
print("")

print("EM ANALISE:")
print(f"R$ {em_analise:,.2f}")
print("")

print("CONVERSAO ESTIMADA:")
print(f"{conversao:.2f}%")
print("")

# ==========================================
# META FINANCEIRA
# ==========================================

meta_mensal = 50000

faltante = meta_mensal - receita_provavel

print("META MENSAL:")
print(f"R$ {meta_mensal:,.2f}")

print("")

if faltante <= 0:
    pass

    print("META ATINGIDA")
    print(
        f"EXCEDENTE: R$ {abs(faltante):,.2f}"
    )

else:
    pass

    print(
        f"FALTAM: R$ {faltante:,.2f}"
    )

print("")
print("===================================")

conn.close()




