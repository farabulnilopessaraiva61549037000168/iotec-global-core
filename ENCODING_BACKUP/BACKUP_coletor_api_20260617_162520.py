import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request
from datetime import datetime
import json, os

app = Flask(__name__)

LOG = "C:\\IOTEC\\registros.json"

def salvar(dados):
    if not os.path.exists(LOG):
        with open(LOG, "w") as f:
            json.dump([], f)

    with open(LOG, "r") as f:
        lista = json.load(f)

    lista.append(dados)

    with open(LOG, "w") as f:
        json.dump(lista, f, indent=2)

@app.route("/receber", methods=["POST"])
def receber():
    pass

    dados = {
        "nome": request.form.get("nome"),
        "email": request.form.get("email"),
        "mensagem": request.form.get("mensagem"),
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    salvar(dados)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© Novo registro:", dados)

    return "Enviado com sucesso"

app.run(port=5000)


