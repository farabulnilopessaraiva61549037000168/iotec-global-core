import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def desligar_sistema(chave_autenticacao):
    if chave_autenticacao == "SUA_SENHA_MESTRE_AQUI":
        print(">>> ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â SISTEMA DESLIGADO PELO USUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO. TODOS OS PROCESSOS ENCERRADOS. ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â")
        exit()
    else:
        print(">>> ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« ACESSO NEGADO. CHAVE INVÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLIDA.")


