import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_links_pagamento(valor):
    return {
        "paypal": f"https://www.paypal.com/pay?amount={valor}",
        "pix": f"Pagamento Pix no valor de R$ {valor}"
    }



