import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

TRACE_DB = r"C:\IOTEC\IOTEC_HYDRO_TRACE.db"

conn = sqlite3.connect(TRACE_DB)

cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS hydro_trace (

    hydro_id TEXT PRIMARY KEY,

    company TEXT,

    segment TEXT,

    product TEXT,

    lead_date TEXT,

    opportunity_date TEXT,

    proposal_date TEXT,

    contract_date TEXT,

    proposal_value REAL,

    contract_value REAL,

    status TEXT

)

""")

conn.commit()

# ==================================
# DADOS EXISTENTES
# ==================================

accounts = [

    (
        "HYDRO-000001",
        "Escola Alfa",
        "EDUCACAO",
        "Auditoria Operacional"
    ),

    (
        "HYDRO-000002",
        "Clinica Vida",
        "SAUDE",
        "Auditoria Inteligente"
    ),

    (
        "HYDRO-000003",
        "Prefeitura Modelo",
        "PREFEITURAS",
        "GovTech Analytics"
    )

]

for hydro_id, company, segment, product in accounts:
    pass

    cur.execute("""

    INSERT OR IGNORE INTO hydro_trace (

        hydro_id,

        company,

        segment,

        product,

        lead_date,

        status

    )

    VALUES (

        ?,?,?,?,?,?

    )

    """,

    (

        hydro_id,

        company,

        segment,

        product,

        str(datetime.now()),

        "LEAD"

    ))

# ==================================
# OPORTUNIDADES
# ==================================

cur.execute("""

UPDATE hydro_trace

SET

    opportunity_date=?,

    status='OPPORTUNITY'

WHERE company='Escola Alfa'

""",

(

    str(datetime.now()),

))

cur.execute("""

UPDATE hydro_trace

SET

    opportunity_date=?,

    status='OPPORTUNITY'

WHERE company='Clinica Vida'

""",

(

    str(datetime.now()),

))

cur.execute("""

UPDATE hydro_trace

SET

    opportunity_date=?,

    status='OPPORTUNITY'

WHERE company='Prefeitura Modelo'

""",

(

    str(datetime.now()),

))

# ==================================
# PROPOSTAS
# ==================================

cur.execute("""

UPDATE hydro_trace

SET

    proposal_date=?,

    proposal_value=5000,

    status='PROPOSAL'

WHERE company='Escola Alfa'

""",

(

    str(datetime.now()),

))

cur.execute("""

UPDATE hydro_trace

SET

    proposal_date=?,

    proposal_value=8000,

    status='PROPOSAL'

WHERE company='Clinica Vida'

""",

(

    str(datetime.now()),

))

cur.execute("""

UPDATE hydro_trace

SET

    proposal_date=?,

    proposal_value=15000,

    status='PROPOSAL'

WHERE company='Prefeitura Modelo'

""",

(

    str(datetime.now()),

))

# ==================================
# CONTRATO EXEMPLO
# ==================================

cur.execute("""

UPDATE hydro_trace

SET

    contract_date=?,

    contract_value=5000,

    status='CONTRACT'

WHERE company='Escola Alfa'

""",

(

    str(datetime.now()),

))

conn.commit()

rows = cur.execute("""

SELECT

    hydro_id,

    company,

    status,

    proposal_value,

    contract_value

FROM hydro_trace

ORDER BY hydro_id

""").fetchall()

report = []

for row in rows:
    pass

    report.append({

        "hydro_id": row[0],

        "company": row[1],

        "status": row[2],

        "proposal_value": row[3],

        "contract_value": row[4]

    })

with open(

    r"C:\IOTEC\IOTEC_HYDRO_TRACE_REPORT.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        report,

        f,

        indent=4,

        ensure_ascii=False

    )

print("")
print("===================================")
print("IOTEC HYDRO TRACE ENGINE")
print("===================================")
print("")

for row in rows:
    pass

    print(

        row[0],
        "|",
        row[1],
        "|",
        row[2]

    )

print("")
print("TOTAL:", len(rows))

print("")
print("DATABASE:")
print(TRACE_DB)

print("")
print("JSON:")
print(
    r"C:\IOTEC\IOTEC_HYDRO_TRACE_REPORT.json"
)

print("")
print("CONCLUIDO")

conn.close()


