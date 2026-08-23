# ==============================================================================# 025_USER_MANAGER.py# ==============================================================================import sqlite3from pathlib import PathROOT = Path(__file__).resolve().parentDB = ROOT / "MISSION_CONTROL" / "database" / "mission_control.db"conn = sqlite3.connect(DB, timeout=30)conn.row_factory = sqlite3.Rowcur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")def listar():    cur.execute("""    SELECT        id,        username,        role,        status    FROM users    ORDER BY id    """)    return cur.fetchall()print("="*80)print("USER MANAGER")print("="*80)for u in listar():    print(        f"{u['id']:03d} | "        f"{u['username']:<15}"        f"{u['role']:<10}"        f"{u['status']}"    )print("="*80)conn.close()

