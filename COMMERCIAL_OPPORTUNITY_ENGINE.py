import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import pandas as pd
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
CSV = r"C:\IOTEC\fila_comercial.csv"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

df = pd.read_csv(CSV)

geradas = 0
receita = 0

for _, row in df.iterrows():
    pass

    empresa = str(row["empresa"])
    setor = str(row["setor"])
    score = int(row["lead_score"])

    servico = None
    valor = 0

    if score >= 40:
        pass

        servico = "AUTOMACAO INDUSTRIAL"
        valor = 10000

    elif score >= 25:
        pass

        servico = "CRM + DASHBOARD"
        valor = 3500

    elif score >= 15:
        pass

        servico = "DIAGNOSTICO EMPRESARIAL"
        valor = 500

    else:
        pass

        continue

    existe = cur.execute("""

    SELECT COUNT(*)

    FROM commercial_opportunities

    WHERE company=?

    """,(empresa,)).fetchone()[0]

    if existe:
        continue

    cur.execute("""

    INSERT INTO commercial_opportunities(

        company,
        sector,
        lead_score,
        recommended_service,
        estimated_value,
        status,
        created_at

    )

    VALUES(

        ?,?,?,?,?,?,?

    )

    """,(

        empresa,
        setor,
        score,
        servico,
        valor,
        "NOVA",
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    ))

    geradas += 1
    receita += valor

conn.commit()
conn.close()

print("")
print("===================================")
print("COMMERCIAL OPPORTUNITY ENGINE")
print("===================================")
print("")
print("OPORTUNIDADES:", geradas)
print("")
print("RECEITA POTENCIAL:")
print(f"R$ {receita:,.2f}")
print("")




