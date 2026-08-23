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
ARQUIVO........: 012_CONNECTOR_MANAGER.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: CONNECTOR MANAGER
VERSÃƒÆ'O.........: 1.0.0
STATUS.........: ENTERPRISE CORE

===============================================================================

CONNECTOR MANAGER

MissÃƒÂ£o
-------

Gerenciar todos os conectores da Plataforma IOTEC.

Este mÃƒÂ³dulo NÃƒÆ'O implementa APIs especÃƒÂ­ficas.

Ele controla todos os conectores.

Exemplos

Ã¢â‚¬Â¢ IBGE
Ã¢â‚¬Â¢ INMET
Ã¢â‚¬Â¢ ANA
Ã¢â‚¬Â¢ CEMADEN
Ã¢â‚¬Â¢ Portal da TransparÃƒÂªncia
Ã¢â‚¬Â¢ Compras PÃƒÂºblicas
Ã¢â‚¬Â¢ Receita Federal
Ã¢â‚¬Â¢ Banco Central
Ã¢â‚¬Â¢ Portal de Dados Abertos
Ã¢â‚¬Â¢ APIs internas
Ã¢â‚¬Â¢ CRM
Ã¢â‚¬Â¢ ERP
Ã¢â‚¬Â¢ Excel
Ã¢â‚¬Â¢ CSV
Ã¢â‚¬Â¢ Banco de Dados
Ã¢â‚¬Â¢ Data Lake

Toda comunicaÃƒÂ§ÃƒÂ£o externa passa por este mÃƒÂ³dulo.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict
import logging
import uuid

LOGGER = logging.getLogger("CONNECTOR_MANAGER")


# =============================================================================
# STATUS
# =============================================================================

class ConnectorStatus(Enum):

    OFFLINE = "OFFLINE"

    ONLINE = "ONLINE"

    ERROR = "ERROR"

    DISABLED = "DISABLED"


# =============================================================================
# CONNECTOR
# =============================================================================

@dataclass
class Connector:

    connector_id: str

    name: str

    category: str

    description: str

    version: str

    status: ConnectorStatus = ConnectorStatus.OFFLINE

    enabled: bool = True

    total_requests: int = 0

    last_execution: datetime | None = None

    metadata: Dict = field(default_factory=dict)


# =============================================================================
# CONNECTOR MANAGER
# =============================================================================

class ConnectorManager:

    def __init__(self):

        self.connectors: Dict[str, Connector] = {}

        LOGGER.info("Connector Manager iniciado.")

    # ----------------------------------------------------------------------

    def register(

        self,

        name,

        category,

        description,

        version="1.0"

    ):

        connector = Connector(

            connector_id=str(uuid.uuid4()),

            name=name,

            category=category,

            description=description,

            version=version

        )

        self.connectors[name] = connector

        LOGGER.info(f"Conector registrado -> {name}")

    # ----------------------------------------------------------------------

    def connect(self, name):

        connector = self.connectors.get(name)

        if connector:

            connector.status = ConnectorStatus.ONLINE

            connector.last_execution = datetime.now()

            LOGGER.info(f"{name} ONLINE")

    # ----------------------------------------------------------------------

    def disconnect(self, name):

        connector = self.connectors.get(name)

        if connector:

            connector.status = ConnectorStatus.OFFLINE

            LOGGER.info(f"{name} OFFLINE")

    # ----------------------------------------------------------------------

    def request(self, name):

        connector = self.connectors.get(name)

        if connector:

            connector.total_requests += 1

            connector.last_execution = datetime.now()

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 90)

        print("CONNECTOR MANAGER")

        print("=" * 90)

        print()

        print("Conectores Registrados:", len(self.connectors))

        print()

        for connector in self.connectors.values():

            print("-" * 90)

            print("Nome..............:", connector.name)

            print("Categoria.........:", connector.category)

            print("Status............:", connector.status.value)

            print("VersÃƒÂ£o............:", connector.version)

            print("RequisiÃƒÂ§ÃƒÂµes.......:", connector.total_requests)

            print("ÃƒÅ¡ltima ExecuÃƒÂ§ÃƒÂ£o...:", connector.last_execution)

            print()

# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    manager = ConnectorManager()

    manager.register(

        "IBGE",

        "Dados EstatÃƒÂ­sticos",

        "Instituto Brasileiro de Geografia e EstatÃƒÂ­stica"

    )

    manager.register(

        "INMET",

        "Meteorologia",

        "Instituto Nacional de Meteorologia"

    )

    manager.register(

        "ANA",

        "Recursos HÃƒÂ­dricos",

        "AgÃƒÂªncia Nacional de ÃƒÂguas"

    )

    manager.register(

        "CEMADEN",

        "Monitoramento",

        "Centro Nacional de Monitoramento"

    )

    manager.register(

        "PORTAL_TRANSPARENCIA",

        "TransparÃƒÂªncia",

        "Portal da TransparÃƒÂªncia"

    )

    manager.register(

        "COMPRAS_PUBLICAS",

        "LicitaÃƒÂ§ÃƒÂµes",

        "Portal de Compras PÃƒÂºblicas"

    )

    manager.connect("IBGE")

    manager.connect("INMET")

    manager.request("IBGE")

    manager.request("IBGE")

    manager.request("INMET")

    manager.dashboard()



