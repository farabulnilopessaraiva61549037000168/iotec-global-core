import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil

# Define as categorias
categorias = {
    "documentos": [".txt", ".docx", ".pdf"],
    "scripts": [".py", ".ipynb"],
    "planilhas": [".xlsx", ".csv"],
    "imagens": [".jpg", ".png", ".gif"]
}

# Pasta de origem (onde os arquivos estÃƒÆ'Ã†â€™o)
pasta_origem = "C:/Users/Bruno Lopes/Projetos_NeoCompleX"

# Criando subpastas para cada categoria
for categoria in categorias.keys():
    os.makedirs(os.path.join(pasta_origem, categoria), exist_ok=True)

# Organizando arquivos
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_arquivo):  # Verifica se ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© um arquivo
        for categoria, extensoes in categorias.items():
            if any(arquivo.endswith(ext) for ext in extensoes):
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, categoria, arquivo))
                print(f"Movendo {arquivo} para {categoria}")

print("OrganizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡")


