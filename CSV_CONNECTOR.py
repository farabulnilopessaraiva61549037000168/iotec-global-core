import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import csv
import sqlite3
from datetime import datetime
from pathlib import Path

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
CSV_FILE = r"C:\IOTEC\empresas.csv"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC CSV CONNECTOR")
print("==================================================")
print("")

if not Path(CSV_FILE).exists():
    pass

    print("ARQUIVO NAO ENCONTRADO")
    print(CSV_FILE)

    conn.close()
    raise SystemExit

total_lidas = 0
novas = 0
duplicadas = 0

with open(
    CSV_FILE,
    "r",
    encoding="utf-8",
    newline=""
) as f:

    reader = csv.DictReader(f)

    for row in reader:
        pass

        total_lidas += 1

        empresa = row.get(
            "empresa",
            ""
        ).strip()

        setor = row.get(
            "setor",
            "GERAL"
        ).strip()

        score = int(
            row.get("funcionarios", 60)
        )

        valor = float(
            10000
        )

        origem = "CSV_IMPORT"

        if not empresa:
            continue

        existe = cur.execute("""

        SELECT id

        FROM commercial_opportunities

        WHERE UPPER(company)=UPPER(?)

        """,(empresa,)).fetchone()

        if existe:
            pass

            duplicadas += 1
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
            "ANALISE_COMERCIAL",
            valor,
            "NOVA",
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

        ))

        novas += 1

conn.commit()

print("EMPRESAS LIDAS:", total_lidas)
print("NOVAS:", novas)
print("DUPLICADAS:", duplicadas)

print("")
print("==================================================")
print("IMPORTACAO FINALIZADA")
print("==================================================")
print("")

conn.close()




