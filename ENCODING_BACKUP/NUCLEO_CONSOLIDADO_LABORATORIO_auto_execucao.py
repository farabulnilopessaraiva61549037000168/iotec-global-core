import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import subprocess

# DefiniÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do nome da pasta e do arquivo
nome_pasta = "Neo_CompleX_Nova_Ia"
nome_arquivo = "estrategia_auto.py"

# Obter o diretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio base do usuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio
diretorio_usuario = os.path.expanduser("~")

# Procurar a pasta na ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Ârea de Trabalho e Documentos
possiveis_caminhos = [
    os.path.join(diretorio_usuario, "Desktop", nome_pasta),
    os.path.join(diretorio_usuario, "Documents", nome_pasta),
]

# Verificar onde a pasta existe
for caminho in possiveis_caminhos:
    if os.path.exists(caminho):
        diretorio_correto = caminho
        break
else:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â A pasta do sistema nÃƒÆ'Ã†â€™o foi encontrada!")
    exit()

# Caminho completo para o arquivo
caminho_arquivo = os.path.join(diretorio_correto, nome_arquivo)

# Verificar se o arquivo estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ presente
if not os.path.exists(caminho_arquivo):
    print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â O arquivo '{nome_arquivo}' nÃƒÆ'Ã†â€™o foi encontrado na pasta correta!")
    exit()

# Navegar automaticamente para a pasta e executar o script
print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio correto identificado: {diretorio_correto}")
print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Executando o sistema...")
subprocess.run(["python", caminho_arquivo])


