import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# BILLING_ORCHESTRATOR.py
#
# ORQUESTRADOR DE FATURAMENTO IOTEC
#
# Fluxo:
#
# PROPOSTA APROVADA
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# FATURA 30%
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# PAGAMENTO 30%
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# LIBERA PROJETO
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# FATURA 70%
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# PAGAMENTO FINAL
#      ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# CLIENTE PREMIUM

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==================================================
# SCHEMA
# ==================================================

campos = [

    ("invoice30_value","REAL"),
    ("invoice70_value","REAL"),

    ("invoice30_status","TEXT"),
    ("invoice70_status","TEXT"),

    ("invoice30_date","TEXT"),
    ("invoice70_date","TEXT")

]

for campo,tipo in campos:
    pass

    try:
        pass

        cur.execute(
            f"""
            ALTER TABLE pipeline
            ADD COLUMN {campo} {tipo}
            """
        )

        print("[OK]",campo)

    except:
        pass

        print("[EXISTE]",campo)

# ==================================================
# GERAR FATURAS
# ==================================================

aprovados = cur.execute("""

SELECT

opportunity_id,
proposal_value

FROM pipeline

WHERE status='PAGAMENTO_PENDENTE'

""").fetchall()

gerados = 0

for op_id,valor in aprovados:
    pass

    entrada = round(valor * 0.30,2)

    final = round(valor * 0.70,2)

    cur.execute("""

    UPDATE pipeline

    SET

    invoice30_value=?,
    invoice70_value=?,

    invoice30_status='AGUARDANDO',

    invoice70_status='BLOQUEADA',

    invoice30_date=?

    WHERE opportunity_id=?

    """,(

        entrada,
        final,
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        ),
        op_id

    ))

    gerados += 1

conn.commit()
conn.close()

print("")
print("===================================")
print("BILLING ORCHESTRATOR")
print("===================================")
print("")
print("FATURAS GERADAS:", gerados)
print("")


