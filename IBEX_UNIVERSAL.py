import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IBEX UNIVERSAL RECEPTION SYSTEM
# ============================================================
# OBJETIVO:
#
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â RecepÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o universal corporativa
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Cliente identifica empresa
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Setor econÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´mico
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Relato de gargalo
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Direcionamento inteligente
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Portal comercial IoTech
# ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â EstÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tica premium IBEX
#
# REQUER:
#
# pip install flask
#
# EXECUTAR:
#
# python portal.py
#
# ============================================================

from flask import (
    Flask,
    render_template_string,
    request,
    redirect
)

from datetime import datetime
import json
from pathlib import Path

# ============================================================
# APP
# ============================================================

app = Flask(__name__)

# ============================================================
# DATABASE
# ============================================================

DATABASE = Path("ibex_clients.json")

# ============================================================
# SAVE DATA
# ============================================================

def save_client(data):
    pass

    existing = []

    if DATABASE.exists():
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
# TEMPLATE
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
                rgba(0,0,0,0.75),
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

            max-width:1000px;
        }

        .logo{

            font-size:90px;

            letter-spacing:14px;

            font-weight:bold;
        }

        .subtitle{

            margin-top:20px;

            font-size:22px;

            color:#bfbfbf;

            line-height:1.7;
        }

        .concept{

            margin-top:40px;

            font-size:18px;

            color:#888;

            line-height:1.9;
        }

        .section{

            padding:90px 12%;
        }

        .title{

            font-size:42px;

            margin-bottom:20px;
        }

        .text{

            color:#aaaaaa;

            line-height:1.9;

            font-size:18px;
        }

        .grid{

            margin-top:60px;

            display:grid;

            grid-template-columns:
            repeat(auto-fit,minmax(250px,1fr));

            gap:30px;
        }

        .card{

            background:#0d0d0d;

            border:1px solid #1f1f1f;

            border-radius:24px;

            padding:35px;

            transition:0.3s;
        }

        .card:hover{

            transform:translateY(-6px);

            border-color:#666;
        }

        .card h3{

            margin-bottom:20px;

            font-size:24px;
        }

        .card p{

            color:#9f9f9f;

            line-height:1.7;
        }

        form{

            margin-top:50px;
        }

        input,
        textarea,
        select{

            width:100%;

            background:#0d0d0d;

            border:1px solid #222;

            border-radius:16px;

            padding:18px;

            color:#f2f2f2;

            margin-bottom:20px;

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

            border-radius:14px;

            font-size:16px;

            cursor:pointer;

            transition:0.3s;
        }

        button:hover{

            transform:scale(1.03);
        }

        .footer{

            padding:50px;

            text-align:center;

            color:#666;

            border-top:1px solid #111;
        }

        .email{

            margin-top:12px;

            color:#999;
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

                Estrutura analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica e tecnolÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³gica
                voltada para modelagem,
                inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia operacional,
                visualizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gica
                e resoluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de gargalos tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnicos.

            </div>

        </div>

    </div>

    <div class="section">

        <div class="title">

            Universal Reception

        </div>

        <div class="text">

            Empresas, instituiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes e profissionais
            podem identificar seu setor econÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´mico,
            relatar gargalos operacionais
            e direcionar demandas tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnicas
            para anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gica da estrutura IoTech.

        </div>

        <div class="grid">

            <div class="card">

                <h3>Modelagem</h3>

                <p>

                    SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes,
                    cenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios,
                    previsÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes,
                    mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tricas
                    e anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise estrutural.

                </p>

            </div>

            <div class="card">

                <h3>GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a</h3>

                <p>

                    OrganizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de fluxos,
                    auditoria,
                    rastreabilidade
                    e inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia operacional.

                </p>

            </div>

            <div class="card">

                <h3>VisualizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</h3>

                <p>

                    Dashboards,
                    grÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ficos,
                    indicadores,
                    relatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rios
                    e painÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©is analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ticos.

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

        IBEX ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ IoTech Platform

        <div class="email">

            iotec.bl@proton.me

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

    app.run(debug=False, use_reloader=False)




