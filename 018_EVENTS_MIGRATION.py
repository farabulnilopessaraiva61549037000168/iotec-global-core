# ==============================================================================# 018_EVENTS_MIGRATION.py# ==============================================================================import sqlite3from pathlib import PathROOT = Path(__file__).resolve().parentDB = ROOT / "MISSION_CONTROL" / "database" / "mission_control.db"conn = sqlite3.connect(DB, timeout=30)cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")cur.execute("PRAGMA table_info(events)")cols = [c[1] for c in cur.fetchall()]required = {    "timestamp":"TEXT",    "event":"TEXT",    "origin":"TEXT",    "severity":"TEXT",    "payload":"TEXT"}for column, dtype in required.items():    if column not in cols:        print(f"[ADD] {column}")        cur.execute(            f"ALTER TABLE events ADD COLUMN {column} {dtype}"        )conn.commit()print()cur.execute("PRAGMA table_info(events)")for c in cur.fetchall():    print(c[1])conn.close()print("\nEVENTS MIGRATION OK")

