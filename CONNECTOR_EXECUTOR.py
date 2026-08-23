import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("===================================")
print("CONNECTOR EXECUTOR")
print("===================================")
print("")

fontes = cur.execute("""

SELECT

    id,
    source_name,
    source_type,
    source_url,
    priority

FROM acquisition_sources

WHERE active = 1

ORDER BY priority DESC,
         source_name

""").fetchall()

if not fontes:
    pass

    print("NENHUMA FONTE ATIVA")
    print("")

    conn.close()
    raise SystemExit

print("FONTES ATIVAS")
print("")

for f in fontes:
    pass

    print(
        f"ID={f[0]} | "
        f"{f[1]} | "
        f"{f[2]} | "
        f"PRIORIDADE={f[4]}"
    )

print("")
print("===================================")
print("RESUMO")
print("===================================")
print("")

print("TOTAL DE FONTES:", len(fontes))

print("")

for f in fontes:
    pass

    print(
        f"EXECUTANDO -> "
        f"{f[1]} "
        f"({f[3]})"
    )

print("")
print("===================================")

conn.close()




