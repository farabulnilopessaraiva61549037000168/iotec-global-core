import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC WATCHER

# SUPERVISOR DE INTEGRIDADE OPERACIONAL

# =========================================================



from flask import Flask, jsonify

from flask_cors import CORS



import requests

import threading

import time



from datetime import datetime



# =========================================================

# APP

# =========================================================



app = Flask(__name__)



CORS(app)



# =========================================================

# SERVICOS MONITORADOS

# =========================================================



SERVICOS = [



    {

        "nome": "nucleo",



        "url":

        "http://127.0.0.1:5000"

    },



    {

        "nome": "traffic",



        "url":

        "http://127.0.0.1:5050"

    }



]



# =========================================================

# STATUS CENTRAL

# =========================================================



STATUS = {



    "servicos": [],



    "alertas": [],



    "ultima_verificacao": None

}



# =========================================================

# VERIFICAR SERVICO

# =========================================================



def verificar_servico(servico):
    pass



    try:
        pass



        resposta = requests.get(



            servico["url"],



            timeout=5

        )



        return {



            "nome":

            servico["nome"],



            "status":

            "online",



            "http":

            resposta.status_code,



            "timestamp":



            datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

        }



    except Exception as e:
        pass



        alerta = (



            f"SERVICO OFFLINE: "

            f"{servico['nome']}"

        )



        if alerta not in STATUS["alertas"]:
            pass



            STATUS["alertas"].append(

                alerta

            )



        return {



            "nome":

            servico["nome"],



            "status":

            "offline",



            "erro":

            str(e),



            "timestamp":



            datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

        }



# =========================================================

# LOOP WATCHER

# =========================================================



def watcher_loop():
    pass



    while True:
        pass



        resultados = []



        for servico in SERVICOS:
            pass



            resultados.append(



                verificar_servico(

                    servico

                )

            )



        STATUS["servicos"] = resultados



        STATUS["ultima_verificacao"] = (



            datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

        )



        time.sleep(20)



# =========================================================

# HOME

# =========================================================



@app.route('/')



def home():
    pass



    return jsonify({



        "watcher": "online",



        "tipo":

        "supervisor_integridade",



        "servicos_monitorados":

        len(SERVICOS),



        "alertas":

        len(STATUS["alertas"])

    })



# =========================================================

# STATUS

# =========================================================



@app.route('/watcher/status')



def status():
    pass



    return jsonify(STATUS)



# =========================================================

# ALERTAS

# =========================================================



@app.route('/watcher/alertas')



def alertas():
    pass



    return jsonify({



        "alertas":

        STATUS["alertas"]

    })



# =========================================================

# BOOT

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("===================================")

    print(" IOTEC WATCHER ONLINE ")

    print("===================================")

    print("")



    threading.Thread(



        target=watcher_loop,



        daemon=True



    ).start()



    app.run(



        host='0.0.0.0',



        port=5001

    )






