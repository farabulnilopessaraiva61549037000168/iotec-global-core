import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
```python
from flask import Flask
from flask_socketio import SocketIO
import threading
import random
import time

app = Flask(__name__)

socketio = SocketIO(
    app,
    async_mode='threading',
    cors_allowed_origins="*"
)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">

<title>IOTEC CONTROL TOWER</title>

<script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#05070d;
    color:white;
    font-family:Arial;
    overflow:hidden;
}

.bg{
    position:fixed;
    inset:0;
    background:
    linear-gradient(
        rgba(0,0,0,0.7),
        rgba(0,20,40,0.9)
    ),
    url('https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?q=80&w=2070&auto=format&fit=crop');
    background-size:cover;
    background-position:center;
    z-index:-2;
}

.header{
    padding:35px;
    font-size:52px;
    font-weight:700;
    letter-spacing:2px;
}

.feed{
    width:100%;
    overflow:hidden;
    white-space:nowrap;
    border-top:1px solid rgba(255,255,255,0.1);
    border-bottom:1px solid rgba(255,255,255,0.1);
    padding:14px 0;
    background:rgba(255,255,255,0.03);
}

.feed-track{
    display:inline-block;
    animation:scroll 25s linear infinite;
}

.feed-track span{
    margin-right:80px;
    color:#58c8ff;
    font-size:14px;
}

@keyframes scroll{
    from{
        transform:translateX(100%);
    }

    to{
        transform:translateX(-100%);
    }
}

.main{
    padding:30px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:20px;
    padding:18px;
    margin-bottom:18px;
    border-radius:18px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
}

.grid:hover{
    border:1px solid #58c8ff;
    transition:0.3s;
}

.title{
    color:#58c8ff;
    font-size:13px;
}

.value{
    margin-top:10px;
    font-size:14px;
}

.panel{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
    margin-top:25px;
}

.box{
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:18px;
    padding:22px;
}

.box h2{
    margin-bottom:18px;
}

.live{
    margin-bottom:12px;
}

.dot{
    width:10px;
    height:10px;
    background:#00ff88;
    border-radius:50%;
    display:inline-block;
    margin-right:10px;
    box-shadow:0 0 10px #00ff88;
}

#events{
    height:220px;
    overflow:auto;
}

.event{
    padding:10px;
    margin-bottom:10px;
    border-left:3px solid #58c8ff;
    background:rgba(255,255,255,0.03);
    border-radius:8px;
}

button{
    margin-top:10px;
    padding:12px 18px;
    border:none;
    border-radius:10px;
    background:#0d6efd;
    color:white;
    cursor:pointer;
    font-weight:bold;
}

button:hover{
    background:#3390ff;
}

.footer{
    position:fixed;
    bottom:10px;
    width:100%;
    text-align:center;
    color:rgba(255,255,255,0.4);
    font-size:11px;
}

</style>

</head>

<body>

<div class="bg"></div>

<div class="header">
IOTEC CONTROL TOWER
</div>

<div class="feed">
<div class="feed-track" id="feed-track"></div>
</div>

<div class="main">

<div id="payments"></div>

<div class="panel">

<div class="box">

<h2>LIVE OPERATIONAL STATUS</h2>

<div class="live">
<span class="dot"></span>
TOWER ONLINE
</div>

<div class="live">
<span class="dot"></span>
SOCKET CONNECTED
</div>

<div class="live">
<span class="dot"></span>
REALTIME ACTIVE
</div>

<div class="live">
<span class="dot"></span>
BROADCAST ONLINE
</div>

<button onclick="openSector('EXECUTIVE')">
EXECUTIVE FLOOR
</button>

<button onclick="openSector('SATELLITE')">
SATELLITE SYSTEMS
</button>

</div>

<div class="box">

<h2>LIVE EVENT STREAM</h2>

<div id="events"></div>

</div>

</div>

</div>

<div class="footer">
IOTEC / IBEX ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ REALTIME CONTROL TOWER
</div>

<script>

const socket = io();

const payments =
    document.getElementById("payments");

const events =
    document.getElementById("events");

const feed =
    document.getElementById("feed-track");

function addPayment(data){

    const div =
        document.createElement("div");

    div.className = "grid";

    div.innerHTML = `

    <div>
        <div class="title">ID</div>
        <div class="value">${data.id}</div>
    </div>

    <div>
        <div class="title">CLIENTE</div>
        <div class="value">${data.client}</div>
    </div>

    <div>
        <div class="title">PAÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂS</div>
        <div class="value">${data.country}</div>
    </div>

    <div>
        <div class="title">SETOR</div>
        <div class="value">${data.sector}</div>
    </div>

    <div>
        <div class="title">PRODUTO</div>
        <div class="value">${data.product}</div>
    </div>

    <div>
        <div class="title">STATUS</div>
        <div class="value">
            <span class="dot"></span>
            ${data.status}
        </div>
    </div>

    `;

    payments.prepend(div);
}

function addEvent(text){

    const div =
        document.createElement("div");

    div.className = "event";

    div.innerHTML = text;

    events.prepend(div);
}

function addFeed(text){

    const span =
        document.createElement("span");

    span.innerHTML = "ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚Â " + text;

    feed.appendChild(span);
}

function openSector(name){

    addEvent(
        "OPENING: " + name
    );

    alert(
        "OPENING " + name
    );
}

socket.on(
    "payment",
    function(data){

        addPayment(data);

        addEvent(
            "NEW PAYMENT RECEIVED"
        );
    }
);

socket.on(
    "feed",
    function(data){

        addFeed(data.message);
    }
);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    pass

    return HTML

EVENTS = [

    "NEW CLIENT CONNECTED",
    "PAYMENT RECEIVED",
    "AI ROUTING ACTIVE",
    "SATELLITE SIGNAL ONLINE",
    "GOVTECH ACTIVE",
    "LIVE BROADCAST ACTIVE",
    "CONTROL TOWER SYNCHRONIZED"
]

def realtime():
    pass

    while True:
        pass

        socketio.emit(

            "feed",

            {
                "message":
                random.choice(EVENTS)
            }
        )

        payment = {

            "id":
            f"IBX-{random.randint(100,999)}",

            "client":
            "LIVE CLIENT",

            "country":
            random.choice([
                "BRAZIL",
                "USA",
                "GERMANY"
            ]),

            "sector":
            random.choice([
                "AUTOMATION",
                "GOVTECH",
                "MEDIA"
            ]),

            "product":
            random.choice([
                "AI SYSTEM",
                "OBSERVABILITY",
                "CONTROL GRID"
            ]),

            "status":
            "ONLINE"
        }

        socketio.emit(
            "payment",
            payment
        )

        time.sleep(4)

threading.Thread(
    target=realtime,
    daemon=True
).start()

print("")
print("================================================")
print(" IOTEC / IBEX LIVE SOCKET TOWER")
print("================================================")
print("")
print("REALTIME ENGINE: ACTIVE")
print("SOCKET.IO: ACTIVE")
print("LIVE FEED: ACTIVE")
print("LIVE PAYMENTS: ACTIVE")
print("")
print("================================================")
print(" OPEN:")
print(" http://127.0.0.1:3000")
print("================================================")
print("")

socketio.run(
    app,
    host="127.0.0.1",
    port=3000,
    debug=True,
    allow_unsafe_werkzeug=True,
    use_reloader=False
)
```


