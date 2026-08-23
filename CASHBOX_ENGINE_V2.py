import sqlite3
from datetime import datetime


class CashboxEngineV2:

    def __init__(self):

        self.payment_db = "iotec_payments.db"
        self.cash_db = "iotec_cashbox.db"

        self.create_cashbox()

    # ----------------------------------------------------------

    def create_cashbox(self):

        conn = sqlite3.connect(self.cash_db)

        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS cashbox(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            order_id TEXT UNIQUE,

            gateway TEXT,

            client TEXT,

            value REAL,

            movement TEXT,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ----------------------------------------------------------

    def import_completed_payments(self):

        pay_conn = sqlite3.connect(self.payment_db)
        pay_cursor = pay_conn.cursor()

        cash_conn = sqlite3.connect(self.cash_db)
        cash_cursor = cash_conn.cursor()

        pay_cursor.execute("""

        SELECT

            gateway,
            order_id,
            client,
            value,
            status

        FROM payments

        WHERE status IN ('APPROVED','COMPLETED')

        """)

        pagamentos = pay_cursor.fetchall()

        total = 0

        for gateway, order_id, client, value, status in pagamentos:

            cash_cursor.execute("""

            SELECT id

            FROM cashbox

            WHERE order_id=?

            """,(order_id,))

            if cash_cursor.fetchone():

                continue

            cash_cursor.execute("""

            INSERT INTO cashbox(

                order_id,
                gateway,
                client,
                value,
                movement,
                created_at

            )

            VALUES(?,?,?,?,?,?)

            """,(

                order_id,
                gateway,
                client,
                value,
                "ENTRADA",
                datetime.now().isoformat()

            ))

            total += value

        cash_conn.commit()

        pay_conn.close()
        cash_conn.close()

        print()

        print("="*60)
        print("CASHBOX ENGINE V2")
        print("="*60)
        print("Valor incorporado ao caixa : R$", round(total,2))
        print("="*60)

    # ----------------------------------------------------------

    def show_cashbox(self):

        conn = sqlite3.connect(self.cash_db)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            id,
            gateway,
            order_id,
            client,
            value,
            movement

        FROM cashbox

        ORDER BY id DESC

        """)

        rows = cursor.fetchall()

        conn.close()

        saldo = sum(r[4] for r in rows)

        print()

        print("="*80)
        print("CAIXA IOTEC")
        print("="*80)

        for r in rows:

            print(r)

        print("-"*80)
        print("SALDO :", round(saldo,2))
        print("="*80)


if __name__ == "__main__":

    engine = CashboxEngineV2()

    engine.import_completed_payments()

    engine.show_cashbox()

