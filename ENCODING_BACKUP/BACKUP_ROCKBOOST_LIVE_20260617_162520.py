import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ROCKBOOST LIVE PANEL
# CENTRAL GOVERNANCE DASHBOARD
# ============================================================

from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path(
    "C:/IOTEC_LIVE_PANEL"
)

BASE.mkdir(
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
IOTEC ROCKBOOST
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<div class="overlay"></div>

<header>

<h1>
IOTEC ROCKBOOST
</h1>

<p>
CENTRAL GOVERNANCE PANEL
</p>

</header>

<section class="grid">

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

<div class="module hibernate">
GLOBAL REALTY
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
    url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1920')
    center/cover fixed;

    font-family:
    Arial;

    color:white;

    overflow-x:hidden;

}

.overlay{

    position:fixed;

    width:100%;
    height:100%;

    background:
    rgba(0,0,0,0.7);

    backdrop-filter:
    blur(8px);

}

header{

    position:relative;

    z-index:2;

    text-align:center;

    padding:60px;

}

header h1{

    font-size:60px;

    letter-spacing:5px;

}

header p{

    font-size:20px;

    opacity:0.8;

}

.grid{

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

    backdrop-filter:
    blur(10px);

    border-radius:25px;

    padding:40px;

    text-align:center;

    transition:0.4s;

}

.card:hover{

    transform:
    translateY(-8px);

    background:
    rgba(255,255,255,0.12);

}

.card h2{

    margin-bottom:20px;

}

.card div{

    font-size:55px;

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

    padding:20px 35px;

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
    rgba(255,180,0,0.2);

    border:
    1px solid rgba(255,180,0,0.4);

}

"""

# ============================================================
# JS
# ============================================================

JS = """

function random(min,max){

    return Math.floor(
        Math.random()*(max-min+1)+min
    )

}

function update(){

    document
    .getElementById('cpu')
    .innerHTML =
    random(10,60)+'%'

    document
    .getElementById('ram')
    .innerHTML =
    random(70,95)+'%'

    document
    .getElementById('latency')
    .innerHTML =
    random(20,240)+'ms'

    document
    .getElementById('users')
    .innerHTML =
    random(1200,25000)

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

PORT = 9900

Handler =
http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(

    ("", PORT),
    Handler

) as httpd:

    print()
    print("===================================")
    print(" IOTEC LIVE PANEL")
    print("===================================")

    print()
    print(
        "SERVER -> http://localhost:9900"
    )

    webbrowser.open(
        "http://localhost:9900"
    )

    httpd.serve_forever()

"""

# ============================================================
# POWERSHELL
# ============================================================

PS1 = """

cd frontend

python server.py

"""

# ============================================================
# PASTAS
# ============================================================

(
    BASE / "frontend"
).mkdir(

    parents=True,
    exist_ok=True

)

# ============================================================
# EXPORTACAO
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

    BASE / "INICIAR_PANEL.ps1",

    "w",
    encoding="utf-8"

) as f:

    f.write(PS1)

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC ROCKBOOST LIVE PANEL")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("ARQUIVOS:")

print(" [+] index.html")
print(" [+] style.css")
print(" [+] script.js")
print(" [+] server.py")
print(" [+] INICIAR_PANEL.ps1")

print()
print("===================================================")
print(" EXECUCAO")
print("===================================================")

print()
print("1. ABRIR POWERSHELL")

print()
print("2. EXECUTAR")

print()
print("./INICIAR_PANEL.ps1")

print()
print("3. ABRIR")

print()
print("http://localhost:9900")

print()
print("===================================================")
print(" PAINEL CENTRALIZADO")
print("===================================================")



