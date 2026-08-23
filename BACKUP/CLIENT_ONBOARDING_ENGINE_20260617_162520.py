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

print("")
print("==================================================")
print("IOTEC CLIENT ONBOARDING ENGINE")
print("==================================================")
print("")

# ==================================================
# TABELAS
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS client_projects(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT UNIQUE,

    created_at TEXT,

    project_code TEXT,

    status TEXT,

    estimated_value REAL,

    kickoff_date TEXT

)

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS onboarding_log(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    event TEXT

)

""")

conn.commit()

# ==================================================
# CLIENTES ATIVOS
# ==================================================

clientes = cur.execute("""

SELECT

    company,
    estimated_value

FROM commercial_opportunities

WHERE status='CLIENTE_ATIVO'

""").fetchall()

novos = 0

for empresa, valor in clientes:
    pass

    existe = cur.execute("""

    SELECT id

    FROM client_projects

    WHERE company=?

    """,(empresa,)).fetchone()

    if existe:
        continue

    codigo = (
        empresa.upper()
        .replace(" ","_")
        [:20]
    )

    codigo = (
        "PRJ_" +
        codigo
    )

    hoje = datetime.now()

    cur.execute("""

    INSERT INTO client_projects(

        company,
        created_at,
        project_code,
        status,
        estimated_value,
        kickoff_date

    )

    VALUES(

        ?,
        ?,
        ?,
        ?,
        ?,
        ?

    )

    """,(

        empresa,

        hoje.strftime(
            "%d/%m/%Y %H:%M:%S"
        ),

        codigo,

        "PLANEJAMENTO",

        valor,

        hoje.strftime(
            "%d/%m/%Y"
        )

    ))

    eventos = [

        "PROJETO_CRIADO",
        "PASTA_CLIENTE_CRIADA",
        "CRONOGRAMA_GERADO",
        "ORDEM_SERVICO_GERADA"

    ]

    for evento in eventos:
        pass

        cur.execute("""

        INSERT INTO onboarding_log(

            created_at,
            company,
            event

        )

        VALUES(

            ?,
            ?,
            ?

        )

        """,(

            hoje.strftime(
                "%d/%m/%Y %H:%M:%S"
            ),

            empresa,

            evento

        ))

    novos += 1

conn.commit()

# ==================================================
# PAINEL
# ==================================================

print("CLIENTES PROCESSADOS")
print("")

print(
    f"CLIENTES ATIVOS: "
    f"{len(clientes)}"
)

print(
    f"NOVOS PROJETOS: "
    f"{novos}"
)

print("")

projetos = cur.execute("""

SELECT

    company,
    project_code,
    status,
    estimated_value

FROM client_projects

ORDER BY estimated_value DESC

""").fetchall()

print("==================================================")
print("PROJETOS")
print("==================================================")
print("")

for p in projetos:
    pass

    print(
        f"{p[0]} | "
        f"{p[1]} | "
        f"{p[2]} | "
        f"R$ {p[3]:,.2f}"
    )

print("")
print("==================================================")
print("RESUMO")
print("==================================================")
print("")

total = sum(
    p[3]
    for p in projetos
)

print(
    f"PROJETOS: "
    f"{len(projetos)}"
)

print(
    f"VALOR TOTAL: "
    f"R$ {total:,.2f}"
)

print("")

if novos > 0:
    pass

    print(
        "NOVOS CLIENTES LIBERADOS "
        "PARA EXECUCAO"
    )

else:
    pass

    print(
        "SEM NOVOS CLIENTES"
    )

print("")
print("==================================================")

conn.close()


