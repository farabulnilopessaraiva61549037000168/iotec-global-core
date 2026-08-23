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
ARQUIVO........: 002_X27_CORE.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: X27 CORE
VERSÃƒÆ'O.........: 1.0.0

DESCRIÃƒâ€¡ÃƒÆ'O
------------------------------------------------------------------------------
Motor Central da Plataforma IOTEC.

Responsabilidades:

Ã¢â‚¬Â¢ Gerenciar o estado do nÃƒÂºcleo
Ã¢â‚¬Â¢ Registrar eventos internos
Ã¢â‚¬Â¢ Controlar agentes
Ã¢â‚¬Â¢ Registrar capacidades
Ã¢â‚¬Â¢ Disponibilizar serviÃƒÂ§os aos mÃƒÂ³dulos
==============================================================================

"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Any
import logging
import uuid

LOGGER = logging.getLogger("X27")


# ==============================================================================
# EVENTO
# ==============================================================================

@dataclass
class Event:

    id: str
    category: str
    source: str
    message: str
    timestamp: datetime


# ==============================================================================
# AGENTE
# ==============================================================================

@dataclass
class CoreAgent:

    name: str
    description: str
    status: str = "OFFLINE"
    heartbeat: datetime | None = None


# ==============================================================================
# X27 CORE
# ==============================================================================

class X27Core:

    def __init__(self):

        self.started_at = datetime.now()

        self.status = "INITIALIZING"

        self.events: List[Event] = []

        self.capabilities: Dict[str, str] = {}

        self.agents: Dict[str, CoreAgent] = {}

        LOGGER.info("X27 Core criado.")

    # ----------------------------------------------------------------------

    def boot(self):

        self.status = "ONLINE"

        LOGGER.info("X27 ONLINE")

    # ----------------------------------------------------------------------

    def register_capability(self, name: str, description: str):

        self.capabilities[name] = description

        LOGGER.info(f"Capacidade registrada -> {name}")

    # ----------------------------------------------------------------------

    def register_agent(self, name: str, description: str):

        self.agents[name] = CoreAgent(

            name=name,

            description=description,

            status="ONLINE",

            heartbeat=datetime.now()

        )

        LOGGER.info(f"Agente registrado -> {name}")

    # ----------------------------------------------------------------------

    def emit_event(

        self,

        category: str,

        source: str,

        message: str

    ):

        event = Event(

            id=str(uuid.uuid4()),

            category=category,

            source=source,

            message=message,

            timestamp=datetime.now()

        )

        self.events.append(event)

        LOGGER.info(f"[{category}] {message}")

    # ----------------------------------------------------------------------

    def heartbeat(self):

        for agent in self.agents.values():

            agent.heartbeat = datetime.now()

    # ----------------------------------------------------------------------

    def diagnostics(self):

        return {

            "status": self.status,

            "started_at": self.started_at,

            "agents": len(self.agents),

            "capabilities": len(self.capabilities),

            "events": len(self.events)

        }

    # ----------------------------------------------------------------------

    def show_status(self):

        print()

        print("=" * 60)

        print("X27 CORE STATUS")

        print("=" * 60)

        print()

        print("STATUS:", self.status)

        print("AGENTES:", len(self.agents))

        print("CAPACIDADES:", len(self.capabilities))

        print("EVENTOS:", len(self.events))

        print()

        print("=" * 60)


# ==============================================================================
# TESTE LOCAL
# ==============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    core = X27Core()

    core.boot()

    core.register_capability(

        "ENTERPRISE_COMMAND_CENTER",

        "Central de Comando Empresarial"

    )

    core.register_capability(

        "REVENUE_RADAR",

        "Monitoramento de Receita"

    )

    core.register_capability(

        "BUDGET_HUNTER",

        "DetecÃƒÂ§ÃƒÂ£o de Oportunidades"

    )

    core.register_agent(

        "COMMERCIAL_AGENT",

        "ResponsÃƒÂ¡vel pelo Comercial"

    )

    core.register_agent(

        "FINANCIAL_AGENT",

        "ResponsÃƒÂ¡vel pelo Financeiro"

    )

    core.emit_event(

        "SYSTEM",

        "X27",

        "InicializaÃƒÂ§ÃƒÂ£o concluÃƒÂ­da."

    )

    core.show_status()



