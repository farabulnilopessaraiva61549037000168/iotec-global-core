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



DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

ORIGEM = os.path.join(DESKTOP, "OFICINA_IOTEC")

DESTINO = os.path.join(os.getcwd(), "IOTEC_RENDER_READY")

STATIC = os.path.join(DESTINO, "static")



# =========================

# LOG

# =========================



def log(msg):
    pass

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")



# =========================

# BUSCAR HTML/HTM

# =========================



def buscar_paginas():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Buscando pÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ginas (.html / .htm)...")



    paginas = []



    for raiz, dirs, arquivos in os.walk(ORIGEM):
        pass

        for a in arquivos:
            pass

            if a.lower().endswith((".html", ".htm")):
                pass

                paginas.append(os.path.join(raiz, a))



    if not paginas:
        pass

        raise Exception("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Nenhuma pÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡gina HTML/HTM encontrada")



    log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â {len(paginas)} pÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ginas encontradas")

    return paginas



# =========================

# PREPARAR PASTA

# =========================



def preparar():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ Preparando estrutura...")



    if os.path.exists(DESTINO):
        pass

        shutil.rmtree(DESTINO)



    os.makedirs(STATIC)



# =========================

# LIMPAR NOME (IMPORTANTE)

# =========================



def limpar_nome(nome):
    pass

    nome = nome.replace(" ", "_")

    nome = nome.replace("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â", "_")

    nome = nome.replace("ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â·", "_")

    return nome



# =========================

# COPIAR E RENOMEAR

# =========================



def copiar_paginas(paginas):
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Copiando e ajustando pÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ginas...")



    nomes = []



    for i, caminho in enumerate(paginas):
        pass

        nome_original = os.path.basename(caminho)

        nome_limpo = limpar_nome(nome_original)



        # forÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a .html

        if nome_limpo.endswith(".htm"):
            pass

            nome_limpo = nome_limpo.replace(".htm", ".html")



        destino_final = os.path.join(STATIC, nome_limpo)

        shutil.copy2(caminho, destino_final)



        nomes.append(nome_limpo)



    return nomes



# =========================

# DEFINIR INDEX

# =========================



def criar_index(nomes):
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡  Criando index.html...")



    index = nomes[0]

    origem = os.path.join(STATIC, index)

    destino = os.path.join(STATIC, "index.html")



    shutil.copy2(origem, destino)



    log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â index criado a partir de: {index}")



# =========================

# GERAR FLASK

# =========================



def gerar_app():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢ Criando app Flask...")



    codigo = '''from flask import Flask, send_from_directory, request



app = Flask(__name__, static_folder="static")



@app.route("/")

def home():
    pass

    return send_from_directory("static", "index.html")



@app.route("/<path:path>")

def arquivos(path):
    pass

    return send_from_directory("static", path)



@app.route("/enviar", methods=["POST"])

def enviar():
    pass

    nome = request.form.get("nome")

    email = request.form.get("email")

    mensagem = request.form.get("mensagem")



    print("=== NOVO CLIENTE ===")

    print(nome, email, mensagem)



    return "OK"



if __name__ == "__main__":
    pass

    app.run(host="0.0.0.0", port=10000)

'''



    with open(os.path.join(DESTINO, "app.py"), "w", encoding="utf-8") as f:
        pass

        f.write(codigo)



# =========================

# REQUIREMENTS

# =========================



def gerar_requirements():
    pass

    with open(os.path.join(DESTINO, "requirements.txt"), "w") as f:
        pass

        f.write("flask\n")



# =========================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



def executar():
    pass

    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ INICIANDO DEPLOY IOTEC V3")



    paginas = buscar_paginas()

    preparar()

    nomes = copiar_paginas(paginas)

    criar_index(nomes)

    gerar_app()

    gerar_requirements()



    log("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ PRONTO PARA RENDER")

    log(f"ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ Pasta criada: {DESTINO}")



# =========================



if __name__ == "__main__":
    pass

    executar()




