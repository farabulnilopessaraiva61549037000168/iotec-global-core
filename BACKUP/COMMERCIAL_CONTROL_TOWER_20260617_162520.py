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
print("IOTEC COMMERCIAL CONTROL TOWER")
print("==================================================")
print("")

# --------------------------------------------------
# OPORTUNIDADES
# --------------------------------------------------

try:
    pass

    total_op = cur.execute("""

    SELECT COUNT(*)

    FROM commercial_opportunities

    """).fetchone()[0]

except:
    pass

    total_op = 0

# --------------------------------------------------
# RECEITA POTENCIAL
# --------------------------------------------------

try:
    pass

    receita = cur.execute("""

    SELECT IFNULL(
        SUM(estimated_value),
        0
    )

    FROM commercial_opportunities

    """).fetchone()[0]

except:
    pass

    receita = 0

# --------------------------------------------------
# CLIENTES ATIVOS
# --------------------------------------------------

try:
    pass

    ativos = cur.execute("""

    SELECT COUNT(*)

    FROM pipeline

    WHERE status='CLIENTE_ATIVO'

    """).fetchone()[0]

except:
    pass

    ativos = 0

# --------------------------------------------------
# PAGAMENTOS PENDENTES
# --------------------------------------------------

try:
    pass

    pendentes = cur.execute("""

    SELECT COUNT(*)

    FROM pipeline

    WHERE status='PAGAMENTO_PENDENTE'

    """).fetchone()[0]

except:
    pass

    pendentes = 0

# --------------------------------------------------
# TOP OPORTUNIDADES
# --------------------------------------------------

print("OPORTUNIDADES:", total_op)
print("")

print("RECEITA POTENCIAL:")
print(f"R$ {receita:,.2f}")
print("")

print("CLIENTES ATIVOS:", ativos)
print("")

print("PAGAMENTOS PENDENTES:", pendentes)
print("")

print("==================================================")
print("TOP OPORTUNIDADES")
print("==================================================")
print("")

try:
    pass

    rows = cur.execute("""

    SELECT

        company,
        recommended_service,
        estimated_value,
        status

    FROM commercial_opportunities

    ORDER BY estimated_value DESC

    LIMIT 20

    """).fetchall()

    for row in rows:
        pass

        print(
            f"{row[0]} | "
            f"{row[1]} | "
            f"R$ {row[2]:,.2f} | "
            f"{row[3]}"
        )

except Exception as e:
    pass

    print("ERRO:")
    print(e)

print("")
print("==================================================")

conn.close()


