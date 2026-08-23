import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC NEXUS CORE

# AUTONOMOUS OPERATION ENGINE

# ============================================================



from pathlib import Path



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_NEXUS_CORE"

)



BASE.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# PASTAS

# ============================================================



PASTAS = [



    "frontend",

    "backend",

    "database",

    "governance",

    "logs",

    "storage"



]



for pasta in PASTAS:
    pass



    (

        BASE / pasta

    ).mkdir(



        parents=True,

        exist_ok=True



    )



# ============================================================

# HTML

# ============================================================



HTML = """

<!DOCTYPE html>



<html lang="en">



<head>



<meta charset="UTF-8">



<meta name="viewport"

content="width=device-width, initial-scale=1.0">



<title>

IOTEC NEXUS CORE

</title>



<link rel="stylesheet"

href="style.css">



</head>



<body>



<div class="overlay"></div>



<header>



<h1>

IOTEC NEXUS CORE

</h1>



<p>

AUTONOMOUS OPERATION ENGINE

</p>



</header>



<section class="dashboard">



<div class="card">



<h2>CPU</h2>



<div id="cpu">

0%

</div>



</div>



<div class="card">



<h2>RAM</h2>



<div id="ram">

0%

</div>



</div>



<div class="card">



<h2>LATENCY</h2>



<div id="latency">

0ms

</div>



</div>



<div class="card">



<h2>USERS</h2>



<div id="users">

0

</div>



</div>



</section>



<section class="modules">



<div class="module online">

ACROPOLE

</div>



<div class="module online">

IA ENGINE

</div>



<div class="module online">

ANALYTICS

</div>



<div class="module hibernate">

STREAMING

</div>



<div class="module online">

GOVERNANCE

</div>



</section>



<script src="script.js"></script>



</body>

</html>

"""



# ============================================================

# CSS

# ============================================================



CSS = """



body{



    margin:0;

    padding:0;



    background:

    url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1920')

    center/cover fixed;



    font-family:Arial;



    color:white;



}



.overlay{



    position:fixed;



    width:100%;

    height:100%;



    background:

    rgba(0,0,0,0.72);



    backdrop-filter:

    blur(7px);



}



header{



    position:relative;



    z-index:2;



    text-align:center;



    padding:60px;



}



header h1{



    font-size:60px;



    letter-spacing:4px;



}



.dashboard{



    position:relative;



    z-index:2;



    display:grid;



    grid-template-columns:

    repeat(auto-fit,minmax(250px,1fr));



    gap:30px;



    padding:40px;



}



.card{



    background:

    rgba(255,255,255,0.08);



    border:

    1px solid rgba(255,255,255,0.15);



    border-radius:25px;



    padding:40px;



    backdrop-filter:

    blur(12px);



    text-align:center;



}



.card div{



    font-size:50px;



    font-weight:bold;



}



.modules{



    position:relative;



    z-index:2;



    display:flex;



    flex-wrap:wrap;



    justify-content:center;



    gap:20px;



    padding:40px;



}



.module{



    padding:18px 35px;



    border-radius:50px;



    font-weight:bold;



    letter-spacing:2px;



}



.online{



    background:

    rgba(0,255,120,0.2);



    border:

    1px solid rgba(0,255,120,0.4);



}



.hibernate{



    background:

    rgba(255,170,0,0.2);



    border:

    1px solid rgba(255,170,0,0.4);



}



"""



# ============================================================

# JAVASCRIPT

# ============================================================



JS = """



function rand(min,max){



    return Math.floor(

        Math.random()*(max-min+1)+min

    )



}



function update(){



    document

    .getElementById('cpu')

    .innerHTML =

    rand(10,55)+'%'



    document

    .getElementById('ram')

    .innerHTML =

    rand(65,92)+'%'



    document

    .getElementById('latency')

    .innerHTML =

    rand(20,220)+'ms'



    document

    .getElementById('users')

    .innerHTML =

    rand(1000,50000)



}



setInterval(

    update,

    2000

)



update()



"""



# ============================================================

# SERVER

# ============================================================



SERVER = """



import http.server

import socketserver

import webbrowser



PORT = 9999



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(



    ("", PORT),

    Handler



) as httpd:



    print()

    print("===================================")

    print(" IOTEC NEXUS CORE")

    print("===================================")



    print()

    print(

        "SERVER -> http://localhost:9999"

    )



    webbrowser.open(

        "http://localhost:9999"

    )



    httpd.serve_forever()



"""



# ============================================================

# GOVERNANCE

# ============================================================



GOVERNANCE = """



import psutil

import json

import time

from pathlib import Path

from datetime import datetime



BASE = Path(

    "C:/IOTEC_NEXUS_CORE/logs"

)



BASE.mkdir(

    parents=True,

    exist_ok=True

)



while True:
    pass



    data = {



        "cpu":

        psutil.cpu_percent(),



        "ram":

        psutil.virtual_memory().percent,



        "timestamp":

        str(datetime.now())



    }



    with open(



        BASE / "live_metrics.json",



        "w",

        encoding="utf-8"



    ) as f:



        json.dump(

            data,

            f,

            indent=4

        )



    print()

    print("===================================")



    print(

        f"CPU -> {data['cpu']}%"

    )



    print(

        f"RAM -> {data['ram']}%"

    )



    time.sleep(5)



"""



# ============================================================

# POWERSHELL

# ============================================================



PS1 = """



Start-Process powershell -ArgumentList "python governance/governance.py"



Start-Sleep -Seconds 2



cd frontend



python server.py



"""



# ============================================================

# EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



with open(



    BASE / "frontend" / "index.html",



    "w",

    encoding="utf-8"



) as f:



    f.write(HTML)



with open(



    BASE / "frontend" / "style.css",



    "w",

    encoding="utf-8"



) as f:



    f.write(CSS)



with open(



    BASE / "frontend" / "script.js",



    "w",

    encoding="utf-8"



) as f:



    f.write(JS)



with open(



    BASE / "frontend" / "server.py",



    "w",

    encoding="utf-8"



) as f:



    f.write(SERVER)



with open(



    BASE / "governance" / "governance.py",



    "w",

    encoding="utf-8"



) as f:



    f.write(GOVERNANCE)



with open(



    BASE / "INICIAR_NEXUS.ps1",



    "w",

    encoding="utf-8"



) as f:



    f.write(PS1)



# ============================================================

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC NEXUS CORE")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("PASTAS:")



for pasta in PASTAS:
    pass



    print(f" [+] {pasta}")



print()

print("ARQUIVOS:")



print(" [+] index.html")

print(" [+] style.css")

print(" [+] script.js")

print(" [+] server.py")

print(" [+] governance.py")

print(" [+] INICIAR_NEXUS.ps1")



print()

print("===================================================")

print(" EXECUCAO")

print("===================================================")



print()

print("1. ABRIR POWERSHELL")



print()

print("2. EXECUTAR")



print()

print("./INICIAR_NEXUS.ps1")



print()

print("3. ACESSAR")



print()

print("http://localhost:9999")



print()

print("===================================================")

print(" NUCLEO AUTONOMO ONLINE")

print("===================================================")







