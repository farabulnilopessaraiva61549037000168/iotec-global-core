import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
META = 50000

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC REVENUE ACCELERATOR ENGINE")
print("==================================================")
print("")

receita_recebida = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

WHERE status='PAGO'

""").fetchone()[0]

faltam = max(
    0,
    META - receita_recebida
)

oportunidades = cur.execute("""

SELECT

    company,
    status,
    lead_score,
    estimated_value

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY estimated_value DESC

""").fetchall()

print("META")
print("")

print(
    f"RECEITA RECEBIDA: "
    f"R$ {receita_recebida:,.2f}"
)

print(
    f"META: "
    f"R$ {META:,.2f}"
)

print(
    f"FALTAM: "
    f"R$ {faltam:,.2f}"
)

print("")
print("==================================================")
print("PLANO DE FECHAMENTO")
print("==================================================")
print("")

potencial = 0
contador = 0

for empresa, status, score, valor in oportunidades:
    pass

    if status == "PAGAMENTO_PENDENTE":
        pass

        chance = 90
        acao = "COBRRANCA"

    elif status == "NEGOCIACAO":
        pass

        chance = 80
        acao = "REUNIAO"

    elif status == "PROPOSTA_ENVIADA":
        pass

        chance = 65
        acao = "FOLLOWUP"

    elif status == "EM_ANALISE":
        pass

        chance = 60
        acao = "DIAGNOSTICO"

    else:
        pass

        chance = min(
            80,
            max(20, score)
        )

        acao = "QUALIFICACAO"

    esperado = (
        valor * chance
    ) / 100

    potencial += esperado
    contador += 1

    print(
        f"{contador}. "
        f"{empresa} | "
        f"{status} | "
        f"CHANCE={chance}% | "
        f"VALOR=R$ {valor:,.2f} | "
        f"ESPERADO=R$ {esperado:,.2f} | "
        f"ACAO={acao}"
    )

print("")
print("==================================================")
print("PROJECAO")
print("==================================================")
print("")

print(
    f"RECEITA POTENCIAL: "
    f"R$ {potencial:,.2f}"
)

receita_total = (
    receita_recebida +
    potencial
)

print(
    f"RECEITA TOTAL PROJETADA: "
    f"R$ {receita_total:,.2f}"
)

print("")

if receita_total >= META:
    pass

    print(
        "META COBERTA"
    )

else:
    pass

    deficit = (
        META -
        receita_total
    )

    print(
        f"DEFICIT: "
        f"R$ {deficit:,.2f}"
    )

print("")
print("==================================================")
print("MISSOES PRIORITARIAS")
print("==================================================")
print("")

prioridades = cur.execute("""

SELECT

    company,
    status,
    estimated_value

FROM commercial_opportunities

WHERE status IN (

'PAGAMENTO_PENDENTE',
'NEGOCIACAO',
'PROPOSTA_ENVIADA'

)

ORDER BY estimated_value DESC

""").fetchall()

for empresa, status, valor in prioridades:
    pass

    print(
        f"{empresa} | "
        f"{status} | "
        f"R$ {valor:,.2f}"
    )

print("")
print("==================================================")

conn.close()


