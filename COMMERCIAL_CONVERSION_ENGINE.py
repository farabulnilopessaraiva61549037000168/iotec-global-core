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

# ============================================
# CLASSIFICADOR DE CONVERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================

rows = cur.execute("""

SELECT
id,
company,
lead_score,
status

FROM commercial_opportunities

""").fetchall()

alteradas = 0

for row in rows:
    pass

    op_id = row[0]
    empresa = row[1]
    score = row[2]
    status_atual = row[3]

    novo_status = status_atual

    if score >= 45:
        pass

        novo_status = "PROPOSTA_ENVIADA"

    elif score >= 25:
        pass

        novo_status = "EM_ANALISE"

    elif score >= 15:
        pass

        novo_status = "NOVA"

    if novo_status != status_atual:
        pass

        cur.execute("""

        UPDATE commercial_opportunities

        SET status=?

        WHERE id=?

        """,(

            novo_status,
            op_id

        ))

        alteradas += 1

conn.commit()

print("")
print("===================================")
print("COMMERCIAL CONVERSION ENGINE")
print("===================================")
print("")
print("OPORTUNIDADES PROCESSADAS:", len(rows))
print("STATUS ALTERADOS:", alteradas)
print("")

# ============================================
# RESUMO
# ============================================

print("RESUMO")
print("")

for status in [

    "PROPOSTA_ENVIADA",
    "EM_ANALISE",
    "NOVA",
    "NEGOCIACAO",
    "PAGAMENTO_PENDENTE",
    "CLIENTE_ATIVO"

]:

    qtd = cur.execute("""

    SELECT COUNT(*)

    FROM commercial_opportunities

    WHERE status=?

    """,(status,)).fetchone()[0]

    print(f"{status}: {qtd}")

print("")

conn.close()




