import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

# Caminho fixo da pasta
diretorio_central = r"C:\Users\Bruno Lopes\Desktop\Neo_System_Core"

# Verificar se a pasta existe
if not os.path.exists(diretorio_central):
    print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â A pasta '{diretorio_central}' nÃƒÆ'Ã†â€™o foi encontrada!")
    exit()

# Listar todos os arquivos .py na pasta
arquivos_python = [f for f in os.listdir(diretorio_central) if f.endswith(".py")]

# Exibir os arquivos encontrados
if arquivos_python:
    print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Arquivos Python encontrados na pasta '{diretorio_central}':")
    for arquivo in arquivos_python:
        print(f"   - {arquivo}")
else:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Nenhum arquivo .py encontrado na pasta!")

# Criar um relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio de ativaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
relatorio_ativacao = os.path.join(diretorio_central, "relatorio_ativacao.txt")

with open(relatorio_ativacao, "w") as file:
    file.write("Arquivos prontos para ativaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:\n")
    for arquivo in arquivos_python:
        file.write(f"- {arquivo}\n")

print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio salvo em: {relatorio_ativacao}")


