import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC REVENUE REALIZATION ENGINE")
print("==================================================")
print("")

pipeline = cur.execute("""

SELECT IFNULL(
SUM(estimated_value),0
)

FROM commercial_opportunities

WHERE status<>'CLIENTE_ATIVO'

""").fetchone()[0]

contratada = cur.execute("""

SELECT IFNULL(
SUM(estimated_value),0
)

FROM client_projects

""").fetchone()[0]

clientes = cur.execute("""

SELECT COUNT(*)

FROM client_projects

""").fetchone()[0]

print("RECEITAS")
print("")

print(
    f"PIPELINE: "
    f"R$ {pipeline:,.2f}"
)

print(
    f"CONTRATADA: "
    f"R$ {contratada:,.2f}"
)

recebida = contratada

print(
    f"RECEBIDA: "
    f"R$ {recebida:,.2f}"
)

print("")
print("==================================================")
print("CLIENTES")
print("==================================================")
print("")

print(
    f"CLIENTES ATIVOS: "
    f"{clientes}"
)

print("")
print("==================================================")
print("INDICADORES")
print("==================================================")
print("")

total = pipeline + contratada

if total > 0:
    pass

    taxa = (
        contratada * 100
    ) / total

else:
    pass

    taxa = 0

print(
    f"REALIZACAO: "
    f"{taxa:.2f}%"
)

print("")

if taxa >= 50:
    pass

    print(
        "RECEITA REALIZADA FORTE"
    )

else:
    pass

    print(
        "FOCO EM CONVERSAO"
    )

print("")
print("==================================================")

conn.close()


