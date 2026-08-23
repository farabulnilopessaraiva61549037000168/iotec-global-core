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
print("IOTEC CLOSING ENGINE")
print("===================================")
print("")

rows = cur.execute("""

SELECT

    company,
    estimated_value,
    lead_score,
    status

FROM commercial_opportunities

WHERE status IN (

    'NEGOCIACAO',
    'PAGAMENTO_PENDENTE',
    'PROPOSTA_ENVIADA'

)

ORDER BY estimated_value DESC

""").fetchall()

analise = []

for row in rows:
    pass

    empresa = row[0]
    valor = row[1]
    score = row[2]
    status = row[3]

    chance = score

    if status == "PAGAMENTO_PENDENTE":
        pass

        chance += 40
        risco = "BAIXO"
        acao = "COBRAR PAGAMENTO"

    elif status == "NEGOCIACAO":
        pass

        chance += 30
        risco = "MEDIO"
        acao = "REUNIAO EXECUTIVA"

    else:
        pass

        chance += 20
        risco = "ALTO"
        acao = "FOLLOW-UP COMERCIAL"

    if chance > 100:
        chance = 100

    valor_esperado = valor * (chance / 100)

    analise.append(

        (
            empresa,
            valor,
            valor_esperado,
            chance,
            risco,
            status,
            acao
        )

    )

analise.sort(
    key=lambda x: x[2],
    reverse=True
)

print("NEGOCIOS PRIORITARIOS")
print("")

total_fechamento = 0

for pos, item in enumerate(analise, start=1):
    pass

    total_fechamento += item[2]

    print(
        f"{pos}. "
        f"{item[0]} | "
        f"R$ {item[1]:,.2f} | "
        f"CHANCE={item[3]}% | "
        f"RISCO={item[4]} | "
        f"{item[5]} | "
        f"ACAO={item[6]}"
    )

print("")
print("===================================")
print("RESUMO DE FECHAMENTO")
print("===================================")
print("")

print(
    f"NEGOCIOS ANALISADOS: {len(analise)}"
)

print(
    f"RECEITA ESPERADA: R$ {total_fechamento:,.2f}"
)

print("")

if analise:
    pass

    print("FOCO MAXIMO:")

    print(
        f"{analise[0][0]} | "
        f"{analise[0][6]}"
    )

print("")
print("===================================")

conn.close()




