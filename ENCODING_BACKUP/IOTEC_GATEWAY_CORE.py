import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC GATEWAY CORE
# CEREBRO CENTRAL OPERACIONAL
# =========================================================

from flask import Flask, jsonify, request

from flask_cors import CORS

import requests

from datetime import datetime

# =========================================================
# APP
# =========================================================

app = Flask(__name__)

CORS(app)

# =========================================================
# MODULOS
# =========================================================

MODULOS = {

    "watcher": {

        "url":
        "http://127.0.0.1:5001/watcher/status",

        "porta":
        5001
    },

    "observer": {

        "url":
        "http://127.0.0.1:5020/observer/status",

        "porta":
        5020
    },

    "traffic": {

        "url":
        "http://127.0.0.1:5050/traffic/status",

        "porta":
        5050
    },

    "nucleo": {

        "url":
        "http://127.0.0.1:5000",

        "porta":
        5000
    }
}

# =========================================================
# CACHE CENTRAL
# =========================================================

CACHE = {}

# =========================================================
# STATUS
# =========================================================

@app.route('/')

def home():
    pass

    return jsonify({

        "gateway":
        "online",

        "tipo":
        "gateway_operacional_iotec",

        "modulos":
        list(MODULOS.keys()),

        "timestamp":
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })

# =========================================================
# HEALTH
# =========================================================

@app.route('/gateway/health')

def health():
    pass

    resultado = {}

    for nome, dados in MODULOS.items():
        pass

        try:
            pass

            r = requests.get(

                dados["url"],

                timeout=2
            )

            resultado[nome] = {

                "status":
                "online",

                "http":
                r.status_code
            }

        except Exception as erro:
            pass

            resultado[nome] = {

                "status":
                "offline",

                "erro":
                str(erro)
            }

    return jsonify({

        "gateway":
        "ativo",

        "modulos":
        resultado,

        "timestamp":
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })

# =========================================================
# FETCH CENTRALIZADO
# =========================================================

@app.route('/gateway/modulo/<nome>')

def modulo(nome):
    pass

    if nome not in MODULOS:
        pass

        return jsonify({

            "erro":
            "modulo_inexistente"
        }), 404

    dados = MODULOS[nome]

    try:
        pass

        r = requests.get(

            dados["url"],

            timeout=3
        )

        resposta = r.json()

        CACHE[nome] = resposta

        return jsonify({

            "gateway":
            "roteamento_ok",

            "modulo":
            nome,

            "dados":
            resposta
        })

    except Exception as erro:
        pass

        return jsonify({

            "gateway":
            "falha",

            "modulo":
            nome,

            "erro":
            str(erro),

            "cache":
            CACHE.get(nome, {})
        })

# =========================================================
# STATUS GLOBAL
# =========================================================

@app.route('/gateway/ecossistema')

def ecossistema():
    pass

    status = {}

    online = 0

    offline = 0

    for nome, dados in MODULOS.items():
        pass

        try:
            pass

            r = requests.get(

                dados["url"],

                timeout=2
            )

            status[nome] = {

                "status":
                "online",

                "http":
                r.status_code
            }

            online += 1

        except:
            pass

            status[nome] = {

                "status":
                "offline"
            }

            offline += 1

    return jsonify({

        "gateway":
        "operacional",

        "online":
        online,

        "offline":
        offline,

        "modulos":
        status,

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
    print("=" * 60)
    print(" IOTEC GATEWAY CORE ")
    print("=" * 60)
    print("")

    app.run(

        host='0.0.0.0',

        port=7000
    )


