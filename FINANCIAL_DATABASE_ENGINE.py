"""
=========================================================
IOTEC FINANCIAL DATABASE ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
PersistÃƒÂªncia Oficial das TransaÃƒÂ§ÃƒÂµes
=========================================================
"""

import sqlite3
from datetime import datetime


class FinancialDatabaseEngine:

    def __init__(self, database="iotec_financial.db"):

        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

        self.create_tables()

    # ----------------------------------------------------

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS financial_transactions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            transaction_id TEXT UNIQUE,

            payer TEXT,

            amount REAL,

            operation TEXT,

            status TEXT,

            created_at TEXT

        )

        """)

        self.connection.commit()

    # ----------------------------------------------------

    def insert(self,
               transaction_id,
               payer,
               amount,
               operation,
               status):

        self.cursor.execute("""

        INSERT INTO financial_transactions(

            transaction_id,

            payer,

            amount,

            operation,

            status,

            created_at

        )

        VALUES (?,?,?,?,?,?)

        """,

        (

            transaction_id,

            payer,

            amount,

            operation,

            status,

            datetime.now().isoformat()

        ))

        self.connection.commit()

        print("")
        print("========================================")
        print("TRANSAÃƒâ€¡ÃƒÆ'O GRAVADA NO BANCO")
        print("========================================")
        print(transaction_id)
        print("========================================")

    # ----------------------------------------------------

    def list_transactions(self):

        print("")
        print("========================================")
        print("TRANSAÃƒâ€¡Ãƒâ€¢ES")
        print("========================================")

        rows = self.cursor.execute("""

            SELECT

                transaction_id,

                payer,

                amount,

                status

            FROM financial_transactions

        """)

        for row in rows:

            print(row)

        print("========================================")


# ========================================================

if __name__ == "__main__":

    db = FinancialDatabaseEngine()

    db.insert(

        transaction_id="TX-000001",

        payer="PRESIDÃƒÅ NCIA IOTEC",

        amount=29.90,

        operation="HOMOLOGAÃƒâ€¡ÃƒÆ'O",

        status="SUCCESS"

    )

    db.list_transactions()

