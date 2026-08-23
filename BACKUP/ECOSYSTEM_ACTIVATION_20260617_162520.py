import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC ECOSYSTEM ACTIVATION ENGINE

# LIVE CONTENT + PREMIUM SECTORS + AUTO FEED

# ============================================================



import json

import random

from pathlib import Path

from datetime import datetime



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_ECOSYSTEM_ENGINE"

)



FRONTEND = BASE / "frontend"



CONTENT = BASE / "content"



FRONTEND.mkdir(

    parents=True,

    exist_ok=True

)



CONTENT.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# CONTEUDOS AUTOMATICOS

# ============================================================



AULAS = [



    "A Nova Era da InteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia Artificial",

    "EducaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o CinemÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica e Imersiva",

    "Plataformas Inteligentes e GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a",

    "Pensamento EstratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gico Digital",

    "Futuro da EducaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Premium"



]



INSIGHTS = [



    "Crescimento de engajamento detectado",

    "IA produziu novos conteÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºdos premium",

    "Streaming otimizado para baixa latÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia",

    "Novos mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³dulos ativados",

    "Ecossistema operacional estabilizado"



]



VIDEOS = [



    "https://cdn.coverr.co/videos/coverr-earth-from-space-1560084400887?download=1080p",

    "https://cdn.coverr.co/videos/coverr-working-on-a-computer-5176?download=1080p"



]



IMAGENS = [



    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",

    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",

    "https://images.unsplash.com/photo-1498050108023-c5249f4df085"



]



# ============================================================

# GERAR CONTEUDO

# ============================================================



conteudos = []



for i in range(8):
    pass



    item = {



        "titulo":

        random.choice(AULAS),



        "insight":

        random.choice(INSIGHTS),



        "imagem":

        random.choice(IMAGENS),



        "video":

        random.choice(VIDEOS),



        "timestamp":

        str(datetime.now())



    }



    conteudos.append(

        item

    )



# ============================================================

# EXPORTAR JSON

# ============================================================



with open(



    CONTENT / "feed.json",



    "w",

    encoding="utf-8"



) as f:



    json.dump(

        conteudos,

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



<title>ACROPOLE ECOSYSTEM</title>



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



ACROPOLE ECOSYSTEM



</div>



<nav>



<a href="#">INÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂCIO</a>

<a href="#">IA</a>

<a href="#">GOVERNANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡A</a>

<a href="#">STREAMING</a>

<a href="#">PREMIUM</a>



</nav>



</header>



<section class="hero">



<h1>



NOVA ERA DA EDUCAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE



</h1>



<p>



Uma plataforma viva alimentada por inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia artificial, automaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e governanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a premium.



</p>



<button onclick="entrar()">



ENTRAR NO ECOSSISTEMA



</button>



</section>



<section class="feed-title">



<h1>



ECOSSISTEMA VIVO



</h1>



<p>



ConteÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºdo sendo produzido automaticamente pelo nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo.



</p>



</section>



<section id="feed" class="feed">



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

background:rgba(0,0,0,0.3);

backdrop-filter:blur(20px);

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



.feed-title{



padding:120px 40px;

text-align:center;



}



.feed-title h1{



font-size:58px;

margin-bottom:20px;



}



.feed-title p{



font-size:22px;

opacity:0.7;



}



.feed{



display:grid;

grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

gap:35px;

padding:60px;



}



.card{



background:rgba(255,255,255,0.06);

backdrop-filter:blur(18px);

border-radius:28px;

overflow:hidden;

border:1px solid rgba(255,255,255,0.08);

transition:0.4s;



}



.card:hover{



transform:translateY(-10px);



}



.card img{



width:100%;

height:220px;

object-fit:cover;



}



.card-content{



padding:30px;



}



.card h2{



font-size:28px;

margin-bottom:20px;



}



.card p{



opacity:0.75;

line-height:1.7;



}



::-webkit-scrollbar{



width:10px;



}



::-webkit-scrollbar-thumb{



background:white;

border-radius:10px;



}

'''



# ============================================================

# JS

# ============================================================



script_js = r'''

async function carregarFeed(){



const resposta = await fetch('../content/feed.json')



const dados = await resposta.json()



const feed = document.getElementById('feed')



dados.forEach(item=>{



const card = document.createElement('div')



card.className = 'card'



card.innerHTML = `



<img src="${item.imagem}">



<div class="card-content">



<h2>${item.titulo}</h2>



<p>${item.insight}</p>



</div>



`



feed.appendChild(card)



})



}



function entrar(){



alert(



'ECOSSISTEMA PREMIUM ONLINE'



)



}



carregarFeed()

'''



# ============================================================

# SERVER

# ============================================================



server_py = r'''

import http.server

import socketserver

import webbrowser

import os



PORT = 9999



BASE = os.path.dirname(__file__)



os.chdir(BASE)



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(



("", PORT),



Handler



) as httpd:



    print()

    print("===================================================")

    print(" ACROPOLE ECOSYSTEM ONLINE")

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

# EXPORTACAO

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



(BASE / "INICIAR_ECOSYSTEM.ps1").write_text(

    ps1,

    encoding="utf-8"

)



# ============================================================

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC ECOSYSTEM ACTIVATION")

print(" LIVE PREMIUM ECOSYSTEM")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("PASTAS:")



print(" [+] frontend")

print(" [+] content")



print()

print("ARQUIVOS:")



print(" [+] frontend/index.html")

print(" [+] frontend/style.css")

print(" [+] frontend/script.js")

print(" [+] frontend/server.py")

print(" [+] content/feed.json")

print(" [+] INICIAR_ECOSYSTEM.ps1")



print()

print("===================================================")

print(" EXECUCAO")

print("===================================================")



print()

print("1. ABRIR POWERSHELL")

print()

print("2. EXECUTAR")

print()

print("./INICIAR_ECOSYSTEM.ps1")

print()

print("3. ACESSAR")

print()

print("http://localhost:9999")



print()

print("===================================================")

print(" ECOSSISTEMA PREMIUM ONLINE")

print("===================================================")





