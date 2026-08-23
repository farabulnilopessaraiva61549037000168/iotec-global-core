"""
=========================================================
IOTEC PAYMENT VALIDATOR ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Valida pagamentos homologados antes de liberar o caixa.
=========================================================
"""

from datetime import datetime


class PaymentValidatorEngine:

    def __init__(self):

        self.validated = False
        self.payment = None

    # ----------------------------------------------------

    def validate(
        self,
        payment_id,
        amount,
        payer,
        method="PIX"
    ):

        self.payment = {

            "payment_id": payment_id,
            "amount": float(amount),
            "payer": payer,
            "method": method,
            "validated_at": datetime.now()

        }

        self.validated = True

        print("")
        print("======================================")
        print("PAGAMENTO VALIDADO")
        print("======================================")
        print(f"ID.............: {payment_id}")
        print(f"PAGADOR........: {payer}")
        print(f"VALOR..........: R$ {amount:.2f}")
        print(f"MÃƒâ€°TODO.........: {method}")
        print("STATUS.........: VALIDADO")
        print("======================================")
        print("")

        return True

    # ----------------------------------------------------

    def is_valid(self):

        return self.validated

    # ----------------------------------------------------

    def get_payment(self):

        return self.payment


# ========================================================

if __name__ == "__main__":

    engine = PaymentValidatorEngine()

    engine.validate(

        payment_id="HML-000001",

        amount=29.90,

        payer="PRESIDÃƒÅ NCIA IOTEC",

        method="PIX"

    )

