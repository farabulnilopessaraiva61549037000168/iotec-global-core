import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC PREMIUM ASCENSION ENGINE

# ULTRA PREMIUM PLATFORM TRANSFORMATION

# ============================================================



import os

from pathlib import Path



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_PREMIUM_ASCENSION"

)



FRONTEND = BASE / "frontend"



FRONTEND.mkdir(

    parents=True,

    exist_ok=True

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



<title>ACROPOLE PREMIUM</title>



<link rel="stylesheet" href="style.css">



<link rel="preconnect" href="https://fonts.googleapis.com">



<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">



</head>



<body>



<div class="overlay"></div>



<video autoplay muted loop id="bgvideo">



<source src="https://cdn.coverr.co/videos/coverr-earth-from-space-1560084400887?download=1080p" type="video/mp4">



</video>



<header>



<div class="logo">



ACROPOLE PREMIUM



</div>



<nav>



<a href="#">INÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂCIO</a>

<a href="#">TECNOLOGIA</a>

<a href="#">IA</a>

<a href="#">PLATAFORMA</a>

<a href="#">PREMIUM</a>



</nav>



</header>



<section class="hero">



<h1>



A NOVA ERA DA EDUCAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE



</h1>



<p>



Uma infraestrutura educacional premium gerida por inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia artificial, preparada para escala global.



</p>



<button>



ENTRAR NO ECOSSISTEMA



</button>



</section>



<section class="grid">



<div class="card">



<h2>IA EDUCACIONAL</h2>



<p>



GeraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica de aulas, avaliaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes, simulados e materiais premium.



</p>



</div>



<div class="card">



<h2>PORTFÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"LIO FÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂSICO</h2>



<p>



ExperiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia premium com fichÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios semestrais e material refinado.



</p>



</div>



<div class="card">



<h2>HYPERSCALE</h2>



<p>



Arquitetura resiliente preparada para milhÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes de operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes distribuÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­das.



</p>



</div>



<div class="card">



<h2>GOVERNANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡A IA</h2>



<p>



Monitoramento inteligente, contenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica e evoluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o contÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­nua.



</p>



</div>



</section>



<section class="premium">



<h1>



PREMIUM EXPERIENCE



</h1>



<p>



Minimalismo. SofisticaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o. Performance. InteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia.



</p>



</section>



<script src="script.js"></script>



</body>



</html>

'''



# ============================================================

# STYLE CSS

# ============================================================



style_css = r'''

*{



margin:0;

padding:0;

box-sizing:border-box;



}



body{



font-family:'Inter',sans-serif;

background:#000;

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

background:rgba(0,0,0,0.25);

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

transition:0.3s;



}



nav a:hover{



opacity:0.6;



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

font-weight:800;

line-height:1.1;



}



.hero p{



margin-top:30px;

font-size:22px;

max-width:900px;

opacity:0.85;



}



.hero button{



margin-top:40px;

padding:18px 50px;

border:none;

border-radius:18px;

background:white;

color:black;

font-size:18px;

font-weight:700;

cursor:pointer;

transition:0.4s;



}



.hero button:hover{



transform:scale(1.05);



}



.grid{



display:grid;

grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

gap:35px;

padding:120px 60px;



}



.card{



background:rgba(255,255,255,0.06);

backdrop-filter:blur(18px);

padding:40px;

border-radius:28px;

border:1px solid rgba(255,255,255,0.08);

transition:0.4s;



}



.card:hover{



transform:translateY(-8px);



}



.card h2{



font-size:30px;

margin-bottom:20px;



}



.card p{



opacity:0.8;

line-height:1.8;



}



.premium{



padding:180px 40px;

text-align:center;



}



.premium h1{



font-size:72px;

margin-bottom:30px;



}



.premium p{



font-size:24px;

opacity:0.8;



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

# SCRIPT JS

# ============================================================



script_js = r'''

window.addEventListener(



"scroll",



()=>{



const cards = document.querySelectorAll(".card")



cards.forEach(



card=>{



const top = card.getBoundingClientRect().top



if(top < window.innerHeight - 100){



card.style.opacity = 1

card.style.transform = "translateY(0px)"



}



}



)



}



)



console.log(



"ACROPOLE PREMIUM ONLINE"



)

'''



# ============================================================

# SERVER PY

# ============================================================



server_py = r'''

import http.server

import socketserver

import webbrowser

import os



PORT = 9999



os.chdir(



os.path.dirname(__file__)



)



Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(



("", PORT),



Handler



) as httpd:



    print()

    print("===================================================")

    print(" ACROPOLE PREMIUM ONLINE")

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



(BASE / "INICIAR_PREMIUM.ps1").write_text(

    ps1,

    encoding="utf-8"

)



# ============================================================

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC PREMIUM ASCENSION")

print(" ULTRA PREMIUM PLATFORM")

print("===================================================")



print()

print(f"BASE -> {BASE}")



print()

print("ARQUIVOS:")



print(" [+] frontend/index.html")

print(" [+] frontend/style.css")

print(" [+] frontend/script.js")

print(" [+] frontend/server.py")

print(" [+] INICIAR_PREMIUM.ps1")



print()

print("===================================================")

print(" EXECUCAO")

print("===================================================")



print()

print("1. ABRIR POWERSHELL")

print()

print("2. EXECUTAR")

print()

print("./INICIAR_PREMIUM.ps1")

print()

print("3. ACESSAR")

print()

print("http://localhost:9999")



print()

print("===================================================")

print(" PLATAFORMA PREMIUM FINALIZADA")

print("===================================================")





