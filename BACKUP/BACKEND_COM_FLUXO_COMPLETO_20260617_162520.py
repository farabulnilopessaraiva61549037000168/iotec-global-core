import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request, jsonify

from idioma import detectar_idioma



app = Flask(__name__)



@app.route("/comando", methods=["POST"])

def comando():
    pass

    texto = request.json["comando"]



    idioma = detectar_idioma(texto)



    if idioma == "en":
        pass

        resposta = "Your request has been received."

    else:
        pass

        resposta = "Seu pedido foi recebido."



    return jsonify({

        "resposta": resposta,

        "idioma": idioma

    })



app.run(port=5000)




