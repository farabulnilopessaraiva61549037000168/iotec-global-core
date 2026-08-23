import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import sys
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==================================================
# HISTORICO
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS commercial_action_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    action_type TEXT,

    result TEXT,

    notes TEXT

)

""")

conn.commit()

print("")
print("==================================================")
print("IOTEC COMMERCIAL ACTION EXECUTOR")
print("==================================================")
print("")

# ==================================================
# MODO CONSULTA
# ==================================================

if len(sys.argv) == 1:
    pass

    filas = cur.execute("""

    SELECT

        id,
        company,
        priority,
        action_type

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

    print("FILA OPERACIONAL")
    print("")

    for f in filas:
        pass

        print(
            f"ID={f[0]} | "
            f"{f[1]} | "
            f"{f[2]} | "
            f"{f[3]}"
        )

    print("")
    print("USO:")
    print("")
    print(
        'python COMMERCIAL_ACTION_EXECUTOR.py '
        '"ID" "RESULTADO"'
    )

    print("")
    print("RESULTADOS:")
    print("")
    print("SEM_RESPOSTA")
    print("INTERESSADO")
    print("REUNIAO_REALIZADA")
    print("PROPOSTA_SOLICITADA")
    print("NEGOCIACAO")
    print("PAGAMENTO_CONFIRMADO")
    print("CLIENTE_ATIVO")

    conn.close()
    raise SystemExit

# ==================================================
# EXECUCAO
# ==================================================

acao_id = int(sys.argv[1])
resultado = sys.argv[2]

acao = cur.execute("""

SELECT

    company,
    action_type

FROM commercial_actions

WHERE id=?

""",(acao_id,)).fetchone()

if not acao:
    pass

    print("ACAO NAO ENCONTRADA")
    conn.close()
    raise SystemExit

empresa = acao[0]
tipo = acao[1]

# ==================================================
# HISTORICO
# ==================================================

cur.execute("""

INSERT INTO commercial_action_history(

    created_at,
    company,
    action_type,
    result,
    notes

)

VALUES(

    ?,
    ?,
    ?,
    ?,
    ?

)

""",(

    datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    ),

    empresa,
    tipo,
    resultado,
    ""

))

# ==================================================
# MARCAR EXECUTADA
# ==================================================

cur.execute("""

UPDATE commercial_actions

SET executed=1

WHERE id=?

""",(acao_id,))

# ==================================================
# ATUALIZAR PIPELINE
# ==================================================

novo_status = None

if resultado == "INTERESSADO":
    novo_status = "EM_ANALISE"

elif resultado == "REUNIAO_REALIZADA":
    novo_status = "NEGOCIACAO"

elif resultado == "PROPOSTA_SOLICITADA":
    novo_status = "PROPOSTA_ENVIADA"

elif resultado == "NEGOCIACAO":
    novo_status = "NEGOCIACAO"

elif resultado == "PAGAMENTO_CONFIRMADO":
    novo_status = "CLIENTE_ATIVO"

elif resultado == "CLIENTE_ATIVO":
    novo_status = "CLIENTE_ATIVO"

if novo_status:
    pass

    cur.execute("""

    UPDATE commercial_opportunities

    SET

        status=?,
        updated_at=?

    WHERE company=?

    """,(

        novo_status,

        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        ),

        empresa

    ))

conn.commit()

print("")
print("==================================================")
print("EXECUCAO REGISTRADA")
print("==================================================")
print("")

print("EMPRESA:", empresa)
print("ACAO:", tipo)
print("RESULTADO:", resultado)

if novo_status:
    pass

    print(
        "NOVO STATUS:",
        novo_status
    )

print("")
print("HISTORICO ATUALIZADO")
print("")

print("==================================================")

conn.close()






