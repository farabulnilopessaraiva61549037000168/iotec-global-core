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
ARQUIVO........: 007_COMMERCIAL_AGENT.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: COMMERCIAL AGENT
VERSÃƒÆ'O.........: 1.0.0

MISSÃƒÆ'O
-------------------------------------------------------------------------------
Gerenciar o ciclo comercial da IOTEC.

Responsabilidades

Ã¢â‚¬Â¢ Registrar Leads
Ã¢â‚¬Â¢ Registrar Oportunidades
Ã¢â‚¬Â¢ Gerenciar Pipeline
Ã¢â‚¬Â¢ Controlar Propostas
Ã¢â‚¬Â¢ Acompanhar NegociaÃƒÂ§ÃƒÂµes
Ã¢â‚¬Â¢ Gerar Indicadores Comerciais
===============================================================================
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import logging

LOGGER = logging.getLogger("COMMERCIAL_AGENT")


# =============================================================================
# STATUS
# =============================================================================

class OpportunityStatus(Enum):

    NEW = "NOVA"

    QUALIFIED = "QUALIFICADA"

    PROPOSAL = "PROPOSTA"

    NEGOTIATION = "NEGOCIAÃƒâ€¡ÃƒÆ'O"

    WON = "GANHA"

    LOST = "PERDIDA"


# =============================================================================
# LEAD
# =============================================================================

@dataclass
class Lead:

    company: str

    contact: str

    email: str

    phone: str

    segment: str

    estimated_value: float

    created_at: datetime

    status: OpportunityStatus


# =============================================================================
# COMMERCIAL AGENT
# =============================================================================

class CommercialAgent:

    def __init__(self):

        self.leads = []

        LOGGER.info("Commercial Agent iniciado.")

    # -------------------------------------------------------------------------

    def add_lead(

        self,

        company,

        contact,

        email,

        phone,

        segment,

        estimated_value

    ):

        lead = Lead(

            company=company,

            contact=contact,

            email=email,

            phone=phone,

            segment=segment,

            estimated_value=estimated_value,

            created_at=datetime.now(),

            status=OpportunityStatus.NEW

        )

        self.leads.append(lead)

        LOGGER.info(f"Lead registrado: {company}")

    # -------------------------------------------------------------------------

    def update_status(

        self,

        company,

        new_status

    ):

        for lead in self.leads:

            if lead.company == company:

                lead.status = new_status

                LOGGER.info(

                    f"{company} -> {new_status.value}"

                )

    # -------------------------------------------------------------------------

    def pipeline_value(self):

        return sum(

            lead.estimated_value

            for lead in self.leads

            if lead.status != OpportunityStatus.LOST

        )

    # -------------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 70)

        print("COMMERCIAL AGENT")

        print("=" * 70)

        print()

        print(f"Leads.............: {len(self.leads)}")

        print(f"Pipeline..........: R$ {self.pipeline_value():,.2f}")

        print()

        status_count = {}

        for lead in self.leads:

            status_count.setdefault(lead.status.value, 0)

            status_count[lead.status.value] += 1

        print("STATUS")

        print("-" * 70)

        for status, qty in status_count.items():

            print(f"{status:15} {qty}")

        print()

        print("LEADS")

        print("-" * 70)

        for lead in self.leads:

            print(f"Empresa.....: {lead.company}")

            print(f"Contato.....: {lead.contact}")

            print(f"Segmento....: {lead.segment}")

            print(f"Valor.......: R$ {lead.estimated_value:,.2f}")

            print(f"Status......: {lead.status.value}")

            print("-" * 70)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    commercial = CommercialAgent()

    commercial.add_lead(

        company="Prefeitura Municipal",

        contact="Departamento de Tecnologia",

        email="tecnologia@prefeitura.gov.br",

        phone="(00)0000-0000",

        segment="Governo",

        estimated_value=180000

    )

    commercial.add_lead(

        company="Empresa Alpha",

        contact="Diretor de OperaÃƒÂ§ÃƒÂµes",

        email="contato@empresa.com",

        phone="(00)0000-0000",

        segment="IndÃƒÂºstria",

        estimated_value=95000

    )

    commercial.update_status(

        "Empresa Alpha",

        OpportunityStatus.PROPOSAL

    )

    commercial.dashboard()



