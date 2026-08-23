import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request, jsonify

import json

from datetime import datetime

import os



app = Flask(__name__)



BASE = "C:\\IOTEC\\CORE"



def salvar_evento(dados):
    pass



    caminho = os.path.join(BASE, "eventos.json")



    if not os.path.exists(caminho):
        pass

        lista = []

    else:
        pass

        with open(caminho, "r", encoding="utf-8") as f:
            pass

            try:
                pass

                lista = json.load(f)

            except:
                pass

                lista = []



    lista.append(dados)



    with open(caminho, "w", encoding="utf-8") as f:
        pass

        json.dump(lista, f, indent=2)





def registrar_log(msg):
    pass



    caminho = os.path.join(BASE, "log.json")



    if not os.path.exists(caminho):
        pass

        lista = []

    else:
        pass

        with open(caminho, "r", encoding="utf-8") as f:
            pass

            try:
                pass

                lista = json.load(f)

            except:
                pass

                lista = []



    lista.append({

        "hora": datetime.now().strftime("%H:%M:%S"),

        "msg": msg

    })



    with open(caminho, "w", encoding="utf-8") as f:
        pass

        json.dump(lista, f, indent=2)





@app.route("/enviar", methods=["POST"])

def receber():
    pass



    data = request.json



    evento = {

        "cliente": data.get("empresa"),

        "responsavel": data.get("nome"),

        "email": data.get("email"),

        "telefone": data.get("telefone"),

        "setor": data.get("setor"),

        "problema": data.get("problema"),

        "status": "novo",

        "hora": datetime.now().strftime("%H:%M:%S")

    }



    salvar_evento(evento)



    registrar_log(f"Nova solicitaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o recebida: {evento['cliente']}")



    return jsonify({"status": "ok"})





if __name__ == "__main__":
    pass

    app.run(port=5000)




