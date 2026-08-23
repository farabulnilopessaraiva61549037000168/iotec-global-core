import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

def criar_pasta_acesso(nome_pasta):
    """Cria automaticamente a pasta de acesso e organiza os diretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios."""

    diretorio_base = "C:\\Users\\Bruno Lopes\\Desktop"
    caminho_pasta = os.path.join(diretorio_base, nome_pasta)

    # Verifica se a pasta jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ existe
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Pasta '{nome_pasta}' criada com sucesso!")
    else:
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â A pasta '{nome_pasta}' jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ existe!")

    return caminho_pasta

# Nome da pasta de acesso
nome_pasta_acesso = "Acesso_Neocomplex"

# Executa a criaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o da pasta
caminho_final = criar_pasta_acesso(nome_pasta_acesso)
print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio de acesso: {caminho_final}")


