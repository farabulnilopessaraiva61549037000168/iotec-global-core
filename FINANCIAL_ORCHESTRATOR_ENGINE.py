"""
=========================================================
IOTEC FINANCIAL ORCHESTRATOR ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Orquestrador Financeiro Oficial
=========================================================
"""

from TRANSACTION_ENGINE import TransactionEngine
from PAYMENT_VALIDATOR_ENGINE import PaymentValidatorEngine
from CASHBOX_ENGINE import CashboxEngine
from LEDGER_ENGINE import LedgerEngine


class FinancialOrchestrator:

    def __init__(self):

        self.transaction = TransactionEngine()
        self.validator = PaymentValidatorEngine()
        self.cashbox = CashboxEngine()
        self.ledger = LedgerEngine()

    # -------------------------------------------------

    def execute(self,
                payer,
                amount,
                description):

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

        print("")
        print("==============================================")
        print("IOTEC FINANCIAL ORCHESTRATOR")
        print("==============================================")
        print("TRANSAÃƒâ€¡ÃƒÆ'O : OK")
        print("VALIDAÃƒâ€¡ÃƒÆ'O : OK")
        print("CAIXA     : OK")
        print("CONTÃƒÂBIL  : OK")
        print("STATUS    : CONCLUÃƒÂDO")
        print("==============================================")

        return tx


# =====================================================

if __name__ == "__main__":

    orchestrator = FinancialOrchestrator()

    orchestrator.execute(

        payer="PRESIDÃƒÅ NCIA IOTEC",

        amount=29.90,

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o"

    )

