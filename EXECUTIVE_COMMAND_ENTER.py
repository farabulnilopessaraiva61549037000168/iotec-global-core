import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC EXECUTIVE COMMAND CENTER

# CENTRAL EXECUTIVA CORPORATIVA DO ECOSSISTEMA

# =========================================================



from flask import Flask, jsonify



from flask_cors import CORS



from datetime import datetime



import requests



# =========================================================

# APP

# =========================================================



app = Flask(__name__)



CORS(app)



# =========================================================

# ENDPOINTS

# =========================================================



SERVICOS = {



    "governanca":

    "http://127.0.0.1:7600/governance/executivo",



    "organograma":

    "http://127.0.0.1:7600/governance/organograma",



    "consolidacao":

    "http://127.0.0.1:7500/consolidation/executivo",



    "curadoria":

    "http://127.0.0.1:7400/curator/executivo",



    "organizacao":

    "http://127.0.0.1:7200/torre/status",



    "criatividade":

    "http://127.0.0.1:7300/creative/inspiracao",



    "gateway":

    "http://127.0.0.1:7000/gateway/ecossistema"

}



# =========================================================

# CONSULTAR

# =========================================================



def consultar(url):
    pass



    try:
        pass



        r = requests.get(



            url,



            timeout=4

        )



        return {



            "status":

            "online",



            "dados":

            r.json()

        }



    except Exception as erro:
        pass



        return {



            "status":

            "offline",



            "erro":

            str(erro)

        }



# =========================================================

# HOME

# =========================================================



@app.route('/')



def home():
    pass



    return jsonify({



        "empresa":

        "IOTEC",



        "executive_center":

        "online",



        "modo":

        "presidencia_operacional",



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# CENTRAL

# =========================================================



@app.route('/executive/central')



def central():
    pass



    relatorio = {}



    for nome, url in SERVICOS.items():
        pass



        relatorio[nome] = consultar(url)



    return jsonify({



        "empresa":

        "IOTEC",



        "modo":

        "torre_executiva_global",



        "servicos":

        relatorio,



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# EXECUTIVOS

# =========================================================



@app.route('/executive/executivos')



def executivos():
    pass



    dados = consultar(



        SERVICOS["governanca"]

    )



    return jsonify({



        "executivos":

        dados

    })



# =========================================================

# CRITICOS

# =========================================================



@app.route('/executive/criticos')



def criticos():
    pass



    dados = consultar(



        "http://127.0.0.1:7600/governance/criticos"

    )



    return jsonify({



        "criticos":

        dados

    })



# =========================================================

# ORGANOGRAMA

# =========================================================



@app.route('/executive/organograma')



def organograma():
    pass



    dados = consultar(



        SERVICOS["organograma"]

    )



    return jsonify({



        "organograma":

        dados

    })



# =========================================================

# ALERTAS

# =========================================================



@app.route('/executive/alertas')



def alertas():
    pass



    alertas = []



    for nome, url in SERVICOS.items():
        pass



        consulta = consultar(url)



        if consulta["status"] == "offline":
            pass



            alertas.append({



                "servico":

                nome,



                "problema":

                "offline"

            })



    return jsonify({



        "alertas":

        len(alertas),



        "eventos":

        alertas

    })



# =========================================================

# PRODUCAO

# =========================================================



@app.route('/executive/producao')



def producao():
    pass



    curadoria = consultar(



        SERVICOS["curadoria"]

    )



    consolidacao = consultar(



        SERVICOS["consolidacao"]

    )



    criatividade = consultar(



        SERVICOS["criatividade"]

    )



    return jsonify({



        "curadoria":

        curadoria,



        "consolidacao":

        consolidacao,



        "criatividade":

        criatividade

    })



# =========================================================

# PRESIDENCIA

# =========================================================



@app.route('/executive/presidencia')



def presidencia():
    pass



    governanca = consultar(



        SERVICOS["governanca"]

    )



    gateway = consultar(



        SERVICOS["gateway"]

    )



    organizacao = consultar(



        SERVICOS["organizacao"]

    )



    return jsonify({



        "presidencia":

        "ativa",



        "governanca":

        governanca,



        "gateway":

        gateway,



        "organizacao":

        organizacao,



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# DASHBOARD EXECUTIVO

# =========================================================



@app.route('/executive/dashboard')



def dashboard():
    pass



    central = consultar(



        "http://127.0.0.1:7700/executive/central"

    )



    alertas = consultar(



        "http://127.0.0.1:7700/executive/alertas"

    )



    return jsonify({



        "empresa":

        "IOTEC",



        "modo":

        "cockpit_executivo",



        "central":

        central,



        "alertas":

        alertas,



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# START

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("=" * 70)

    print(" IOTEC EXECUTIVE COMMAND CENTER ")

    print("=" * 70)

    print("")



    app.run(



        host='0.0.0.0',



        port=7700

    )






