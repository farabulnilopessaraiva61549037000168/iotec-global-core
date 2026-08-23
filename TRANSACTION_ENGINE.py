"""
=========================================================
IOTEC TRANSACTION ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Gerador Oficial de TransaÃƒÂ§ÃƒÂµes Financeiras
=========================================================
"""

from datetime import datetime
import uuid


class TransactionEngine:

    def __init__(self):

        self.transactions = []

    # -------------------------------------------------

    def create(
        self,
        payer,
        amount,
        description,
        payment_method="PIX"
    ):

        transaction = {

            "transaction_id":
                "TX-" +
                datetime.now().strftime("%Y%m%d") +
                "-" +
                uuid.uuid4().hex[:8].upper(),

            "created_at":
                datetime.now(),

            "payer":
                payer,

            "amount":
                float(amount),

            "description":
                description,

            "payment_method":
                payment_method,

            "status":
                "CREATED"

        }

        self.transactions.append(transaction)

        print("")
        print("==========================================")
        print("TRANSAÃƒâ€¡ÃƒÆ'O GERADA")
        print("==========================================")
        print(f"ID.........: {transaction['transaction_id']}")
        print(f"PAGADOR....: {transaction['payer']}")
        print(f"VALOR......: R$ {transaction['amount']:.2f}")
        print(f"MÃƒâ€°TODO.....: {transaction['payment_method']}")
        print(f"STATUS.....: {transaction['status']}")
        print("==========================================")
        print("")

        return transaction

    # -------------------------------------------------

    def approve(self, transaction):

        transaction["status"] = "APPROVED"

        print(
            f"TransaÃƒÂ§ÃƒÂ£o {transaction['transaction_id']} APROVADA."
        )

        return transaction

    # -------------------------------------------------

    def reject(self, transaction):

        transaction["status"] = "REJECTED"

        print(
            f"TransaÃƒÂ§ÃƒÂ£o {transaction['transaction_id']} REJEITADA."
        )

        return transaction


# =====================================================

if __name__ == "__main__":

    engine = TransactionEngine()

    tx = engine.create(

        payer="PRESIDÃƒÅ NCIA IOTEC",

        amount=29.90,

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o"

    )

    engine.approve(tx)

