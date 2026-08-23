import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC LIVE EXECUTIVE VISUAL CENTER
# TORRE OPERACIONAL EM TEMPO REAL
# =========================================================

from flask import Flask, jsonify

from flask_cors import CORS

import requests

from datetime import datetime

app = Flask(__name__)

CORS(app)

# =========================================================
# SERVICOS
# =========================================================

SERVICOS = {

    "Governanca":
    "http://127.0.0.1:7600/",

    "Presidencia":
    "http://127.0.0.1:7700/",

    "Curadoria":
    "http://127.0.0.1:7400/",

    "Consolidacao":
    "http://127.0.0.1:7500/",

    "Criatividade":
    "http://127.0.0.1:7300/",

    "Organizacao":
    "http://127.0.0.1:7200/",

    "Orchestrator":
    "http://127.0.0.1:7800/"
}

# =========================================================
# STATUS
# =========================================================

def verificar(url):
    pass

    try:
        pass

        r = requests.get(
            url,
            timeout=2
        )

        if r.status_code == 200:
            pass

            return "ONLINE"

        return "OFFLINE"

    except:
        pass

        return "OFFLINE"

# =========================================================
# HTML
# =========================================================

@app.route('/')

def home():
    pass

    return """
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>IOTEC LIVE CENTER</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial;
}

body{

    background:#02050b;

    color:white;

    overflow:hidden;
}

.topbar{

    width:100%;

    height:90px;

    background:linear-gradient(
        90deg,
        #06111f,
        #0c1d35,
        #06111f
    );

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:0 40px;

    border-bottom:1px solid #18416f;
}

.logo{

    font-size:42px;

    font-weight:bold;

    color:#4fb6ff;

    letter-spacing:3px;
}

.subtitle{

    font-size:14px;

    color:#6c97c2;
}

.clock{

    font-size:20px;

    color:#7dcbff;
}

.main{

    display:grid;

    grid-template-columns:25% 50% 25%;

    height:calc(100vh - 90px);
}

.panel{

    padding:20px;

    overflow:auto;
}

.left{

    background:#07111b;
}

.center{

    background:#02050b;

    display:flex;

    align-items:center;

    justify-content:center;
}

.right{

    background:#07111b;
}

.card{

    background:#0a1625;

    border:1px solid #183e69;

    border-radius:18px;

    padding:20px;

    margin-bottom:20px;
}

.card-title{

    font-size:20px;

    color:#4eb8ff;

    margin-bottom:15px;
}

.service{

    display:flex;

    justify-content:space-between;

    align-items:center;

    background:#101d2f;

    padding:14px;

    border-radius:10px;

    margin-bottom:12px;
}

.online{

    color:#67ffae;

    font-weight:bold;
}

.offline{

    color:#ff6565;

    font-weight:bold;
}

.tower{

    width:90%;

    height:90%;

    border-radius:30px;

    border:1px solid #1a4674;

    background:linear-gradient(
        180deg,
        #07111b,
        #02050b
    );

    position:relative;

    overflow:hidden;

    box-shadow:0 0 60px rgba(0,153,255,0.15);
}

.glow{

    position:absolute;

    width:800px;

    height:800px;

    background:radial-gradient(
        circle,
        rgba(0,153,255,0.20),
        transparent
    );

    top:-250px;

    left:50%;

    transform:translateX(-50%);

    animation:pulse 4s infinite;
}

@keyframes pulse{

    0%{
        opacity:0.3;
    }

    50%{
        opacity:1;
    }

    100%{
        opacity:0.3;
    }
}

.title{

    position:absolute;

    top:40px;

    width:100%;

    text-align:center;

    font-size:52px;

    color:#56c2ff;

    font-weight:bold;

    letter-spacing:4px;
}

.layers{

    position:absolute;

    top:150px;

    width:100%;

    display:flex;

    flex-direction:column;

    align-items:center;

    gap:25px;
}

.layer{

    width:75%;

    height:80px;

    border-radius:18px;

    border:1px solid #1c4a7d;

    background:#091321;

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:0 30px;

    font-size:24px;

    color:#66c7ff;

    box-shadow:0 0 25px rgba(0,0,0,0.4);
}

.heartbeat{

    width:16px;

    height:16px;

    border-radius:50%;

    background:#67ffae;

    animation:heartbeat 1s infinite;
}

@keyframes heartbeat{

    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.8);
    }

    100%{
        transform:scale(1);
    }
}

.alert{

    background:#1c1010;

    border:1px solid #6b2d2d;

    padding:14px;

    border-radius:10px;

    color:#ff9d9d;
}

.footer{

    position:absolute;

    bottom:15px;

    width:100%;

    text-align:center;

    color:#54779d;

    font-size:13px;
}

</style>

</head>

<body>

<div class="topbar">

    <div>

        <div class="logo">
            IOTEC LIVE CENTER
        </div>

        <div class="subtitle">
            PresidÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ GovernanÃƒÆ'Ã†â€™a ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ OrquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
        </div>

    </div>

    <div class="clock" id="clock">
        --:--:--
    </div>

</div>

<div class="main">

    <div class="panel left">

        <div class="card">

            <div class="card-title">
                SERVIÃƒÆ'Ã†â€™OS
            </div>

            <div id="services">
            </div>

        </div>

        <div class="card">

            <div class="card-title">
                ALERTAS
            </div>

            <div id="alerts">

                <div class="alert">
                    Nenhum alerta crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico
                </div>

            </div>

        </div>

    </div>

    <div class="panel center">

        <div class="tower">

            <div class="glow"></div>

            <div class="title">
                TORRE EXECUTIVA
            </div>

            <div class="layers">

                <div class="layer">
                    PRESIDÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA
                    <div class="heartbeat"></div>
                </div>

                <div class="layer">
                    GOVERNANÃƒÆ'Ã†â€™A
                    <div class="heartbeat"></div>
                </div>

                <div class="layer">
                    PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
                    <div class="heartbeat"></div>
                </div>

                <div class="layer">
                    CURADORIA
                    <div class="heartbeat"></div>
                </div>

                <div class="layer">
                    CRIATIVIDADE
                    <div class="heartbeat"></div>
                </div>

                <div class="layer">
                    ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
                    <div class="heartbeat"></div>
                </div>

            </div>

            <div class="footer">
                IOTEC LIVE EXECUTIVE VISUAL OPERATIONS CENTER
            </div>

        </div>

    </div>

    <div class="panel right">

        <div class="card">

            <div class="card-title">
                STATUS GLOBAL
            </div>

            <div id="global">
            </div>

        </div>

    </div>

</div>

<script>

async function atualizar(){

    const res = await fetch('/status')

    const dados = await res.json()

    let html = ''

    let online = 0

    let offline = 0

    for(let nome in dados.servicos){

        let status = dados.servicos[nome]

        if(status === 'ONLINE'){
            online++
        }else{
            offline++
        }

        html += `
            <div class="service">
                <span>${nome}</span>
                <span class="${status === 'ONLINE' ? 'online' : 'offline'}">
                    ${status}
                </span>
            </div>
        `
    }

    document.getElementById('services').innerHTML = html

    document.getElementById('global').innerHTML = `

        <div class="service">
            <span>ONLINE</span>
            <span class="online">${online}</span>
        </div>

        <div class="service">
            <span>OFFLINE</span>
            <span class="offline">${offline}</span>
        </div>

        <div class="service">
            <span>ECOSSISTEMA</span>
            <span class="online">ATIVO</span>
        </div>

    `
}

function relogio(){

    const agora = new Date()

    document.getElementById('clock').innerHTML =
        agora.toLocaleTimeString()
}

setInterval(atualizar,3000)

setInterval(relogio,1000)

atualizar()

relogio()

</script>

</body>

</html>
"""

# =========================================================
# STATUS
# =========================================================

@app.route('/status')

def status():
    pass

    relatorio = {}

    for nome, url in SERVICOS.items():
        pass

        relatorio[nome] = verificar(url)

    return jsonify({

        "servicos":
        relatorio,

        "timestamp":
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })

# =========================================================
# START
# =========================================================

if __name__ == '__main__':
    pass

    print("")
    print("=" * 70)
    print(" IOTEC LIVE EXECUTIVE VISUAL CENTER ")
    print("=" * 70)
    print("")

    app.run(

        host='0.0.0.0',

        port=7950
    )


