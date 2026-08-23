import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request



app = Flask(__name__, static_folder="static")



@app.route("/")

def home():
    pass

    return app.send_static_file("index.html")



# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ ESSA ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â° A PARTE QUE FALTAVA

@app.route("/enviar", methods=["POST"])

def enviar():
    pass

    nome = request.form.get("nome")

    email = request.form.get("email")

    mensagem = request.form.get("mensagem")



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© NOVO LEAD:", nome, email, mensagem)



    return "OK RECEBIDO"



# manter rota para arquivos

@app.route("/<path:path>")

def serve(path):
    pass

    return app.send_static_file(path)



if __name__ == "__main__":
    pass

    app.run(host="0.0.0.0", port=8080)




