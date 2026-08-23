import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
==============================================================================
ARQUIVO........: 005_REVENUE_RADAR.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: REVENUE RADAR
VERSÃƒÆ'O.........: 1.0.0

MISSÃƒÆ'O
------------------------------------------------------------------------------
Monitorar continuamente a geraÃƒÂ§ÃƒÂ£o de receita da plataforma.

O Revenue Radar responde:

Ã¢â‚¬Â¢ Quanto entrou?
Ã¢â‚¬Â¢ Quanto vai entrar?
Ã¢â‚¬Â¢ Quem pagou?
Ã¢â‚¬Â¢ Qual produto foi vendido?
Ã¢â‚¬Â¢ Qual contrato originou a receita?
Ã¢â‚¬Â¢ Qual vendedor realizou a venda?
Ã¢â‚¬Â¢ Existe inadimplÃƒÂªncia?
Ã¢â‚¬Â¢ Qual receita ÃƒÂ© recorrente?

==============================================================================
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

import logging

LOGGER = logging.getLogger("REVENUE_RADAR")


# ============================================================================
# RECEITA
# ============================================================================

@dataclass
class RevenueRecord:

    client: str

    product: str

    contract: str

    amount: Decimal

    payment_method: str

    recurring: bool

    created_at: datetime


# ============================================================================
# REVENUE RADAR
# ============================================================================

class RevenueRadar:

    def __init__(self):

        self.records = []

        LOGGER.info("Revenue Radar iniciado.")

    # ------------------------------------------------------------------------

    def register_payment(

        self,

        client,

        product,

        contract,

        amount,

        payment_method="PIX",

        recurring=False

    ):

        revenue = RevenueRecord(

            client=client,

            product=product,

            contract=contract,

            amount=Decimal(str(amount)),

            payment_method=payment_method,

            recurring=recurring,

            created_at=datetime.now()

        )

        self.records.append(revenue)

    # ------------------------------------------------------------------------

    def total_revenue(self):

        return sum(r.amount for r in self.records)

    # ------------------------------------------------------------------------

    def recurring_revenue(self):

        return sum(

            r.amount

            for r in self.records

            if r.recurring

        )

    # ------------------------------------------------------------------------

    def report(self):

        print()

        print("=" * 70)

        print("REVENUE RADAR")

        print("=" * 70)

        print()

        print(f"Receitas registradas : {len(self.records)}")

        print(f"Receita Total........: R$ {self.total_revenue():,.2f}")

        print(f"Receita Recorrente..: R$ {self.recurring_revenue():,.2f}")

        print()

        print("=" * 70)

        print()

        for revenue in self.records:

            print(

                f"{revenue.client:25}"

                f"{revenue.product:25}"

                f"R$ {revenue.amount:,.2f}"

            )


# ============================================================================
# TESTE
# ============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    radar = RevenueRadar()

    radar.register_payment(

        client="Prefeitura Municipal",

        product="Enterprise Command Center",

        contract="CTR-2026-001",

        amount=18000,

        recurring=True

    )

    radar.register_payment(

        client="Empresa XYZ",

        product="Risk Intelligence",

        contract="CTR-2026-002",

        amount=8500,

        recurring=False

    )

    radar.report()



