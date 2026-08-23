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

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==================================================
# TABELA DE LOG
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS lead_acquisition_log(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    sector TEXT,

    lead_score INTEGER,

    estimated_value REAL,

    source TEXT,

    created_at TEXT

)

""")

conn.commit()

print("")
print("==================================================")
print("IOTEC LEAD ACQUISITION ENGINE")
print("==================================================")
print("")

# ==================================================
# IMPORTACAO MANUAL
# ==================================================

if len(sys.argv) >= 6:
    pass

    empresa = sys.argv[1]
    setor = sys.argv[2]
    score = int(sys.argv[3])
    valor = float(sys.argv[4])
    origem = sys.argv[5]

    existe = cur.execute("""

    SELECT id

    FROM commercial_opportunities

    WHERE UPPER(company)=UPPER(?)

    """,(empresa,)).fetchone()

    if existe:
        pass

        print("EMPRESA JA EXISTE")
        print(empresa)

        conn.close()
        raise SystemExit

    cur.execute("""

    INSERT INTO commercial_opportunities(

        company,
        sector,
        lead_score,
        recommended_service,
        estimated_value,
        status,
        created_at

    )

    VALUES(

        ?,?,?,?,?,?,?

    )

    """,(

        empresa,
        setor,
        score,
        "ANALISE_COMERCIAL",
        valor,
        "NOVA",
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    ))

    cur.execute("""

    INSERT INTO lead_acquisition_log(

        company,
        sector,
        lead_score,
        estimated_value,
        source,
        created_at

    )

    VALUES(

        ?,?,?,?,?,?

    )

    """,(

        empresa,
        setor,
        score,
        valor,
        origem,
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    ))

    conn.commit()

    print("")
    print("LEAD ADICIONADO")
    print("")
    print("EMPRESA:", empresa)
    print("SETOR:", setor)
    print("SCORE:", score)
    print("VALOR:", valor)
    print("ORIGEM:", origem)
    print("")

    conn.close()
    raise SystemExit

# ==================================================
# RELATORIO
# ==================================================

total = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

novas = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='NOVA'

""").fetchone()[0]

mes = cur.execute("""

SELECT COUNT(*)

FROM lead_acquisition_log

""").fetchone()[0]

ultimas = cur.execute("""

SELECT

company,
sector,
estimated_value,
source

FROM lead_acquisition_log

ORDER BY id DESC

LIMIT 10

""").fetchall()

print("EMPRESAS NO RESERVATORIO")
print(total)

print("")

print("EMPRESAS NOVAS")
print(novas)

print("")

print("LEADS CAPTADOS")
print(mes)

print("")

print("==================================================")
print("ULTIMAS AQUISICOES")
print("==================================================")
print("")

for x in ultimas:
    pass

    print(
        f"{x[0]} | "
        f"{x[1]} | "
        f"R$ {x[2]:,.2f} | "
        f"{x[3]}"
    )

print("")
print("==================================================")

conn.close()


