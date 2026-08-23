import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
ARQUIVO........: 009_FINANCIAL_CENTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: FINANCIAL CENTER
VERSÃƒÆ'O.........: 1.0.0

MISSÃƒÆ'O
-------------------------------------------------------------------------------

Centro Financeiro da Plataforma IOTEC

ResponsÃƒÂ¡vel por:

Ã¢â‚¬Â¢ Contas a Receber
Ã¢â‚¬Â¢ Contas a Pagar
Ã¢â‚¬Â¢ Fluxo de Caixa
Ã¢â‚¬Â¢ Livro Caixa
Ã¢â‚¬Â¢ Receita
Ã¢â‚¬Â¢ Despesa
Ã¢â‚¬Â¢ Indicadores Financeiros
Ã¢â‚¬Â¢ Auditoria Financeira

===============================================================================
"""

from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from enum import Enum
import uuid
import logging

LOGGER = logging.getLogger("FINANCIAL_CENTER")


# ============================================================================
# ENUM
# ============================================================================

class TransactionType(Enum):

    RECEITA = "RECEITA"

    DESPESA = "DESPESA"


class TransactionStatus(Enum):

    PENDENTE = "PENDENTE"

    PAGO = "PAGO"

    CANCELADO = "CANCELADO"


# ============================================================================
# TRANSAÃƒâ€¡ÃƒÆ'O
# ============================================================================

@dataclass

class FinancialTransaction:

    id: str

    description: str

    category: str

    client: str

    amount: Decimal

    transaction_type: TransactionType

    status: TransactionStatus

    created_at: datetime


# ============================================================================
# FINANCIAL CENTER
# ============================================================================

class FinancialCenter:

    def __init__(self):

        self.transactions = []

        LOGGER.info("Financial Center iniciado.")

    # ---------------------------------------------------------------------

    def add_income(

        self,

        description,

        category,

        client,

        amount

    ):

        self.transactions.append(

            FinancialTransaction(

                id=str(uuid.uuid4()),

                description=description,

                category=category,

                client=client,

                amount=Decimal(str(amount)),

                transaction_type=TransactionType.RECEITA,

                status=TransactionStatus.PAGO,

                created_at=datetime.now()

            )

        )

    # ---------------------------------------------------------------------

    def add_expense(

        self,

        description,

        category,

        amount

    ):

        self.transactions.append(

            FinancialTransaction(

                id=str(uuid.uuid4()),

                description=description,

                category=category,

                client="-",

                amount=Decimal(str(amount)),

                transaction_type=TransactionType.DESPESA,

                status=TransactionStatus.PAGO,

                created_at=datetime.now()

            )

        )

    # ---------------------------------------------------------------------

    def total_income(self):

        return sum(

            t.amount

            for t in self.transactions

            if t.transaction_type == TransactionType.RECEITA

        )

    # ---------------------------------------------------------------------

    def total_expense(self):

        return sum(

            t.amount

            for t in self.transactions

            if t.transaction_type == TransactionType.DESPESA

        )

    # ---------------------------------------------------------------------

    def balance(self):

        return self.total_income() - self.total_expense()

    # ---------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 70)

        print("FINANCIAL CENTER")

        print("=" * 70)

        print()

        print("Receitas.......: R$ {:,.2f}".format(self.total_income()))

        print("Despesas.......: R$ {:,.2f}".format(self.total_expense()))

        print("Saldo..........: R$ {:,.2f}".format(self.balance()))

        print()

        print("=" * 70)

        print()

        for t in self.transactions:

            print(f"[{t.transaction_type.value}]")

            print("DescriÃƒÂ§ÃƒÂ£o:", t.description)

            print("Categoria:", t.category)

            print("Cliente..:", t.client)

            print("Valor....: R$ {:,.2f}".format(t.amount))

            print("Status...:", t.status.value)

            print("-" * 70)


# ============================================================================
# TESTE
# ============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    finance = FinancialCenter()

    finance.add_income(

        description="Contrato Enterprise Command Center",

        category="Software",

        client="Prefeitura Municipal",

        amount=18500

    )

    finance.add_income(

        description="Mensalidade Risk Intelligence",

        category="Assinatura",

        client="Empresa Alpha",

        amount=6200

    )

    finance.add_expense(

        description="Servidor Cloud",

        category="Infraestrutura",

        amount=980

    )

    finance.add_expense(

        description="DomÃƒÂ­nio e Hospedagem",

        category="Operacional",

        amount=350

    )

    finance.dashboard()



