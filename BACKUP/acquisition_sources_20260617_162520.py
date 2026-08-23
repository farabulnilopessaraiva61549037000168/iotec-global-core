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

cur.execute("""

CREATE TABLE IF NOT EXISTS acquisition_sources (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source_name TEXT,
    source_type TEXT,
    source_url TEXT,

    active INTEGER DEFAULT 1,

    priority INTEGER DEFAULT 50,

    created_at TEXT

)

""")

conn.commit()

# ==================================================
# ADD
# ==================================================

if len(sys.argv) >= 5 and sys.argv[1].lower() == "add":
    pass

    nome = sys.argv[2]
    tipo = sys.argv[3]
    url = sys.argv[4]

    cur.execute("""

    INSERT INTO acquisition_sources(

        source_name,
        source_type,
        source_url,
        active,
        priority,
        created_at

    )

    VALUES(

        ?,?,?,1,50,?

    )

    """,(

        nome,
        tipo,
        url,
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    ))

    conn.commit()

    print("")
    print("===================================")
    print("FONTE ADICIONADA")
    print("===================================")
    print("")
    print("NOME:", nome)
    print("TIPO:", tipo)
    print("URL :", url)
    print("")

    conn.close()
    raise SystemExit

# ==================================================
# ENABLE
# ==================================================

if len(sys.argv) >= 3 and sys.argv[1].lower() == "enable":
    pass

    fonte_id = int(sys.argv[2])

    cur.execute("""

    UPDATE acquisition_sources

    SET active = 1

    WHERE id = ?

    """,(fonte_id,))

    conn.commit()

    print("")
    print("FONTE ATIVADA")
    print("ID:", fonte_id)
    print("")

    conn.close()
    raise SystemExit

# ==================================================
# DISABLE
# ==================================================

if len(sys.argv) >= 3 and sys.argv[1].lower() == "disable":
    pass

    fonte_id = int(sys.argv[2])

    cur.execute("""

    UPDATE acquisition_sources

    SET active = 0

    WHERE id = ?

    """,(fonte_id,))

    conn.commit()

    print("")
    print("FONTE DESATIVADA")
    print("ID:", fonte_id)
    print("")

    conn.close()
    raise SystemExit

# ==================================================
# DELETE
# ==================================================

if len(sys.argv) >= 3 and sys.argv[1].lower() == "delete":
    pass

    fonte_id = int(sys.argv[2])

    cur.execute("""

    DELETE FROM acquisition_sources

    WHERE id = ?

    """,(fonte_id,))

    conn.commit()

    print("")
    print("FONTE REMOVIDA")
    print("ID:", fonte_id)
    print("")

    conn.close()
    raise SystemExit

# ==================================================
# LIST
# ==================================================

if len(sys.argv) >= 2 and sys.argv[1].lower() == "list":
    pass

    print("")
    print("===================================")
    print("FONTES CADASTRADAS")
    print("===================================")
    print("")

    fontes = cur.execute("""

    SELECT

        id,
        source_name,
        source_type,
        active,
        priority

    FROM acquisition_sources

    ORDER BY priority DESC,
             source_name

    """).fetchall()

    if not fontes:
        pass

        print("NENHUMA FONTE CADASTRADA")
        print("")

    else:
        pass

        for f in fontes:
            pass

            status = "ATIVA"

            if f[3] == 0:
                status = "INATIVA"

            print(
                f"ID={f[0]} | "
                f"{f[1]} | "
                f"{f[2]} | "
                f"{status} | "
                f"PRIORIDADE={f[4]}"
            )

    print("")
    print("===================================")

    conn.close()
    raise SystemExit

# ==================================================
# DASHBOARD
# ==================================================

total = cur.execute("""

SELECT COUNT(*)

FROM acquisition_sources

""").fetchone()[0]

ativas = cur.execute("""

SELECT COUNT(*)

FROM acquisition_sources

WHERE active = 1

""").fetchone()[0]

print("")
print("===================================")
print("REAL SOURCE MANAGER")
print("===================================")
print("")
print("FONTES:", total)
print("ATIVAS:", ativas)
print("")
print("USO:")
print("")
print('python REAL_SOURCE_MANAGER.py add "NOME" "TIPO" "URL"')
print("python REAL_SOURCE_MANAGER.py list")
print("python REAL_SOURCE_MANAGER.py enable ID")
print("python REAL_SOURCE_MANAGER.py disable ID")
print("python REAL_SOURCE_MANAGER.py delete ID")
print("")
print("===================================")

conn.close()


