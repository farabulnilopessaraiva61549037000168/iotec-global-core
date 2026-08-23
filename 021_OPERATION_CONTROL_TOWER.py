# ==============================================================================
# IOTEC - OPERATION CONTROL TOWER
# VersÃ£o: 1.0
# ==============================================================================

from datetime import datetime
from dataclasses import dataclass, field
from typing import List
import uuid

# ==============================================================================
# EVENTO
# ==============================================================================

@dataclass
class Evento:

    id: str
    horario: str
    sala: str
    titulo: str
    descricao: str
    prioridade: str = "NORMAL"
    clicavel: bool = True
    origem: str = ""

# ==============================================================================
# TORRE
# ==============================================================================

class OperationControlTower:

    def __init__(self):

        self.eventos: List[Evento] = []

    def registrar(
            self,
            sala,
            titulo,
            descricao,
            prioridade="NORMAL",
            origem=""
    ):

        evento = Evento(

            id=str(uuid.uuid4())[:8],

            horario=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            sala=sala,

            titulo=titulo,

            descricao=descricao,

            prioridade=prioridade,

            origem=origem

        )

        self.eventos.append(evento)

        print(f"[{evento.horario}] {evento.sala} -> {evento.titulo}")

    def timeline(self):

        print("\n")
        print("=" * 70)
        print("IOTEC - TORRE DE OPERAÃ‡Ã•ES")
        print("=" * 70)

        for e in self.eventos:

            print(f"""
[{e.horario}]

Sala.............: {e.sala}

Evento...........: {e.titulo}

DescriÃ§Ã£o........: {e.descricao}

Prioridade.......: {e.prioridade}

Evento clicÃ¡vel..: {e.clicavel}

Origem...........: {e.origem}

ID...............: {e.id}

------------------------------------------------------------------
""")

# ==============================================================================
# EXEMPLO
# ==============================================================================

if __name__ == "__main__":

    torre = OperationControlTower()

    torre.registrar(

        sala="Comercial",

        titulo="Nova missÃ£o criada",

        descricao="Iniciar venda do RelatÃ³rio DiagnÃ³stico IOTEC.",

        origem="MISSAO-0001"

    )

    torre.registrar(

        sala="Financeira",

        titulo="Pagamento confirmado",

        descricao="Recebimento de R$ 29,90.",

        prioridade="ALTA",

        origem="PEDIDO-0001"

    )

    torre.registrar(

        sala="InteligÃªncia",

        titulo="Empresa encontrada",

        descricao="Nova oportunidade localizada no setor de engenharia.",

        origem="PESQUISA"

    )

    torre.timeline()

