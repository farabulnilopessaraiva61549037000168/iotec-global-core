import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC PIPELINE VELOCITY ENGINE")
print("==================================================")
print("")

# ==================================================
# GARANTIR COLUNA
# ==================================================

try:
    pass

    cur.execute("""

    ALTER TABLE commercial_opportunities
    ADD COLUMN updated_at TEXT

    """)

    conn.commit()

except:
    pass

# ==================================================
# LEITURA
# ==================================================

rows = cur.execute("""

SELECT

    company,
    status,
    estimated_value,
    created_at,
    updated_at

FROM commercial_opportunities

WHERE status NOT IN (

    'CLIENTE_ATIVO'

)

ORDER BY estimated_value DESC

""").fetchall()

# ==================================================
# ANALISE
# ==================================================

criticos = 0
atencao = 0
normal = 0

print("VELOCIDADE DO PIPELINE")
print("")

for row in rows:
    pass

    empresa = row[0]
    status = row[1]
    valor = row[2]
    criado = row[3]
    atualizado = row[4]

    dias = 0

    try:
        pass

        data_ref = atualizado

        if not data_ref:
            data_ref = criado

        dt = datetime.strptime(
            data_ref,
            "%d/%m/%Y %H:%M:%S"
        )

        dias = (
            datetime.now() - dt
        ).days

    except:
        pass

        dias = 0

    if dias >= 15:
        pass

        nivel = "CRITICO"
        criticos += 1

    elif dias >= 7:
        pass

        nivel = "ATENCAO"
        atencao += 1

    else:
        pass

        nivel = "NORMAL"
        normal += 1

    print(
        f"{empresa} | "
        f"{status} | "
        f"R$ {valor:,.2f} | "
        f"{dias} dias | "
        f"{nivel}"
    )

# ==================================================
# INDICADORES
# ==================================================

total = len(rows)

velocidade = 0

if total > 0:
    pass

    velocidade = (
        (normal * 100)
        /
        total
    )

print("")
print("==================================================")
print("INDICADORES")
print("==================================================")
print("")

print("OPORTUNIDADES:", total)

print(
    f"NORMAL: {normal}"
)

print(
    f"ATENCAO: {atencao}"
)

print(
    f"CRITICO: {criticos}"
)

print("")

print(
    f"VELOCIDADE COMERCIAL: "
    f"{velocidade:.2f}%"
)

print("")

print("==================================================")
print("DECISAO EXECUTIVA")
print("==================================================")
print("")

if criticos > 0:
    pass

    print(
        f"RECUPERAR {criticos} "
        f"OPORTUNIDADES CRITICAS"
    )

elif atencao > 0:
    pass

    print(
        f"ACELERAR {atencao} "
        f"OPORTUNIDADES"
    )

else:
    pass

    print(
        "PIPELINE SAUDAVEL"
    )

print("")
print("==================================================")

conn.close()




