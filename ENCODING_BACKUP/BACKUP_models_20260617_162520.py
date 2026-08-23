import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid


class Produto(BaseModel):
    chave: str
    nome: str
    nivel: str
    preco: float
    prazo_dias: int
    canais: List[str]


class Pedido(BaseModel):
    id: str
    cliente: str
    produto: Produto
    status: str
    criado_em: datetime

    @staticmethod
    def criar(cliente: str, produto: Produto):
        return Pedido(
            id=str(uuid.uuid4())[:8],
            cliente=cliente,
            produto=produto,
            status="CAPTADO",
            criado_em=datetime.now()
        )


