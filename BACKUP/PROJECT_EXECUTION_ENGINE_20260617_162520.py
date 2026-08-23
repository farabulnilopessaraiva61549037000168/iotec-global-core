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
print("IOTEC PROJECT EXECUTION ENGINE")
print("==================================================")
print("")

cur.execute("""

CREATE TABLE IF NOT EXISTS project_tasks(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    project_code TEXT,

    company TEXT,

    task_name TEXT,

    status TEXT,

    created_at TEXT,

    completed_at TEXT

)

""")

conn.commit()

projetos = cur.execute("""

SELECT

company,
project_code

FROM client_projects

""").fetchall()

novas_tarefas = 0

for empresa, codigo in projetos:
    pass

    existe = cur.execute("""

    SELECT COUNT(*)

    FROM project_tasks

    WHERE project_code=?

    """,(codigo,)).fetchone()[0]

    if existe > 0:
        continue

    tarefas = [

        "LEVANTAMENTO",
        "DIAGNOSTICO",
        "DESENVOLVIMENTO",
        "TESTES",
        "IMPLANTACAO",
        "ENTREGA"

    ]

    for tarefa in tarefas:
        pass

        cur.execute("""

        INSERT INTO project_tasks(

            project_code,
            company,
            task_name,
            status,
            created_at

        )

        VALUES(

            ?,
            ?,
            ?,
            'PENDENTE',
            ?

        )

        """,(

            codigo,
            empresa,
            tarefa,
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

        ))

        novas_tarefas += 1

conn.commit()

print("PROJETOS")
print("")

for empresa, codigo in projetos:
    pass

    total = cur.execute("""

    SELECT COUNT(*)

    FROM project_tasks

    WHERE project_code=?

    """,(codigo,)).fetchone()[0]

    concluidas = cur.execute("""

    SELECT COUNT(*)

    FROM project_tasks

    WHERE project_code=?
    AND status='CONCLUIDA'

    """,(codigo,)).fetchone()[0]

    progresso = 0

    if total > 0:
        progresso = (
            concluidas * 100
        ) / total

    print(
        f"{empresa} | "
        f"{codigo} | "
        f"{progresso:.0f}%"
    )

print("")
print("==================================================")
print("RESUMO")
print("==================================================")
print("")

print(
    f"TAREFAS CRIADAS: "
    f"{novas_tarefas}"
)

print(
    f"PROJETOS: "
    f"{len(projetos)}"
)

print("")
print("==================================================")

conn.close()


