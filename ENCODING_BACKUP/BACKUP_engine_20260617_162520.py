import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from core.models import Produto

PRODUTOS = {
    "light": {
        "nome": "Sentinel Light",
        "nivel": "ENTRY",
        "preco": 49,
        "prazo": 2
    },
    "pro": {
        "nome": "Sentinel Regional",
        "nivel": "PRO",
        "preco": 199,
        "prazo": 7
    },
    "premium": {
        "nome": "Sentinel Institucional",
        "nivel": "PREMIUM",
        "preco": 5000,
        "prazo": 30
    }
}

CANAIS = {
    "ENTRY": ["Gumroad", "Hotmart", "Etsy"],
    "PRO": ["Upwork", "Fiverr"],
    "PREMIUM": ["LinkedIn", "Venda Direta"]
}


def obter_produto(chave: str) -> Produto:
    data = PRODUTOS[chave]
    return Produto(
        chave=chave,
        nome=data["nome"],
        nivel=data["nivel"],
        preco=data["preco"],
        prazo_dias=data["prazo"],
        canais=CANAIS[data["nivel"]]
    )


def classificar_por_orcamento(valor: float) -> str:
    if valor <= 100:
        return "ENTRY"
    elif valor <= 1000:
        return "PRO"
    return "PREMIUM"


