import sqlite3
from datetime import datetime


class PaymentDatabaseEngine:

    def __init__(self):

        self.database = "iotec_payments.db"

        self.create_database()

    # --------------------------------------------------------

    def create_database(self):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gateway TEXT,

            order_id TEXT,

            reference TEXT,

            client TEXT,

            description TEXT,

            value REAL,

            status TEXT,

            checkout_url TEXT,

            created_at TEXT,

            updated_at TEXT

        )
        """)

        conn.commit()

        conn.close()

    # --------------------------------------------------------

    def save(self,
             gateway,
             order_id,
             reference,
             client,
             description,
             value,
             status,
             checkout_url):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        now = datetime.now().isoformat()

        cursor.execute("""
        INSERT INTO payments(

            gateway,
            order_id,
            reference,
            client,
            description,
            value,
            status,
            checkout_url,
            created_at,
            updated_at

        )
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (

            gateway,
            order_id,
            reference,
            client,
            description,
            value,
            status,
            checkout_url,
            now,
            now

        ))

        conn.commit()

        conn.close()

        print()
        print("=" * 60)
        print("PAYMENT DATABASE ENGINE")
        print("=" * 60)
        print("Pagamento registrado com sucesso.")
        print("=" * 60)

    # --------------------------------------------------------

    def list_all(self):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            id,
            gateway,
            order_id,
            client,
            value,
            status
        FROM payments
        ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        print()
        print("=" * 60)
        print("PAGAMENTOS REGISTRADOS")
        print("=" * 60)

        for row in rows:
            print(row)

        print("=" * 60)


if __name__ == "__main__":

    db = PaymentDatabaseEngine()

    db.save(

        gateway="PAYPAL",

        order_id="77648136M3134303X",

        reference="IOTEC-001",

        client="PRESIDÃƒÅ NCIA IOTEC",

        description="HomologaÃƒÂ§ÃƒÂ£o Primeiro PavilhÃƒÂ£o",

        value=29.90,

        status="CREATED",

        checkout_url="https://www.sandbox.paypal.com/checkoutnow?token=77648136M3134303X"

    )

    db.list_all()

