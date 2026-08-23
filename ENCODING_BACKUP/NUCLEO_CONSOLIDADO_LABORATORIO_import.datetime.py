import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil
import datetime
import zipfile

def criar_capsula(caminho_raiz, destino):
    data = datetime.datetime.now().strftime("%Y-%m-%d")
    nome_capsula = f"CapsulaVida_{data}.zip"
    caminho_capsula = os.path.join(destino, nome_capsula)

    with zipfile.ZipFile(caminho_capsula, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(caminho_raiz):
            for file in files:
                caminho_arquivo = os.path.join(root, file)
                zipf.write(caminho_arquivo,
                           os.path.relpath(caminho_arquivo, caminho_raiz))

    print(f'ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡psula de Vida criada com sucesso: {caminho_capsula}')

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ EXECUTAR
criar_capsula('C:/MeuSistema', 'D:/BackupCofre')



