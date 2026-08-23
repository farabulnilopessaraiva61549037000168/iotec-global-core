import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC NEXUS REALTIME SYNC
# LIVE GOVERNANCE INTEGRATION ENGINE
# ============================================================

from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path(
    "C:/IOTEC_NEXUS_REALTIME"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    "frontend",
    "governance",
    "logs"

]

for pasta in PASTAS:
    pass

    (
        BASE / pasta
    ).mkdir(

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
IOTEC NEXUS REALTIME
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<div class="overlay"></div>

<header>

<h1>
IOTEC NEXUS REALTIME
</h1>

<p>
LIVE GOVERNANCE SYSTEM
</p>

</header>

<section class="dashboard">

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

<h2>UPTIME</h2>

<div id="uptime">
0h
</div>

</div>

<div class="card">

<h2>STATUS</h2>

<div id="status">
ONLINE
</div>

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

    font-family:Arial;

    color:white;

}

.overlay{

    position:fixed;

    width:100%;
    height:100%;

    background:
    rgba(0,0,0,0.72);

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

    font-size:55px;

    letter-spacing:4px;

}

.dashboard{

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

    border-radius:25px;

    padding:40px;

    backdrop-filter:
    blur(10px);

    text-align:center;

}

.card h2{

    margin-bottom:20px;

}

.card div{

    font-size:50px;

    font-weight:bold;

}

"""

# ============================================================
# JAVASCRIPT
# ============================================================

JS = """

async function update(){

    try{

        const response =
        await fetch(
            '../logs/live_metrics.json'
        )

        const data =
        await response.json()

        document
        .getElementById('cpu')
        .innerHTML =
        data.cpu + '%'

        document
        .getElementById('ram')
        .innerHTML =
        data.ram + '%'

        document
        .getElementById('uptime')
        .innerHTML =
        data.uptime

        document
        .getElementById('status')
        .innerHTML =
        data.status

    }

    catch{

        console.log(
            'ERRO METRICS'
        )

    }

}

setInterval(
    update,
    2000
)

update()

"""

# ============================================================
# GOVERNANCE
# ============================================================

GOVERNANCE = """

import psutil
import json
import time
from pathlib import Path
from datetime import datetime

BASE = Path(
    "C:/IOTEC_NEXUS_REALTIME/logs"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

START = time.time()

while True:
    pass

    uptime_seconds = int(

        time.time() - START

    )

    hours = uptime_seconds // 3600

    minutes = (

        uptime_seconds % 3600

    ) // 60

    uptime = f"{hours}h {minutes}m"

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    status = "ONLINE"

    if ram >= 90:
        pass

        status = "ALERTA"

    if cpu >= 80:
        pass

        status = "CRITICO"

    data = {

        "cpu": cpu,

        "ram": ram,

        "uptime": uptime,

        "status": status,

        "timestamp":
        str(datetime.now())

    }

    with open(

        BASE / "live_metrics.json",

        "w",
        encoding="utf-8"

    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )

    print()
    print("===================================")

    print(
        f"CPU -> {cpu}%"
    )

    print(
        f"RAM -> {ram}%"
    )

    print(
        f"UPTIME -> {uptime}"
    )

    print(
        f"STATUS -> {status}"
    )

    time.sleep(2)

"""

# ============================================================
# SERVER
# ============================================================

SERVER = """

import http.server
import socketserver
import webbrowser

PORT = 9998

Handler =
http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(

    ("", PORT),
    Handler

) as httpd:

    print()
    print("===================================")
    print(" IOTEC NEXUS REALTIME")
    print("===================================")

    print()
    print(
        "SERVER -> http://localhost:9998/frontend"
    )

    webbrowser.open(
        "http://localhost:9998/frontend"
    )

    httpd.serve_forever()

"""

# ============================================================
# POWERSHELL
# ============================================================

PS1 = """

Start-Process powershell -ArgumentList "python governance/governance.py"

Start-Sleep -Seconds 2

python server.py

"""

# ============================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
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

    BASE / "governance" / "governance.py",

    "w",
    encoding="utf-8"

) as f:

    f.write(GOVERNANCE)

with open(

    BASE / "server.py",

    "w",
    encoding="utf-8"

) as f:

    f.write(SERVER)

with open(

    BASE / "INICIAR_REALTIME.ps1",

    "w",
    encoding="utf-8"

) as f:

    f.write(PS1)

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC NEXUS REALTIME")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("PASTAS:")

for pasta in PASTAS:
    pass

    print(f" [+] {pasta}")

print()
print("ARQUIVOS:")

print(" [+] index.html")
print(" [+] style.css")
print(" [+] script.js")
print(" [+] governance.py")
print(" [+] server.py")
print(" [+] INICIAR_REALTIME.ps1")

print()
print("===================================================")
print(" EXECUCAO")
print("===================================================")

print()
print("1. ABRIR POWERSHELL")

print()
print("2. EXECUTAR")

print()
print("./INICIAR_REALTIME.ps1")

print()
print("3. ACESSAR")

print()
print("http://localhost:9998/frontend")

print()
print("===================================================")
print(" GOVERNANCA REALTIME ONLINE")
print("===================================================")


