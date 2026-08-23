# ==========================================================
# 089_EXECUTIVE_SKIN_DASHBOARD.py
# EXECUTIVE SKIN DASHBOARD
# ==========================================================

from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

PAINEIS = [

("PresidÃƒÂªncia","ONLINE","#00ff99"),

("Chief of Staff","ONLINE","#00ff99"),

("Knowledge Kernel","ONLINE","#00ff99"),

("Executive Cockpit","ONLINE","#00ff99"),

("Infrastructure","ONLINE","#00ff99"),

("Discovery","ONLINE","#00ff99"),

("Campaign Center","ONLINE","#00ff99"),

("CRM","ONLINE","#00ff99"),

("Financeiro","ONLINE","#00ff99"),

("Experience Warehouse","ONLINE","#00ff99"),

("Visual Genome","ONLINE","#00ff99"),

("Official Assets","ONLINE","#00ff99"),

("Render","ONLINE","#00ff99"),

("Netlify","ONLINE","#00ff99"),

("PayPal","ONLINE","#00ff99"),

("Proton Mail","ONLINE","#00ff99"),

("Google Maps","PENDENTE","#ff5555"),

("WhatsApp Business","IMPLANTAÃƒâ€¡ÃƒÆ'O","#ffaa00"),

("LinkedIn","PENDENTE","#ff5555"),

("OpenAI","PENDENTE","#ff5555")

]

HTML="""

<!doctype html>

<html>

<head>

<meta charset="utf-8">

<title>IOTEC Executive Skin</title>

<style>

body{

margin:0;

background:#07111c;

font-family:Segoe UI;

color:white;

}

header{

padding:30px;

background:#0d2238;

border-bottom:3px solid #00ff99;

}

h1{

margin:0;

font-size:34px;

}

.sub{

color:#8fd6ff;

margin-top:8px;

}

.grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

gap:18px;

padding:30px;

}

.card{

background:#10253d;

border-radius:14px;

padding:18px;

box-shadow:0 0 25px rgba(0,0,0,.4);

}

.status{

font-size:18px;

font-weight:bold;

margin-top:15px;

}

footer{

padding:20px;

text-align:center;

color:#9ab7d1;

}

</style>

</head>

<body>

<header>

<h1>IOTEC ENTERPRISE OPERATING SYSTEM</h1>

<div class="sub">

Executive Skin

</div>

</header>

<div class="grid">

{% for nome,status,cor in paineis %}

<div class="card">

<h2>{{nome}}</h2>

<div class="status" style="color:{{cor}}">

{{status}}

</div>

</div>

{% endfor %}

</div>

<footer>

Empresa Operacional |

{{hora}}

</footer>

</body>

</html>

"""

@app.route("/")

def inicio():

    return render_template_string(

        HTML,

        paineis=PAINEIS,

        hora=datetime.now().strftime("%d/%m/%Y %H:%M")

    )

if __name__=="__main__":

    print()

    print("="*70)

    print("EXECUTIVE SKIN DASHBOARD")

    print("="*70)

    print()

    print("http://127.0.0.1:5000")

    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )


