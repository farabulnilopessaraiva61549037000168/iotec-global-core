import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC_CORE_LIVE_QUEUE.py

# Painel central conectado ao e-mail (entrada automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica)

# IOTEC - NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo Operacional

# ============================================================



import streamlit as st

import imaplib

import email

from email.header import decode_header



st.set_page_config(layout="wide")



st.title("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  IOTEC - Central Operacional")

st.subheader("Fila automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica alimentada por e-mail")



# =========================

# CONFIG EMAIL

# =========================



EMAIL_USER = "seu@gmail.com"

EMAIL_PASS = "senha_app"

IMAP_SERVER = "imap.gmail.com"



# =========================

# ESTADO

# =========================



if "clientes" not in st.session_state:
    pass

    st.session_state.clientes = []



if "historico" not in st.session_state:
    pass

    st.session_state.historico = []



# =========================

# FILTRO DE CLIENTE

# =========================



def eh_cliente(corpo):
    pass

    return "[IOTEC_REQUEST]" in corpo



# =========================

# EXTRAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



def extrair_dados(corpo):
    pass



    dados = {}



    for linha in corpo.split("\n"):
        pass

        if "NOME:" in linha:
            pass

            dados["nome"] = linha.split("NOME:")[1].strip()



        elif "SERVICO:" in linha:
            pass

            dados["servico"] = linha.split("SERVICO:")[1].strip()



        elif "PRIORIDADE:" in linha:
            pass

            dados["prioridade"] = linha.split("PRIORIDADE:")[1].strip()



    return dados



# =========================

# ADICIONAR CLIENTE

# =========================



def adicionar_cliente(dados):
    pass



    # evita duplicado

    nomes = [c["nome"] for c in st.session_state.clientes]



    if dados["nome"] not in nomes:
        pass

        st.session_state.clientes.append({

            "nome": dados["nome"],

            "servico": dados.get("servico", "NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o definido"),

            "prioridade": dados.get("prioridade", "MEDIA"),

            "status": "ATIVO"

        })



# =========================

# LER EMAIL

# =========================



def ler_email():
    pass



    try:
        pass

        mail = imaplib.IMAP4_SSL(IMAP_SERVER)

        mail.login(EMAIL_USER, EMAIL_PASS)

        mail.select("inbox")



        status, mensagens = mail.search(None, "UNSEEN")

        mensagens = mensagens[0].split()



        for num in mensagens:
            pass



            status, msg_data = mail.fetch(num, "(RFC822)")

            msg = email.message_from_bytes(msg_data[0][1])



            corpo = ""



            if msg.is_multipart():
                pass

                for part in msg.walk():
                    pass

                    if part.get_content_type() == "text/plain":
                        pass

                        corpo = part.get_payload(decode=True).decode()

            else:
                pass

                corpo = msg.get_payload(decode=True).decode()



            if eh_cliente(corpo):
                pass

                dados = extrair_dados(corpo)

                adicionar_cliente(dados)



            # marca como lido

            mail.store(num, '+FLAGS', '\\Seen')



    except Exception as e:
        pass

        st.error(f"Erro ao ler e-mail: {e}")



# =========================

# ORDENAR

# =========================



def ordenar():
    pass



    prioridade_map = {

        "ALTA": 1,

        "MEDIA": 2,

        "BAIXA": 3

    }



    st.session_state.clientes.sort(

        key=lambda x: prioridade_map.get(x["prioridade"], 2)

    )



# =========================

# CONCLUIR

# =========================



def concluir(index):
    pass



    cliente = st.session_state.clientes.pop(index)

    st.session_state.historico.append(cliente)



# =========================

# ATUALIZAR AUTOMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂTICO

# =========================



if st.button("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¾ Atualizar (puxar e-mail)"):
    pass

    ler_email()



ordenar()



# =========================

# FILA ATIVA

# =========================



st.markdown("### ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¹ Fila Ativa")



for i, c in enumerate(st.session_state.clientes):
    pass



    col1, col2, col3, col4 = st.columns([3,2,2,1])



    col1.write(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ {c['nome']}")

    col2.write(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ {c['prioridade']}")

    col3.write(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼ {c['servico']}")



    if col4.button("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ Concluir", key=i):
        pass

        concluir(i)



# =========================

# HISTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RICO

# =========================



st.markdown("### ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¾ Auditoria")



for h in st.session_state.historico:
    pass

    st.write(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¯ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â {h['nome']} - {h['servico']}")






