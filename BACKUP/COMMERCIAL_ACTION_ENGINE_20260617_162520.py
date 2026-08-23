import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==================================================
# TABELA DE ACOES
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS commercial_actions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    status TEXT,

    priority TEXT,

    action_type TEXT,

    action_text TEXT,

    executed INTEGER DEFAULT 0

)

""")

conn.commit()

print("")
print("==================================================")
print("IOTEC COMMERCIAL ACTION ENGINE")
print("==================================================")
print("")

# ==================================================
# LIMPEZA DA FILA
# ==================================================

cur.execute("""

DELETE FROM commercial_actions

WHERE executed=0

""")

conn.commit()

# ==================================================
# OPORTUNIDADES
# ==================================================

rows = cur.execute("""

SELECT

company,
status,
estimated_value

FROM commercial_opportunities

WHERE status IN (

'NEGOCIACAO',
'PAGAMENTO_PENDENTE',
'PROPOSTA_ENVIADA',
'EM_ANALISE',
'NOVA'

)

ORDER BY estimated_value DESC

""").fetchall()

geradas = 0

for empresa, status, valor in rows:
    pass

    prioridade = "MEDIA"
    tipo = ""
    texto = ""

    if status == "PAGAMENTO_PENDENTE":
        pass

        prioridade = "CRITICA"

        tipo = "COBRANCA"

        texto = (
            f"Entrar em contato com {empresa} "
            f"para confirmar pagamento "
            f"de R$ {valor:,.2f}"
        )

    elif status == "NEGOCIACAO":
        pass

        prioridade = "ALTA"

        tipo = "REUNIAO"

        texto = (
            f"Agendar reuniao executiva "
            f"com {empresa}"
        )

    elif status == "PROPOSTA_ENVIADA":
        pass

        prioridade = "MEDIA"

        tipo = "FOLLOWUP"

        texto = (
            f"Realizar follow-up comercial "
            f"com {empresa}"
        )

    elif status == "EM_ANALISE":
        pass

        prioridade = "MEDIA"

        tipo = "DIAGNOSTICO"

        texto = (
            f"Enviar diagnostico "
            f"para {empresa}"
        )

    else:
        pass

        prioridade = "BAIXA"

        tipo = "QUALIFICACAO"

        texto = (
            f"Qualificar oportunidade "
            f"{empresa}"
        )

    cur.execute("""

    INSERT INTO commercial_actions(

        created_at,
        company,
        status,
        priority,
        action_type,
        action_text

    )

    VALUES(

        datetime('now'),

        ?,
        ?,
        ?,
        ?,
        ?

    )

    """,(

        empresa,
        status,
        prioridade,
        tipo,
        texto

    ))

    geradas += 1

conn.commit()

# ==================================================
# PAINEL
# ==================================================

acoes = cur.execute("""

SELECT

company,
priority,
action_type,
action_text

FROM commercial_actions

WHERE executed=0

ORDER BY

CASE priority

WHEN 'CRITICA' THEN 1
WHEN 'ALTA' THEN 2
WHEN 'MEDIA' THEN 3
ELSE 4

END

""").fetchall()

print("ACOES GERADAS")
print("")

for a in acoes:
    pass

    print(
        f"{a[0]} | "
        f"{a[1]} | "
        f"{a[2]}"
    )

print("")
print("==================================================")
print("RESUMO")
print("==================================================")
print("")

print(
    f"ACOES: {geradas}"
)

criticas = sum(
    1 for a in acoes
    if a[1] == "CRITICA"
)

altas = sum(
    1 for a in acoes
    if a[1] == "ALTA"
)

print(
    f"CRITICAS: {criticas}"
)

print(
    f"ALTAS: {altas}"
)

print("")

if criticas > 0:
    pass

    print(
        "FOCO IMEDIATO: COBRANCAS"
    )

elif altas > 0:
    pass

    print(
        "FOCO IMEDIATO: REUNIOES"
    )

else:
    pass

    print(
        "OPERACAO NORMAL"
    )

print("")
print("==================================================")

conn.close()


