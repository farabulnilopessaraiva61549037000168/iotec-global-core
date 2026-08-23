"""
=========================================================
IOTEC LEDGER ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Livro RazÃƒÂ£o Oficial da Plataforma
=========================================================
"""

from datetime import datetime


class LedgerEngine:

    def __init__(self):

        self.records = []

    # -------------------------------------------------

    def register(self,
                 operation,
                 value,
                 origin,
                 reference):

        item = {

            "date": datetime.now(),
            "operation": operation,
            "value": float(value),
            "origin": origin,
            "reference": reference

        }

        self.records.append(item)

        print("")
        print("===================================")
        print("LANÃƒâ€¡AMENTO CONTÃƒÂBIL")
        print("===================================")
        print(f"OperaÃƒÂ§ÃƒÂ£o : {operation}")
        print(f"Valor....: R$ {value:.2f}")
        print(f"Origem...: {origin}")
        print(f"Ref......: {reference}")
        print("===================================")

    # -------------------------------------------------

    def report(self):

        print("")
        print("===================================")
        print("LIVRO RAZÃƒÆ'O IOTEC")
        print("===================================")

        total = 0

        for r in self.records:

            print(f"{r['date']}")
            print(f"{r['operation']}")
            print(f"R$ {r['value']:.2f}")
            print(f"{r['origin']}")
            print("----------------------------")

            total += r["value"]

        print("")
        print(f"TOTAL CONTÃƒÂBIL : R$ {total:.2f}")
        print("===================================")


# =====================================================

if __name__ == "__main__":

    ledger = LedgerEngine()

    ledger.register(

        operation="HOMOLOGAÃƒâ€¡ÃƒÆ'O",

        value=29.90,

        origin="PAYMENT_VALIDATOR_ENGINE",

        reference="HML-000001"

    )

    ledger.report()

