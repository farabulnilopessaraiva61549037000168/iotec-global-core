import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC OMEGA CORE - CINEMATIC ENTERPRISE ENGINE

# VERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O: ULTRA PREMIUM 7.0

# ============================================================



"""

OBJETIVO:



TRANSFORMAR O FRONTEND EM:



- EXPERIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIA ENTERPRISE CINEMATOGRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂFICA

- ECOSSISTEMA VISUAL OPERACIONAL

- HUB AUDIOVISUAL CORPORATIVO

- PORTAL INTERATIVO GLOBAL

- INTERFACE PREMIUM REAL

- AMBIENTE MULTIMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDIA VIVO



============================================================



ESTE SCRIPT:



ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" cria estrutura enterprise

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" baixa bibliotecas necessÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rias

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" cria vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­deos fallback

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" corrige botÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" ativa mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³dulos

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" adiciona fundo Terra espacial

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" cria formulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios inteligentes

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" ativa animaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" cria navegaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" liga cards

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" adiciona glow premium

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" adiciona vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­deos corporativos

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" organiza assets

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" prepara ambiente web



============================================================

"""



# ============================================================

# IMPORTS

# ============================================================



import os

import subprocess

import textwrap



# ============================================================

# PASTA BASE

# ============================================================



BASE = r"C:\IOTEC_OMEGA_ULTRA"



FRONTEND = os.path.join(BASE, "frontend")

ASSETS = os.path.join(FRONTEND, "assets")

VIDEOS = os.path.join(ASSETS, "videos")

IMAGES = os.path.join(ASSETS, "images")



# ============================================================

# CRIAR ESTRUTURA

# ============================================================



pastas = [



    BASE,

    FRONTEND,

    ASSETS,

    VIDEOS,

    IMAGES



]



for pasta in pastas:
    pass



    os.makedirs(pasta, exist_ok=True)



# ============================================================

# HTML PRINCIPAL

# ============================================================



html = r"""

<!DOCTYPE html>

<html lang="en">



<head>



<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">



<title>IOTEC OMEGA CORE</title>



<link rel="stylesheet" href="style.css">



</head>



<body>



<!-- ===================================================== -->

<!-- HERO -->

<!-- ===================================================== -->



<section class="hero">



<div class="earth-overlay"></div>



<div class="hero-content">



<h1>

GLOBAL <br>

ENTERPRISE <br>

INTELLIGENCE

</h1>



<p>

Luxury operational ecosystem for realty, analytics,

governance, streaming and enterprise intelligence.

</p>



<div class="top-buttons">



<button onclick="abrirModulo('realty')">

REALTY

</button>



<button onclick="abrirModulo('analytics')">

ANALYTICS

</button>



<button onclick="abrirModulo('governance')">

GOVERNANCE

</button>



<button onclick="abrirModulo('streaming')">

STREAMING

</button>



</div>



</div>



</section>



<!-- ===================================================== -->

<!-- MODULES -->

<!-- ===================================================== -->



<section class="modules">



<h2>Enterprise Modules</h2>



<div class="cards">



<div class="card" onclick="abrirModulo('realty')">



<img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200&auto=format&fit=crop">



<div class="card-content">



<h3>Luxury Realty</h3>



<p>

Global premium real estate infrastructure with luxury intelligence.

</p>



</div>



</div>



<div class="card" onclick="abrirModulo('analytics')">



<img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop">



<div class="card-content">



<h3>Operational Analytics</h3>



<p>

Predictive operational intelligence with enterprise monitoring.

</p>



</div>



</div>



<div class="card" onclick="abrirModulo('governance')">



<img src="https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?q=80&w=1200&auto=format&fit=crop">



<div class="card-content">



<h3>Global Governance</h3>



<p>

Security, traceability, compliance and monitoring.

</p>



</div>



</div>



</div>



</section>



<!-- ===================================================== -->

<!-- STREAMING -->

<!-- ===================================================== -->



<section class="streaming">



<h2>Corporate Streaming</h2>



<div class="video-grid">



<div class="video-card">



<video autoplay muted loop playsinline controls>



<source

src="https://www.w3schools.com/html/mov_bbb.mp4"

type="video/mp4">



</video>



<div class="video-info">



<h3>Global Expansion</h3>



<p>

Enterprise infrastructure operations.

</p>



</div>



</div>



<div class="video-card">



<video autoplay muted loop playsinline controls>



<source

src="https://www.w3schools.com/html/movie.mp4"

type="video/mp4">



</video>



<div class="video-info">



<h3>Executive Intelligence</h3>



<p>

Luxury operational ecosystem.

</p>



</div>



</div>



</div>



</section>



<!-- ===================================================== -->

<!-- LIVE ANALYTICS -->

<!-- ===================================================== -->



<section class="analytics-live">



<h2>Live Analytics</h2>



<div class="stats">



<div class="stat">



<h3>US$ 8.4M</h3>

<p>Operational Projection</p>



</div>



<div class="stat">



<h3>94%</h3>

<p>Strategic Confidence</p>



</div>



<div class="stat">



<h3>GLOBAL</h3>

<p>Enterprise Infrastructure</p>



</div>



<div class="stat">



<h3>24/7</h3>

<p>Operational Monitoring</p>



</div>



</div>



</section>



<!-- ===================================================== -->

<!-- CONTACT -->

<!-- ===================================================== -->



<section class="contact">



<h2>Enterprise Contact</h2>



<form class="contact-form">



<input type="text" placeholder="Company Name">



<input type="email" placeholder="Business Email">



<textarea

placeholder="Describe your project, infrastructure or operational need">

</textarea>



<button type="submit">

SEND REQUEST

</button>



</form>



<div class="contact-info">



<p>

CONTACT:

</p>



<p>

iotec.bl@proton.me

</p>



</div>



</section>



<!-- ===================================================== -->

<!-- MODAL -->

<!-- ===================================================== -->



<div id="modal" class="modal">



<div class="modal-content">



<span class="close" onclick="fecharModal()">

ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â

</span>



<div id="modal-body"></div>



</div>



</div>



<script src="script.js"></script>



</body>

</html>

"""



# ============================================================

# CSS

# ============================================================



css = r"""

*{

margin:0;

padding:0;

box-sizing:border-box;

font-family:Arial;

}



body{

background:#060816;

color:white;

overflow-x:hidden;

}



.hero{

position:relative;

min-height:100vh;

display:flex;

align-items:center;

padding:80px;

background:

linear-gradient(

rgba(0,0,0,0.65),

rgba(0,0,0,0.85)

),

url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072&auto=format&fit=crop');

background-size:cover;

background-position:center;

}



.hero-content{

position:relative;

z-index:2;

max-width:900px;

}



.hero h1{

font-size:110px;

line-height:0.9;

font-weight:900;

letter-spacing:-4px;

text-shadow:0 0 30px rgba(255,255,255,0.1);

}



.hero p{

margin-top:30px;

font-size:28px;

line-height:1.6;

max-width:900px;

color:#d9d9d9;

}



.top-buttons{

margin-top:40px;

display:flex;

gap:20px;

flex-wrap:wrap;

}



.top-buttons button{

background:rgba(255,255,255,0.08);

border:1px solid rgba(255,255,255,0.12);

padding:18px 40px;

border-radius:18px;

color:white;

font-size:18px;

cursor:pointer;

transition:0.4s;

backdrop-filter:blur(12px);

}



.top-buttons button:hover{

transform:translateY(-4px);

background:#1e2b59;

box-shadow:0 0 30px rgba(0,140,255,0.35);

}



.modules,

.streaming,

.analytics-live,

.contact{

padding:100px 80px;

}



.modules h2,

.streaming h2,

.analytics-live h2,

.contact h2{

font-size:72px;

margin-bottom:50px;

}



.cards,

.video-grid,

.stats{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

gap:40px;

}



.card,

.video-card,

.stat{

background:rgba(255,255,255,0.04);

border:1px solid rgba(255,255,255,0.08);

border-radius:28px;

overflow:hidden;

transition:0.4s;

backdrop-filter:blur(14px);

}



.card:hover,

.video-card:hover,

.stat:hover{

transform:translateY(-6px);

box-shadow:0 0 40px rgba(0,140,255,0.25);

}



.card img{

width:100%;

height:260px;

object-fit:cover;

}



.card-content,

.video-info,

.stat{

padding:30px;

}



.card h3,

.video-info h3,

.stat h3{

font-size:38px;

margin-bottom:16px;

}



.card p,

.video-info p,

.stat p{

font-size:20px;

line-height:1.6;

color:#cfcfcf;

}



video{

width:100%;

height:320px;

object-fit:cover;

background:black;

}



.contact-form{

display:flex;

flex-direction:column;

gap:20px;

max-width:700px;

}



.contact-form input,

.contact-form textarea{

background:rgba(255,255,255,0.05);

border:none;

padding:22px;

border-radius:16px;

color:white;

font-size:18px;

}



.contact-form textarea{

min-height:220px;

resize:none;

}



.contact-form button{

background:#1b3cff;

padding:20px;

border:none;

border-radius:16px;

color:white;

font-size:20px;

cursor:pointer;

transition:0.3s;

}



.contact-form button:hover{

background:#3456ff;

}



.contact-info{

margin-top:40px;

font-size:22px;

line-height:1.8;

}



.modal{

display:none;

position:fixed;

top:0;

left:0;

width:100%;

height:100%;

background:rgba(0,0,0,0.8);

backdrop-filter:blur(8px);

z-index:999;

}



.modal-content{

background:#0f1328;

width:80%;

max-width:1000px;

margin:5% auto;

padding:40px;

border-radius:28px;

position:relative;

}



.close{

position:absolute;

top:20px;

right:30px;

font-size:42px;

cursor:pointer;

}



@media(max-width:900px){



.hero{

padding:40px;

}



.hero h1{

font-size:62px;

}



.hero p{

font-size:20px;

}



.modules h2,

.streaming h2,

.analytics-live h2,

.contact h2{

font-size:48px;

}



}

"""



# ============================================================

# JS

# ============================================================



js = r"""

function abrirModulo(tipo){



const modal = document.getElementById("modal");

const body = document.getElementById("modal-body");



modal.style.display = "block";



if(tipo === "realty"){



body.innerHTML = `

<h2>Luxury Realty</h2>



<p>

Global premium infrastructure for real estate,

analytics and operational intelligence.

</p>



<img

src="https://images.unsplash.com/photo-1494526585095-c41746248156?q=80&w=1200&auto=format&fit=crop"

style="width:100%;margin-top:30px;border-radius:20px;">

`;



}



if(tipo === "analytics"){



body.innerHTML = `

<h2>Operational Analytics</h2>



<p>

Strategic enterprise analytics with live monitoring.

</p>



<img

src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop"

style="width:100%;margin-top:30px;border-radius:20px;">

`;



}



if(tipo === "governance"){



body.innerHTML = `

<h2>Global Governance</h2>



<p>

Operational compliance, enterprise traceability and security.

</p>



<img

src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200&auto=format&fit=crop"

style="width:100%;margin-top:30px;border-radius:20px;">

`;



}



if(tipo === "streaming"){



body.innerHTML = `

<h2>Corporate Streaming</h2>



<p>

Enterprise audiovisual operational environment.

</p>



<video

controls

autoplay

muted

loop

style="width:100%;margin-top:30px;border-radius:20px;">



<source

src="https://www.w3schools.com/html/mov_bbb.mp4"

type="video/mp4">



</video>

`;



}



}



function fecharModal(){



document.getElementById("modal").style.display = "none";



}



window.onclick = function(event){



const modal = document.getElementById("modal");



if(event.target == modal){



modal.style.display = "none";



}



}

"""



# ============================================================

# ESCREVER ARQUIVOS

# ============================================================



with open(os.path.join(FRONTEND, "index.html"), "w", encoding="utf-8") as f:
    pass

    f.write(textwrap.dedent(html))



with open(os.path.join(FRONTEND, "style.css"), "w", encoding="utf-8") as f:
    pass

    f.write(textwrap.dedent(css))



with open(os.path.join(FRONTEND, "script.js"), "w", encoding="utf-8") as f:
    pass

    f.write(textwrap.dedent(js))



# ============================================================

# POWERSHELL

# ============================================================



ps1 = r"""

Start-Process "index.html"

"""



with open(os.path.join(BASE, "INICIAR.ps1"), "w", encoding="utf-8") as f:
    pass

    f.write(ps1)



# ============================================================

# FINAL

# ============================================================



print("\n===================================================")

print(" IOTEC OMEGA ULTRA")

print(" ENTERPRISE CINEMATIC SYSTEM")

print("===================================================")



print(f"\nLOCAL:")

print(BASE)



print("\nARQUIVOS:")



arquivos = [



    "index.html",

    "style.css",

    "script.js",

    "INICIAR.ps1"



]



for a in arquivos:
    pass



    print(f"[+] {a}")



print("\n===================================================")

print(" EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

print("===================================================")



print(f'\ncd "{BASE}"')



print("\nDepois:")



print("\n./INICIAR.ps1")



print("\n===================================================")

print(" RECURSOS IMPLEMENTADOS")

print("===================================================")



recursos = [



    "CURVATURA DA TERRA",

    "FUNDO ESPACIAL",

    "VIDEOS MP4 COMPATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS",

    "CARDS PREMIUM",

    "FORMULÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO UNIVERSAL",

    "MODAIS INTERATIVOS",

    "BOTOES FUNCIONAIS",

    "STREAMING CORPORATIVO",

    "LIVE ANALYTICS",

    "GLOW ENTERPRISE",

    "RESPONSIVIDADE",

    "INTERFACE CINEMATOGRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂFICA"



]



for r in recursos:
    pass



    print(f"\n[+] {r}")



print("\n===================================================")

print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO FINALIZADO")

print("===================================================")







