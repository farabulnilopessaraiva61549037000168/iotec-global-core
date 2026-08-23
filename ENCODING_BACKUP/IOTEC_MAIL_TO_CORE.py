import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import imaplib
import email

EMAIL = "seuemail@gmail.com"
SENHA = "senha_app"

def extrair_dados(corpo):
    pass

    dados = {}

    for linha in corpo.split("\n"):
        if "NOME:" in linha:
            dados["nome"] = linha.split("NOME:")[1].strip()

        elif "EMPRESA:" in linha:
            dados["empresa"] = linha.split("EMPRESA:")[1].strip()

        elif "TELEFONE:" in linha:
            dados["telefone"] = linha.split("TELEFONE:")[1].strip()

        elif "PROBLEMA:" in linha:
            dados["problema"] = linha.split("PROBLEMA:")[1].strip()

    return dados


