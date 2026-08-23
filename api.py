import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request, jsonify

from agente import interpretar, executar



app = Flask(__name__)



@app.route("/comando", methods=["POST"])

def comando():
    pass

    data = request.json

    texto = data["comando"]



    acao = interpretar(texto)

    executar(acao)



    return jsonify({"resposta": "Executado com sucesso"})



app.run(port=5000)







