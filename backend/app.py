import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request, jsonify

import random



app = Flask(__name__)



@app.route("/processar", methods=["POST"])

def processar():
    pass

    data = request.json

    pedido = data.get("pedido")

    valor = random.uniform(1,5)



    return jsonify({"resposta": f"Processado: {pedido}", "valor": valor})



if __name__ == "__main__":
    pass

    app.run(port=5000)




