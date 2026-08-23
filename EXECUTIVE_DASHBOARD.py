import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC EXECUTIVE DASHBOARD ENGINE

# ENTERPRISE CONTROL CENTER

# ============================================================



import json

import random

from pathlib import Path

from datetime import datetime



# ============================================================

# BASE

# ============================================================



BASE = Path("C:/IOTEC_EXECUTIVE_DASHBOARD")



# ============================================================

# PASTAS

# ============================================================



PASTAS = [



    BASE,

    BASE / "frontend",

    BASE / "backend",

    BASE / "database",

    BASE / "assets",

    BASE / "exports",

    BASE / "logs"



]



for pasta in PASTAS:
    pass



    pasta.mkdir(

        parents=True,

        exist_ok=True

    )



# ============================================================

# DATABASE SIMULADA

# ============================================================



DADOS = {



    "empresa": {



        "nome": "IOTEC GLOBAL REALTY",

        "cnpj": "61.549.037/0001-68",

        "email": "iotec.bl@proton.me"



    },



    "receita_global_usd": 1834920,



    "operacoes": [



        {



            "pais": "Estados Unidos",

            "cidade": "Miami",

            "tipo": "Luxury",

            "ticket": 82000



        },



        {



            "pais": "Europa",

            "cidade": "Amsterdam",

            "tipo": "Port Logistics",

            "ticket": 128000



        },



        {



            "pais": "Brasil",

            "cidade": "SÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Paulo",

            "tipo": "Commercial",

            "ticket": 34000



        }



    ]



}



# ============================================================

# EXPORT DATABASE

# ============================================================



with open(



    BASE / "database/dashboard_data.json",

    "w",

    encoding="utf-8"



) as arquivo:



    json.dump(



        DADOS,

        arquivo,

        indent=4,

        ensure_ascii=False



    )



# ============================================================

# INDEX HTML

# ============================================================



INDEX = """

<!DOCTYPE html>



<html lang="en">



<head>



<meta charset="UTF-8">



<meta name="viewport"

content="width=device-width, initial-scale=1.0">



<title>IOTEC EXECUTIVE DASHBOARD</title>



<link

rel="stylesheet"

href="style.css">



</head>



<body>



<div class="background"></div>



<div class="layout">



    <aside class="sidebar">



        <h1>IOTEC</h1>



        <div class="menu">



            <button>GLOBAL</button>

            <button>ANALYTICS</button>

            <button>CLIENTS</button>

            <button>TICKETS</button>

            <button>SECURITY</button>

            <button>MONITOR</button>



        </div>



    </aside>



    <main class="main">



        <header class="topbar">



            <div>



                <h2>

                    EXECUTIVE CONTROL CENTER

                </h2>



                <p>

                    Global Realty Operations

                </p>



            </div>



            <div class="company">



                IOTEC GLOBAL REALTY



            </div>



        </header>



        <section class="cards">



            <div class="card">



                <h3>

                    GLOBAL REVENUE

                </h3>



                <h1>

                    US$ 1.834.920

                </h1>



            </div>



            <div class="card">



                <h3>

                    ACTIVE CLIENTS

                </h3>



                <h1>

                    128

                </h1>



            </div>



            <div class="card">



                <h3>

                    ACTIVE OPERATIONS

                </h3>



                <h1>

                    42

                </h1>



            </div>



        </section>



        <section class="operations">



            <div class="table">



                <h2>

                    GLOBAL OPERATIONS

                </h2>



                <table>



                    <tr>



                        <th>Country</th>

                        <th>City</th>

                        <th>Sector</th>

                        <th>Ticket</th>



                    </tr>



                    <tr>



                        <td>USA</td>

                        <td>Miami</td>

                        <td>Luxury</td>

                        <td>US$ 82.000</td>



                    </tr>



                    <tr>



                        <td>Europe</td>

                        <td>Amsterdam</td>

                        <td>Port Logistics</td>

                        <td>US$ 128.000</td>



                    </tr>



                    <tr>



                        <td>Brazil</td>

                        <td>SÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Paulo</td>

                        <td>Commercial</td>

                        <td>US$ 34.000</td>



                    </tr>



                </table>



            </div>



            <div class="map">



                <h2>

                    GLOBAL MAP

                </h2>



                <div class="mapbox">



                    WORLD OPERATIONS MAP



                </div>



            </div>



        </section>



    </main>



</div>



</body>



</html>

"""



# ============================================================

# STYLE CSS

# ============================================================



STYLE = """

* {



    margin: 0;

    padding: 0;

    box-sizing: border-box;



}



body {



    background: #050505;

    color: white;

    font-family: Arial;

    overflow: hidden;



}



.background {



    position: fixed;



    width: 100%;

    height: 100%;



    background:



    radial-gradient(

        circle at top left,

        rgba(0,140,255,0.18),

        transparent 30%

    ),



    radial-gradient(

        circle at bottom right,

        rgba(0,255,200,0.12),

        transparent 30%

    );



    z-index: -1;



}



.layout {



    display: flex;

    width: 100vw;

    height: 100vh;



}



.sidebar {



    width: 260px;



    background: rgba(15,15,15,0.92);



    border-right:

    1px solid rgba(255,255,255,0.08);



    padding: 30px;



    backdrop-filter: blur(20px);



}



.sidebar h1 {



    font-size: 34px;

    margin-bottom: 40px;



}



.menu {



    display: flex;

    flex-direction: column;

    gap: 16px;



}



.menu button {



    background: rgba(255,255,255,0.04);



    border: none;



    color: white;



    padding: 18px;



    border-radius: 14px;



    cursor: pointer;



    transition: 0.3s;



}



.menu button:hover {



    background: rgba(0,140,255,0.25);



}



.main {



    flex: 1;

    padding: 30px;



}



.topbar {



    display: flex;

    justify-content: space-between;

    align-items: center;



    margin-bottom: 30px;



}



.topbar h2 {



    font-size: 38px;



}



.topbar p {



    opacity: 0.7;

    margin-top: 8px;



}



.company {



    background: rgba(255,255,255,0.04);



    padding: 14px 24px;



    border-radius: 14px;



}



.cards {



    display: flex;

    gap: 20px;



    margin-bottom: 30px;



}



.card {



    flex: 1;



    background: rgba(255,255,255,0.04);



    border:

    1px solid rgba(255,255,255,0.08);



    padding: 30px;



    border-radius: 22px;



    backdrop-filter: blur(18px);



}



.card h3 {



    opacity: 0.7;

    margin-bottom: 16px;



}



.card h1 {



    font-size: 42px;



}



.operations {



    display: flex;

    gap: 20px;



    height: 60vh;



}



.table {



    flex: 1.2;



    background: rgba(255,255,255,0.04);



    border:

    1px solid rgba(255,255,255,0.08);



    border-radius: 22px;



    padding: 24px;



}



.table h2 {



    margin-bottom: 20px;



}



table {



    width: 100%;

    border-collapse: collapse;



}



th, td {



    padding: 18px;

    text-align: left;



}



tr {



    border-bottom:

    1px solid rgba(255,255,255,0.06);



}



.map {



    flex: 1;



    background: rgba(255,255,255,0.04);



    border:

    1px solid rgba(255,255,255,0.08);



    border-radius: 22px;



    padding: 24px;



}



.mapbox {



    margin-top: 20px;



    width: 100%;

    height: 88%;



    border-radius: 20px;



    background:



    linear-gradient(

        135deg,

        rgba(0,140,255,0.25),

        rgba(0,255,200,0.08)

    );



    display: flex;



    justify-content: center;

    align-items: center;



    font-size: 22px;



}

"""



# ============================================================

# START SERVER

# ============================================================



SERVER = """

import http.server

import socketserver

import webbrowser



PORT = 8080



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(

    ('', PORT),

    Handler

) as httpd:



    print()

    print('===================================================')

    print(' IOTEC EXECUTIVE DASHBOARD')

    print('===================================================')



    print()

    print(f'SERVER -> http://localhost:{PORT}')



    webbrowser.open(

        f'http://localhost:{PORT}'

    )



    httpd.serve_forever()

"""



# ============================================================

# EXPORT

# ============================================================



with open(



    BASE / "frontend/index.html",

    "w",

    encoding="utf-8"



) as arquivo:



    arquivo.write(INDEX)



# ============================================================



with open(



    BASE / "frontend/style.css",

    "w",

    encoding="utf-8"



) as arquivo:



    arquivo.write(STYLE)



# ============================================================



with open(



    BASE / "frontend/server.py",

    "w",

    encoding="utf-8"



) as arquivo:



    arquivo.write(SERVER)



# ============================================================

# START PS1

# ============================================================



PS1 = f'''

cd "{BASE / "frontend"}"



python server.py

'''



with open(



    BASE / "INICIAR_DASHBOARD.ps1",

    "w",

    encoding="utf-8"



) as arquivo:



    arquivo.write(PS1)



# ============================================================

# FINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC EXECUTIVE DASHBOARD")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("PASTAS:")



for pasta in PASTAS:
    pass



    print(f" [+] {pasta.name}")



print()

print("ARQUIVOS:")



print(" [+] dashboard_data.json")

print(" [+] index.html")

print(" [+] style.css")

print(" [+] server.py")

print(" [+] INICIAR_DASHBOARD.ps1")



print()

print("===================================================")

print(" EXECUCAO")

print("===================================================")



print()

print("1. ABRIR POWERSHELL")



print()

print("2. EXECUTAR:")



print()

print("./INICIAR_DASHBOARD.ps1")



print()

print("===================================================")

print(" DASHBOARD FINALIZADO")

print("===================================================")







