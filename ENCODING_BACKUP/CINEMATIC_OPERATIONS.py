import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC CINEMATIC OPERATIONS CENTER
# CENTRAL CINEMATOGRAFICA OPERACIONAL
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
# LOGS
# =========================================================

EVENTOS = []

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

<title>IOTEC CINEMATIC CENTER</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial;
}

body{

    background:#01040a;

    overflow:hidden;

    color:white;
}

body::before{

    content:"";

    position:absolute;

    width:1200px;

    height:1200px;

    background:radial-gradient(
        circle,
        rgba(0,153,255,0.12),
        transparent
    );

    top:-500px;

    left:50%;

    transform:translateX(-50%);

    animation:pulse 5s infinite;
}

@keyframes pulse{

    0%{
        opacity:0.2;
    }

    50%{
        opacity:1;
    }

    100%{
        opacity:0.2;
    }
}

.topbar{

    height:90px;

    background:#07111c;

    border-bottom:1px solid #1c4b7c;

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:0 40px;

    position:relative;

    z-index:2;
}

.logo{

    font-size:42px;

    color:#46b7ff;

    font-weight:bold;

    letter-spacing:3px;
}

.subtitle{

    color:#6f97c0;

    font-size:14px;
}

.clock{

    font-size:24px;

    color:#7fd0ff;
}

.main{

    display:grid;

    grid-template-columns:24% 52% 24%;

    height:calc(100vh - 90px);

    position:relative;

    z-index:2;
}

.panel{

    padding:20px;

    overflow:auto;
}

.card{

    background:#07111b;

    border:1px solid #19466f;

    border-radius:20px;

    padding:20px;

    margin-bottom:20px;

    box-shadow:0 0 35px rgba(0,0,0,0.4);
}

.card-title{

    font-size:22px;

    color:#50bbff;

    margin-bottom:15px;
}

.service{

    display:flex;

    justify-content:space-between;

    background:#0e1d30;

    padding:14px;

    border-radius:12px;

    margin-bottom:12px;
}

.online{

    color:#67ffae;

    font-weight:bold;
}

.offline{

    color:#ff6464;

    font-weight:bold;

    animation:blink 1s infinite;
}

@keyframes blink{

    0%{
        opacity:1;
    }

    50%{
        opacity:0.3;
    }

    100%{
        opacity:1;
    }
}

.center{

    display:flex;

    justify-content:center;

    align-items:center;
}

.tower{

    width:92%;

    height:92%;

    border-radius:30px;

    border:1px solid #1e4f85;

    background:linear-gradient(
        180deg,
        #07111b,
        #02050b
    );

    position:relative;

    overflow:hidden;
}

.title{

    position:absolute;

    top:40px;

    width:100%;

    text-align:center;

    font-size:56px;

    color:#47bbff;

    font-weight:bold;

    letter-spacing:4px;
}

.lines{

    position:absolute;

    width:100%;

    height:100%;
}

.line{

    position:absolute;

    height:2px;

    background:linear-gradient(
        90deg,
        transparent,
        #46b7ff,
        transparent
    );

    animation:flow 2s linear infinite;
}

@keyframes flow{

    0%{
        transform:translateX(-100%);
    }

    100%{
        transform:translateX(100%);
    }
}

.layer{

    width:70%;

    height:80px;

    margin:22px auto;

    margin-top:30px;

    background:#0a1625;

    border:1px solid #1f5187;

    border-radius:18px;

    display:flex;

    justify-content:space-between;

    align-items:center;

    padding:0 30px;

    color:#59c4ff;

    font-size:24px;
}

.dot{

    width:18px;

    height:18px;

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

.log{

    background:#0d1a2b;

    border-radius:10px;

    padding:12px;

    margin-bottom:10px;

    color:#89d2ff;

    font-size:13px;
}

.footer{

    position:absolute;

    bottom:15px;

    width:100%;

    text-align:center;

    color:#4b7398;

    font-size:12px;
}

</style>

</head>

<body>

<div class="topbar">

    <div>

        <div class="logo">
            IOTEC CINEMATIC CENTER
        </div>

        <div class="subtitle">
            PresidÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ GovernanÃƒÆ'Ã†â€™a ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Torre Viva
        </div>

    </div>

    <div class="clock" id="clock">
        --:--:--
    </div>

</div>

<div class="main">

    <div class="panel">

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
            </div>

        </div>

    </div>

    <div class="center">

        <div class="tower">

            <div class="title">
                TORRE EXECUTIVA
            </div>

            <div class="lines">

                <div class="line"
                style="top:220px;width:100%;">
                </div>

                <div class="line"
                style="top:320px;width:100%;">
                </div>

                <div class="line"
                style="top:420px;width:100%;">
                </div>

                <div class="line"
                style="top:520px;width:100%;">
                </div>

            </div>

            <div style="margin-top:150px;">

                <div class="layer">
                    PRESIDÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA
                    <div class="dot"></div>
                </div>

                <div class="layer">
                    GOVERNANÃƒÆ'Ã†â€™A
                    <div class="dot"></div>
                </div>

                <div class="layer">
                    PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
                    <div class="dot"></div>
                </div>

                <div class="layer">
                    CURADORIA
                    <div class="dot"></div>
                </div>

                <div class="layer">
                    ORQUESTRAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
                    <div class="dot"></div>
                </div>

            </div>

            <div class="footer">
                IOTEC CINEMATIC OPERATIONS CENTER
            </div>

        </div>

    </div>

    <div class="panel">

        <div class="card">

            <div class="card-title">
                EVENTOS AO VIVO
            </div>

            <div id="logs">
            </div>

        </div>

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

let historico = {}

async function atualizar(){

    const res = await fetch('/status')

    const dados = await res.json()

    let html = ''

    let logs = ''

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

                <span class="${
                    status === 'ONLINE'
                    ? 'online'
                    : 'offline'
                }">

                    ${status}

                </span>
            </div>
        `

        if(historico[nome] !== status){

            logs += `
                <div class="log">

                    [${new Date().toLocaleTimeString()}]

                    ${nome}

                    mudou para

                    ${status}

                </div>
            `

            historico[nome] = status
        }
    }

    document.getElementById('services').innerHTML = html

    document.getElementById('logs').innerHTML += logs

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

    let alertas = ''

    if(offline > 0){

        alertas = `
            <div class="service">
                <span>SERVIÃƒÆ'Ã†â€™OS OFFLINE</span>
                <span class="offline">${offline}</span>
            </div>
        `

    }else{

        alertas = `
            <div class="service">
                <span>ESTABILIDADE</span>
                <span class="online">
                    TOTAL
                </span>
            </div>
        `
    }

    document.getElementById('alerts').innerHTML = alertas
}

function relogio(){

    document.getElementById('clock').innerHTML =
        new Date().toLocaleTimeString()
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
# STATUS API
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
    print(" IOTEC CINEMATIC OPERATIONS CENTER ")
    print("=" * 70)
    print("")

    app.run(

        host='0.0.0.0',

        port=7990
    )


