import sqlite3
from datetime import datetime


class PaymentStatusEngine:

    def __init__(self):

        self.database = "iotec_payments.db"

    # ---------------------------------------------------

    def update_status(self, order_id, new_status):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""

        UPDATE payments

        SET

            status=?,

            updated_at=?

        WHERE

            order_id=?

        """, (

            new_status,

            datetime.now().isoformat(),

            order_id

        ))

        conn.commit()

        affected = cursor.rowcount

        conn.close()

        print()

        print("=" * 60)

        print("PAYMENT STATUS ENGINE")

        print("=" * 60)

        if affected:

            print("Order........:", order_id)
            print("Novo Status..:", new_status)
            print("Registro atualizado com sucesso.")

        else:

            print("Order nÃƒÂ£o encontrada.")

        print("=" * 60)

    # ---------------------------------------------------

    def history(self):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            id,

            gateway,

            order_id,

            client,

            value,

            status,

            updated_at

        FROM payments

        ORDER BY id DESC

        """)

        rows = cursor.fetchall()

        conn.close()

        print()

        print("=" * 80)

        print("HISTÃƒâ€œRICO DE PAGAMENTOS")

        print("=" * 80)

        for row in rows:

            print(row)

        print("=" * 80)


# =======================================================

if __name__ == "__main__":

    engine = PaymentStatusEngine()

    engine.update_status(

        order_id="77648136M3134303X",

        new_status="APPROVED"

    )

    engine.history()

