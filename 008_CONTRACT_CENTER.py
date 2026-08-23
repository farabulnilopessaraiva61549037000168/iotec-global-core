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
ARQUIVO........: 008_CONTRACT_CENTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: CONTRACT CENTER
VERSÃƒÆ'O.........: 1.0.0
STATUS.........: ENTERPRISE

===============================================================================

CONTRACT CENTER

MissÃƒÂ£o

Gerenciar todo o ciclo de vida dos contratos.

Responsabilidades

Ã¢â‚¬Â¢ Cadastro de Contratos
Ã¢â‚¬Â¢ GestÃƒÂ£o de Clientes
Ã¢â‚¬Â¢ VigÃƒÂªncia
Ã¢â‚¬Â¢ RenovaÃƒÂ§ÃƒÂ£o
Ã¢â‚¬Â¢ SLA
Ã¢â‚¬Â¢ Receita Esperada
Ã¢â‚¬Â¢ Auditoria
Ã¢â‚¬Â¢ HistÃƒÂ³rico

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal
from enum import Enum
from typing import List
import uuid
import logging

LOGGER = logging.getLogger("CONTRACT_CENTER")


# =============================================================================
# STATUS
# =============================================================================

class ContractStatus(Enum):

    DRAFT = "RASCUNHO"

    NEGOTIATION = "NEGOCIAÃƒâ€¡ÃƒÆ'O"

    ACTIVE = "ATIVO"

    SUSPENDED = "SUSPENSO"

    FINISHED = "ENCERRADO"

    CANCELLED = "CANCELADO"


# =============================================================================
# CONTRATO
# =============================================================================

@dataclass
class Contract:

    contract_id: str

    client: str

    product: str

    manager: str

    monthly_value: Decimal

    implementation_value: Decimal

    start_date: datetime

    end_date: datetime

    status: ContractStatus

    sla_hours: int = 24

    notes: List[str] = field(default_factory=list)


# =============================================================================
# CONTRACT CENTER
# =============================================================================

class ContractCenter:

    def __init__(self):

        self.contracts: List[Contract] = []

        LOGGER.info("Contract Center iniciado.")

    # ----------------------------------------------------------------------

    def create_contract(

        self,

        client,

        product,

        manager,

        monthly_value,

        implementation_value,

        months=12,

        sla_hours=24

    ):

        start = datetime.now()

        end = start + timedelta(days=30 * months)

        contract = Contract(

            contract_id=str(uuid.uuid4()),

            client=client,

            product=product,

            manager=manager,

            monthly_value=Decimal(str(monthly_value)),

            implementation_value=Decimal(str(implementation_value)),

            start_date=start,

            end_date=end,

            status=ContractStatus.ACTIVE,

            sla_hours=sla_hours

        )

        self.contracts.append(contract)

        LOGGER.info(f"Contrato criado -> {client}")

        return contract

    # ----------------------------------------------------------------------

    def monthly_recurring_revenue(self):

        total = Decimal("0")

        for contract in self.contracts:

            if contract.status == ContractStatus.ACTIVE:

                total += contract.monthly_value

        return total

    # ----------------------------------------------------------------------

    def implementation_revenue(self):

        total = Decimal("0")

        for contract in self.contracts:

            if contract.status == ContractStatus.ACTIVE:

                total += contract.implementation_value

        return total

    # ----------------------------------------------------------------------

    def contracts_expiring(self, days=30):

        limit = datetime.now() + timedelta(days=days)

        return [

            c

            for c in self.contracts

            if c.end_date <= limit

            and c.status == ContractStatus.ACTIVE

        ]

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 75)

        print("CONTRACT CENTER")

        print("=" * 75)

        print()

        print("Contratos Ativos.......:",

              len(

                  [

                      c

                      for c in self.contracts

                      if c.status == ContractStatus.ACTIVE

                  ]

              )

        )

        print()

        print("MRR....................: R$ {:,.2f}".format(

            self.monthly_recurring_revenue()

        ))

        print()

        print("ImplantaÃƒÂ§ÃƒÂµes...........: R$ {:,.2f}".format(

            self.implementation_revenue()

        ))

        print()

        print("PrÃƒÂ³ximos Vencimentos...:",

              len(self.contracts_expiring())

        )

        print()

        print("=" * 75)

        print()

        for contract in self.contracts:

            print("Cliente........:", contract.client)

            print("Produto........:", contract.product)

            print("Gestor.........:", contract.manager)

            print("Mensalidade....: R$ {:,.2f}".format(

                contract.monthly_value

            ))

            print("ImplantaÃƒÂ§ÃƒÂ£o....: R$ {:,.2f}".format(

                contract.implementation_value

            ))

            print("InÃƒÂ­cio.........:",

                  contract.start_date.strftime("%d/%m/%Y"))

            print("Fim............:",

                  contract.end_date.strftime("%d/%m/%Y"))

            print("SLA............:",

                  contract.sla_hours,

                  "horas")

            print("Status.........:",

                  contract.status.value)

            print("-" * 75)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    center = ContractCenter()

    center.create_contract(

        client="Prefeitura Municipal",

        product="Enterprise Command Center",

        manager="Diretor de Tecnologia",

        monthly_value=18500,

        implementation_value=65000,

        months=24

    )

    center.create_contract(

        client="Empresa Alpha",

        product="Risk Intelligence",

        manager="Diretor de OperaÃƒÂ§ÃƒÂµes",

        monthly_value=6200,

        implementation_value=18000,

        months=12

    )

    center.dashboard()



