"""
=========================================================
IOTEC FINANCIAL PIPELINE ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Fluxo Financeiro Integrado
=========================================================
"""

from PAYMENT_VALIDATOR_ENGINE import PaymentValidatorEngine
from CASHBOX_ENGINE import CashboxEngine
from LEDGER_ENGINE import LedgerEngine


class FinancialPipeline:

    def __init__(self):

        self.validator = PaymentValidatorEngine()
        self.cashbox = CashboxEngine()
        self.ledger = LedgerEngine()

    # -------------------------------------------------

    def process(self,
                payment_id,
                payer,
                amount):

        ok = self.validator.validate(
            payment_id=payment_id,
            payer=payer,
            amount=amount,
            method="PIX"
        )

        if not ok:

            print("Pagamento recusado.")
            return False

        self.cashbox.deposit(
            description="HomologaÃƒÂ§ÃƒÂ£o Primeiro PavilhÃƒÂ£o",
            amount=amount,
            source="PAYMENT_VALIDATOR_ENGINE"
        )

        self.ledger.register(
            operation="HOMOLOGAÃƒâ€¡ÃƒÆ'O",
            value=amount,
            origin="PAYMENT_VALIDATOR_ENGINE",
            reference=payment_id
        )

        print("")
        print("======================================")
        print("PIPELINE FINANCEIRO CONCLUÃƒÂDO")
        print("======================================")
        print("VALIDAÃƒâ€¡ÃƒÆ'O  : OK")
        print("CAIXA      : OK")
        print("LIVRO      : OK")
        print("======================================")

        return True


# ======================================================

if __name__ == "__main__":

    pipeline = FinancialPipeline()

    pipeline.process(

        payment_id="HML-000001",

        payer="PRESIDÃƒÅ NCIA IOTEC",

        amount=29.90

    )

