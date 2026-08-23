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

leads = cur.execute("""

SELECT

id,
sector,
message,
employees,
users_expected,
urgency

FROM leads

""").fetchall()

for lead in leads:
    pass

    lead_id = lead[0]
    sector = str(lead[1] or "").upper()
    message = str(lead[2] or "").upper()
    employees = lead[3] or 0
    users = lead[4] or 0
    urgency = str(lead[5] or "").upper()

    score = 0

    # setor

    if "TECNOLOG" in sector:
        score += 3

    if "INDUSTR" in sector:
        score += 2

    if "AUTOMATION" in sector:
        score += 3

    # mensagem

    if "IA" in message:
        score += 5

    if "DADOS" in message:
        score += 4

    if "AUTOM" in message:
        score += 3

    # porte

    if employees >= 50:
        score += 2

    if employees >= 200:
        score += 3

    # usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios

    if users >= 20:
        score += 2

    if users >= 100:
        score += 3

    # urgÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia

    if urgency == "ALTA":
        score += 2

    if urgency == "CRITICA":
        score += 4

    cur.execute(
        """
        UPDATE leads
        SET lead_score=?
        WHERE id=?
        """,
        (score, lead_id)
    )

conn.commit()
conn.close()

print("LEAD SCORE CALCULADO")




