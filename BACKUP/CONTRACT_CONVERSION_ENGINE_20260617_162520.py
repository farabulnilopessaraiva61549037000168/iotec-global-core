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
print("IOTEC CONTRACT CONVERSION ENGINE")
print("==================================================")
print("")

receita_quente = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status IN (

'NEGOCIACAO',
'PAGAMENTO_PENDENTE'

)

""").fetchone()[0]

oportunidades = cur.execute("""

SELECT

company,
status,
lead_score,
estimated_value

FROM commercial_opportunities

WHERE status IN (

'PAGAMENTO_PENDENTE',
'NEGOCIACAO',
'PROPOSTA_ENVIADA',
'EM_ANALISE'

)

ORDER BY

estimated_value DESC,
lead_score DESC

""").fetchall()

receita_convertivel = 0

print("MISSOES DE CONVERSAO")
print("")

for empresa, status, score, valor in oportunidades:
    pass

    if status == "PAGAMENTO_PENDENTE":
        pass

        acao = "COBRAR PAGAMENTO"
        prioridade = "CRITICA"

    elif status == "NEGOCIACAO":
        pass

        acao = "REUNIAO EXECUTIVA"
        prioridade = "ALTA"

    elif status == "PROPOSTA_ENVIADA":
        pass

        acao = "FOLLOW-UP COMERCIAL"
        prioridade = "MEDIA"

    else:
        pass

        acao = "ENVIAR DIAGNOSTICO"
        prioridade = "MEDIA"

    receita_convertivel += valor

    print(
        f"{empresa} | "
        f"{status} | "
        f"PRIORIDADE={prioridade} | "
        f"ACAO={acao} | "
        f"R$ {valor:,.2f}"
    )

print("")
print("==================================================")
print("RESUMO DE CONVERSAO")
print("==================================================")
print("")

print(
    f"OPORTUNIDADES: "
    f"{len(oportunidades)}"
)

print(
    f"RECEITA CONVERTIVEL: "
    f"R$ {receita_convertivel:,.2f}"
)

potencial_total = (
    receita_quente +
    receita_convertivel
)

print(
    f"POTENCIAL TOTAL: "
    f"R$ {potencial_total:,.2f}"
)

print("")

if potencial_total >= META:
    pass

    print(
        "MISSAO SUFICIENTE PARA BATER A META"
    )

else:
    pass

    faltam = META - potencial_total

    print(
        f"FALTAM R$ {faltam:,.2f}"
    )

    print(
        "GERAR NOVAS OPORTUNIDADES"
    )

print("")
print("==================================================")

conn.close()


