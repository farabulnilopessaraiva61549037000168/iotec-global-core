import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DATABASE = "opportunity_radar.db"

def commercial_queue():
    pass

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""

    SELECT *

    FROM opportunities

    WHERE status='OPEN'

    ORDER BY score DESC

    """)

    rows = cur.fetchall()

    conn.close()

    print("")
    print("================================================")
    print(" COMMERCIAL TOWER ")
    print("================================================")

    for row in rows:
        pass

        score = row["score"]

        if score >= 60:
            action = "PRIORIDADE MAXIMA"

        elif score >= 40:
            action = "ANALISAR"

        elif score >= 20:
            action = "OBSERVAR"

        else:
            action = "BAIXA PRIORIDADE"

        print("")
        print("ID       :", row["id"])
        print("TITLE    :", row["title"])
        print("ENGINE   :", row["matched_engine"])
        print("SCORE    :", score)
        print("ACTION   :", action)

    print("")
    print("================================================")

if __name__ == "__main__":
    pass

    commercial_queue()


