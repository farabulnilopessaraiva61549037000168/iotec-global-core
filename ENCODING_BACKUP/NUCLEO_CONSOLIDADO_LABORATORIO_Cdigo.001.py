import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Jaguar :: CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo 001
# Nome: jaguar_sigma_access.py
# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: Acesso inicial ao sistema Sigma e abertura automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica de interface via token mestre.

import sys

# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INICIAL
SENHA_MESTRE = "FLF48017248"
TOKEN_ATIVO = True

def autenticar_usuario(senha_digitada):
    if senha_digitada == SENHA_MESTRE and TOKEN_ATIVO:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Acesso concedido: Interface Jaguar liberada.")
        abrir_interface_sigma()
    else:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Acesso negado: Token invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido ou senha incorreta.")

def abrir_interface_sigma():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Conectando ÃƒÆ'Ã†â€™  plataforma Sigma...")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Carregando estrutura Jaguar...")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Interfaces inteligentes ativadas.")
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Sistema pronto para comando manual.")

# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICA AO INICIAR SCRIPT
if __name__ == "__main__":
    senha_usuario = input("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å" Digite sua senha mestra para acesso ao Jaguar: ")
    autenticar_usuario(senha_usuario)


