import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC REALTIME EXECUTIVE CORE
# ENTERPRISE LIVE DASHBOARD
# VERSAO 3.0
# ============================================================

import os
import json
from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_REALTIME_EXECUTIVE_CORE")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
    BASE / "backend",
    BASE / "database",
    BASE / "logs",
    BASE / "exports"

]

for pasta in PASTAS:
    pass

    pasta.mkdir(
        parents=True,
        exist_ok=True
    )

# ============================================================
# DATABASE
# ============================================================

DATABASE = {

    "empresa": {

        "nome": "IOTEC GLOBAL REALTY",
        "cnpj": "61.549.037/0001-68",
        "email": "iotec.bl@proton.me"

    },

    "receita_global": 2483912,

    "clientes_ativos": 182,

    "operacoes_ativas": 58,

    "operacoes": [

        {

            "pais": "Estados Unidos",
            "cidade": "Miami",
            "categoria": "Luxury",
            "ticket": "US$ 82.000"

        },

        {

            "pais": "Europa",
            "cidade": "Amsterdam",
            "categoria": "Port Logistics",
            "ticket": "US$ 128.000"

        },

        {

            "pais": "Brasil",
            "cidade": "SÃƒÆ'Ã†â€™o Paulo",
            "categoria": "Commercial",
            "ticket": "US$ 34.000"

        }

    ]

}

# ============================================================
# EXPORT DATABASE
# ============================================================

with open(

    BASE / "database/live_data.json",
    "w",
    encoding="utf-8"

) as arquivo:

    json.dump(

        DATABASE,
        arquivo,
        indent=4,
        ensure_ascii=False

    )

# ============================================================
# FASTAPI BACKEND
# ============================================================

BACKEND = """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.get("/")

def home():
    pass

    return {

        "status": "ONLINE",
        "nucleus": "ACTIVE"

    }

@app.get("/dashboard")

def dashboard():
    pass

    with open(

        "../database/live_data.json",
        "r",
        encoding="utf-8"

    ) as arquivo:

        dados = json.load(arquivo)

    return dados
"""

# ============================================================
# FRONTEND
# ============================================================

INDEX = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>IOTEC REALTIME EXECUTIVE CORE</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<div class="background"></div>

<div class="layout">

    <aside class="sidebar">

        <h1>IOTEC</h1>

        <div class="menu">

            <button>GLOBAL</button>
            <button>ANALYTICS</button>
            <button>CLIENTS</button>
            <button>OPERATIONS</button>
            <button>SECURITY</button>
            <button>MONITOR</button>

        </div>

    </aside>

    <main class="main">

        <header class="topbar">

            <div>

                <h2>
                    REALTIME EXECUTIVE CORE
                </h2>

                <p>
                    Enterprise Operational Intelligence
                </p>

            </div>

            <div class="status">

                ONLINE

            </div>

        </header>

        <section class="cards">

            <div class="card">

                <h3>
                    GLOBAL REVENUE
                </h3>

                <h1 id="revenue">

                    ...

                </h1>

            </div>

            <div class="card">

                <h3>
                    ACTIVE CLIENTS
                </h3>

                <h1 id="clients">

                    ...

                </h1>

            </div>

            <div class="card">

                <h3>
                    ACTIVE OPERATIONS
                </h3>

                <h1 id="operations">

                    ...

                </h1>

            </div>

        </section>

        <section class="content">

            <div class="table-box">

                <h2>
                    GLOBAL OPERATIONS
                </h2>

                <table>

                    <thead>

                        <tr>

                            <th>Country</th>
                            <th>City</th>
                            <th>Category</th>
                            <th>Ticket</th>

                        </tr>

                    </thead>

                    <tbody id="tableBody">

                    </tbody>

                </table>

            </div>

            <div class="map-box">

                <h2>
                    WORLD OPERATIONS
                </h2>

                <div class="map">

                    LIVE GLOBAL MAP

                </div>

            </div>

        </section>

    </main>

</div>

<script src="script.js"></script>

</body>

</html>
"""

# ============================================================
# SCRIPT JS
# ============================================================

SCRIPT = """
async function carregarDashboard() {

    const resposta = await fetch(
        'http://127.0.0.1:8000/dashboard'
    );

    const dados = await resposta.json();

    document.getElementById(
        'revenue'
    ).innerText =
    'US$ ' + dados.receita_global;

    document.getElementById(
        'clients'
    ).innerText =
    dados.clientes_ativos;

    document.getElementById(
        'operations'
    ).innerText =
    dados.operacoes_ativas;

    const tabela =
    document.getElementById(
        'tableBody'
    );

    tabela.innerHTML = '';

    dados.operacoes.forEach(

        item => {

            tabela.innerHTML += `

            <tr>

                <td>${item.pais}</td>
                <td>${item.cidade}</td>
                <td>${item.categoria}</td>
                <td>${item.ticket}</td>

            </tr>

            `;

        }

    );

}

carregarDashboard();

setInterval(
    carregarDashboard,
    5000
);
"""

# ============================================================
# STYLE
# ============================================================

STYLE = """
* {

    margin: 0;
    padding: 0;
    box-sizing: border-box;

}

body {

    background: #050505;
    color: white;
    font-family: Arial;
    overflow: hidden;

}

.background {

    position: fixed;

    width: 100%;
    height: 100%;

    background:

    radial-gradient(
        circle at top left,
        rgba(0,140,255,0.18),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(0,255,200,0.08),
        transparent 30%
    );

    z-index: -1;

}

.layout {

    display: flex;
    width: 100vw;
    height: 100vh;

}

.sidebar {

    width: 250px;

    background: rgba(12,12,12,0.94);

    border-right:
    1px solid rgba(255,255,255,0.08);

    padding: 30px;

    backdrop-filter: blur(20px);

}

.sidebar h1 {

    font-size: 36px;
    margin-bottom: 40px;

}

.menu {

    display: flex;
    flex-direction: column;
    gap: 16px;

}

.menu button {

    background: rgba(255,255,255,0.04);

    border: none;

    color: white;

    padding: 18px;

    border-radius: 14px;

    cursor: pointer;

    transition: 0.3s;

}

.menu button:hover {

    background:
    rgba(0,140,255,0.25);

}

.main {

    flex: 1;
    padding: 30px;

}

.topbar {

    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 30px;

}

.topbar h2 {

    font-size: 38px;

}

.topbar p {

    opacity: 0.7;
    margin-top: 8px;

}

.status {

    background:
    rgba(0,255,120,0.18);

    padding: 14px 24px;

    border-radius: 14px;

}

.cards {

    display: flex;
    gap: 20px;

    margin-bottom: 30px;

}

.card {

    flex: 1;

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    padding: 30px;

    border-radius: 24px;

    backdrop-filter: blur(20px);

}

.card h3 {

    opacity: 0.7;
    margin-bottom: 18px;

}

.card h1 {

    font-size: 42px;

}

.content {

    display: flex;
    gap: 20px;

    height: 60vh;

}

.table-box {

    flex: 1.2;

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 24px;

}

table {

    width: 100%;
    margin-top: 20px;

    border-collapse: collapse;

}

th, td {

    padding: 18px;
    text-align: left;

}

tr {

    border-bottom:
    1px solid rgba(255,255,255,0.06);

}

.map-box {

    flex: 1;

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 24px;

}

.map {

    width: 100%;
    height: 90%;

    margin-top: 20px;

    border-radius: 22px;

    background:

    linear-gradient(

        135deg,
        rgba(0,140,255,0.24),
        rgba(0,255,200,0.08)

    );

    display: flex;

    justify-content: center;
    align-items: center;

    font-size: 24px;

}
"""

# ============================================================
# SERVER
# ============================================================

SERVER = """
import http.server
import socketserver
import webbrowser

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ('', PORT),
    Handler
) as httpd:

    print()
    print('===================================================')
    print(' IOTEC REALTIME EXECUTIVE CORE')
    print('===================================================')

    print()
    print(f'SERVER -> http://localhost:{PORT}')

    webbrowser.open(
        f'http://localhost:{PORT}'
    )

    httpd.serve_forever()
"""

# ============================================================
# PS1 FRONT
# ============================================================

PS1_FRONT = f'''
cd "{BASE / "frontend"}"

python server.py
'''

# ============================================================
# PS1 BACK
# ============================================================

PS1_BACK = f'''
cd "{BASE / "backend"}"

python -m uvicorn main:app --reload
'''

# ============================================================
# EXPORT
# ============================================================

with open(

    BASE / "backend/main.py",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(BACKEND)

# ============================================================

with open(

    BASE / "frontend/index.html",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(INDEX)

# ============================================================

with open(

    BASE / "frontend/script.js",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(SCRIPT)

# ============================================================

with open(

    BASE / "frontend/style.css",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(STYLE)

# ============================================================

with open(

    BASE / "frontend/server.py",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(SERVER)

# ============================================================

with open(

    BASE / "INICIAR_FRONTEND.ps1",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(PS1_FRONT)

# ============================================================

with open(

    BASE / "INICIAR_BACKEND.ps1",
    "w",
    encoding="utf-8"

) as arquivo:

    arquivo.write(PS1_BACK)

# ============================================================
# FINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC REALTIME EXECUTIVE CORE")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("ARQUIVOS:")

print(" [+] backend/main.py")
print(" [+] frontend/index.html")
print(" [+] frontend/script.js")
print(" [+] frontend/style.css")
print(" [+] frontend/server.py")
print(" [+] live_data.json")
print(" [+] INICIAR_FRONTEND.ps1")
print(" [+] INICIAR_BACKEND.ps1")

print()
print("===================================================")
print(" EXECUCAO")
print("===================================================")

print()
print("1. EXECUTAR BACKEND:")
print("   ./INICIAR_BACKEND.ps1")

print()
print("2. EXECUTAR FRONTEND:")
print("   ./INICIAR_FRONTEND.ps1")

print()
print("3. ABRIR:")
print("   http://localhost:8080")

print()
print("===================================================")
print(" NUCLEO FINALIZADO")
print("===================================================")



