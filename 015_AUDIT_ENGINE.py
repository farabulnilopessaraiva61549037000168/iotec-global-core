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
ARQUIVO........: 015_AUDIT_ENGINE.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: AUDIT ENGINE
VERSÃƒÆ'O.........: 1.0.0
STATUS.........: ENTERPRISE CORE

===============================================================================

AUDIT ENGINE

MISSÃƒÆ'O

Registrar todos os eventos relevantes da plataforma.

Responsabilidades

Ã¢â‚¬Â¢ Auditoria do Sistema
Ã¢â‚¬Â¢ Auditoria Comercial
Ã¢â‚¬Â¢ Auditoria Financeira
Ã¢â‚¬Â¢ Auditoria de SeguranÃƒÂ§a
Ã¢â‚¬Â¢ Auditoria de Contratos
Ã¢â‚¬Â¢ Auditoria de APIs
Ã¢â‚¬Â¢ Auditoria de Conectores
Ã¢â‚¬Â¢ Rastreabilidade das OperaÃƒÂ§ÃƒÂµes

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import logging
import uuid

LOGGER = logging.getLogger("AUDIT_ENGINE")


# ==============================================================================
# NÃƒÂVEL
# ==============================================================================

class AuditLevel(Enum):

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"


# ==============================================================================
# EVENTO
# ==============================================================================

@dataclass
class AuditEvent:

    event_id: str

    module: str

    action: str

    user: str

    level: AuditLevel

    description: str

    timestamp: datetime = field(default_factory=datetime.now)


# ==============================================================================
# AUDIT ENGINE
# ==============================================================================

class AuditEngine:

    def __init__(self):

        self.events = []

        LOGGER.info("Audit Engine iniciado.")

    # ----------------------------------------------------------------------

    def register(

        self,

        module,

        action,

        user,

        level,

        description

    ):

        event = AuditEvent(

            event_id=str(uuid.uuid4()),

            module=module,

            action=action,

            user=user,

            level=level,

            description=description

        )

        self.events.append(event)

        LOGGER.info(f"[{module}] {action}")

    # ----------------------------------------------------------------------

    def total_events(self):

        return len(self.events)

    # ----------------------------------------------------------------------

    def count_by_level(self):

        result = {}

        for level in AuditLevel:

            result[level.value] = 0

        for event in self.events:

            result[event.level.value] += 1

        return result

    # ----------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 90)

        print("AUDIT ENGINE")

        print("=" * 90)

        print()

        print("Eventos Registrados:", self.total_events())

        print()

        print("POR NÃƒÂVEL")

        print("-" * 90)

        for level, total in self.count_by_level().items():

            print(f"{level:10} : {total}")

        print()

        print("=" * 90)

        print()

        for event in self.events:

            print(f"ID...........: {event.event_id}")

            print(f"MÃƒÂ³dulo.......: {event.module}")

            print(f"AÃƒÂ§ÃƒÂ£o.........: {event.action}")

            print(f"UsuÃƒÂ¡rio......: {event.user}")

            print(f"NÃƒÂ­vel........: {event.level.value}")

            print(f"DescriÃƒÂ§ÃƒÂ£o....: {event.description}")

            print(f"Data.........: {event.timestamp}")

            print("-" * 90)


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    audit = AuditEngine()

    audit.register(

        module="COMMERCIAL_AGENT",

        action="Nova oportunidade registrada",

        user="admin",

        level=AuditLevel.INFO,

        description="Lead incluÃƒÂ­do no pipeline comercial."

    )

    audit.register(

        module="FINANCIAL_CENTER",

        action="Pagamento confirmado",

        user="system",

        level=AuditLevel.INFO,

        description="Receita registrada no livro-caixa."

    )

    audit.register(

        module="SECURITY_CENTER",

        action="Tentativa de login invÃƒÂ¡lida",

        user="desconhecido",

        level=AuditLevel.WARNING,

        description="Credenciais invÃƒÂ¡lidas."

    )

    audit.dashboard()



