import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
META = 50000

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC TARGET CLOSURE ENGINE")
print("==================================================")
print("")

# ==================================================
# RECEITA ATUAL
# ==================================================

receita_recebida = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

WHERE status='PAGO'

""").fetchone()[0]

deficit = max(
    0,
    META - receita_recebida
)

print("META EXECUTIVA")
print("")

print(
    f"META: "
    f"R$ {META:,.2f}"
)

print(
    f"RECEITA ATUAL: "
    f"R$ {receita_recebida:,.2f}"
)

print(
    f"DEFICIT: "
    f"R$ {deficit:,.2f}"
)

# ==================================================
# OPORTUNIDADES
# ==================================================

oportunidades = cur.execute("""

SELECT

company,
status,
estimated_value,
lead_score

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY

estimated_value DESC,
lead_score DESC

""").fetchall()

print("")
print("==================================================")
print("MISSAO DE FECHAMENTO")
print("==================================================")
print("")

acumulado = 0
selecionadas = []

for empresa, status, valor, score in oportunidades:
    pass

    if acumulado >= deficit:
        break

    acumulado += valor

    selecionadas.append(
        (
            empresa,
            status,
            valor,
            score
        )
    )

for idx, item in enumerate(
    selecionadas,
    start=1
):

    empresa, status, valor, score = item

    print(
        f"{idx}. "
        f"{empresa} | "
        f"{status} | "
        f"SCORE={score} | "
        f"R$ {valor:,.2f}"
    )

print("")
print("==================================================")
print("RESULTADO")
print("==================================================")
print("")

print(
    f"OPORTUNIDADES NECESSARIAS: "
    f"{len(selecionadas)}"
)

print(
    f"VALOR COBERTO: "
    f"R$ {acumulado:,.2f}"
)

print(
    f"DEFICIT ORIGINAL: "
    f"R$ {deficit:,.2f}"
)

print("")

if acumulado >= deficit:
    pass

    excedente = (
        acumulado - deficit
    )

    print(
        "META COBERTA"
    )

    print(
        f"EXCEDENTE: "
        f"R$ {excedente:,.2f}"
    )

else:
    pass

    faltam = (
        deficit - acumulado
    )

    print(
        f"FALTAM: "
        f"R$ {faltam:,.2f}"
    )

print("")
print("==================================================")
print("MISSAO PRIORITARIA")
print("==================================================")
print("")

if selecionadas:
    pass

    empresa, status, valor, score = selecionadas[0]

    print(
        f"EMPRESA: {empresa}"
    )

    print(
        f"STATUS: {status}"
    )

    print(
        f"VALOR: R$ {valor:,.2f}"
    )

    print(
        f"SCORE: {score}"
    )

print("")
print("==================================================")

conn.close()




