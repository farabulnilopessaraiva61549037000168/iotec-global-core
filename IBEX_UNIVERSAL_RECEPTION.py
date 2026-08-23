import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IBEX UNIVERSAL RECEPTION ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â FULL AUTO VERSION
# ============================================================
# OBJETIVO:
#
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â InicializaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Flask automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tico
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Banco JSON automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tico
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â RecepÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o universal
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Dashboard premium
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Coleta de gargalos
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Estrutura corporativa
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Visual IBEX
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Pronto para expansÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o
#
# REQUER:
#
# pip install flask
#
# EXECUTAR:
#
# python UNIVERSAL_RECEPTION_EMAIL.py
#
# ABRIR:
#
# http://127.0.0.1:5000
#
# ============================================================

from flask import (
    Flask,
    render_template_string,
    request,
    redirect
)

from pathlib import Path
from datetime import datetime
import json

# ============================================================
# APP
# ============================================================

app = Flask(__name__)

# ============================================================
# DATABASE
# ============================================================

DATABASE = Path("IBEX_clients.json")

if not DATABASE.exists():
    pass

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump([], f)

# ============================================================
# SAVE CLIENT
# ============================================================

def save_client(data):
    pass

    with open(
        DATABASE,
        "r",
        encoding="utf-8"
    ) as f:

        existing = json.load(f)

    existing.append(data)

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            existing,
            f,
            ensure_ascii=False,
            indent=4
        )

# ============================================================
# HTML
# ============================================================

HTML = """

<!DOCTYPE html>
<html>

<head>

<title>IBEX ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ IoTech</title>

<meta charset="utf-8">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{

    background:#050505;

    color:#f2f2f2;

    font-family:Arial;

    overflow-x:hidden;
}

.hero{

    height:100vh;

    background:
    linear-gradient(
        rgba(0,0,0,0.72),
        rgba(0,0,0,0.92)
    ),
    url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee');

    background-size:cover;
    background-position:center;

    display:flex;

    align-items:center;
    justify-content:center;

    text-align:center;

    padding:40px;
}

.hero-content{

    max-width:1100px;
}

.logo{

    font-size:110px;

    letter-spacing:18px;

    font-weight:bold;

    color:#ffffff;
}

.subtitle{

    margin-top:20px;

    font-size:24px;

    color:#bfbfbf;

    line-height:1.8;
}

.concept{

    margin-top:40px;

    font-size:18px;

    color:#8f8f8f;

    line-height:2;
}

.reception{

    margin-top:50px;

    display:inline-block;

    padding:20px 34px;

    border-radius:22px;

    border:1px solid #222;

    background:rgba(255,255,255,0.03);

    backdrop-filter:blur(12px);
}

.reception-title{

    color:#777;

    letter-spacing:4px;

    font-size:12px;

    margin-bottom:10px;
}

.reception-email{

    color:#ffffff;

    font-size:18px;
}

.section{

    padding:90px 10%;
}

.title{

    font-size:48px;

    margin-bottom:25px;
}

.text{

    color:#9a9a9a;

    font-size:18px;

    line-height:2;
}

.grid{

    margin-top:60px;

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(260px,1fr));

    gap:30px;
}

.card{

    background:#0d0d0d;

    border:1px solid #1e1e1e;

    border-radius:26px;

    padding:36px;

    transition:0.35s;
}

.card:hover{

    transform:translateY(-7px);

    border-color:#666;
}

.card h3{

    margin-bottom:20px;

    font-size:24px;
}

.card p{

    color:#8f8f8f;

    line-height:1.8;
}

form{

    margin-top:70px;
}

input,
textarea{

    width:100%;

    background:#0d0d0d;

    border:1px solid #222;

    border-radius:18px;

    padding:20px;

    color:#f2f2f2;

    margin-bottom:22px;

    font-size:16px;
}

textarea{

    min-height:180px;

    resize:vertical;
}

button{

    background:#f2f2f2;

    color:#000;

    border:none;

    padding:18px 40px;

    border-radius:16px;

    font-size:16px;

    cursor:pointer;

    transition:0.3s;
}

button:hover{

    transform:scale(1.03);
}

.footer{

    border-top:1px solid #111;

    padding:60px;

    text-align:center;
}

.footer-logo{

    font-size:24px;

    letter-spacing:8px;

    margin-bottom:16px;
}

.footer-email{

    margin-top:14px;

    color:#999;
}

.footer-mini{

    margin-top:24px;

    color:#555;

    font-size:13px;
}

</style>

</head>

<body>

<div class="hero">

    <div class="hero-content">

        <div class="logo">

            IBEX

        </div>

        <div class="subtitle">

            Precision ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Intelligence ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Altitude

        </div>

        <div class="concept">

            Plataforma estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gica de inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia,
            modelagem,
            anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise operacional,
            visualizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica
            e recepÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o universal corporativa.

        </div>

        <div class="reception">

            <div class="reception-title">

                UNIVERSAL RECEPTION

            </div>

            <div class="reception-email">

                iotec.bl@proton.me

            </div>

        </div>

    </div>

</div>

<div class="section">

    <div class="title">

        Universal Reception ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ IoTech

    </div>

    <div class="text">

        Empresas,
        instituiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes,
        operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnicas
        e setores econÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´micos
        podem registrar gargalos,
        demandas estruturais
        e necessidades operacionais
        para anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gica da estrutura IBEX.

    </div>

    <div class="grid">

        <div class="card">

            <h3>Modelagem</h3>

            <p>

                SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes,
                cenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios,
                mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tricas,
                elasticidade,
                projeÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes
                e inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica.

            </p>

        </div>

        <div class="card">

            <h3>GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a</h3>

            <p>

                Fluxos operacionais,
                rastreabilidade,
                auditoria,
                organizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o
                e controle estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gico.

            </p>

        </div>

        <div class="card">

            <h3>VisualizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</h3>

            <p>

                Dashboards,
                grÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ficos,
                painÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©is,
                indicadores
                e anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise visual executiva.

            </p>

        </div>

    </div>

    <form method="POST" action="/submit">

        <input
            type="text"
            name="empresa"
            placeholder="Empresa / InstituiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o"
            required
        >

        <input
            type="email"
            name="email"
            placeholder="E-mail Corporativo"
            required
        >

        <input
            type="text"
            name="setor"
            placeholder="Setor EconÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´mico"
            required
        >

        <input
            type="text"
            name="nome"
            placeholder="ResponsÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡vel"
            required
        >

        <textarea
            name="gargalo"
            placeholder="Relate o gargalo tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnico, operacional ou estrutural"
            required
        ></textarea>

        <button type="submit">

            ENVIAR PARA ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE

        </button>

    </form>

</div>

<div class="footer">

    <div class="footer-logo">

        IBEX

    </div>

    <div>

        Universal Reception ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ IoTech Platform

    </div>

    <div class="footer-email">

        iotec.bl@proton.me

    </div>

    <div class="footer-mini">

        Precision ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Intelligence ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Altitude

    </div>

</div>

</body>

</html>

"""

# ============================================================
# ROUTES
# ============================================================

@app.route("/")

def home():
    pass

    return render_template_string(HTML)

# ============================================================

@app.route("/submit", methods=["POST"])

def submit():
    pass

    data = {

        "empresa":
            request.form["empresa"],

        "email":
            request.form["email"],

        "setor":
            request.form["setor"],

        "nome":
            request.form["nome"],

        "gargalo":
            request.form["gargalo"],

        "created_at":
            datetime.now().isoformat()
    }

    save_client(data)

    return redirect("/")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    print("\n===================================")
    print(" IBEX UNIVERSAL RECEPTION ONLINE")
    print("===================================\n")

    print("LOCAL:")
    print("http://127.0.0.1:5000\n")

    app.run(
        debug=False, use_reloader=False,
        host="0.0.0.0",
        port=5000
    )




