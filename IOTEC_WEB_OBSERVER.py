import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC WEB OBSERVER

# CENTRAL DE SUPERVISAO OPERACIONAL WEB

# =========================================================



from flask import Flask, jsonify

from flask_cors import CORS



import requests

import threading

import time

import socket

import re



from bs4 import BeautifulSoup



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



    # =====================================================

    # NUCLEO

    # =====================================================



    {

        "nome": "nucleo",



        "tipo": "local",



        "url":

        "http://127.0.0.1:5000"

    },



    # =====================================================

    # TRAFFIC CONTROLLER

    # =====================================================



    {

        "nome": "traffic",



        "tipo": "local",



        "url":

        "http://127.0.0.1:5050"

    },



    # =====================================================

    # WATCHER

    # =====================================================



    {

        "nome": "watcher",



        "tipo": "local",



        "url":

        "http://127.0.0.1:5001"

    },



    # =====================================================

    # NETLIFY

    # SUBSTITUA PELO SEU LINK

    # =====================================================



    {

        "nome": "netlify",



        "tipo": "web",



        "url":

        "https://SEU-SITE.netlify.app"

    },



    # =====================================================

    # RENDER

    # SUBSTITUA PELO SEU LINK

    # =====================================================



    {

        "nome": "render",



        "tipo": "web",



        "url":

        "https://SEU-NUCLEO.onrender.com"

    }

]



# =========================================================

# ESTADO CENTRAL

# =========================================================



ESTADO = {



    "infraestrutura": "online",



    "servicos": [],



    "alertas": [],



    "anomalias": [],



    "ultima_verificacao": None

}



# =========================================================

# DETECTAR POLUICAO VISUAL

# =========================================================



def detectar_poluicao(html):
    pass



    caracteres_suspeitos = [



        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢",

        " ",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â",

        "ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤",

        " "

    ]



    encontrados = []



    for caractere in caracteres_suspeitos:
        pass



        if caractere in html:
            pass



            encontrados.append(caractere)



    return encontrados



# =========================================================

# DETECTAR IMAGENS

# =========================================================



def detectar_imagens(html):
    pass



    soup = BeautifulSoup(

        html,

        'html.parser'

    )



    imagens = soup.find_all('img')



    return len(imagens)



# =========================================================

# DETECTAR CSS

# =========================================================



def detectar_css(html):
    pass



    soup = BeautifulSoup(

        html,

        'html.parser'

    )



    css = soup.find_all('link')



    return len(css)



# =========================================================

# VERIFICAR SERVICO

# =========================================================



def verificar_servico(servico):
    pass



    try:
        pass



        resposta = requests.get(



            servico["url"],



            timeout=10

        )



        html = resposta.text



        imagens = detectar_imagens(

            html

        )



        css = detectar_css(

            html

        )



        poluicao = detectar_poluicao(

            html

        )



        status = {



            "nome":

            servico["nome"],



            "tipo":

            servico["tipo"],



            "status":

            "online",



            "http":

            resposta.status_code,



            "imagens":

            imagens,



            "css":

            css,



            "poluicao":

            poluicao,



            "timestamp":



            datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

        }



        # =================================================

        # DETECTAR POLUICAO

        # =================================================



        if len(poluicao) > 0:
            pass



            alerta = (



                f"POLUICAO VISUAL: "

                f"{servico['nome']}"

            )



            if alerta not in ESTADO["anomalias"]:
                pass



                ESTADO["anomalias"].append(

                    alerta

                )



        # =================================================

        # DETECTAR FALTA DE IMAGENS

        # =================================================



        if imagens == 0 and servico["tipo"] == "web":
            pass



            alerta = (



                f"INTERFACE SEM IMAGENS: "

                f"{servico['nome']}"

            )



            if alerta not in ESTADO["anomalias"]:
                pass



                ESTADO["anomalias"].append(

                    alerta

                )



        return status



    except Exception as e:
        pass



        alerta = (



            f"SERVICO OFFLINE: "

            f"{servico['nome']}"

        )



        if alerta not in ESTADO["alertas"]:
            pass



            ESTADO["alertas"].append(

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

# LOOP PRINCIPAL

# =========================================================



def observer_loop():
    pass



    while True:
        pass



        resultados = []



        for servico in SERVICOS:
            pass



            resultado = verificar_servico(

                servico

            )



            resultados.append(

                resultado

            )



        ESTADO["servicos"] = resultados



        ESTADO["ultima_verificacao"] = (



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



        "observer": "online",



        "tipo":

        "central_supervisao_web",



        "servicos_monitorados":

        len(SERVICOS),



        "alertas":

        len(ESTADO["alertas"]),



        "anomalias":

        len(ESTADO["anomalias"])

    })



# =========================================================

# STATUS

# =========================================================



@app.route('/observer/status')



def status():
    pass



    return jsonify(ESTADO)



# =========================================================

# ALERTAS

# =========================================================



@app.route('/observer/alertas')



def alertas():
    pass



    return jsonify({



        "alertas":

        ESTADO["alertas"]

    })



# =========================================================

# ANOMALIAS

# =========================================================



@app.route('/observer/anomalias')



def anomalias():
    pass



    return jsonify({



        "anomalias":

        ESTADO["anomalias"]

    })



# =========================================================

# SERVICOS

# =========================================================



@app.route('/observer/servicos')



def servicos():
    pass



    return jsonify({



        "servicos":

        ESTADO["servicos"]

    })



# =========================================================

# BOOT

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("=" * 60)

    print(" IOTEC WEB OBSERVER ")

    print("=" * 60)

    print("")



    threading.Thread(



        target=observer_loop,



        daemon=True



    ).start()



    app.run(



        host='0.0.0.0',



        port=5020

    )






