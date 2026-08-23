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
ARQUIVO........: 011_CRM_CENTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: CRM CENTER
VERSÃƒÆ'O.........: 1.0.0
STATUS.........: ENTERPRISE

===============================================================================

CRM CENTER

MissÃƒÂ£o

Gerenciar todo o relacionamento da IOTEC
com clientes, prospects, parceiros e contratos.

O CRM representa a memÃƒÂ³ria comercial da empresa.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from decimal import Decimal
from typing import List
import uuid
import logging

LOGGER = logging.getLogger("CRM_CENTER")


# =============================================================================
# STATUS
# =============================================================================

class CustomerStatus(Enum):

    LEAD = "LEAD"

    PROSPECT = "PROSPECT"

    CLIENT = "CLIENTE"

    VIP = "VIP"

    PARTNER = "PARCEIRO"

    INACTIVE = "INATIVO"


# =============================================================================
# CUSTOMER
# =============================================================================

@dataclass

class Customer:

    customer_id: str

    company: str

    contact: str

    email: str

    phone: str

    city: str

    state: str

    segment: str

    status: CustomerStatus

    total_contracts: int = 0

    total_revenue: Decimal = Decimal("0")

    notes: List[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)


# =============================================================================
# CRM CENTER
# =============================================================================

class CRMCenter:

    def __init__(self):

        self.customers = []

        LOGGER.info("CRM Center iniciado.")

    # ----------------------------------------------------------------------

    def add_customer(

        self,

        company,

        contact,

        email,

        phone,

        city,

        state,

        segment,

        status=CustomerStatus.LEAD

    ):

        customer = Customer(

            customer_id=str(uuid.uuid4()),

            company=company,

            contact=contact,

            email=email,

            phone=phone,

            city=city,

            state=state,

            segment=segment,

            status=status

        )

        self.customers.append(customer)

        LOGGER.info(f"Cliente registrado -> {company}")

        return customer

    # ----------------------------------------------------------------------

    def register_contract(

        self,

        company,

        value

    ):

        for customer in self.customers:

            if customer.company == company:

                customer.total_contracts += 1

                customer.total_revenue += Decimal(str(value))

                customer.status = CustomerStatus.CLIENT

    # ----------------------------------------------------------------------

    def add_note(

        self,

        company,

        text

    ):

        for customer in self.customers:

            if customer.company == company:

                customer.notes.append(text)

    # ----------------------------------------------------------------------

    def total_clients(self):

        return len(

            [

                c

                for c in self.customers

                if c.status == CustomerStatus.CLIENT

            ]

        )

    # ----------------------------------------------------------------------

    def total_leads(self):

        return len(

            [

                c

                for c in self.customers

                if c.status == CustomerStatus.LEAD

            ]

        )

    # ----------------------------------------------------------------------

    def total_revenue(self):

        total = Decimal("0")

        for c in self.customers:

            total += c.total_revenue

        return total

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 80)

        print("CRM CENTER")

        print("=" * 80)

        print()

        print("Cadastros........:", len(self.customers))

        print("Clientes.........:", self.total_clients())

        print("Leads............:", self.total_leads())

        print("Receita..........: R$ {:,.2f}".format(

            self.total_revenue()

        ))

        print()

        print("=" * 80)

        print()

        for customer in self.customers:

            print("Empresa.........:", customer.company)

            print("Contato.........:", customer.contact)

            print("Cidade..........:", customer.city)

            print("Estado..........:", customer.state)

            print("Segmento........:", customer.segment)

            print("Status..........:", customer.status.value)

            print("Contratos.......:", customer.total_contracts)

            print("Receita.........: R$ {:,.2f}".format(

                customer.total_revenue

            ))

            print("-" * 80)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    crm = CRMCenter()

    crm.add_customer(

        company="Prefeitura Municipal",

        contact="SecretÃƒÂ¡rio de Tecnologia",

        email="tecnologia@prefeitura.gov.br",

        phone="(88)99999-9999",

        city="Ibicuitinga",

        state="CE",

        segment="Governo"

    )

    crm.register_contract(

        "Prefeitura Municipal",

        18500

    )

    crm.add_note(

        "Prefeitura Municipal",

        "Interesse em Central de Comando Empresarial."

    )

    crm.dashboard()



