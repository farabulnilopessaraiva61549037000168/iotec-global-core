# ==============================================================================
# IOTEC
# 022_OPERATION_EVENT_BUS.py
# Barramento Central de Eventos Operacionais
# ==============================================================================

from dataclasses import dataclass, asdict
from datetime import datetime
from collections import deque
import uuid


# ==============================================================================
# EVENTO
# ==============================================================================

@dataclass
class OperationEvent:

    id: str

    timestamp: str

    sala: str

    tipo: str

    titulo: str

    descricao: str

    prioridade: str

    origem: str

    status: str

    dados: dict


# ==============================================================================
# EVENT BUS
# ==============================================================================

class OperationEventBus:

    def __init__(self):

        self.eventos = deque(maxlen=5000)

    # -------------------------------------------------------------------------

    def emit(

        self,

        sala,

        tipo,

        titulo,

        descricao,

        prioridade="NORMAL",

        origem="",

        status="NOVO",

        dados=None

    ):

        if dados is None:
            dados = {}

        evento = OperationEvent(

            id=str(uuid.uuid4())[:8],

            timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            sala=sala,

            tipo=tipo,

            titulo=titulo,

            descricao=descricao,

            prioridade=prioridade,

            origem=origem,

            status=status,

            dados=dados

        )

        self.eventos.append(evento)

        print(
            f"[EVENT BUS] {evento.timestamp} | "
            f"{evento.sala} | "
            f"{evento.titulo}"
        )

        return evento

    # -------------------------------------------------------------------------

    def listar(self):

        return list(self.eventos)

    # -------------------------------------------------------------------------

    def por_sala(self, sala):

        return [

            e

            for e in self.eventos

            if e.sala == sala

        ]

    # -------------------------------------------------------------------------

    def por_tipo(self, tipo):

        return [

            e

            for e in self.eventos

            if e.tipo == tipo

        ]

    # -------------------------------------------------------------------------

    def localizar(self, event_id):

        for e in self.eventos:

            if e.id == event_id:

                return e

        return None

    # -------------------------------------------------------------------------

    def imprimir(self):

        print("\n")

        print("=" * 80)

        print("EVENT BUS")

        print("=" * 80)

        for e in self.eventos:

            print(f"""

ID..............: {e.id}

HorÃ¡rio.........: {e.timestamp}

Sala............: {e.sala}

Tipo............: {e.tipo}

Evento..........: {e.titulo}

DescriÃ§Ã£o.......: {e.descricao}

Status..........: {e.status}

Prioridade......: {e.prioridade}

Origem..........: {e.origem}

Dados...........: {e.dados}

------------------------------------------------------------

""")

# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    bus = OperationEventBus()

    bus.emit(

        sala="Financeira",

        tipo="PAGAMENTO",

        titulo="Pagamento confirmado",

        descricao="Recebimento do Pedido 0001",

        prioridade="ALTA",

        origem="PEDIDO-0001",

        dados={

            "cliente": "Bruno",

            "valor": 29.90,

            "produto": "RelatÃ³rio DiagnÃ³stico",

            "forma_pagamento": "PayPal"

        }

    )

    bus.emit(

        sala="Comercial",

        tipo="PROPOSTA",

        titulo="Nova proposta enviada",

        descricao="Proposta enviada ao Cliente",

        origem="CRM"

    )

    bus.imprimir()

