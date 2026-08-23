# ==============================================================================
# IOTEC - WATCH TOWER
# Torre Central de VigilÃ¢ncia
# VersÃ£o: 1.0
# ==============================================================================

from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
import uuid


# ==============================================================================
# STATUS
# ==============================================================================

class StatusMissao(Enum):
    CRIADA = "CRIADA"
    EXECUTANDO = "EXECUTANDO"
    PAUSADA = "PAUSADA"
    CONCLUIDA = "CONCLUIDA"
    CONTIDA = "CONTIDA"


# ==============================================================================
# EVENTOS
# ==============================================================================

@dataclass
class Evento:

    horario: str
    agente: str
    tipo: str
    descricao: str


# ==============================================================================
# MISSÃƒO
# ==============================================================================

@dataclass
class Missao:

    id: str
    titulo: str
    agente: str

    status: StatusMissao = StatusMissao.CRIADA

    eventos: list = field(default_factory=list)


# ==============================================================================
# TORRE
# ==============================================================================

class WatchTower:

    def __init__(self):

        self.missoes = {}
        self.log_global = []

    # --------------------------------------------------------

    def criar_missao(self, titulo, agente):

        codigo = str(uuid.uuid4())[:8]

        m = Missao(
            id=codigo,
            titulo=titulo,
            agente=agente
        )

        self.missoes[codigo] = m

        self.registrar(
            agente,
            "MISSAO",
            f"MissÃ£o criada -> {titulo}"
        )

        return codigo

    # --------------------------------------------------------

    def registrar(self, agente, tipo, descricao):

        evento = Evento(

            horario=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            agente=agente,

            tipo=tipo,

            descricao=descricao

        )

        self.log_global.append(evento)

    # --------------------------------------------------------

    def iniciar(self, codigo):

        self.missoes[codigo].status = StatusMissao.EXECUTANDO

        self.registrar(

            self.missoes[codigo].agente,

            "STATUS",

            "MissÃ£o iniciada"

        )

    # --------------------------------------------------------

    def pausar(self, codigo):

        self.missoes[codigo].status = StatusMissao.PAUSADA

        self.registrar(

            self.missoes[codigo].agente,

            "STATUS",

            "MissÃ£o pausada"

        )

    # --------------------------------------------------------

    def conter(self, codigo, motivo):

        self.missoes[codigo].status = StatusMissao.CONTIDA

        self.registrar(

            self.missoes[codigo].agente,

            "CONTENCAO",

            motivo

        )

    # --------------------------------------------------------

    def concluir(self, codigo):

        self.missoes[codigo].status = StatusMissao.CONCLUIDA

        self.registrar(

            self.missoes[codigo].agente,

            "STATUS",

            "MissÃ£o concluÃ­da"

        )

    # --------------------------------------------------------

    def listar(self):

        print("\n========== MISSÃ•ES ==========\n")

        for m in self.missoes.values():

            print(

                m.id,

                m.agente,

                m.status.value,

                m.titulo

            )

    # --------------------------------------------------------

    def auditoria(self):

        print("\n========== LOG GLOBAL ==========\n")

        for e in self.log_global:

            print(

                e.horario,

                "|",

                e.agente,

                "|",

                e.tipo,

                "|",

                e.descricao

            )


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    torre = WatchTower()

    codigo = torre.criar_missao(

        "Prospectar empresa de engenharia",

        "AGENTE_COMERCIAL"

    )

    torre.iniciar(codigo)

    torre.registrar(

        "AGENTE_COMERCIAL",

        "INFO",

        "Cliente localizado"

    )

    torre.registrar(

        "AGENTE_COMERCIAL",

        "INFO",

        "Proposta enviada"

    )

    torre.conter(

        codigo,

        "Tentativa de acessar recurso nÃ£o autorizado"

    )

    torre.listar()

    torre.auditoria()

