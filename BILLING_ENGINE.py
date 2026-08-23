"""
=========================================================
IOTEC - BILLING ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
EmissÃƒÂ£o da cobranÃƒÂ§a de homologaÃƒÂ§ÃƒÂ£o.
=========================================================
"""

from datetime import datetime
import uuid


class BillingEngine:

    def __init__(self):

        self.invoice = None

    # --------------------------------------------------

    def create_invoice(
        self,
        customer,
        description,
        value
    ):

        self.invoice = {

            "id": str(uuid.uuid4())[:8].upper(),

            "customer": customer,

            "description": description,

            "value": float(value),

            "status": "AGUARDANDO PAGAMENTO",

            "created_at": datetime.now()

        }

    # --------------------------------------------------

    def mark_as_paid(self):

        if self.invoice:

            self.invoice["status"] = "PAGO"
            self.invoice["paid_at"] = datetime.now()

    # --------------------------------------------------

    def show(self):

        if not self.invoice:

            print("Nenhuma cobranÃƒÂ§a criada.")
            return

        print("\n========================================")
        print("IOTEC BILLING ENGINE")
        print("========================================")

        print(f"Fatura      : {self.invoice['id']}")
        print(f"Cliente     : {self.invoice['customer']}")
        print(f"DescriÃƒÂ§ÃƒÂ£o   : {self.invoice['description']}")
        print(f"Valor       : R$ {self.invoice['value']:.2f}")
        print(f"Status      : {self.invoice['status']}")
        print(f"Criada em   : {self.invoice['created_at']}")

        if "paid_at" in self.invoice:
            print(f"Pagamento   : {self.invoice['paid_at']}")

        print("========================================\n")


# ======================================================

if __name__ == "__main__":

    engine = BillingEngine()

    engine.create_invoice(

        customer="PRESIDÃƒÅ NCIA IOTEC",

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o",

        value=29.90

    )

    engine.show()

    print("Simulando pagamento...\n")

    engine.mark_as_paid()

    engine.show()


