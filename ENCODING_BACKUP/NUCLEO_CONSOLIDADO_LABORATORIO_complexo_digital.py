import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import flask
from flask import Flask, request, jsonify

# ==========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O PRINCIPAL
# ==========================
BASE_DIR = "C:\\Users\\Bruno Lopes\\Desktop\\Neo_System_Core"

# Bloquear execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o caso esteja fora da pasta correta
if os.getcwd() != BASE_DIR:
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ERRO: Sistema deve ser executado dentro da pasta correta!")
    exit()

# Garantir que o sistema sempre opere no local correto
os.chdir(BASE_DIR)
print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio de trabalho fixado em: {BASE_DIR}")

# ==========================
# SISTEMA WEB API
# ==========================
app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    total_arquivos = {folder: len(os.listdir(os.path.join(BASE_DIR, folder))) for folder in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, folder))}
    return jsonify(total_arquivos)

@app.route('/upload', methods=['POST'])
def upload_arquivo():
    if 'arquivo' not in request.files:
        return "Nenhum arquivo encontrado", 400
    arquivo = request.files['arquivo']
    caminho = os.path.join(BASE_DIR, "Entrada", arquivo.filename)
    arquivo.save(caminho)
    return f"Arquivo {arquivo.filename} salvo!", 200

# ==========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO SISTEMA
# ==========================
if __name__ == "__main__":
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ COMPLEXO DIGITAL ATIVADO!")
    app.run(host='0.0.0.0', port=5000)


