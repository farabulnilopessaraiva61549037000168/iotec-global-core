import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
msg_cliente = "1"



tipo = interpretar_mensagem(msg_cliente)



resposta = responder(tipo, "Bruno", "AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise de folha")



print(resposta)







