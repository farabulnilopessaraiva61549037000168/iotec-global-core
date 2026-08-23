import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil
from datetime import datetime

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FIXA
# =========================

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
PASTA_ORIGEM = os.path.join(DESKTOP, "OFICINA_IOTEC")
PASTA_DESTINO = os.path.join(os.getcwd(), "IOTEC_RENDER_READY")
PASTA_STATIC = os.path.join(PASTA_DESTINO, "static")

# =========================
# LOG
# =========================

def log(msg):
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] {msg}")

# =========================
# VALIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INICIAL
# =========================

def validar_origem():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Verificando pasta OFICINA_IOTEC...")

    if not os.path.exists(PASTA_ORIGEM):
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Pasta OFICINA_IOTEC NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O encontrada no Desktop")

    arquivos = os.listdir(PASTA_ORIGEM)
    htmls = [f for f in arquivos if f.lower().endswith(".html")]

    if not htmls:
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Nenhum arquivo HTML encontrado")

    log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {len(htmls)} interfaces detectadas")
    return htmls

# =========================
# LIMPAR E PREPARAR
# =========================

def preparar_destino():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Preparando ambiente de deploy...")

    if os.path.exists(PASTA_DESTINO):
        shutil.rmtree(PASTA_DESTINO)

    os.makedirs(PASTA_STATIC)

# =========================
# COPIAR ARQUIVOS
# =========================

def copiar_arquivos():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Copiando arquivos...")

    for item in os.listdir(PASTA_ORIGEM):
        origem = os.path.join(PASTA_ORIGEM, item)
        destino = os.path.join(PASTA_STATIC, item)

        if os.path.isfile(origem):
            shutil.copy2(origem, destino)

        elif os.path.isdir(origem):
            shutil.copytree(origem, destino)

# =========================
# GARANTIR INDEX
# =========================

def garantir_index(htmls):
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â  Verificando index.html...")

    caminho_index = os.path.join(PASTA_STATIC, "index.html")

    if not os.path.exists(caminho_index):
        primeiro = htmls[0]
        origem = os.path.join(PASTA_STATIC, primeiro)
        shutil.copy2(origem, caminho_index)

        log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  index.html criado a partir de {primeiro}")
    else:
        log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â index.html OK")

# =========================
# GERAR FLASK APP
# =========================

def gerar_app():
    log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ Criando app Flask...")

    codigo = '''from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def arquivos(path):
    return send_from_directory("static", path)

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")

    print("=== NOVO LEAD ===")
    print("Nome:", nome)
    print("Email:", email)
    print("Mensagem:", mensagem)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
'''

    with open(os.path.join(PASTA_DESTINO, "app.py"), "w", encoding="utf-8") as f:
        f.write(codigo)

# =========================
# REQUIREMENTS
# =========================

def gerar_requirements():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" Criando requirements.txt")

    with open(os.path.join(PASTA_DESTINO, "requirements.txt"), "w") as f:
        f.write("flask\n")

# =========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O PRINCIPAL
# =========================

def executar():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIANDO DEPLOY MASTER IOTEC")

    htmls = validar_origem()
    preparar_destino()
    copiar_arquivos()
    garantir_index(htmls)
    gerar_app()
    gerar_requirements()

    log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ SISTEMA PRONTO PARA RENDER")
    log(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Pasta criada: {PASTA_DESTINO}")

# =========================

if __name__ == "__main__":
    executar()


