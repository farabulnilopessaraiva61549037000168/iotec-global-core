import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_CORE_EMAIL_24H.py
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo 24h lendo Gmail (clientes + PayPal)
# ============================================================

import os
import time
import json
import imaplib
import email
from email.header import decode_header
import re

ARQ = "iotec_fluxo.json"

EMAIL_USER = os.getenv("IOTEC_EMAIL")
EMAIL_PASS = os.getenv("IOTEC_PASS")
IMAP_SERVER = "imap.gmail.com"

# =========================
# UTIL
# =========================

def carregar():
    try:
        with open(ARQ, "r") as f:
            return json.load(f)
    except:
        return {"entradas": [], "saidas": [], "bloqueios": [], "pagamentos": []}

def salvar(d):
    with open(ARQ, "w") as f:
        json.dump(d, f, indent=2)

def normalizar_texto(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors="ignore")
    else:
        return msg.get_payload(decode=True).decode(errors="ignore")
    return ""

def decodificar_assunto(msg):
    assunto, enc = decode_header(msg.get("Subject", ""))[0]
    if isinstance(assunto, bytes):
        return assunto.decode(enc or "utf-8", errors="ignore")
    return assunto or ""

# =========================
# DETECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# =========================

def eh_formulario_iotec(corpo):
    return "[IOTEC_REQUEST]" in corpo

def extrair_formulario(corpo):
    dados = {}
    for linha in corpo.split("\n"):
        if "NOME:" in linha:
            dados["nome"] = linha.split("NOME:")[1].strip()
        elif "SERVICO:" in linha:
            dados["servico"] = linha.split("SERVICO:")[1].strip()
        elif "PRIORIDADE:" in linha:
            dados["prioridade"] = linha.split("PRIORIDADE:")[1].strip()
    return dados

def eh_paypal(remetente, assunto, corpo):
    r = (remetente or "").lower()
    a = (assunto or "").lower()
    c = (corpo or "").lower()
    if "paypal" in r and ("payment" in a or "pagamento" in a):
        return True
    if "you received a payment" in c or "vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª recebeu um pagamento" in c:
        return True
    return False

def extrair_valor(corpo):
    m = re.search(r'(\$|r\$)\s?([\d\.,]+)', corpo.lower())
    return m.group(2) if m else None

# =========================
# DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O (simples)
# =========================

def decidir_score(dados):
    # fallback se nÃƒÆ'Ã†â€™o vier prioridade
    mapa = {"ALTA": 30, "MEDIA": 20, "BAIXA": 10}
    p = (dados.get("prioridade") or "MEDIA").upper()
    return mapa.get(p, 20)

def classificar(score):
    if score >= 30: return "saida"
    if score >= 20: return "monitorar"
    if score >= 10: return "esperar"
    return "bloqueio"

# =========================
# LOOP 24H
# =========================

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo 24h (Gmail) iniciado...")

while True:
    try:
        dados = carregar()

        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        status, msgs = mail.search(None, "UNSEEN")
        ids = msgs[0].split()

        for num in ids:
            status, msg_data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            assunto = decodificar_assunto(msg)
            remetente = msg.get("From", "")
            corpo = normalizar_texto(msg)

            # 1) FORMULÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO DO SEU SISTEMA
            if eh_formulario_iotec(corpo):
                info = extrair_formulario(corpo)
                score = decidir_score(info)
                decisao = classificar(score)

                entrada = {
                    "tipo": "cliente",
                    "nome": info.get("nome", "N/A"),
                    "servico": info.get("servico", "N/A"),
                    "prioridade": info.get("prioridade", "MEDIA"),
                    "score": score
                }

                dados["entradas"].append(entrada)

                if decisao == "saida":
                    dados["saidas"].append(entrada)
                elif decisao == "bloqueio":
                    dados["bloqueios"].append(entrada)

            # 2) PAYPAL (PAGAMENTO)
            elif eh_paypal(remetente, assunto, corpo):
                valor = extrair_valor(corpo)

                pagamento = {
                    "tipo": "paypal",
                    "assunto": assunto,
                    "valor": valor
                }

                dados["pagamentos"].append(pagamento)

                # opcional: promover ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltima entrada para "saida"
                if dados["entradas"]:
                    dados["saidas"].append(dados["entradas"][-1])

            # marcar como lido
            mail.store(num, '+FLAGS', '\\Seen')

        salvar(dados)
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ciclo e-mail executado")

    except Exception as e:
        print("Erro:", e)

    time.sleep(30)


