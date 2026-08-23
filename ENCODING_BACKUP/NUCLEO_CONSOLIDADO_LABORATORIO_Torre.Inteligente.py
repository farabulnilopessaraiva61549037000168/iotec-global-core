import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de Dados Digital - Torre Inteligente
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo aberto para expansÃƒÆ'Ã†â€™o e integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de sistemas globais

from flask import Flask, request, jsonify
import os
import shutil
from datetime import datetime

app = Flask(__name__)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â DiretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio principal do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de Dados
BASE_DIR = os.path.expanduser("~/NucleoDeDadosDigital")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Estrutura de diretÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios
folders = [
    "Entrada",
    "Processando",
    "Organizado/Documentos",
    "Organizado/Imagens",
    "Organizado/Audios",
    "Organizado/Projetos",
    "Organizado/LicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
    "Organizado/Consultoria",
    "Organizado/ForenseDigital",
    "Organizado/AgronegÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio",
    "Organizado/Tecnologia",
    "Organizado/JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico",
    "Organizado/SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂºdePsicologia",
    "Logs"
]

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para criar estrutura de pastas
def criar_pastas():
    for folder in folders:
        caminho = os.path.join(BASE_DIR, folder)
        os.makedirs(caminho, exist_ok=True)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¥ Upload de arquivos para Entrada
@app.route('/upload', methods=['POST'])
def upload_arquivo():
    if 'arquivo' not in request.files:
        return "Nenhum arquivo encontrado", 400
    arquivo = request.files['arquivo']
    caminho = os.path.join(BASE_DIR, "Entrada", arquivo.filename)
    arquivo.save(caminho)
    log_evento(f"Arquivo {arquivo.filename} recebido em Entrada")
    return f"Arquivo {arquivo.filename} salvo com sucesso", 200

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Processamento dos Arquivos
@app.route('/processar', methods=['POST'])
def processar_arquivos():
    entrada_dir = os.path.join(BASE_DIR, "Entrada")
    processado = 0
    for filename in os.listdir(entrada_dir):
        origem = os.path.join(entrada_dir, filename)
        destino = classificar_arquivo(filename)
        shutil.move(origem, destino)
        processado += 1
        log_evento(f"Arquivo {filename} movido para {destino}")
    return jsonify({"arquivos_processados": processado})

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ClassificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de arquivos
def classificar_arquivo(nome_arquivo):
    extensao = nome_arquivo.lower().split('.')[-1]
    if extensao in ['pdf', 'doc', 'docx', 'txt']:
        return os.path.join(BASE_DIR, "Organizado", "Documentos", nome_arquivo)
    elif extensao in ['jpg', 'jpeg', 'png', 'svg']:
        return os.path.join(BASE_DIR, "Organizado", "Imagens", nome_arquivo)
    elif extensao in ['mp3', 'wav', 'm4a']:
        return os.path.join(BASE_DIR, "Organizado", "Audios", nome_arquivo)
    elif 'licitacao' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "LicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes", nome_arquivo)
    elif 'forense' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "ForenseDigital", nome_arquivo)
    elif 'consultoria' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "Consultoria", nome_arquivo)
    elif 'psicologia' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂºdePsicologia", nome_arquivo)
    elif 'agronegocio' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "AgronegÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio", nome_arquivo)
    elif 'tecnologia' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "Tecnologia", nome_arquivo)
    elif 'juridico' in nome_arquivo.lower():
        return os.path.join(BASE_DIR, "Organizado", "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico", nome_arquivo)
    else:
        return os.path.join(BASE_DIR, "Organizado", "Projetos", nome_arquivo)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Logs dos eventos
def log_evento(mensagem):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = f"[{agora}] {mensagem}\n"
    with open(os.path.join(BASE_DIR, "Logs", "log_eventos.txt"), "a") as log_file:
        log_file.write(log)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â½ Status do Sistema
@app.route('/status', methods=['GET'])
def status():
    total_arquivos = {}
    for folder in folders:
        caminho = os.path.join(BASE_DIR, folder)
        total_arquivos[folder] = len(os.listdir(caminho)) if os.path.exists(caminho) else 0
    return jsonify(total_arquivos)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ InicializaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
if __name__ == '__main__':
    criar_pastas()
    app.run(host='0.0.0.0', port=5000)


