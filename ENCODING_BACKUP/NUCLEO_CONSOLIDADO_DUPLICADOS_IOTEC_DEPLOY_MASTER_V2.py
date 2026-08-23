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
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
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
# BUSCA HTML (INTELIGENTE)
# =========================

def buscar_htmls():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Procurando arquivos HTML em toda a estrutura...")

    if not os.path.exists(PASTA_ORIGEM):
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Pasta OFICINA_IOTEC nÃƒÆ'Ã†â€™o encontrada no Desktop")

    htmls = []

    for raiz, dirs, arquivos in os.walk(PASTA_ORIGEM):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".html"):
                caminho = os.path.join(raiz, arquivo)
                htmls.append(caminho)

    if not htmls:
        raise Exception("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Nenhum HTML encontrado em nenhuma subpasta")

    log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {len(htmls)} arquivos HTML encontrados")
    return htmls

# =========================
# PREPARAR DESTINO
# =========================

def preparar_destino():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Preparando ambiente de deploy...")

    if os.path.exists(PASTA_DESTINO):
        shutil.rmtree(PASTA_DESTINO)

    os.makedirs(PASTA_STATIC)

# =========================
# COPIAR TUDO (ESTRUTURA COMPLETA)
# =========================

def copiar_estrutura():
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Copiando toda a estrutura da OFICINA_IOTEC...")

    shutil.copytree(PASTA_ORIGEM, PASTA_STATIC, dirs_exist_ok=True)

# =========================
# GARANTIR INDEX
# =========================

def garantir_index(htmls):
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â  Garantindo index.html...")

    caminho_index = os.path.join(PASTA_STATIC, "index.html")

    if os.path.exists(caminho_index):
        log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â index.html jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ existe na raiz")
        return

    # pega o primeiro HTML encontrado
    origem = htmls[0]

    # copia como index
    shutil.copy2(origem, caminho_index)

    log(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  index.html criado a partir de: {os.path.basename(origem)}")

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
    log("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIANDO IOTEC DEPLOY MASTER V2")

    htmls = buscar_htmls()
    preparar_destino()
    copiar_estrutura()
    garantir_index(htmls)
    gerar_app()
    gerar_requirements()

    log("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ DEPLOY PRONTO PARA RENDER")
    log(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Pasta criada: {PASTA_DESTINO}")

# =========================

if __name__ == "__main__":
    executar()


