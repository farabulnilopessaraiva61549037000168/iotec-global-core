# ==========================================================
# 084_EXECUTIVE_SKIN_SERVER.py
# IOTEC EXECUTIVE SKIN SERVER
# ==========================================================

from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """

<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="utf-8">

<title>IOTEC Executive Skin</title>

<style>

body{

background:#08131d;

margin:0;

font-family:Segoe UI;

color:white;

}

header{

padding:25px;

background:#0d2235;

border-bottom:2px solid #19d37d;

}

h1{

margin:0;

font-size:32px;

}

.subtitle{

color:#6fe3b5;

}

.grid{

display:grid;

grid-template-columns:repeat(4,1fr);

gap:18px;

padding:25px;

}

.card{

background:#10273d;

border-radius:14px;

padding:18px;

box-shadow:0 0 15px rgba(0,0,0,.4);

transition:.25s;

}

.card:hover{

transform:scale(1.02);

}

.online{

color:#19d37d;

font-weight:bold;

}

.pending{

color:orange;

font-weight:bold;

}

footer{

padding:20px;

text-align:center;

color:#9aa9b6;

}

button{

padding:10px 18px;

border:none;

border-radius:8px;

background:#19d37d;

cursor:pointer;

font-size:15px;

margin-top:12px;

}

button:hover{

background:#24f79a;

}

</style>

</head>

<body>

<header>

<h1>IOTEC EXECUTIVE SKIN</h1>

<div class="subtitle">

Empresa Operacional

</div>

</header>

<div class="grid">

<div class="card">

<h2>PresidÃƒÂªncia</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>Kernel</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>Render</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>Netlify</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>PayPal</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>Proton Mail</h2>

<p class="online">ONLINE</p>

</div>

<div class="card">

<h2>Google Maps</h2>

<p class="pending">PENDENTE</p>

</div>

<div class="card">

<h2>LinkedIn</h2>

<p class="pending">PENDENTE</p>

</div>

<div class="card">

<h2>WhatsApp Business</h2>

<p class="pending">EM IMPLANTAÃƒâ€¡ÃƒÆ'O</p>

</div>

<div class="card">

<h2>Executive Cockpit</h2>

<button>Abrir</button>

</div>

<div class="card">

<h2>Discovery Center</h2>

<button>Abrir</button>

</div>

<div class="card">

<h2>Experience Warehouse</h2>

<button>Abrir</button>

</div>

</div>

<footer>

{{data}}

</footer>

</body>

</html>

"""

@app.route("/")

def home():

    return render_template_string(

        HTML,

        data=datetime.now().strftime("%d/%m/%Y %H:%M")

    )

if __name__=="__main__":

    print()

    print("="*70)

    print("IOTEC EXECUTIVE SKIN SERVER")

    print("="*70)

    print()

    print("Servidor iniciado.")

    print()

    print("http://127.0.0.1:5000")

    print()

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

    )


