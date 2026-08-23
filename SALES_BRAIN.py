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
print("IOTEC SALES BRAIN")
print("===================================")
print("")

rows = cur.execute("""

SELECT

    id,
    company,
    sector,
    lead_score,
    estimated_value,
    status

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY estimated_value DESC

""").fetchall()

analise = []

for row in rows:
    pass

    op_id = row[0]
    empresa = row[1]
    setor = row[2]
    score = row[3]
    valor = row[4]
    status = row[5]

    chance = score

    if status == "NEGOCIACAO":
        chance += 30

    elif status == "PAGAMENTO_PENDENTE":
        chance += 40

    elif status == "PROPOSTA_ENVIADA":
        chance += 20

    elif status == "EM_ANALISE":
        chance += 10

    if chance > 100:
        chance = 100

    valor_esperado = valor * (chance / 100)

    if status == "PAGAMENTO_PENDENTE":
        pass

        acao = "COBRAR PAGAMENTO"

    elif status == "NEGOCIACAO":
        pass

        acao = "AGENDAR REUNIAO"

    elif status == "PROPOSTA_ENVIADA":
        pass

        acao = "FOLLOW-UP"

    elif status == "EM_ANALISE":
        pass

        acao = "ENVIAR DIAGNOSTICO"

    else:
        pass

        acao = "QUALIFICAR"

    analise.append(

        (
            empresa,
            chance,
            valor,
            valor_esperado,
            status,
            acao
        )

    )

analise.sort(
    key=lambda x: x[3],
    reverse=True
)

print("RANKING DE PRIORIDADE")
print("")

for item in analise:
    pass

    print(
        f"{item[0]} | "
        f"CHANCE={item[1]}% | "
        f"VALOR=R$ {item[2]:,.2f} | "
        f"ESPERADO=R$ {item[3]:,.2f} | "
        f"{item[4]} | "
        f"ACAO={item[5]}"
    )

print("")
print("===================================")

conn.close()




