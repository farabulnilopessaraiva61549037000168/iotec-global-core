import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# acesso_guardiao.py

import hashlib

# Hash da chave verdadeira, protegida
CHAVE_MESTRA_HASH = "d5f3c831..."  # Oculto neste exemplo

def validar_chave_sls(chave_digitada: str) -> bool:
    hash_input = hashlib.sha256(chave_digitada.encode()).hexdigest()
    return hash_input == CHAVE_MESTRA_HASH

def iniciar_sistema():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Acesso concedido ao GuardiÃƒÆ'Ã†â€™o.")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Jaguar ativado.")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Omega online.")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ Varredura IMAP iniciada.")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo de seguranÃƒÆ'Ã†â€™a em alta vigilÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia.")
    # Aqui pode-se acionar os sistemas reais

if __name__ == "__main__":
    chave = input("Digite a chave de acesso: ")
    if validar_chave_sls(chave):
        iniciar_sistema()
    else:
        print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Acesso negado. Chave invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida.")


