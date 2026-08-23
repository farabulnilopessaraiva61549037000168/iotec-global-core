"""
=========================================================
IOTEC FINANCIAL CORE ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
NÃƒÂºcleo Financeiro Oficial
=========================================================
"""

from TRANSACTION_ENGINE import TransactionEngine
from PAYMENT_VALIDATOR_ENGINE import PaymentValidatorEngine
from CASHBOX_ENGINE import CashboxEngine
from LEDGER_ENGINE import LedgerEngine
from FINANCIAL_AUDIT_ENGINE import FinancialAuditEngine
from FINANCIAL_DATABASE_ENGINE import FinancialDatabaseEngine


class FinancialCoreEngine:

    def __init__(self):

        self.transaction = TransactionEngine()

        self.validator = PaymentValidatorEngine()

        self.cashbox = CashboxEngine()

        self.ledger = LedgerEngine()

        self.audit = FinancialAuditEngine()

        self.database = FinancialDatabaseEngine()

    # ----------------------------------------------------

    def execute(
        self,
        payer,
        amount,
        description
    ):

        tx = self.transaction.create(

            payer=payer,

            amount=amount,

            description=description

        )

        self.transaction.approve(tx)

        self.validator.validate(

            payment_id=tx["transaction_id"],

            payer=tx["payer"],

            amount=tx["amount"],

            method=tx["payment_method"]

        )

        self.cashbox.deposit(

            description=tx["description"],

            amount=tx["amount"],

            source=tx["transaction_id"]

        )

        self.ledger.register(

            operation="RECEBIMENTO",

            value=tx["amount"],

            origin=tx["payer"],

            reference=tx["transaction_id"]

        )

        self.audit.register(

            transaction_id=tx["transaction_id"],

            status="SUCCESS",

            amount=tx["amount"],

            payer=tx["payer"],

            operation="RECEBIMENTO"

        )

        self.database.insert(

            transaction_id=tx["transaction_id"],

            payer=tx["payer"],

            amount=tx["amount"],

            operation="RECEBIMENTO",

            status="SUCCESS"

        )

        print("")
        print("===================================================")
        print("IOTEC FINANCIAL CORE")
        print("===================================================")
        print("TRANSACTION ............. OK")
        print("VALIDATOR ............... OK")
        print("CASHBOX ................ OK")
        print("LEDGER ................. OK")
        print("AUDIT ................. OK")
        print("DATABASE .............. OK")
        print("STATUS ................ CONCLUÃƒÂDO")
        print("===================================================")

        return tx


# =========================================================

if __name__ == "__main__":

    engine = FinancialCoreEngine()

    engine.execute(

        payer="PRESIDÃƒÅ NCIA IOTEC",

        amount=29.90,

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o"

    )

