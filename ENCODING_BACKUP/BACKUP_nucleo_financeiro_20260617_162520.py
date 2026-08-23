import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from datetime import datetime

BASE = "C:\\IOTEC"

PASTA_FIN = os.path.join(BASE, "financeiro")
PASTA_PED = os.path.join(BASE, "pedidos")
PASTA_ENT = os.path.join(BASE, "entregas")

os.makedirs(PASTA_FIN, exist_ok=True)
os.makedirs(PASTA_PED, exist_ok=True)
os.makedirs(PASTA_ENT, exist_ok=True)

ARQ_FIN = os.path.join(PASTA_FIN, "livro_caixa.json")

# =========================
# UTIL
# =========================

def carregar_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def salvar_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# =========================
# FINANCEIRO
# =========================

def registrar_pagamento(valor, descricao):
    dados = carregar_json(ARQ_FIN)

    pagamento = {
        "id": f"PG-{len(dados)+1:03}",
        "valor": valor,
        "descricao": descricao,
        "status": "confirmado",
        "origem": "paypal",
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    dados.append(pagamento)
    salvar_json(ARQ_FIN, dados)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Pagamento registrado:", pagamento["id"])

    return pagamento

# =========================
# PEDIDO (CAIXA)
# =========================

def criar_pedido(pagamento, servico="auditoria"):
    pedido = {
        "id": f"PED-{pagamento['id']}",
        "servico": servico,
        "status": "em_producao",
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    path = os.path.join(PASTA_PED, f"{pedido['id']}.json")
    salvar_json(path, pedido)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Pedido criado:", pedido["id"])

    return pedido

# =========================
# ENTREGA
# =========================

def gerar_entrega(pedido):
    path = os.path.join(PASTA_ENT, f"{pedido['id']}.txt")

    conteudo = f"""
IOTEC - ENTREGA DIGITAL

Pedido: {pedido['id']}
ServiÃƒÆ'Ã†â€™o: {pedido['servico']}

Status: CONCLUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDO

DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:
AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise realizada com base nos dados fornecidos.

PrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ximos passos:
ImplementaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o recomendada.

Obrigado por utilizar a IOTEC.
"""

    with open(path, "w") as f:
        f.write(conteudo)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ Entrega gerada:", path)

    return path

# =========================
# COMUNICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def notificar_cliente(pedido):
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© Cliente notificado: {pedido['id']}")

# =========================
# FLUXO PRINCIPAL
# =========================

def processar_pagamento(valor, descricao):
    pagamento = registrar_pagamento(valor, descricao)
    pedido = criar_pedido(pagamento)
    entrega = gerar_entrega(pedido)
    notificar_cliente(pedido)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Fluxo completo executado")

# =========================
# TESTE
# =========================

if __name__ == "__main__":
    processar_pagamento(29.90, "ValidaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o inicial do sistema")


