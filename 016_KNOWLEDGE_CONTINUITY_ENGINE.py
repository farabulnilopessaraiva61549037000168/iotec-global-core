# ==============================================================================
# 016_KNOWLEDGE_CONTINUITY_ENGINE.py
# IOTEC - KNOWLEDGE CONTINUITY ENGINE
# Nunca esquecer uma investigaÃ§Ã£o
# ==============================================================================

import json
import uuid
from pathlib import Path
from dataclasses import dataclass, asdict, field
from datetime import datetime


DATABASE = Path("database/knowledge")
DATABASE.mkdir(parents=True, exist_ok=True)

ARQUIVO = DATABASE / "investigations.json"


# ==============================================================================
# MODELO
# ==============================================================================

@dataclass
class Investigation:

    id: str

    titulo: str

    descricao: str

    categoria: str

    prioridade: str

    status: str

    criado_em: str

    atualizado_em: str

    progresso: int = 0

    checkpoint: str = ""

    resultado: str = ""

    arquivos: list = field(default_factory=list)

    observacoes: list = field(default_factory=list)


# ==============================================================================
# ENGINE
# ==============================================================================

class KnowledgeContinuityEngine:

    def __init__(self):

        self.investigations = {}

        self.carregar()

        print("\nKNOWLEDGE CONTINUITY ENGINE ONLINE\n")


    # --------------------------------------------------------------------------

    def agora(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    # --------------------------------------------------------------------------

    def salvar(self):

        dados = {
            k: asdict(v)
            for k, v in self.investigations.items()
        }

        with open(ARQUIVO, "w", encoding="utf-8") as f:

            json.dump(
                dados,
                f,
                indent=4,
                ensure_ascii=False
            )


    # --------------------------------------------------------------------------

    def carregar(self):

        if not ARQUIVO.exists():

            return

        with open(ARQUIVO, "r", encoding="utf-8") as f:

            dados = json.load(f)

        for k, v in dados.items():

            self.investigations[k] = Investigation(**v)


    # --------------------------------------------------------------------------

    def nova_investigacao(
        self,
        titulo,
        descricao,
        categoria,
        prioridade="MEDIA"
    ):

        uid = uuid.uuid4().hex[:8].upper()

        inv = Investigation(

            id=uid,

            titulo=titulo,

            descricao=descricao,

            categoria=categoria,

            prioridade=prioridade,

            status="EM_EXECUCAO",

            criado_em=self.agora(),

            atualizado_em=self.agora()
        )

        self.investigations[uid] = inv

        self.salvar()

        print("=" * 60)
        print("NOVA INVESTIGAÃ‡ÃƒO")
        print("=" * 60)
        print("ID.............", uid)
        print("TÃTULO.........", titulo)
        print("STATUS.........", inv.status)
        print()

        return uid


    # --------------------------------------------------------------------------

    def checkpoint(self, uid, texto):

        inv = self.investigations[uid]

        inv.checkpoint = texto

        inv.atualizado_em = self.agora()

        self.salvar()

        print(f"[CHECKPOINT] {uid}")


    # --------------------------------------------------------------------------

    def progresso(self, uid, valor):

        inv = self.investigations[uid]

        inv.progresso = valor

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def adicionar_observacao(self, uid, texto):

        inv = self.investigations[uid]

        inv.observacoes.append(

            f"{self.agora()} - {texto}"

        )

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def adicionar_arquivo(self, uid, arquivo):

        inv = self.investigations[uid]

        if arquivo not in inv.arquivos:

            inv.arquivos.append(arquivo)

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def pausar(self, uid):

        inv = self.investigations[uid]

        inv.status = "PAUSADA"

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def retomar(self, uid):

        inv = self.investigations[uid]

        inv.status = "EM_EXECUCAO"

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def concluir(self, uid, resultado):

        inv = self.investigations[uid]

        inv.status = "CONCLUIDA"

        inv.resultado = resultado

        inv.progresso = 100

        inv.atualizado_em = self.agora()

        self.salvar()


    # --------------------------------------------------------------------------

    def listar(self, status=None):

        print("\n" + "=" * 70)
        print("INVESTIGAÃ‡Ã•ES")
        print("=" * 70)

        total = 0

        for inv in self.investigations.values():

            if status and inv.status != status:

                continue

            total += 1

            print(f"[{inv.id}]")

            print("TÃ­tulo......:", inv.titulo)

            print("Categoria...:", inv.categoria)

            print("Status......:", inv.status)

            print("Progresso...:", f"{inv.progresso}%")

            print("Checkpoint..:", inv.checkpoint)

            print("-" * 70)

        print("TOTAL:", total)
        print()


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    engine = KnowledgeContinuityEngine()

    codigo = engine.nova_investigacao(

        titulo="Descobrir gargalos da arquitetura",

        descricao="Analisar todo o nÃºcleo da IOTEC",

        categoria="ARQUITETURA",

        prioridade="ALTA"

    )

    engine.checkpoint(

        codigo,

        "Ãšltimo mÃ³dulo analisado: 015_PAYMENT_GATEWAY_ENGINE.py"

    )

    engine.progresso(codigo, 42)

    engine.adicionar_arquivo(

        codigo,

        "015_PAYMENT_GATEWAY_ENGINE.py"

    )

    engine.adicionar_observacao(

        codigo,

        "Encontrada oportunidade de integrar PayPal."

    )

    engine.listar()

