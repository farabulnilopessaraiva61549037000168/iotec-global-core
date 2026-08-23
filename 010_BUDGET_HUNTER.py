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

ARQUIVO........: 010_BUDGET_HUNTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: BUDGET HUNTER
VERSÃƒÆ'O.........: 1.0.0

===============================================================================

BUDGET HUNTER

MISSÃƒÆ'O

Organizar informaÃƒÂ§ÃƒÂµes sobre oportunidades
com potencial comercial para a IOTEC.

Responsabilidades

Ã¢â‚¬Â¢ Registrar oportunidades
Ã¢â‚¬Â¢ Classificar prioridade
Ã¢â‚¬Â¢ Estimar potencial financeiro
Ã¢â‚¬Â¢ Organizar pipeline
Ã¢â‚¬Â¢ Gerar ranking comercial
Ã¢â‚¬Â¢ Apoiar equipe de vendas

===============================================================================
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
import logging

LOGGER = logging.getLogger("BUDGET_HUNTER")


# ============================================================================
# PRIORIDADE
# ============================================================================

class Priority(Enum):

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


# ============================================================================
# OPORTUNIDADE
# ============================================================================

@dataclass
class BudgetOpportunity:

    organization: str

    segment: str

    source: str

    estimated_budget: Decimal

    priority: Priority

    opportunity_score: int

    observation: str

    created_at: datetime


# ============================================================================
# BUDGET HUNTER
# ============================================================================

class BudgetHunter:

    def __init__(self):

        self.opportunities = []

        LOGGER.info("Budget Hunter iniciado.")

    # ---------------------------------------------------------------------

    def register(

        self,

        organization,

        segment,

        source,

        estimated_budget,

        priority,

        score,

        observation=""

    ):

        self.opportunities.append(

            BudgetOpportunity(

                organization=organization,

                segment=segment,

                source=source,

                estimated_budget=Decimal(str(estimated_budget)),

                priority=priority,

                opportunity_score=score,

                observation=observation,

                created_at=datetime.now()

            )

        )

    # ---------------------------------------------------------------------

    def total_pipeline(self):

        return sum(

            item.estimated_budget

            for item in self.opportunities

        )

    # ---------------------------------------------------------------------

    def top_opportunities(self):

        return sorted(

            self.opportunities,

            key=lambda item: (

                item.opportunity_score,

                item.estimated_budget

            ),

            reverse=True

        )

    # ---------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 75)

        print("BUDGET HUNTER")

        print("=" * 75)

        print()

        print("Oportunidades.....:", len(self.opportunities))

        print("Pipeline Estimado.: R$ {:,.2f}".format(

            self.total_pipeline()

        ))

        print()

        print("=" * 75)

        print()

        for item in self.top_opportunities():

            print("OrganizaÃƒÂ§ÃƒÂ£o :", item.organization)

            print("Segmento....:", item.segment)

            print("Origem......:", item.source)

            print("Valor.......: R$ {:,.2f}".format(

                item.estimated_budget

            ))

            print("Prioridade..:", item.priority.name)

            print("Score.......:", item.opportunity_score)

            print("ObservaÃƒÂ§ÃƒÂ£o..:", item.observation)

            print("-" * 75)


# ============================================================================
# TESTE
# ============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    hunter = BudgetHunter()

    hunter.register(

        organization="Prefeitura Municipal",

        segment="Defesa Civil",

        source="Planejamento OrÃƒÂ§amentÃƒÂ¡rio",

        estimated_budget=250000,

        priority=Priority.CRITICAL,

        score=98,

        observation="Alta aderÃƒÂªncia ao Enterprise Command Center."

    )

    hunter.register(

        organization="Empresa Alpha",

        segment="Energia",

        source="Consulta Comercial",

        estimated_budget=95000,

        priority=Priority.HIGH,

        score=87,

        observation="Projeto de monitoramento operacional."

    )

    hunter.dashboard()



