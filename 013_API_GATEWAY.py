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

ARQUIVO........: 013_API_GATEWAY.py
PROJETO........: IOTEC ENTERPRISE PLATFORM
MÃƒâ€œDULO.........: API GATEWAY
VERSÃƒÆ'O.........: 1.0.0
STATUS.........: ENTERPRISE

===============================================================================

API GATEWAY

MISSÃƒÆ'O

Centralizar toda comunicaÃƒÂ§ÃƒÂ£o da Plataforma IOTEC
com serviÃƒÂ§os internos e externos.

Nenhum mÃƒÂ³dulo deve acessar APIs diretamente.

Toda comunicaÃƒÂ§ÃƒÂ£o passa pelo Gateway.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, Any
import uuid
import logging

LOGGER = logging.getLogger("API_GATEWAY")


# ==============================================================================
# STATUS
# ==============================================================================

class GatewayStatus(Enum):

    ONLINE = "ONLINE"

    OFFLINE = "OFFLINE"

    ERROR = "ERROR"


# ==============================================================================
# REQUEST
# ==============================================================================

@dataclass

class APIRequest:

    request_id: str

    connector: str

    endpoint: str

    method: str

    payload: Dict[str, Any]

    created_at: datetime


# ==============================================================================
# RESPONSE
# ==============================================================================

@dataclass

class APIResponse:

    request_id: str

    success: bool

    status_code: int

    message: str

    data: Dict[str, Any] = field(default_factory=dict)


# ==============================================================================
# API GATEWAY
# ==============================================================================

class APIGateway:

    def __init__(self):

        self.status = GatewayStatus.ONLINE

        self.requests = []

        self.responses = []

        self.statistics = {

            "total_requests": 0,

            "success": 0,

            "errors": 0

        }

        LOGGER.info("API Gateway iniciado.")

    # -------------------------------------------------------------------------

    def execute(

        self,

        connector,

        endpoint,

        method="GET",

        payload=None

    ):

        if payload is None:

            payload = {}

        request = APIRequest(

            request_id=str(uuid.uuid4()),

            connector=connector,

            endpoint=endpoint,

            method=method,

            payload=payload,

            created_at=datetime.now()

        )

        self.requests.append(request)

        self.statistics["total_requests"] += 1

        response = APIResponse(

            request_id=request.request_id,

            success=True,

            status_code=200,

            message="RequisiÃƒÂ§ÃƒÂ£o registrada.",

            data={}

        )

        self.responses.append(response)

        self.statistics["success"] += 1

        LOGGER.info(

            f"[{connector}] {method} {endpoint}"

        )

        return response

    # -------------------------------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 80)

        print("API GATEWAY")

        print("=" * 80)

        print()

        print("STATUS..............:", self.status.value)

        print("REQUISIÃƒâ€¡Ãƒâ€¢ES.........:", self.statistics["total_requests"])

        print("SUCESSOS............:", self.statistics["success"])

        print("ERROS...............:", self.statistics["errors"])

        print()

        print("=" * 80)

        print()

        for request in self.requests:

            print("Connector :", request.connector)

            print("Endpoint..:", request.endpoint)

            print("MÃƒÂ©todo....:", request.method)

            print("Data.......:", request.created_at)

            print("-" * 80)


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    gateway = APIGateway()

    gateway.execute(

        connector="IBGE",

        endpoint="/municipios"

    )

    gateway.execute(

        connector="INMET",

        endpoint="/previsao"

    )

    gateway.execute(

        connector="PORTAL_TRANSPARENCIA",

        endpoint="/licitacoes"

    )

    gateway.dashboard()



