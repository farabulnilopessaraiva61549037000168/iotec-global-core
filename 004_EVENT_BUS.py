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

ARQUIVO........: 004_EVENT_BUS.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: EVENT BUS
VERSÃƒÆ'O.........: 1.0.0

===============================================================================

Sistema de ComunicaÃƒÂ§ÃƒÂ£o Interna da Plataforma.

Responsabilidades

Ã¢â‚¬Â¢ Distribuir Eventos

Ã¢â‚¬Â¢ Registrar Eventos

Ã¢â‚¬Â¢ Encaminhar Eventos

Ã¢â‚¬Â¢ Publicar Eventos

Ã¢â‚¬Â¢ Inscrever Agentes

Ã¢â‚¬Â¢ Auditoria de Eventos

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Callable
import uuid
import logging

LOGGER = logging.getLogger("EVENT_BUS")


# ==============================================================================
# EVENTO
# ==============================================================================

@dataclass
class Event:

    id: str

    category: str

    source: str

    action: str

    payload: dict

    created_at: datetime


# ==============================================================================
# EVENT BUS
# ==============================================================================

class EventBus:

    def __init__(self):

        self.listeners = {}

        self.history = []

        LOGGER.info("Event Bus iniciado.")

    # -------------------------------------------------------------------------

    def subscribe(

        self,

        category: str,

        callback: Callable

    ):

        if category not in self.listeners:

            self.listeners[category] = []

        self.listeners[category].append(callback)

    # -------------------------------------------------------------------------

    def publish(

        self,

        category,

        source,

        action,

        payload=None

    ):

        if payload is None:

            payload = {}

        event = Event(

            id=str(uuid.uuid4()),

            category=category,

            source=source,

            action=action,

            payload=payload,

            created_at=datetime.now()

        )

        self.history.append(event)

        LOGGER.info(f"[{category}] {action}")

        if category in self.listeners:

            for callback in self.listeners[category]:

                callback(event)

    # -------------------------------------------------------------------------

    def statistics(self):

        return {

            "events": len(self.history),

            "listeners": len(self.listeners)

        }


# ==============================================================================
# TESTE
# ==============================================================================

def commercial_listener(event):

    print()

    print("COMMERCIAL AGENT")

    print(event.action)

    print(event.payload)


def finance_listener(event):

    print()

    print("FINANCIAL AGENT")

    print(event.action)

    print(event.payload)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    bus = EventBus()

    bus.subscribe(

        "COMMERCIAL",

        commercial_listener

    )

    bus.subscribe(

        "FINANCE",

        finance_listener

    )

    bus.publish(

        "COMMERCIAL",

        "MARKET_HUNTER",

        "Nova oportunidade encontrada.",

        {

            "cliente":"Prefeitura",

            "cidade":"Ibicuitinga",

            "valor_estimado":120000

        }

    )

    bus.publish(

        "FINANCE",

        "PAYMENT_GATEWAY",

        "Pagamento confirmado.",

        {

            "cliente":"Empresa X",

            "valor":2500

        }

    )

    print()

    print(bus.statistics())



