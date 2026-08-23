import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# REAL_ACQUISITION_ENGINE.py

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

class RealAcquisitionEngine:
    pass

    def __init__(self):
        pass

        self.conn = sqlite3.connect(DB)
        self.cur = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        pass

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS acquired_companies (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,
            sector TEXT,
            city TEXT,

            website TEXT,
            phone TEXT,

            source TEXT,
            acquisition_date TEXT,

            score INTEGER,

            reservoir TEXT,

            status TEXT

        )

        """)

        self.conn.commit()

    def validate_company(
        self,
        company,
        source
    ):

        if not company:
            return False

        if not source:
            return False

        return True

    def company_exists(
        self,
        company
    ):

        row = self.cur.execute("""

        SELECT id

        FROM acquired_companies

        WHERE company = ?

        LIMIT 1

        """, (company,)).fetchone()

        return row is not None

    def add_company(
        self,
        company,
        sector,
        city,
        website,
        phone,
        source,
        score
    ):

        if not self.validate_company(
            company,
            source
        ):
            return

        if self.company_exists(company):
            return

        reservoir = "OPERACIONAL"

        if score >= 90:
            reservoir = "TOP_TIER"

        elif score >= 80:
            reservoir = "PREMIUM"

        self.cur.execute("""

        INSERT INTO acquired_companies (

            company,
            sector,
            city,

            website,
            phone,

            source,
            acquisition_date,

            score,

            reservoir,

            status

        )

        VALUES (

            ?, ?, ?,
            ?, ?,
            ?, ?,
            ?, ?, ?

        )

        """, (

            company,
            sector,
            city,

            website,
            phone,

            source,
            datetime.now().isoformat(),

            score,

            reservoir,

            "ATIVA"

        ))

        self.conn.commit()

    def dashboard(self):
        pass

        total = self.cur.execute("""

        SELECT COUNT(*)

        FROM acquired_companies

        """).fetchone()[0]

        print("")
        print("=" * 50)
        print("IOTEC REAL ACQUISITION ENGINE")
        print("=" * 50)
        print("")

        print(f"EMPRESAS: {total}")

        print("")
        print("RESERVATORIOS")
        print("")

        rows = self.cur.execute("""

        SELECT reservoir,
               COUNT(*)

        FROM acquired_companies

        GROUP BY reservoir

        """).fetchall()

        for r, q in rows:
            pass

            print(
                f"{r}: {q}"
            )

        print("")
        print("=" * 50)

if __name__ == "__main__":
    pass

    engine = RealAcquisitionEngine()

    engine.dashboard()


