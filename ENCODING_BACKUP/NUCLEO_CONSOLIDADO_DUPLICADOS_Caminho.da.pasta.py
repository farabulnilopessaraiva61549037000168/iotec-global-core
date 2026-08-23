import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import hashlib
import getpass

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para gerar o hash da chave
def gerar_hash(chave):
    return hashlib.sha256(chave.encode()).hexdigest()

# Defina sua chave mestra aqui (pode ser uma frase secreta complexa)
chave_mestra = "MeuSistemaUltraSecreto123#"

# Gere o hash da chave
hash_esperado = gerar_hash(chave_mestra)

# Mensagem inicial
print("="*50)
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â ACESSO AO SISTEMA PRIVADO ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â")
print("="*50)

# UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio insere a chave
chave_input = getpass.getpass("Digite sua chave de acesso: ")

# Valida a chave
if gerar_hash(chave_input) == hash_esperado:
    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Acesso autorizado!")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Sistema desbloqueado com sucesso.")
    # Aqui vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode colocar os comandos para abrir os mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos do seu sistema
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¾Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Carregando mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos do sistema...")
    # Exemplo fictÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cio:
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Banco de Dados carregado")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å" InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Artificial iniciada")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¼ Painel Administrativo disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel")
else:
    print("\nÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Acesso negado. Chave incorreta!")


