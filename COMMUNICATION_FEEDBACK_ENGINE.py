import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime
import sys

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

RESULTADOS_VALIDOS = [

    "SEM_RESPOSTA",
    "INTERESSADO",
    "REUNIAO_AGENDADA",
    "PROPOSTA_SOLICITADA",
    "NEGOCIACAO",
    "RECUSADO",
    "CLIENTE_ATIVO"

]

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==================================================
# TABELA
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS communication_feedback(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    channel TEXT,

    result TEXT,

    observation TEXT,

    created_at TEXT

)

""")

conn.commit()

# ==================================================
# AJUDA
# ==================================================

if len(sys.argv) < 4:
    pass

    print("")
    print("===================================")
    print("COMMUNICATION FEEDBACK ENGINE")
    print("===================================")
    print("")
    print("USO:")
    print("")
    print("python COMMUNICATION_FEEDBACK_ENGINE.py")
    print('"EMPRESA" "CANAL" "RESULTADO"')
    print("")
    print("EXEMPLO:")
    print("")
    print('python COMMUNICATION_FEEDBACK_ENGINE.py')
    print('"ALFA INDUSTRIAL" "COMERCIAL" "INTERESSADO"')
    print("")
    print("RESULTADOS:")
    print("")

    for r in RESULTADOS_VALIDOS:
        print(r)

    print("")
    conn.close()
    raise SystemExit

empresa = sys.argv[1]
canal = sys.argv[2]
resultado = sys.argv[3]

if resultado not in RESULTADOS_VALIDOS:
    pass

    print("")
    print("RESULTADO INVALIDO")
    print("")
    conn.close()
    raise SystemExit

observacao = ""

if len(sys.argv) > 4:
    observacao = " ".join(sys.argv[4:])

# ==================================================
# FEEDBACK
# ==================================================

cur.execute("""

INSERT INTO communication_feedback(

    company,
    channel,
    result,
    observation,
    created_at

)

VALUES(

    ?,?,?,?,?

)

""",(

    empresa,
    canal,
    resultado,
    observacao,
    datetime.now().strftime("%d/%m/%Y %H:%M:%S")

))

# ==================================================
# ATUALIZA STATUS COMERCIAL
# ==================================================

novo_status = None

if resultado == "NEGOCIACAO":
    novo_status = "NEGOCIACAO"

elif resultado == "CLIENTE_ATIVO":
    novo_status = "CLIENTE_ATIVO"

elif resultado == "PROPOSTA_SOLICITADA":
    novo_status = "PROPOSTA_ENVIADA"

elif resultado == "INTERESSADO":
    novo_status = "EM_ANALISE"

if novo_status:
    pass

    cur.execute("""

    UPDATE commercial_opportunities

    SET status=?

    WHERE company=?

    """,(

        novo_status,
        empresa

    ))

conn.commit()

print("")
print("===================================")
print("COMMUNICATION FEEDBACK ENGINE")
print("===================================")
print("")
print("EMPRESA:", empresa)
print("CANAL:", canal)
print("RESULTADO:", resultado)

if novo_status:
    print("STATUS COMERCIAL:", novo_status)

print("")
print("REGISTRO SALVO")
print("")

conn.close()




