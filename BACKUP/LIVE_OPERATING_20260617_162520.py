import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC LIVE OPERATING ECOSYSTEM

# REALTIME DASHBOARD + IA + FEED + GOVERNANCE

# ============================================================



import os

import json

import random

from pathlib import Path

from datetime import datetime



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_OPERATING_ECOSYSTEM"

)



FRONTEND = BASE / "frontend"



API = BASE / "api"



DATA = BASE / "data"



FRONTEND.mkdir(

    parents=True,

    exist_ok=True

)



API.mkdir(

    parents=True,

    exist_ok=True

)



DATA.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# FEED DINAMICO

# ============================================================



EVENTOS = [



    "IA gerou nova aula premium",

    "Novo dashboard operacional ativado",

    "GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a estabilizou o nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo",

    "Streaming premium sincronizado",

    "Nova trilha educacional produzida",

    "Analytics detectou crescimento",

    "Novo conteÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºdo cinematogrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡fico publicado",

    "Sistema de IA iniciou produÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica"



]



MODULOS = [



    "IA_ENGINE",

    "STREAMING",

    "ANALYTICS",

    "GOVERNANCA",

    "PREMIUM_MEDIA",

    "WEBSOCKET"



]



feed = []



for i in range(12):
    pass



    item = {



        "titulo":

        random.choice(EVENTOS),



        "modulo":

        random.choice(MODULOS),



        "usuarios":

        random.randint(

            500,

            50000

        ),



        "timestamp":

        str(datetime.now())



    }



    feed.append(

        item

    )



# ============================================================

# EXPORT FEED

# ============================================================



with open(



    DATA / "feed.json",



    "w",

    encoding="utf-8"



) as f:



    json.dump(

        feed,

        f,

        indent=4,

        ensure_ascii=False

    )



# ============================================================

# INDEX HTML

# ============================================================



index_html = r'''

<!DOCTYPE html>

<html lang="pt-br">



<head>



<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">



<title>IOTEC OPERATING ECOSYSTEM</title>



<link rel="stylesheet" href="style.css">



<link rel="preconnect" href="https://fonts.googleapis.com">



<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">



</head>



<body>



<video autoplay muted loop id="bgvideo">



<source src="https://cdn.coverr.co/videos/coverr-earth-from-space-1560084400887?download=1080p" type="video/mp4">



</video>



<div class="overlay"></div>



<header>



<div class="logo">



IOTEC ECOSYSTEM



</div>



<nav>



<a href="#">INÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂCIO</a>

<a href="#">IA</a>

<a href="#">ANALYTICS</a>

<a href="#">GOVERNANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡A</a>

<a href="#">PREMIUM</a>



</nav>



</header>



<section class="hero">



<h1>



NOVA ERA DA EDUCAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE



</h1>



<p>



Ecossistema operacional vivo alimentado por inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia artificial e governanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a premium.



</p>



<button onclick="entrar()">



ENTRAR NO ECOSSISTEMA



</button>



</section>



<section id="dashboard" class="dashboard hidden">



<div class="metric">



<h2>USUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIOS ONLINE</h2>



<h1 id="usuarios">0</h1>



</div>



<div class="metric">



<h2>CPU</h2>



<h1 id="cpu">0%</h1>



</div>



<div class="metric">



<h2>RAM</h2>



<h1 id="ram">0%</h1>



</div>



<div class="metric">



<h2>MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS</h2>



<h1>ONLINE</h1>



</div>



</section>



<section class="feed-title hidden" id="feed-title">



<h1>



NUCLEO OPERACIONAL



</h1>



<p>



ProduÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica em tempo real.



</p>



</section>



<section id="feed" class="feed hidden">



</section>



<script src="script.js"></script>



</body>



</html>

'''



# ============================================================

# CSS

# ============================================================



style_css = r'''

*{



margin:0;

padding:0;

box-sizing:border-box;



}



body{



font-family:'Inter',sans-serif;

background:black;

color:white;

overflow-x:hidden;



}



#bgvideo{



position:fixed;

right:0;

bottom:0;

min-width:100%;

min-height:100%;

object-fit:cover;

z-index:-3;



}



.overlay{



position:fixed;

width:100%;

height:100%;

background:rgba(0,0,0,0.72);

z-index:-2;



}



header{



position:fixed;

top:0;

width:100%;

display:flex;

justify-content:space-between;

align-items:center;

padding:25px 60px;

backdrop-filter:blur(20px);

background:rgba(0,0,0,0.3);

z-index:100;



}



.logo{



font-size:28px;

font-weight:800;

letter-spacing:4px;



}



nav{



display:flex;

gap:35px;



}



nav a{



text-decoration:none;

color:white;

font-weight:600;



}



.hero{



height:100vh;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

text-align:center;

padding:40px;



}



.hero h1{



font-size:78px;

max-width:1200px;

line-height:1.1;



}



.hero p{



margin-top:30px;

font-size:24px;

opacity:0.8;

max-width:900px;



}



.hero button{



margin-top:40px;

padding:20px 60px;

border:none;

border-radius:20px;

background:white;

color:black;

font-size:18px;

font-weight:800;

cursor:pointer;

transition:0.4s;



}



.hero button:hover{



transform:scale(1.05);



}



.dashboard{



display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:30px;

padding:80px;



}



.metric{



background:rgba(255,255,255,0.07);

backdrop-filter:blur(18px);

padding:40px;

border-radius:28px;

text-align:center;



}



.metric h1{



font-size:52px;

margin-top:15px;



}



.feed-title{



padding:100px 40px;

text-align:center;



}



.feed-title h1{



font-size:60px;



}



.feed-title p{



margin-top:20px;

font-size:22px;

opacity:0.7;



}



.feed{



display:grid;

grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

gap:30px;

padding:60px;



}



.card{



background:rgba(255,255,255,0.07);

backdrop-filter:blur(18px);

padding:35px;

border-radius:28px;

transition:0.4s;



}



.card:hover{



transform:translateY(-8px);



}



.card h2{



font-size:28px;

margin-bottom:20px;



}



.card p{



opacity:0.75;

line-height:1.7;



}



.hidden{



display:none;



}

'''



# ============================================================

# JS

# ============================================================



script_js = r'''

async function carregarFeed(){



const resposta = await fetch('../data/feed.json')



const dados = await resposta.json()



const feed = document.getElementById('feed')



feed.innerHTML = ''



dados.forEach(item=>{



const card = document.createElement('div')



card.className = 'card'



card.innerHTML = `



<h2>${item.titulo}</h2>



<p>



MODULO: ${item.modulo}



</p>



<p>



USUARIOS: ${item.usuarios}



</p>



<p>



${item.timestamp}



</p>



`



feed.appendChild(card)



})



}



function gerarMetricas(){



document.getElementById('usuarios').innerText =



Math.floor(Math.random()*500000)



document.getElementById('cpu').innerText =



Math.floor(Math.random()*70)+'%'



document.getElementById('ram').innerText =



Math.floor(Math.random()*80)+'%'



}



function entrar(){



document.querySelector('.hero').style.display='none'



document.getElementById('dashboard').classList.remove('hidden')



document.getElementById('feed').classList.remove('hidden')



document.getElementById('feed-title').classList.remove('hidden')



gerarMetricas()



carregarFeed()



setInterval(



()=>{



gerarMetricas()

carregarFeed()



},



4000



)



}



console.log(



'IOTEC OPERATING ECOSYSTEM ONLINE'



)

'''



# ============================================================

# SERVER

# ============================================================



server_py = r'''

import http.server

import socketserver

import webbrowser

import os



PORT = 8080



BASE = os.path.dirname(__file__)



os.chdir(BASE)



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(



("", PORT),



Handler



) as httpd:



    print()

    print("===================================================")

    print(" IOTEC OPERATING ECOSYSTEM ONLINE")

    print("===================================================")

    print()

    print(f"http://localhost:{PORT}")

    print()

    print("===================================================")



    webbrowser.open(



    f"http://localhost:{PORT}"



    )



    httpd.serve_forever()

'''



# ============================================================

# POWERSHELL

# ============================================================



ps1 = r'''

cd frontend

python server.py

'''



# ============================================================

# EXPORT

# ============================================================



(FRONTEND / "index.html").write_text(

    index_html,

    encoding="utf-8"

)



(FRONTEND / "style.css").write_text(

    style_css,

    encoding="utf-8"

)



(FRONTEND / "script.js").write_text(

    script_js,

    encoding="utf-8"

)



(FRONTEND / "server.py").write_text(

    server_py,

    encoding="utf-8"

)



(BASE / "INICIAR_OPERATING_ECOSYSTEM.ps1").write_text(

    ps1,

    encoding="utf-8"

)



# ============================================================

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC OPERATING ECOSYSTEM")

print(" LIVE OPERATIONAL PLATFORM")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("PASTAS:")



print(" [+] frontend")

print(" [+] api")

print(" [+] data")



print()

print("ARQUIVOS:")



print(" [+] frontend/index.html")

print(" [+] frontend/style.css")

print(" [+] frontend/script.js")

print(" [+] frontend/server.py")

print(" [+] data/feed.json")

print(" [+] INICIAR_OPERATING_ECOSYSTEM.ps1")



print()

print("===================================================")

print(" EXECUCAO")

print("===================================================")



print()

print("1. ABRIR POWERSHELL")

print()

print("2. EXECUTAR")

print()

print("./INICIAR_OPERATING_ECOSYSTEM.ps1")

print()

print("3. ACESSAR")

print()

print("http://localhost:8080")



print()

print("===================================================")

print(" ECOSSISTEMA OPERACIONAL ONLINE")

print("===================================================")





