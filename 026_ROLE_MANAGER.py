# ==============================================================================# 026_ROLE_MANAGER.py# ==============================================================================import sqlite3from pathlib import PathROOT = Path(__file__).resolve().parentDB = ROOT / "MISSION_CONTROL" / "database" / "mission_control.db"conn = sqlite3.connect(DB, timeout=30)conn.row_factory = sqlite3.Rowcur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")cur.execute("""SELECT    u.username,    u.role,    COUNT(p.permission) permissionsFROM users uLEFT JOIN permissions pON u.role=p.roleGROUP BY    u.username,    u.roleORDER BY    u.username""")print("="*80)print("ROLE MANAGER")print("="*80)for row in cur.fetchall():    print(        f"{row['username']:<20}"        f"{row['role']:<10}"        f"{row['permissions']}"    )print("="*80)conn.close()

