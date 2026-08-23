import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC ADAPTIVE CORE MANAGER
# GERENCIADOR INTELIGENTE AUTOADAPTATIVO
# =========================================================

import os
import time
import requests
import subprocess
import threading

from flask import Flask, jsonify
from flask_cors import CORS

from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

ROOT = r"C:\IOTEC"

ARQUIVO_NUCLEO = "app.py"

NUCLEO_PATH = os.path.join(

    ROOT,
    ARQUIVO_NUCLEO
)

PORTA_NUCLEO = 5000

URL_NUCLEO = (

    f"http://127.0.0.1:{PORTA_NUCLEO}"
)

# =========================================================
# APP
# =========================================================

app = Flask(__name__)

CORS(app)

# =========================================================
# ESTADO
# =========================================================

ESTADO = {

    "manager":
    "online",

    "nucleo":
    "desconhecido",

    "tipo_detectado":
    None,

    "reinicios":
    0,

    "heartbeat":
    None,

    "ultimo_evento":
    None,

    "porta":
    PORTA_NUCLEO,

    "tipo":
    "adaptive_runtime_manager"
}

# =========================================================
# CACHE
# =========================================================

ULTIMO_COMANDO = None

# =========================================================
# DETECTAR TIPO
# =========================================================

def detectar_tipo():
    pass

    if not os.path.exists(NUCLEO_PATH):
        pass

        return "desconhecido"

    try:
        pass

        with open(

            NUCLEO_PATH,

            "r",

            encoding="utf-8",

            errors="ignore"
        ) as f:

            codigo = f.read().lower()

        # =================================================
        # STREAMLIT
        # =================================================

        if "import streamlit" in codigo:
            pass

            return "streamlit"

        # =================================================
        # FLASK
        # =================================================

        if "from flask import" in codigo:
            pass

            return "flask"

        # =================================================
        # FASTAPI
        # =================================================

        if "from fastapi" in codigo:
            pass

            return "fastapi"

        # =================================================
        # DJANGO
        # =================================================

        if "django" in codigo:
            pass

            return "django"

        return "python"

    except:
        pass

        return "erro"

# =========================================================
# TESTAR ONLINE
# =========================================================

def nucleo_online():
    pass

    try:
        pass

        r = requests.get(

            URL_NUCLEO,

            timeout=3
        )

        return r.status_code == 200

    except:
        pass

        return False

# =========================================================
# GERAR COMANDO
# =========================================================

def gerar_comando(tipo):
    pass

    if tipo == "streamlit":
        pass

        return (

            f'cd /d "{ROOT}" && '
            f'streamlit run {ARQUIVO_NUCLEO} '
            f'--server.port {PORTA_NUCLEO}'
        )

    if tipo == "flask":
        pass

        return (

            f'cd /d "{ROOT}" && '
            f'python {ARQUIVO_NUCLEO}'
        )

    if tipo == "fastapi":
        pass

        return (

            f'cd /d "{ROOT}" && '
            f'uvicorn app:app '
            f'--host 0.0.0.0 '
            f'--port {PORTA_NUCLEO}'
        )

    if tipo == "django":
        pass

        return (

            f'cd /d "{ROOT}" && '
            f'python manage.py runserver '
            f'0.0.0.0:{PORTA_NUCLEO}'
        )

    return (

        f'cd /d "{ROOT}" && '
        f'python {ARQUIVO_NUCLEO}'
    )

# =========================================================
# INICIAR NUCLEO
# =========================================================

def iniciar_nucleo():
    pass

    global ULTIMO_COMANDO

    tipo = detectar_tipo()

    ESTADO["tipo_detectado"] = tipo

    comando = gerar_comando(tipo)

    ULTIMO_COMANDO = comando

    print("")
    print("=" * 60)
    print(" IOTEC ADAPTIVE CORE MANAGER ")
    print("=" * 60)
    print("")
    print(f"TIPO DETECTADO: {tipo}")
    print("")
    print(f"COMANDO:")
    print(comando)
    print("")

    subprocess.Popen(

        comando,

        shell=True
    )

    ESTADO["reinicios"] += 1

    ESTADO["ultimo_evento"] = (

        f"reinicio_{tipo}"
    )

# =========================================================
# LOOP
# =========================================================

def loop():
    pass

    while True:
        pass

        ESTADO["heartbeat"] = (

            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        online = nucleo_online()

        if online:
            pass

            ESTADO["nucleo"] = "online"

        else:
            pass

            ESTADO["nucleo"] = "offline"

            iniciar_nucleo()

            time.sleep(10)

        time.sleep(5)

# =========================================================
# STATUS
# =========================================================

@app.route('/')

def home():
    pass

    return jsonify({

        "adaptive_manager":
        "online"
    })

# =========================================================
# STATUS CORE
# =========================================================

@app.route('/core/status')

def status():
    pass

    return jsonify({

        **ESTADO,

        "ultimo_comando":
        ULTIMO_COMANDO
    })

# =========================================================
# START LOOP
# =========================================================

threading.Thread(

    target=loop,

    daemon=True

).start()

# =========================================================
# START
# =========================================================

if __name__ == '__main__':
    pass

    print("")
    print("=" * 60)
    print(" IOTEC ADAPTIVE CORE MANAGER ")
    print("=" * 60)
    print("")

    app.run(

        host='0.0.0.0',

        port=7100
    )


