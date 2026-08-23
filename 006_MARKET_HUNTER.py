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

ARQUIVO........: 006_MARKET_HUNTER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: MARKET HUNTER
VERSÃƒÆ'O.........: 1.0.0

===============================================================================

MARKET HUNTER

MissÃƒÂ£o

Identificar oportunidades comerciais.

O mÃƒÂ³dulo organiza oportunidades detectadas em
fontes de mercado, licitaÃƒÂ§ÃƒÂµes, editais,
consultas pÃƒÂºblicas e outras informaÃƒÂ§ÃƒÂµes
disponibilizadas oficialmente.

NÃƒÆ'O realiza contatos automÃƒÂ¡ticos.

Seu papel ÃƒÂ© gerar inteligÃƒÂªncia comercial
para a equipe da IOTEC.

===============================================================================
"""

from dataclasses import dataclass
from datetime import datetime
import logging

LOGGER = logging.getLogger("MARKET_HUNTER")

# ============================================================================
# OPORTUNIDADE
# ============================================================================

@dataclass
class Opportunity:

    title: str

    organization: str

    segment: str

    estimated_value: float

    source: str

    created_at: datetime

    priority: int = 0

# ============================================================================
# MARKET HUNTER
# ============================================================================

class MarketHunter:

    def __init__(self):

        self.opportunities = []

        LOGGER.info("Market Hunter iniciado.")

    # ----------------------------------------------------------------------

    def register_opportunity(

        self,

        title,

        organization,

        segment,

        estimated_value,

        source,

        priority=5

    ):

        opportunity = Opportunity(

            title=title,

            organization=organization,

            segment=segment,

            estimated_value=estimated_value,

            source=source,

            created_at=datetime.now(),

            priority=priority

        )

        self.opportunities.append(opportunity)

        LOGGER.info(f"Oportunidade registrada: {title}")

    # ----------------------------------------------------------------------

    def total_pipeline(self):

        return sum(o.estimated_value for o in self.opportunities)

    # ----------------------------------------------------------------------

    def show_pipeline(self):

        print()

        print("=" * 70)

        print("MARKET HUNTER")

        print("=" * 70)

        print()

        print(f"Oportunidades : {len(self.opportunities)}")

        print(f"Pipeline Total: R$ {self.total_pipeline():,.2f}")

        print()

        for o in sorted(
            self.opportunities,
            key=lambda item: (-item.priority, -item.estimated_value)
        ):

            print("-" * 70)

            print("TÃƒÂ­tulo.......:", o.title)

            print("OrganizaÃƒÂ§ÃƒÂ£o..:", o.organization)

            print("Segmento.....:", o.segment)

            print("Valor Est....: R$ {:,.2f}".format(o.estimated_value))

            print("Fonte........:", o.source)

            print("Prioridade...:", o.priority)

# ============================================================================
# TESTE
# ============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    hunter = MarketHunter()

    hunter.register_opportunity(

        title="Central de Comando Empresarial",

        organization="Prefeitura Municipal",

        segment="Defesa Civil",

        estimated_value=180000,

        source="Portal de Compras",

        priority=10

    )

    hunter.register_opportunity(

        title="Painel de InteligÃƒÂªncia ClimÃƒÂ¡tica",

        organization="Companhia de Energia",

        segment="Energia",

        estimated_value=95000,

        source="Consulta Comercial",

        priority=8

    )

    hunter.show_pipeline()



