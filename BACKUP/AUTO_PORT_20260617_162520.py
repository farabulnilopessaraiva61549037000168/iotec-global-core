import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC AUTO PORT ENGINE

# DETECTOR E CORRETOR AUTOMATICO DE PORTAS

# ============================================================



import socket

from pathlib import Path



# ============================================================

# BASE

# ============================================================



SERVER_PATH = Path(

    "C:/IOTEC_REALTIME_EXECUTIVE_CORE/frontend/server.py"

)



# ============================================================

# PORTAS PARA TESTAR

# ============================================================



PORTAS = [



    8080,

    8090,

    8100,

    8200,

    8300,

    8400,

    8500



]



# ============================================================

# VERIFICAR PORTA

# ============================================================



def porta_livre(porta):
    pass



    with socket.socket(

        socket.AF_INET,

        socket.SOCK_STREAM

    ) as s:



        return s.connect_ex(

            ('127.0.0.1', porta)

        ) != 0



# ============================================================

# ENCONTRAR PORTA

# ============================================================



PORTA_FINAL = None



for porta in PORTAS:
    pass



    if porta_livre(porta):
        pass



        PORTA_FINAL = porta

        break



# ============================================================

# VALIDACAO

# ============================================================



if PORTA_FINAL is None:
    pass



    print()

    print("===================================================")

    print(" ERRO")

    print("===================================================")



    print()

    print("NENHUMA PORTA DISPONIVEL")



    exit()



# ============================================================

# NOVO SERVER

# ============================================================



SERVER = f"""

import http.server

import socketserver

import webbrowser



PORT = {PORTA_FINAL}



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(

    ('', PORT),

    Handler

) as httpd:



    print()

    print('===================================================')

    print(' IOTEC REALTIME EXECUTIVE CORE')

    print('===================================================')



    print()

    print(f'SERVER -> http://localhost:{{PORT}}')



    webbrowser.open(

        f'http://localhost:{{PORT}}'

    )



    httpd.serve_forever()

"""



# ============================================================

# ESCREVER SERVER

# ============================================================



with open(



    SERVER_PATH,

    "w",

    encoding="utf-8"



) as arquivo:



    arquivo.write(SERVER)



# ============================================================

# FINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC AUTO PORT ENGINE")

print("===================================================")



print()

print(f"PORTA LIVRE -> {PORTA_FINAL}")



print()

print("SERVER.py ATUALIZADO")



print()

print("===================================================")

print(" EXECUTAR")

print("===================================================")



print()

print("./INICIAR_FRONTEND.ps1")



print()

print("===================================================")

print(" NUCLEO FINALIZADO")

print("===================================================")




