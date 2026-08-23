import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from fastapi import FastAPI
from core.engine import obter_produto, classificar_por_orcamento
from core.models import Pedido
from core.pipeline import avancar_status

app = FastAPI(title="IOTEC API")

pedidos_db = []


@app.get("/")
def home():
    return {"status": "IOTEC ONLINE"}


@app.get("/produtos")
def listar_produtos():
    return ["light", "pro", "premium"]


@app.post("/comprar")
def comprar(cliente: str, produto: str):
    p = obter_produto(produto)
    pedido = Pedido.criar(cliente, p)
    pedidos_db.append(pedido)
    return pedido


@app.post("/comprar-por-orcamento")
def comprar_por_orcamento(cliente: str, valor: float):
    nivel = classificar_por_orcamento(valor)

    mapa = {
        "ENTRY": "light",
        "PRO": "pro",
        "PREMIUM": "premium"
    }

    produto = obter_produto(mapa[nivel])
    pedido = Pedido.criar(cliente, produto)
    pedidos_db.append(pedido)

    return pedido


@app.get("/pedidos")
def listar_pedidos():
    return pedidos_db


@app.post("/avancar/{pedido_id}")
def avancar(pedido_id: str):
    for p in pedidos_db:
        if p.id == pedido_id:
            p.status = avancar_status(p.status)
            return p

    return {"erro": "Pedido nÃƒÆ'Ã†â€™o encontrado"}


