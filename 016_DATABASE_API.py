# ==============================================================================# 016_DATABASE_API.py# ==============================================================================import sqlite3from pathlib import PathROOT = Path(__file__).resolve().parentDB = ROOT / "MISSION_CONTROL" / "database" / "mission_control.db"conn = sqlite3.connect(DB, timeout=30)conn.row_factory = sqlite3.Rowcur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")TABELAS = [    "missions",    "events",    "logs",    "system_logs",    "maestro_history",    "api_requests",    "api_routes"]print("="*80)print("DATABASE INSPECTOR")print("="*80)for tabela in TABELAS:    try:        cur.execute(f"SELECT COUNT(*) total FROM {tabela}")        total = cur.fetchone()["total"]        print(f"{tabela:<20} {total}")    except Exception as e:        print(f"{tabela:<20} ERRO -> {e}")print("="*80)conn.close()

