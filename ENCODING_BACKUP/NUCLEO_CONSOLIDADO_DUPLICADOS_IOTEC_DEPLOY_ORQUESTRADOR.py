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
# CONFIG
# =========================

BASE_DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop", "oficina_Iotech")
DESTINO_PROJETO = os.path.join(os.getcwd(), "deploy_render")
STATIC_DIR = os.path.join(DESTINO_PROJETO, "static")

# =========================
# LOG
# =========================

def log(msg):
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] {msg}")

# =========================
# ETAPA 1 - VERIFICAR ORIGEM
# =========================

def verificar_origem():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Verificando pasta oficina_Iotech...")

    if not os.path.exists(BASE_DESKTOP):
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Pasta oficina_Iotech nÃƒÆ'Ã†â€™o encontrada no Desktop")

    arquivos = os.listdir(BASE_DESKTOP)
    htmls = [f for f in arquivos if f.endswith(".html")]

    if len(htmls) == 0:
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Nenhum arquivo HTML encontrado")

    log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {len(htmls)} interfaces encontradas")
    return htmls

# =========================
# ETAPA 2 - PREPARAR ESTRUTURA
# =========================

def preparar_estrutura():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Preparando estrutura de deploy...")

    if os.path.exists(DESTINO_PROJETO):
        shutil.rmtree(DESTINO_PROJETO)

    os.makedirs(STATIC_DIR)

# =========================
# ETAPA 3 - COPIAR ARQUIVOS
# =========================

def copiar_interfaces():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Copiando interfaces...")

    for item in os.listdir(BASE_DESKTOP):
        origem = os.path.join(BASE_DESKTOP, item)
        destino = os.path.join(STATIC_DIR, item)

        if os.path.isfile(origem):
            shutil.copy(origem, destino)

# =========================
# ETAPA 4 - DEFINIR INDEX
# =========================

def garantir_index(htmls):
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â  Garantindo index.html...")

    if "index.html" not in htmls:
        primeiro = htmls[0]
        origem = os.path.join(STATIC_DIR, primeiro)
        destino = os.path.join(STATIC_DIR, "index.html")

        shutil.copy(origem, destino)
        log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  index.html criado a partir de {primeiro}")
    else:
        log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â index.html jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ existe")

# =========================
# ETAPA 5 - GERAR FLASK
# =========================

def gerar_flask():
    log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ Gerando app Flask...")

    app_code = '''
from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")

    print("NOVO LEAD:")
    print(nome, email, mensagem)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
'''

    with open(os.path.join(DESTINO_PROJETO, "app.py"), "w", encoding="utf-8") as f:
        f.write(app_code)

# =========================
# ETAPA 6 - REQUIREMENTS
# =========================

def gerar_requirements():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" Criando requirements.txt")

    with open(os.path.join(DESTINO_PROJETO, "requirements.txt"), "w") as f:
        f.write("flask\n")

# =========================
# ETAPA FINAL
# =========================

def executar():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIANDO ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O IOTEC")

    htmls = verificar_origem()
    preparar_estrutura()
    copiar_interfaces()
    garantir_index(htmls)
    gerar_flask()
    gerar_requirements()

    log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ PACOTE PRONTO PARA RENDER")
    log(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Local: {DESTINO_PROJETO}")

# =========================

if __name__ == "__main__":
    executar()


