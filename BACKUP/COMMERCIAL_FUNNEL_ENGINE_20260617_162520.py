import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import sys

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

if len(sys.argv) < 3:
    pass

    print("")
    print("USO:")
    print("")
    print("python COMMERCIAL_FUNNEL_ENGINE.py 1 NEGOCIACAO")
    print("")
    print("STATUS VALIDOS:")
    print("")
    print("NOVA")
    print("EM_ANALISE")
    print("PROPOSTA_ENVIADA")
    print("NEGOCIACAO")
    print("PAGAMENTO_PENDENTE")
    print("CLIENTE_ATIVO")
    print("")
    exit()

op_id = int(sys.argv[1])

novo_status = sys.argv[2].upper()

VALIDOS = [

    "NOVA",
    "EM_ANALISE",
    "PROPOSTA_ENVIADA",
    "NEGOCIACAO",
    "PAGAMENTO_PENDENTE",
    "CLIENTE_ATIVO"

]

if novo_status not in VALIDOS:
    pass

    print("")
    print("STATUS INVALIDO")
    print("")
    exit()

conn = sqlite3.connect(DB)
cur = conn.cursor()

row = cur.execute("""

SELECT
company,
status

FROM commercial_opportunities

WHERE id=?

""",(op_id,)).fetchone()

if not row:
    pass

    print("")
    print("OPORTUNIDADE NAO ENCONTRADA")
    print("")
    conn.close()
    exit()

empresa = row[0]
status_antigo = row[1]

cur.execute("""

UPDATE commercial_opportunities

SET status=?

WHERE id=?

""",(

    novo_status,
    op_id

))

conn.commit()
conn.close()

print("")
print("===================================")
print("COMMERCIAL FUNNEL ENGINE")
print("===================================")
print("")
print("EMPRESA:", empresa)
print("")
print("DE:", status_antigo)
print("PARA:", novo_status)
print("")


