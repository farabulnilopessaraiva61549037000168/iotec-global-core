# ==============================================================================# 058A_DATABASE_MIGRATION_EXECUTION_LOGS.py# ==============================================================================import sqlite3from pathlib import PathROOT = Path(__file__).resolve().parentDB = ROOT / "MISSION_CONTROL" / "database" / "mission_control.db"conn = sqlite3.connect(DB, timeout=30)cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")print("="*80)print("EXECUTION LOGS MIGRATION")print("="*80)cur.execute("PRAGMA table_info(execution_queue)")cols = [c[1] for c in cur.fetchall()]novas = [    ("stdout","TEXT"),    ("stderr","TEXT"),    ("exit_code","INTEGER")]for nome,tipo in novas:    if nome not in cols:        cur.execute(f"""        ALTER TABLE execution_queue        ADD COLUMN {nome} {tipo}        """)        print(f"[OK] Coluna criada -> {nome}")    else:        print(f"[OK] JÃ¡ existe -> {nome}")conn.commit()print("="*80)print("MIGRATION FINALIZADA")print("="*80)conn.close()

