"""
=========================================================
IOTEC FINANCIAL AUDIT ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Auditoria Financeira Oficial
=========================================================
"""

from datetime import datetime


class FinancialAuditEngine:

    def __init__(self):

        self.events = []

    # -------------------------------------------------

    def register(self,
                 transaction_id,
                 status,
                 amount,
                 payer,
                 operation):

        event = {

            "timestamp": datetime.now(),

            "transaction_id": transaction_id,

            "status": status,

            "amount": float(amount),

            "payer": payer,

            "operation": operation

        }

        self.events.append(event)

        print("")
        print("=========================================")
        print("AUDITORIA FINANCEIRA")
        print("=========================================")
        print(f"DATA.......: {event['timestamp']}")
        print(f"ID.........: {transaction_id}")
        print(f"PAGADOR....: {payer}")
        print(f"VALOR......: R$ {amount:.2f}")
        print(f"OPERAÃƒâ€¡ÃƒÆ'O...: {operation}")
        print(f"STATUS.....: {status}")
        print("=========================================")

    # -------------------------------------------------

    def report(self):

        print("")
        print("=========================================")
        print("RELATÃƒâ€œRIO DE AUDITORIA")
        print("=========================================")

        for item in self.events:

            print(f"{item['transaction_id']}")

            print(f"{item['status']}")

            print(f"R$ {item['amount']:.2f}")

            print("-----------------------------")

        print(f"TOTAL DE EVENTOS : {len(self.events)}")

        print("=========================================")


# ======================================================

if __name__ == "__main__":

    audit = FinancialAuditEngine()

    audit.register(

        transaction_id="TX-DEMO",

        status="SUCCESS",

        amount=29.90,

        payer="PRESIDÃƒÅ NCIA IOTEC",

        operation="HOMOLOGAÃƒâ€¡ÃƒÆ'O"

    )

    audit.report()

