import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# -*- coding: utf-8 -*-



import os

import subprocess

import webbrowser

import time



BASE = r"C:\IOTEC_OMEGA_X"



API_PATH = os.path.join(BASE, "CORE", "api")

FRONTEND_PATH = os.path.join(BASE, "frontend")



print("\n====================================")

print(" IOTEC OMEGA X BOOT SEQUENCE")

print("====================================\n")



print("[1] Iniciando API...")



api_process = subprocess.Popen(

    [

        "python",

        "-m",

        "uvicorn",

        "server:app",

        "--host",

        "127.0.0.1",

        "--port",

        "8000",

        "--reload"

    ],

    cwd=API_PATH

)



time.sleep(5)



print("[2] Iniciando Frontend...")



frontend_process = subprocess.Popen(

    [

        "python",

        "-m",

        "http.server",

        "5500"

    ],

    cwd=FRONTEND_PATH

)



time.sleep(3)



print("[3] Abrindo ecossistema...")



webbrowser.open(

    "http://127.0.0.1:5500/public_demo/index.html"

)



time.sleep(2)



print("[4] Abrindo torre de controle...")



webbrowser.open(

    "http://127.0.0.1:8000/api/orders"

)



print("\n====================================")

print(" NUCLEO OPERACIONAL ONLINE")

print("====================================\n")



print("Frontend: ONLINE")

print("API: ONLINE")

print("Tower: ONLINE")

print("Convergencia: ATIVA")

print("\nAperte CTRL+C para encerrar.\n")



try:
    pass

    while True:
        pass

        time.sleep(1)



except KeyboardInterrupt:
    pass



    print("\nEncerrando nucleo...\n")



    api_process.kill()

    frontend_process.kill()



    print("Nucleo encerrado.")




