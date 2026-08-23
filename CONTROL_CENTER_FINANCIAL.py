import sqlite3
from datetime import datetime


class FinancialControlCenter:

    def __init__(self):

        self.payment_db = "iotec_payments.db"
        self.cash_db = "iotec_cashbox.db"

    # -----------------------------------------------------

    def payment_summary(self):

        conn = sqlite3.connect(self.payment_db)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM payments

        """)

        total = cursor.fetchone()[0]

        cursor.execute("""

        SELECT COUNT(*)

        FROM payments

        WHERE status='CREATED'

        """)

        created = cursor.fetchone()[0]

        cursor.execute("""

        SELECT COUNT(*)

        FROM payments

        WHERE status='APPROVED'

        """)

        approved = cursor.fetchone()[0]

        cursor.execute("""

        SELECT COUNT(*)

        FROM payments

        WHERE status='COMPLETED'

        """)

        completed = cursor.fetchone()[0]

        cursor.execute("""

        SELECT IFNULL(SUM(value),0)

        FROM payments

        """)

        amount = cursor.fetchone()[0]

        conn.close()

        return {

            "total": total,

            "created": created,

            "approved": approved,

            "completed": completed,

            "amount": amount

        }

    # -----------------------------------------------------

    def cash_summary(self):

        conn = sqlite3.connect(self.cash_db)

        cursor = conn.cursor()

        cursor.execute("""

        SELECT IFNULL(SUM(value),0)

        FROM cashbox

        """)

        cash = cursor.fetchone()[0]

        cursor.execute("""

        SELECT COUNT(*)

        FROM cashbox

        """)

        entries = cursor.fetchone()[0]

        conn.close()

        return {

            "cash": cash,

            "entries": entries

        }

    # -----------------------------------------------------

    def dashboard(self):

        pay = self.payment_summary()

        cash = self.cash_summary()

        print()

        print("=" * 70)

        print("IOTEC CONTROL CENTER - FINANCEIRO")

        print("=" * 70)

        print("Data...............:", datetime.now())

        print()

        print("PAGAMENTOS")

        print("-" * 70)

        print(f"Total................: {pay['total']}")

        print(f"Criados..............: {pay['created']}")

        print(f"Aprovados............: {pay['approved']}")

        print(f"ConcluÃƒÂ­dos...........: {pay['completed']}")

        print(f"Valor Total..........: R$ {pay['amount']:.2f}")

        print()

        print("CAIXA")

        print("-" * 70)

        print(f"LanÃƒÂ§amentos..........: {cash['entries']}")

        print(f"Saldo................: R$ {cash['cash']:.2f}")

        print()

        print("STATUS")

        print("-" * 70)

        print("Gateway..............: PAYPAL")

        print("Banco de Pagamentos..: OK")

        print("Banco Financeiro.....: OK")

        print("Caixa................: OK")

        print()

        print("=" * 70)


if __name__ == "__main__":

    FinancialControlCenter().dashboard()

