import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if eh_pagamento_paypal(remetente, assunto, corpo):
    pass

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Pagamento confirmado via PayPal")

    # exemplo: atualizar cliente
    for c in st.session_state.clientes:
        if c["status"] == "AGUARDANDO_PAGAMENTO":
            c["status"] = "PAGO"
            c["prioridade"] = "ALTA"


