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

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC PROJECT PROGRESS ENGINE")
print("==================================================")
print("")

# ==================================================
# CONSULTA
# ==================================================

if len(sys.argv) == 1:
    pass

    projetos = cur.execute("""

    SELECT

        project_code,
        company,
        status

    FROM client_projects

    ORDER BY company

    """).fetchall()

    print("PROJETOS")
    print("")

    for codigo, empresa, status in projetos:
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
            pass

            progresso = (
                concluidas * 100
            ) / total

        print(
            f"{codigo} | "
            f"{empresa} | "
            f"{progresso:.0f}% | "
            f"{status}"
        )

    print("")
    print("TAREFAS")
    print("")

    tarefas = cur.execute("""

    SELECT

        id,
        company,
        task_name,
        status

    FROM project_tasks

    ORDER BY id

    """).fetchall()

    for t in tarefas:
        pass

        print(
            f"ID={t[0]} | "
            f"{t[1]} | "
            f"{t[2]} | "
            f"{t[3]}"
        )

    print("")
    print("USO:")
    print("")
    print(
        'python PROJECT_PROGRESS_ENGINE.py ID'
    )

    conn.close()
    raise SystemExit

# ==================================================
# CONCLUIR TAREFA
# ==================================================

task_id = int(sys.argv[1])

cur.execute("""

UPDATE project_tasks

SET

    status='CONCLUIDA',
    completed_at=?

WHERE id=?

""",(

    datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    ),

    task_id

))

conn.commit()

# ==================================================
# IDENTIFICAR PROJETO
# ==================================================

info = cur.execute("""

SELECT

    project_code,
    company

FROM project_tasks

WHERE id=?

""",(task_id,)).fetchone()

if not info:
    pass

    print("TAREFA NAO ENCONTRADA")
    conn.close()
    raise SystemExit

codigo = info[0]
empresa = info[1]

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

progresso = (
    concluidas * 100
) / total

# ==================================================
# STATUS PROJETO
# ==================================================

novo_status = "PLANEJAMENTO"

if progresso >= 100:
    pass

    novo_status = "ENTREGUE"

elif progresso >= 80:
    pass

    novo_status = "IMPLANTACAO"

elif progresso >= 50:
    pass

    novo_status = "DESENVOLVIMENTO"

elif progresso >= 20:
    pass

    novo_status = "DIAGNOSTICO"

cur.execute("""

UPDATE client_projects

SET status=?

WHERE project_code=?

""",(

    novo_status,
    codigo

))

conn.commit()

print("")
print("==================================================")
print("ATUALIZACAO")
print("==================================================")
print("")

print("EMPRESA:", empresa)
print("PROJETO:", codigo)

print(
    f"PROGRESSO: "
    f"{progresso:.0f}%"
)

print(
    "STATUS:",
    novo_status
)

if progresso == 100:
    pass

    print("")
    print(
        "PROJETO ENTREGUE"
    )

print("")
print("==================================================")

conn.close()


