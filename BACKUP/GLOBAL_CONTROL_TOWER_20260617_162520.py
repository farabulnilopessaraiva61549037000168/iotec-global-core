import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask
from flask_socketio import SocketIO
import threading
import random
import time

app = Flask(__name__)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

HTML = """

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>IOTEC GLOBAL CONTROL TOWER</title>

<script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{

    background:#050505;
    color:white;
    font-family:Arial;
    overflow:hidden;
}

.bg{

    position:fixed;
    inset:0;

    background:
    linear-gradient(
        rgba(0,0,0,0.82),
        rgba(0,0,0,0.92)
    ),
    url('https://images.unsplash.com/photo-1497366754035-f200968a6e72?q=80&w=2070&auto=format&fit=crop');

    background-size:cover;
    background-position:center;

    z-index:-2;
}

.layout{

    display:grid;
    grid-template-columns:300px 1fr;

    height:100vh;
}

.sidebar{

    background:rgba(0,0,0,0.92);

    border-right:1px solid rgba(255,255,255,0.08);

    padding:24px;
}

.logo{

    font-size:34px;
    font-weight:700;

    margin-bottom:30px;
}

.menu button{

    width:100%;

    padding:16px;

    margin-bottom:14px;

    border:none;

    border-radius:14px;

    background:rgba(255,255,255,0.05);

    color:white;

    cursor:pointer;

    transition:0.3s;

    text-align:left;
}

.menu button:hover{

    background:white;
    color:black;
}

.main{

    padding:24px;

    overflow:auto;
}

.title{

    font-size:48px;
    margin-bottom:24px;
}

.grid{

    display:grid;
    grid-template-columns:1fr 1fr;
    gap:22px;
}

.card{

    background:rgba(255,255,255,0.04);

    border-radius:22px;

    border:1px solid rgba(255,255,255,0.08);

    padding:22px;

    backdrop-filter:blur(12px);
}

.card h2{

    margin-bottom:18px;
}

.metrics{

    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
}

.metric{

    background:rgba(255,255,255,0.03);

    border-radius:14px;

    padding:18px;
}

.metric-title{

    color:#bbbbbb;
    font-size:12px;
}

.metric-value{

    margin-top:10px;

    font-size:28px;
    font-weight:700;
}

.feed{

    height:320px;
    overflow:auto;
}

.event{

    padding:12px;

    margin-bottom:12px;

    border-left:3px solid white;

    background:rgba(255,255,255,0.03);

    border-radius:10px;
}

.monitors{

    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
}

.monitor{

    height:180px;

    border-radius:16px;

    overflow:hidden;

    position:relative;

    cursor:pointer;
}

.monitor video{

    width:100%;
    height:100%;
    object-fit:cover;
}

.overlay{

    position:absolute;
    inset:0;

    background:
    linear-gradient(
        rgba(0,0,0,0.1),
        rgba(0,0,0,0.82)
    );

    display:flex;
    align-items:end;

    padding:18px;

    font-size:18px;
    font-weight:700;
}

.footer{

    position:fixed;
    bottom:12px;
    right:20px;

    font-size:11px;

    color:rgba(255,255,255,0.45);
}

</style>

</head>

<body>

<div class="bg"></div>

<div class="layout">

    <div class="sidebar">

        <div class="logo">
            IOTEC / IBEX
        </div>

        <div class="menu">

            <button onclick="openSector('TREASURY')">
                TREASURY
            </button>

            <button onclick="openSector('OBSERVABILITY')">
                OBSERVABILITY
            </button>

            <button onclick="openSector('GLOBAL FLOW')">
                GLOBAL FLOW
            </button>

            <button onclick="openSector('BROADCAST')">
                BROADCAST
            </button>

            <button onclick="openSector('AI SYSTEMS')">
                AI SYSTEMS
            </button>

        </div>

    </div>

    <div class="main">

        <div class="title">
            GLOBAL CONTROL TOWER
        </div>

        <div class="grid">

            <div class="card">

                <h2>GLOBAL OBSERVABILITY</h2>

                <div class="metrics">

                    <div class="metric">

                        <div class="metric-title">
                            CLIENTS
                        </div>

                        <div class="metric-value" id="clients">
                            0
                        </div>

                    </div>

                    <div class="metric">

                        <div class="metric-title">
                            PAYMENTS
                        </div>

                        <div class="metric-value" id="payments">
                            0
                        </div>

                    </div>

                    <div class="metric">

                        <div class="metric-title">
                            SIGNALS
                        </div>

                        <div class="metric-value" id="signals">
                            0
                        </div>

                    </div>

                    <div class="metric">

                        <div class="metric-title">
                            TREASURY
                        </div>

                        <div class="metric-value" id="treasury">
                            R$0
                        </div>

                    </div>

                </div>

            </div>

            <div class="card">

                <h2>LIVE FLOW</h2>

                <div class="feed" id="feed"></div>

            </div>

            <div class="card">

                <h2>ACTIVE ENVIRONMENTS</h2>

                <div class="monitors">

                    <div class="monitor">

                        <video autoplay muted loop>

                            <source src="https://cdn.coverr.co/videos/coverr-modern-office-workspace-5176/1080p.mp4" type="video/mp4">

                        </video>

                        <div class="overlay">
                            EXECUTIVE
                        </div>

                    </div>

                    <div class="monitor">

                        <video autoplay muted loop>

                            <source src="https://cdn.coverr.co/videos/coverr-server-room-1567066570470/1080p.mp4" type="video/mp4">

                        </video>

                        <div class="overlay">
                            GOVTECH
                        </div>

                    </div>

                    <div class="monitor">

                        <video autoplay muted loop>

                            <source src="https://cdn.coverr.co/videos/coverr-earth-from-space-1569846731678/1080p.mp4" type="video/mp4">

                        </video>

                        <div class="overlay">
                            SATELLITE
                        </div>

                    </div>

                    <div class="monitor">

                        <video autoplay muted loop>

                            <source src="https://cdn.coverr.co/videos/coverr-coding-on-laptop-5177/1080p.mp4" type="video/mp4">

                        </video>

                        <div class="overlay">
                            AI SYSTEMS
                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</div>

<div class="footer">
IOTEC / IBEX ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ GLOBAL OPERATIONAL CENTER
</div>

<script>

const socket = io();

const feed =
document.getElementById("feed");

socket.on("event", function(data){

    const div =
    document.createElement("div");

    div.className = "event";

    div.innerHTML = data.message;

    feed.prepend(div);

    document.getElementById("clients").innerHTML =
    data.clients;

    document.getElementById("payments").innerHTML =
    data.payments;

    document.getElementById("signals").innerHTML =
    data.signals;

    document.getElementById("treasury").innerHTML =
    data.treasury;
});

function openSector(name){

    alert("OPENING: " + name);
}

</script>

</body>

</html>

"""

@app.route("/")
def home():
    pass

    return HTML

state = {

    "clients":0,
    "payments":0,
    "signals":0,
    "treasury":0
}

EVENTS = [

    "CLIENT CONNECTED",
    "PAYMENT RECEIVED",
    "PAYPAL SIGNAL DETECTED",
    "OBSERVABILITY ACTIVE",
    "GLOBAL ROUTING ACTIVE",
    "AI SYSTEMS ONLINE",
    "SATELLITE NODE ACTIVE"
]

def realtime():
    pass

    while True:
        pass

        state["clients"] += random.randint(0,2)
        state["payments"] += random.randint(0,1)
        state["signals"] += random.randint(1,5)

        value = random.randint(100,9000)

        state["treasury"] += value

        socketio.emit(

            "event",

            {

                "message":
                random.choice(EVENTS),

                "clients":
                state["clients"],

                "payments":
                state["payments"],

                "signals":
                state["signals"],

                "treasury":
                f"R$ {state['treasury']:,}"
            }
        )

        time.sleep(4)

threading.Thread(
    target=realtime,
    daemon=True
).start()

print("")
print("================================================")
print(" IOTEC / IBEX GLOBAL CONTROL TOWER")
print("================================================")
print("")
print("OPEN:")
print("http://127.0.0.1:3000")
print("")

socketio.run(
    app,
    host="127.0.0.1",
    port=3000,
    debug=True,
    allow_unsafe_werkzeug=True,
    use_reloader=False
)



