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
    pass

    if not os.path.exists(path):
        pass

        return []

    with open(path, "r") as f:
        pass

        return json.load(f)



def salvar_json(path, data):
    pass

    with open(path, "w") as f:
        pass

        json.dump(data, f, indent=2)



# =========================

# FINANCEIRO

# =========================



def registrar_pagamento(valor, descricao):
    pass

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



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° Pagamento registrado:", pagamento["id"])



    return pagamento



# =========================

# PEDIDO (CAIXA)

# =========================



def criar_pedido(pagamento, servico="auditoria"):
    pass

    pedido = {

        "id": f"PED-{pagamento['id']}",

        "servico": servico,

        "status": "em_producao",

        "data": datetime.now().strftime("%Y-%m-%d %H:%M")

    }



    path = os.path.join(PASTA_PED, f"{pedido['id']}.json")

    salvar_json(path, pedido)



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ Pedido criado:", pedido["id"])



    return pedido



# =========================

# ENTREGA

# =========================



def gerar_entrega(pedido):
    pass

    path = os.path.join(PASTA_ENT, f"{pedido['id']}.txt")



    conteudo = f"""

IOTEC - ENTREGA DIGITAL



Pedido: {pedido['id']}

ServiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o: {pedido['servico']}



Status: CONCLUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDO



DescriÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o:

AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise realizada com base nos dados fornecidos.



PrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ximos passos:

ImplementaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o recomendada.



Obrigado por utilizar a IOTEC.

"""



    with open(path, "w") as f:
        pass

        f.write(conteudo)



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¾ Entrega gerada:", path)



    return path



# =========================

# COMUNICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



def notificar_cliente(pedido):
    pass

    print(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© Cliente notificado: {pedido['id']}")



# =========================

# FLUXO PRINCIPAL

# =========================



def processar_pagamento(valor, descricao):
    pass

    pagamento = registrar_pagamento(valor, descricao)

    pedido = criar_pedido(pagamento)

    entrega = gerar_entrega(pedido)

    notificar_cliente(pedido)



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ Fluxo completo executado")



# =========================

# TESTE

# =========================



if __name__ == "__main__":
    pass

    processar_pagamento(29.90, "ValidaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o inicial do sistema")




