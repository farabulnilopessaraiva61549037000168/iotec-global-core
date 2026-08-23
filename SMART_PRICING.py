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

def calcular_preco(setor,mensagem):
    pass

    msg = mensagem.upper()

    if "IA" in msg:
        pass

        servico = "IA_EMPRESARIAL"

    elif "DADOS" in msg:
        pass

        servico = "ANALISE_DADOS"

    elif "AUTOM" in msg:
        pass

        servico = "AUTOMACAO"

    else:
        pass

        servico = "DIAGNOSTICO"

    valor = cur.execute(

        """
        SELECT base_value
        FROM pricing_rules
        WHERE service=?
        """,

        (servico,)

    ).fetchone()[0]

    return servico, valor

leads = cur.execute("""

SELECT

o.id,
l.sector,
l.message

FROM opportunities o

JOIN leads l
ON l.id=o.lead_id

""").fetchall()

for item in leads:
    pass

    op_id = item[0]
    setor = item[1]
    mensagem = item[2]

    servico, valor = calcular_preco(
        setor,
        mensagem
    )

    cur.execute("""

    UPDATE pipeline

    SET

    proposal_value=?,
    observations=?

    WHERE opportunity_id=?

    """,(

        valor,
        servico,
        op_id

    ))

conn.commit()

conn.close()

print("PRECIFICACAO ATUALIZADA")




