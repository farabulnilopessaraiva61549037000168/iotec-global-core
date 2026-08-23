import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if eh_pagamento_paypal(remetente, assunto, corpo):
    pass



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° Pagamento confirmado via PayPal")



    # exemplo: atualizar cliente

    for c in st.session_state.clientes:
        pass

        if c["status"] == "AGUARDANDO_PAGAMENTO":
            pass

            c["status"] = "PAGO"

            c["prioridade"] = "ALTA"




