import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC CORE MANAGER
# PROTECAO PERMANENTE DO NUCLEO
# =========================================================

import requests

import subprocess

import threading

import time

import os

from datetime import datetime

from flask import Flask, jsonify

from flask_cors import CORS

# =========================================================
# CONFIG
# =========================================================

NUCLEO_URL = "http://127.0.0.1:5000"

NUCLEO_PORTA = 5000

NUCLEO_ARQUIVO = "app.py"

ROOT = r"C:\IOTEC"

# =========================================================
# APP
# =========================================================

app = Flask(__name__)

CORS(app)

# =========================================================
# ESTADO
# =========================================================

ESTADO = {

    "core_manager":
    "online",

    "nucleo":
    "desconhecido",

    "reinicios":
    0,

    "heartbeat":
    None,

    "ultimo_evento":
    None,

    "uptime":
    "0s",

    "porta":
    5000,

    "tipo":
    "gerenciador_permanente_nucleo"
}

# =========================================================
# TEMPO
# =========================================================

START = time.time()

# =========================================================
# VERIFICAR NUCLEO
# =========================================================

def nucleo_online():
    pass

    try:
        pass

        r = requests.get(

            NUCLEO_URL,

            timeout=2
        )

        return r.status_code == 200

    except:
        pass

        return False

# =========================================================
# SUBIR NUCLEO
# =========================================================

def iniciar_nucleo():
    pass

    print("")
    print("=" * 60)
    print(" REINICIANDO NUCLEO ")
    print("=" * 60)
    print("")

    subprocess.Popen(

        f'cd /d {ROOT} && python {NUCLEO_ARQUIVO}',

        shell=True
    )

    ESTADO["reinicios"] += 1

    ESTADO["ultimo_evento"] = (

        "nucleo_reiniciado"
    )

# =========================================================
# LOOP
# =========================================================

def loop_nucleo():
    pass

    while True:
        pass

        online = nucleo_online()

        uptime_segundos = int(

            time.time() - START
        )

        ESTADO["uptime"] = (

            f"{uptime_segundos}s"
        )

        ESTADO["heartbeat"] = (

            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        if online:
            pass

            ESTADO["nucleo"] = "online"

        else:
            pass

            ESTADO["nucleo"] = "offline"

            iniciar_nucleo()

        time.sleep(5)

# =========================================================
# STATUS
# =========================================================

@app.route('/')

def home():
    pass

    return jsonify({

        "core_manager":
        "online"
    })

# =========================================================
# STATUS CORE
# =========================================================

@app.route('/core/status')

def status():
    pass

    return jsonify(ESTADO)

# =========================================================
# START THREAD
# =========================================================

threading.Thread(

    target=loop_nucleo,

    daemon=True

).start()

# =========================================================
# START
# =========================================================

if __name__ == '__main__':
    pass

    print("")
    print("=" * 60)
    print(" IOTEC CORE MANAGER ")
    print("=" * 60)
    print("")

    app.run(

        host='0.0.0.0',

        port=7100
    )


