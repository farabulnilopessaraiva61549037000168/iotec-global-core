import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from modulo_exemplo import executar

def cc(pedido):
    resp = executar(pedido)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo:", resp["status"], "-", resp["mensagem"])

    return resp



