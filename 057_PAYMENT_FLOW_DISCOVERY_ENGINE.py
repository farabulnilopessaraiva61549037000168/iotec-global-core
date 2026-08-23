# ==========================================================
# 057_PAYMENT_FLOW_DISCOVERY_ENGINE.py
# IOTEC PAYMENT FLOW DISCOVERY
# ==========================================================

import os
import re
import sqlite3

ROOT = r"C:\IOTEC"
DB = "iotec_kernel.db"

IGNORAR = {
    "venv",
    "node_modules",
    "__pycache__",
    "BACKUP",
    "ENCODING_BACKUP",
    "DUPLICADOS",
    "LABORATORIO",
    "_SANITIZADA",
    "_QUARENTENA"
}

IMPORT_RE = re.compile(r'^\s*(?:from\s+([A-Za-z0-9_\.]+)|import\s+([A-Za-z0-9_\.]+))')

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS payment_flow(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arquivo TEXT,
    importa TEXT
)
""")

cur.execute("DELETE FROM payment_flow")
conn.commit()

arquivos = 0
ligacoes = 0

for pasta, dirs, files in os.walk(ROOT):

    dirs[:] = [d for d in dirs if d not in IGNORAR]

    for nome in files:

        if not nome.endswith(".py"):
            continue

        caminho = os.path.join(pasta, nome)

        arquivos += 1

        try:
            with open(caminho, encoding="utf8", errors="ignore") as f:

                for linha in f:

                    m = IMPORT_RE.search(linha)

                    if not m:
                        continue

                    modulo = m.group(1) or m.group(2)

                    cur.execute("""

                    INSERT INTO payment_flow(
                        arquivo,
                        importa
                    )
                    VALUES(?,?)

                    """,(nome, modulo))

                    ligacoes += 1

        except:
            pass

conn.commit()

print("="*70)
print("IOTEC PAYMENT FLOW DISCOVERY")
print("="*70)
print()

print("Arquivos analisados :", arquivos)
print("LigaÃƒÂ§ÃƒÂµes encontradas:", ligacoes)
print()

print("="*70)
print("ARQUIVOS MAIS CONECTADOS")
print("="*70)
print()

cur.execute("""

SELECT
arquivo,
COUNT(*)
FROM payment_flow
GROUP BY arquivo
ORDER BY COUNT(*) DESC
LIMIT 30

""")

for arq,total in cur.fetchall():

    print(f"{total:>4}  {arq}")

print()

print("="*70)
print("IMPORTAÃƒâ€¡Ãƒâ€¢ES PARA MÃƒâ€œDULOS DE PAGAMENTO")
print("="*70)
print()

cur.execute("""

SELECT
arquivo,
importa
FROM payment_flow

WHERE
LOWER(importa) LIKE '%paypal%'
OR LOWER(importa) LIKE '%payment%'
OR LOWER(importa) LIKE '%checkout%'
OR LOWER(importa) LIKE '%gateway%'

ORDER BY arquivo

""")

dados = cur.fetchall()

if dados:

    for arq,mod in dados:

        print(f"{arq:<45} -> {mod}")

else:

    print("Nenhuma importaÃƒÂ§ÃƒÂ£o direta encontrada.")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("O Kernel iniciou a reconstruÃƒÂ§ÃƒÂ£o")
print("do fluxo real do sistema")
print("financeiro.")

print()
print("PrÃƒÂ³xima etapa:")
print("identificar quem chama")
print("quem durante")
print("uma venda.")

conn.close()


