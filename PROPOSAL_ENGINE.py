import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime
from pathlib import Path

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

PROPOSTAS = Path(
    r"C:\IOTEC_OMEGA_X\PROPOSALS"
)

PROPOSTAS.mkdir(exist_ok=True)

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

dados = cur.execute("""

SELECT

p.opportunity_id,
l.company,
l.email,
l.sector

FROM pipeline p

JOIN opportunities o
ON o.id = p.opportunity_id

JOIN leads l
ON l.id = o.lead_id

WHERE p.status='RELATORIO_ENVIADO'

""").fetchall()

geradas = 0

for row in dados:
    pass

    op_id = row[0]
    empresa = row[1]
    email = row[2]
    setor = row[3]

    arquivo = PROPOSTAS / f"PROPOSTA_OP_{op_id}.txt"

    valor = 2500.00

    proposta = f"""
==================================================
PROPOSTA COMERCIAL IOTEC
==================================================

EMPRESA:
{empresa}

EMAIL:
{email}

SETOR:
{setor}

DATA:
{datetime.now()}

==================================================
ESCOPO
==================================================

Analise operacional

Diagnostico de processos

Mapeamento de oportunidades

Automacao e integracao

Suporte consultivo inicial

==================================================
INVESTIMENTO
==================================================

R$ {valor:,.2f}

==================================================
VALIDADE
==================================================

15 dias

==================================================
STATUS
==================================================

AGUARDANDO APROVACAO

==================================================
"""

    arquivo.write_text(
        proposta,
        encoding="utf-8"
    )

    cur.execute("""

    UPDATE pipeline

    SET

    proposal_sent=1,
    proposal_value=?,
    proposal_file=?,
    status='PROPOSTA_ENVIADA',
    updated_at=datetime('now')

    WHERE opportunity_id=?

    """,(

        valor,
        str(arquivo),
        op_id

    ))

    geradas += 1

conn.commit()
conn.close()

print("")
print("======================================")
print("PROPOSTAS GERADAS:", geradas)
print("======================================")
print("")




