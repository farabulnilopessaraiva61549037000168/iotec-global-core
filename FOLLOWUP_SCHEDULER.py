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
print("FOLLOWUP SCHEDULER")
print("===================================")
print("")

acoes = []

rows = cur.execute("""

SELECT

    company,
    status,
    estimated_value,
    lead_score

FROM commercial_opportunities

""").fetchall()

for row in rows:
    pass

    empresa = row[0]
    status = row[1]
    valor = row[2]
    score = row[3]

    prioridade = score

    if status == "PAGAMENTO_PENDENTE":
        pass

        prioridade += 100
        acao = "COBRAR PAGAMENTO"

    elif status == "NEGOCIACAO":
        pass

        prioridade += 80
        acao = "AGENDAR REUNIAO"

    elif status == "PROPOSTA_ENVIADA":
        pass

        prioridade += 60
        acao = "FOLLOW-UP"

    elif status == "EM_ANALISE":
        pass

        prioridade += 40
        acao = "ENVIAR DIAGNOSTICO"

    else:
        pass

        prioridade += 10
        acao = "QUALIFICAR"

    acoes.append(

        (
            prioridade,
            empresa,
            status,
            valor,
            acao
        )

    )

acoes.sort(
    reverse=True,
    key=lambda x: x[0]
)

receita_risco = 0

for a in acoes:
    pass

    if a[2] in (
        "PAGAMENTO_PENDENTE",
        "NEGOCIACAO",
        "PROPOSTA_ENVIADA"
    ):
        receita_risco += a[3]

print("AGENDA COMERCIAL")
print("")

for i, a in enumerate(acoes, start=1):
    pass

    print(
        f"{i}. "
        f"{a[1]} | "
        f"{a[4]} | "
        f"{a[2]} | "
        f"R$ {a[3]:,.2f}"
    )

print("")
print("===================================")
print("INDICADORES")
print("===================================")
print("")

print("OPORTUNIDADES:", len(acoes))
print("RECEITA EM RISCO: R$ {:,.2f}".format(receita_risco))

print("")

if len(acoes) > 0:
    pass

    print("PROXIMA ACAO PRIORITARIA:")
    print(
        acoes[0][1],
        "|",
        acoes[0][4]
    )

print("")
print("===================================")

conn.close()




