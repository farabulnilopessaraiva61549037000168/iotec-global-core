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

REPORTS = Path(
    r"C:\IOTEC_OMEGA_X\REPORTS"
)

REPORTS.mkdir(exist_ok=True)

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

dados = cur.execute("""

SELECT

o.id,
l.company,
l.email,
l.sector,
l.message

FROM opportunities o

JOIN leads l

ON l.id = o.lead_id

""").fetchall()

gerados = 0

for row in dados:
    pass

    op_id = row[0]
    empresa = row[1]
    email = row[2]
    setor = row[3]
    mensagem = row[4]

    pipeline = cur.execute("""

    SELECT report_sent
    FROM pipeline
    WHERE opportunity_id=?

    """,(op_id,)).fetchone()

    if pipeline and pipeline[0] == 1:
        continue

    arquivo = REPORTS / f"RELATORIO_OP_{op_id}.txt"

    conteudo = f"""
==================================================
RELATORIO EXECUTIVO IOTEC
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
RESUMO
==================================================

Solicitacao recebida:

{mensagem}

==================================================
ANALISE PRELIMINAR
==================================================

A oportunidade foi registrada no CRM IOTEC.

Foi identificada demanda potencial para:

- Automacao
- Inteligencia Operacional
- Analise de Dados
- Integracao de Sistemas

==================================================
PROXIMOS PASSOS
==================================================

1. Revisao tecnica

2. Reuniao de diagnostico

3. Elaboracao de proposta

4. Implantacao

==================================================
"""

    arquivo.write_text(
        conteudo,
        encoding="utf-8"
    )

    cur.execute("""

    UPDATE pipeline

    SET

    report_sent=1,
    status='RELATORIO_ENVIADO',
    report_file=?,
    updated_at=datetime('now')

    WHERE opportunity_id=?

    """,(

    str(arquivo),
    op_id

    ))

    gerados += 1

conn.commit()
conn.close()

print("")
print("======================================")
print("RELATORIOS GERADOS:", gerados)
print("======================================")
print("")




