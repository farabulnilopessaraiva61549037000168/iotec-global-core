import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==================================================
# TABELA
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS communication_queue(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    channel TEXT,

    objective TEXT,

    priority TEXT,

    message TEXT,

    status TEXT

)

""")

conn.commit()

# ==================================================
# OPORTUNIDADES
# ==================================================

rows = cur.execute("""

SELECT

    company,
    sector,
    recommended_service,
    estimated_value,
    status

FROM commercial_opportunities

ORDER BY estimated_value DESC

""").fetchall()

geradas = 0

for row in rows:
    pass

    empresa = row[0]
    setor = row[1]
    servico = row[2]
    valor = row[3]
    status = row[4]

    # ---------------------------------------------

    if status == "PAGAMENTO_PENDENTE":
        pass

        prioridade = "CRITICA"
        canal = "FINANCEIRO"

        objetivo = "CONFIRMACAO_PAGAMENTO"

        mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {empresa}.

Estamos com sua implantaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o pronta para inÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cio.

GostarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­amos de verificar a previsÃƒÆ'Ã†â€™o de confirmaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o financeira
para reserva definitiva da agenda tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica.

Equipe IOTEC.
"""

    elif status == "NEGOCIACAO":
        pass

        prioridade = "ALTA"
        canal = "COMERCIAL"

        objetivo = "AGENDAR_REUNIAO"

        mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {empresa}.

Identificamos potencial para aplicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o da soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:

{servico}

GostarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­amos de apresentar ganhos operacionais,
reduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de retrabalho e oportunidades de automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.

Equipe IOTEC.
"""

    elif status == "PROPOSTA_ENVIADA":
        pass

        prioridade = "MEDIA"
        canal = "COMERCIAL"

        objetivo = "FOLLOWUP"

        mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {empresa}.

GostarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­amos de verificar se existem dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvidas sobre a proposta enviada.

Permanecemos ÃƒÆ'Ã†â€™  disposiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para esclarecimentos.

Equipe IOTEC.
"""

    elif status == "EM_ANALISE":
        pass

        prioridade = "MEDIA"
        canal = "CONSULTORIA"

        objetivo = "DIAGNOSTICO"

        mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {empresa}.

Estamos avaliando oportunidades para o setor {setor}.

Podemos compartilhar um diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico inicial sem compromisso.

Equipe IOTEC.
"""

    else:
        pass

        prioridade = "BAIXA"
        canal = "PROSPECCAO"

        objetivo = "QUALIFICACAO"

        mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {empresa}.

A IOTEC atua com automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o,
painÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©is gerenciais e transformaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o digital.

GostarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­amos de entender seus desafios atuais.

Equipe IOTEC.
"""

    existe = cur.execute("""

    SELECT id

    FROM communication_queue

    WHERE company=?
    AND objective=?
    AND status='PENDENTE'

    """,(empresa, objetivo)).fetchone()

    if existe:
        continue

    cur.execute("""

    INSERT INTO communication_queue(

        created_at,
        company,
        channel,
        objective,
        priority,
        message,
        status

    )

    VALUES(?,?,?,?,?,?,?)

    """,(

        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        empresa,
        canal,
        objetivo,
        prioridade,
        mensagem,
        "PENDENTE"

    ))

    geradas += 1

conn.commit()

total = cur.execute("""

SELECT COUNT(*)

FROM communication_queue

""").fetchone()[0]

print("")
print("===================================")
print("COMMUNICATION CENTER")
print("===================================")
print("")
print("MENSAGENS GERADAS:", geradas)
print("FILA TOTAL:", total)
print("")

for row in cur.execute("""

SELECT

company,
priority,
objective,
status

FROM communication_queue

ORDER BY id DESC

LIMIT 20

""").fetchall():

    print(row)

print("")
print("===================================")

conn.close()


