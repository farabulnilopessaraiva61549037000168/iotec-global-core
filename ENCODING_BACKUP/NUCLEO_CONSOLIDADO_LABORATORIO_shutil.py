import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil

# Caminhos das pastas
origem = "C:/Users/Bruno Lopes"
pasta_codigo_de_deus = "C:/Users/Bruno Lopes/CODIGO_DE_DEUS_ANALISE"
sistema_pasta = "C:/Users/Bruno Lopes/Sistema_Aprovado"

# Criar pastas organizadas, se ainda nÃƒÆ'Ã†â€™o existirem
os.makedirs(pasta_codigo_de_deus, exist_ok=True)
os.makedirs(sistema_pasta, exist_ok=True)

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para mover arquivos
def mover_para_pasta(caminho_origem):
    for arquivo in os.listdir(caminho_origem):
        caminho_arquivo = os.path.join(caminho_origem, arquivo)

        # Barrar "CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo de Deus" e mover para anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise especial
        if "CODIGO DE DEUS" in arquivo:
            shutil.move(caminho_arquivo, os.path.join(pasta_codigo_de_deus, arquivo))
        else:
            shutil.move(caminho_arquivo, os.path.join(sistema_pasta, arquivo))

# Executar triagem automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica
mover_para_pasta(origem)

print("Triagem concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da! 'CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo de Deus' isolado para anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise especial.")


