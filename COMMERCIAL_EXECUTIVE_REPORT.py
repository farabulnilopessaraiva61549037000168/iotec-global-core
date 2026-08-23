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
print("======================================================")
print("IOTEC COMMERCIAL EXECUTIVE REPORT")
print("======================================================")
print("")

# ======================================================
# EMPRESAS ANALISADAS
# ======================================================

try:
    pass

    empresas = cur.execute("""

    SELECT COUNT(*)

    FROM commercial_opportunities

    """).fetchone()[0]

except:
    pass

    empresas = 0

# ======================================================
# RECEITA POTENCIAL
# ======================================================

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

# ======================================================
# STATUS
# ======================================================

status_list = [

    "NOVA",
    "EM_ANALISE",
    "PROPOSTA_ENVIADA",
    "NEGOCIACAO",
    "PAGAMENTO_PENDENTE",
    "CLIENTE_ATIVO"

]

status_count = {}

for s in status_list:
    pass

    try:
        pass

        qtd = cur.execute("""

        SELECT COUNT(*)

        FROM commercial_opportunities

        WHERE status=?

        """,(s,)).fetchone()[0]

    except:
        pass

        qtd = 0

    status_count[s] = qtd

# ======================================================
# CLIENTES ATIVOS DO PIPELINE
# ======================================================

try:
    pass

    clientes_ativos = cur.execute("""

    SELECT COUNT(*)

    FROM pipeline

    WHERE status='CLIENTE_ATIVO'

    """).fetchone()[0]

except:
    pass

    clientes_ativos = 0

# ======================================================
# PROJETOS LIBERADOS
# ======================================================

try:
    pass

    projetos = cur.execute("""

    SELECT COUNT(*)

    FROM pipeline

    WHERE status='PROJETO_LIBERADO'

    """).fetchone()[0]

except:
    pass

    projetos = 0

# ======================================================
# TAXA DE CONVERSAO
# ======================================================

if empresas > 0:
    pass

    conversao = (
        clientes_ativos / empresas
    ) * 100

else:
    pass

    conversao = 0

# ======================================================
# RELATORIO
# ======================================================

print(f"EMPRESAS ANALISADAS: {empresas}")
print("")

print("RECEITA POTENCIAL:")
print(f"R$ {receita:,.2f}")
print("")

print("STATUS COMERCIAIS")
print("------------------------------")

for k,v in status_count.items():
    pass

    print(f"{k}: {v}")

print("")

print(f"CLIENTES ATIVOS: {clientes_ativos}")
print(f"PROJETOS LIBERADOS: {projetos}")

print("")

print(
    f"TAXA DE CONVERSAO: "
    f"{conversao:.2f}%"
)

print("")
print("======================================================")

conn.close()




