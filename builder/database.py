import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path

class Database:

    def build(self):

        Path("database").mkdir(exist_ok=True)

        conn=sqlite3.connect("database/iotec.db")

        conn.execute("""

        CREATE TABLE IF NOT EXISTS system(

            id INTEGER PRIMARY KEY,

            created TEXT

        )

        """)

        conn.commit()

        conn.close()

        print("[DATABASE] ONLINE")


