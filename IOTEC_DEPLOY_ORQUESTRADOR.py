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
    pass

    agora = datetime.now().strftime("%H:%M:%S")

    print(f"[{agora}] {msg}")



# =========================

# ETAPA 1 - VERIFICAR ORIGEM

# =========================



def verificar_origem():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Verificando pasta oficina_Iotech...")



    if not os.path.exists(BASE_DESKTOP):
        pass

        raise Exception("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Pasta oficina_Iotech nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o encontrada no Desktop")



    arquivos = os.listdir(BASE_DESKTOP)

    htmls = [f for f in arquivos if f.endswith(".html")]



    if len(htmls) == 0:
        pass

        raise Exception("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Nenhum arquivo HTML encontrado")



    log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â {len(htmls)} interfaces encontradas")

    return htmls



# =========================

# ETAPA 2 - PREPARAR ESTRUTURA

# =========================



def preparar_estrutura():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ Preparando estrutura de deploy...")



    if os.path.exists(DESTINO_PROJETO):
        pass

        shutil.rmtree(DESTINO_PROJETO)



    os.makedirs(STATIC_DIR)



# =========================

# ETAPA 3 - COPIAR ARQUIVOS

# =========================



def copiar_interfaces():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Copiando interfaces...")



    for item in os.listdir(BASE_DESKTOP):
        pass

        origem = os.path.join(BASE_DESKTOP, item)

        destino = os.path.join(STATIC_DIR, item)



        if os.path.isfile(origem):
            pass

            shutil.copy(origem, destino)



# =========================

# ETAPA 4 - DEFINIR INDEX

# =========================



def garantir_index(htmls):
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡  Garantindo index.html...")



    if "index.html" not in htmls:
        pass

        primeiro = htmls[0]

        origem = os.path.join(STATIC_DIR, primeiro)

        destino = os.path.join(STATIC_DIR, "index.html")



        shutil.copy(origem, destino)

        log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  index.html criado a partir de {primeiro}")

    else:
        pass

        log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â index.html jÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ existe")



# =========================

# ETAPA 5 - GERAR FLASK

# =========================



def gerar_flask():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢ Gerando app Flask...")



    app_code = '''

from flask import Flask, send_from_directory, request



app = Flask(__name__, static_folder="static")



@app.route("/")

def home():
    pass

    return send_from_directory("static", "index.html")



@app.route("/<path:path>")

def static_files(path):
    pass

    return send_from_directory("static", path)



@app.route("/enviar", methods=["POST"])

def enviar():
    pass

    nome = request.form.get("nome")

    email = request.form.get("email")

    mensagem = request.form.get("mensagem")



    print("NOVO LEAD:")

    print(nome, email, mensagem)



    return "OK"



if __name__ == "__main__":
    pass

    app.run(host="0.0.0.0", port=10000)

'''



    with open(os.path.join(DESTINO_PROJETO, "app.py"), "w", encoding="utf-8") as f:
        pass

        f.write(app_code)



# =========================

# ETAPA 6 - REQUIREMENTS

# =========================



def gerar_requirements():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Criando requirements.txt")



    with open(os.path.join(DESTINO_PROJETO, "requirements.txt"), "w") as f:
        pass

        f.write("flask\n")



# =========================

# ETAPA FINAL

# =========================



def executar():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ INICIANDO ORQUESTRAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O IOTEC")



    htmls = verificar_origem()

    preparar_estrutura()

    copiar_interfaces()

    garantir_index(htmls)

    gerar_flask()

    gerar_requirements()



    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ PACOTE PRONTO PARA RENDER")

    log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ Local: {DESTINO_PROJETO}")



# =========================



if __name__ == "__main__":
    pass

    executar()






