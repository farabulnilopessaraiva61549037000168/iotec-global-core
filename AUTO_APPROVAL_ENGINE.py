import sqlite3
import subprocess
import sys

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

print("="*70)
print("AUTO APPROVAL ENGINE")
print("="*70)

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""

SELECT opportunity_id

FROM pipeline

WHERE status='PROPOSTA_ENVIADA'

ORDER BY opportunity_id

""").fetchall()

if not rows:

    print()
    print("Nenhuma proposta aguardando aprovaÃ§Ã£o.")

else:

    print()
    print(f"Propostas encontradas: {len(rows)}")
    print()

    for (op_id,) in rows:

        print(f"Aprovando Opportunity {op_id}")

        subprocess.run(

            [
                sys.executable,
                r"C:\IOTEC\APPROVE_PROPOSAL.py",
                str(op_id)
            ]

        )

conn.close()

print()
print("FINALIZADO")


