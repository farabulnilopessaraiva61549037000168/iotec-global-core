import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import os
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

PASTA = r"C:\IOTEC\PROPOSALS"

os.makedirs(PASTA, exist_ok=True)

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""

SELECT
company,
recommended_service,
estimated_value,
status

FROM commercial_opportunities

WHERE status='PROPOSTA_ENVIADA'

""").fetchall()

geradas = 0

for empresa, servico, valor, status in rows:
    pass

    entrada = round(valor * 0.30, 2)
    saldo = round(valor * 0.70, 2)

    nome_arquivo = (
        empresa
        .replace(" ", "_")
        .replace("/", "_")
        + "_PROPOSTA.txt"
    )

    caminho = os.path.join(
        PASTA,
        nome_arquivo
    )

    if os.path.exists(caminho):
        continue

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("IOTEC - PROPOSTA COMERCIAL\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"EMPRESA: {empresa}\n")
        f.write(f"SERVICO: {servico}\n")
        f.write(f"VALOR TOTAL: R$ {valor:,.2f}\n")
        f.write(f"ENTRADA 30%: R$ {entrada:,.2f}\n")
        f.write(f"SALDO 70%: R$ {saldo:,.2f}\n")
        f.write(
            f"DATA: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        )

        f.write("\n")
        f.write(
            "Projeto sujeito a validacao tecnica "
            "e aprovacao comercial.\n"
        )

    geradas += 1

conn.close()

print("")
print("===================================")
print("PROPOSAL GENERATOR")
print("===================================")
print("")
print("PROPOSTAS GERADAS:", geradas)
print("")
print("PASTA:")
print(PASTA)
print("")




