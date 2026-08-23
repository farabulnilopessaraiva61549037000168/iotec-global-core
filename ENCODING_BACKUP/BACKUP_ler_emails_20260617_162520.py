import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def ler_emails():
    pass

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, SENHA)
    mail.select("inbox")

    status, mensagens = mail.search(None, "ALL")
    mensagens = mensagens[0].split()

    for num in mensagens[-10:]:
        pass

        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        corpo = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    corpo = part.get_payload(decode=True).decode()
        else:
            corpo = msg.get_payload(decode=True).decode()

        # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ FILTRO IMPORTANTE
        if "[IOTEC_FORM]" in corpo:
            pass

            dados = extrair_dados(corpo)

            print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  NOVO CLIENTE DETECTADO")
            print(dados)

            organizar_cliente(dados)


