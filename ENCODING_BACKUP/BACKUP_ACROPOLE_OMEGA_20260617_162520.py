import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ACROPOLE OMEGA
# GLOBAL EDUCATIONAL OPERATING SYSTEM
# VERSION 4.0
# ============================================================

from pathlib import Path
import json

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ACROPOLE_OMEGA")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
    BASE / "frontend/assets",
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

        "nome": "IOTEC ACROPOLE OMEGA",
        "cnpj": "61.549.037/0001-68",

        "email":
        "iotec.bl@proton.me",

        "status":
        "ONLINE"

    },

    "usuarios": [

        {

            "nome":
            "Administrador",

            "tipo":
            "MASTER"

        }

    ],

    "planos": [

        {

            "nome": "BASIC",
            "valor": "US$ 900"

        },

        {

            "nome": "PRO",
            "valor": "US$ 3.200"

        },

        {

            "nome": "PREMIUM",
            "valor": "US$ 12.000"

        }

    ]

}

with open(

    BASE / "database/database.json",
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
# HTML
# ============================================================

INDEX = r"""
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>
ACROPOLE OMEGA
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<div class="background"></div>

<!-- LOGIN -->

<section
id="login"
class="login-screen">

    <div class="login-box">

        <h1>
            ACROPOLE OMEGA
        </h1>

        <p>

            Global Educational
            Operating System

        </p>

        <input
        placeholder="E-mail">

        <input
        type="password"
        placeholder="Senha">

        <button onclick="entrar()">

            ENTRAR

        </button>

    </div>

</section>

<!-- DASHBOARD -->

<section
id="dashboard"
class="dashboard hidden">

    <!-- SIDEBAR -->

    <aside class="sidebar">

        <div class="logo">

            <h1>
                ACRÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPOLE
            </h1>

            <span>
                OMEGA
            </span>

        </div>

        <button onclick="abrir('inicio')">
            InÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cio
        </button>

        <button onclick="abrir('ia')">
            IA Educacional
        </button>

        <button onclick="abrir('biblioteca')">
            Biblioteca
        </button>

        <button onclick="abrir('mapa')">
            Mapa Global
        </button>

        <button onclick="abrir('planos')">
            Planos
        </button>

        <button onclick="abrir('familias')">
            FamÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias
        </button>

        <button onclick="abrir('residencia')">
            ResidÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
        </button>

        <button onclick="abrir('mentores')">
            Mentores
        </button>

    </aside>

    <!-- MAIN -->

    <main class="main">

        <!-- HERO -->

        <section class="hero">

            <div class="overlay"></div>

            <div class="hero-content">

                <h1>

                    EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.
                    CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.
                    Futuro.

                </h1>

                <p>

                    Uma plataforma premium
                    internacional para famÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias,
                    estudantes e mentores.

                </p>

                <div class="search">

                    <input
                    id="pesquisa"
                    placeholder="
                    O que deseja aprender?
                    ">

                    <button onclick="explorar()">

                        EXPLORAR

                    </button>

                </div>

            </div>

        </section>

        <!-- STATS -->

        <section class="stats">

            <div class="card">

                <h2>250K+</h2>

                <p>
                    Estudantes
                </p>

            </div>

            <div class="card">

                <h2>5K+</h2>

                <p>
                    Mentores
                </p>

            </div>

            <div class="card">

                <h2>120+</h2>

                <p>
                    PaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ses
                </p>

            </div>

            <div class="card">

                <h2>98%</h2>

                <p>
                    AprovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
                </p>

            </div>

        </section>

        <!-- CAMADA -->

        <section
        id="camada"
        class="camada">

            <h1>

                Bem-vindo ÃƒÆ'Ã†â€™  AcrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pole Omega

            </h1>

            <p>

                Um ecossistema educacional
                internacional preparado para
                o futuro da aprendizagem.

            </p>

        </section>

    </main>

</section>

<script src="script.js"></script>

</body>

</html>
"""

# ============================================================
# CSS
# ============================================================

STYLE = r"""
* {

    margin: 0;
    padding: 0;
    box-sizing: border-box;

}

body {

    background: #050816;
    color: white;

    font-family: Arial;

    overflow-x: hidden;

}

.background {

    position: fixed;

    width: 100%;
    height: 100%;

    background:

    radial-gradient(
        circle at top left,
        rgba(0,120,255,0.18),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(255,215,0,0.05),
        transparent 30%
    );

    z-index: -1;

}

.hidden {

    display: none;

}

.login-screen {

    height: 100vh;

    display: flex;

    justify-content: center;
    align-items: center;

}

.login-box {

    width: 420px;

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    padding: 50px;

    border-radius: 28px;

    backdrop-filter: blur(20px);

}

.login-box h1 {

    font-size: 42px;

    color: gold;

    margin-bottom: 20px;

}

.login-box p {

    opacity: 0.7;

    margin-bottom: 30px;

}

.login-box input {

    width: 100%;

    padding: 18px;

    margin-bottom: 18px;

    border: none;

    border-radius: 14px;

    background:

    rgba(255,255,255,0.08);

    color: white;

}

.login-box button {

    width: 100%;

    padding: 18px;

    border: none;

    border-radius: 14px;

    background:

    linear-gradient(
        135deg,
        #0077ff,
        #00d4ff
    );

    color: white;

    font-weight: bold;

    cursor: pointer;

}

.dashboard {

    display: flex;

    min-height: 100vh;

}

.sidebar {

    width: 280px;

    padding: 40px 20px;

    background:

    rgba(255,255,255,0.03);

    border-right:

    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

}

.logo {

    margin-bottom: 40px;

}

.logo h1 {

    color: gold;

}

.logo span {

    opacity: 0.7;

}

.sidebar button {

    width: 100%;

    margin-bottom: 14px;

    padding: 16px;

    border: none;

    border-radius: 14px;

    background:

    rgba(255,255,255,0.04);

    color: white;

    text-align: left;

    cursor: pointer;

    transition: 0.3s;

}

.sidebar button:hover {

    background:

    rgba(0,120,255,0.16);

    transform:
    translateX(6px);

}

.main {

    flex: 1;

    padding: 40px;

}

.hero {

    position: relative;

    height: 360px;

    border-radius: 30px;

    overflow: hidden;

    background:

    url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f');

    background-size: cover;
    background-position: center;

    margin-bottom: 30px;

}

.overlay {

    position: absolute;

    width: 100%;
    height: 100%;

    background:

    linear-gradient(
        rgba(0,0,0,0.4),
        rgba(0,0,0,0.8)
    );

}

.hero-content {

    position: relative;

    z-index: 2;

    padding: 60px;

}

.hero h1 {

    font-size: 64px;

    margin-bottom: 20px;

}

.hero p {

    font-size: 22px;

    opacity: 0.82;

    margin-bottom: 30px;

}

.search {

    display: flex;

    gap: 12px;

}

.search input {

    width: 420px;

    padding: 18px;

    border: none;

    border-radius: 14px;

    background:

    rgba(255,255,255,0.08);

    color: white;

}

.search button {

    padding: 18px 28px;

    border: none;

    border-radius: 14px;

    background:

    linear-gradient(
        135deg,
        #0077ff,
        #00d4ff
    );

    color: white;

    cursor: pointer;

    font-weight: bold;

}

.stats {

    display: grid;

    grid-template-columns:
    repeat(4,1fr);

    gap: 20px;

    margin-bottom: 30px;

}

.card {

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 40px;

    text-align: center;

    backdrop-filter: blur(18px);

}

.card h2 {

    font-size: 42px;

    margin-bottom: 10px;

}

.camada {

    min-height: 360px;

    background:

    rgba(255,255,255,0.03);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 40px;

}

.grid {

    display: grid;

    grid-template-columns:
    repeat(3,1fr);

    gap: 20px;

}

.item {

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    overflow: hidden;

}

.item img {

    width: 100%;
    height: 220px;

    object-fit: cover;

}

.item .content {

    padding: 20px;

}

.item h2 {

    margin-bottom: 12px;

}
"""

# ============================================================
# JS
# ============================================================

SCRIPT = r"""
function entrar() {

    document.getElementById(
        "login"
    ).classList.add("hidden");

    document.getElementById(
        "dashboard"
    ).classList.remove("hidden");

}

function explorar() {

    const valor =
    document.getElementById(
        "pesquisa"
    ).value;

    const camada =
    document.getElementById(
        "camada"
    );

    camada.innerHTML = `

    <h1 style="
    margin-bottom:20px;
    ">
    Trilha Inteligente
    </h1>

    <p style="
    margin-bottom:20px;
    opacity:0.8;
    ">

    O nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo criou um ambiente
    de aprendizagem para:

    <strong>
    ${valor}
    </strong>

    </p>

    <div class="grid">

        <div class="item">

            <img src="
            https://images.unsplash.com/photo-1509062522246-3755977927d7
            ">

            <div class="content">

                <h2>
                    Aula Especial
                </h2>

                <p>
                    ConteÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºdo premium
                    e mentoria avanÃƒÆ'Ã†â€™ada.
                </p>

            </div>

        </div>

        <div class="item">

            <img src="
            https://images.unsplash.com/photo-1451187580459-43490279c0fa
            ">

            <div class="content">

                <h2>
                    IA PedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica
                </h2>

                <p>
                    ExercÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cios e revisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
                    automatizadas.
                </p>

            </div>

        </div>

        <div class="item">

            <img src="
            https://images.unsplash.com/photo-1516321318423-f06f85e504b3
            ">

            <div class="content">

                <h2>
                    Biblioteca Global
                </h2>

                <p>
                    Livros, artigos
                    e cultura internacional.
                </p>

            </div>

        </div>

    </div>

    `;

}

function abrir(tipo) {

    const camada =
    document.getElementById(
        "camada"
    );

    if(tipo === "mapa") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        Mapa Global
        </h1>

        <div class="grid">

            <div class="card">

                <h2>
                    Brasil
                </h2>

                <p>
                    120K estudantes
                </p>

            </div>

            <div class="card">

                <h2>
                    EUA
                </h2>

                <p>
                    60K estudantes
                </p>

            </div>

            <div class="card">

                <h2>
                    JapÃƒÆ'Ã†â€™o
                </h2>

                <p>
                    22K estudantes
                </p>

            </div>

        </div>

        `;

    }

    if(tipo === "planos") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        Planos Premium
        </h1>

        <div class="grid">

            <div class="card">

                <h2>
                    BASIC
                </h2>

                <p>
                    US$ 900/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

            </div>

            <div class="card">

                <h2>
                    PRO
                </h2>

                <p>
                    US$ 3.200/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

            </div>

            <div class="card">

                <h2>
                    PREMIUM
                </h2>

                <p>
                    US$ 12.000/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

            </div>

        </div>

        `;

    }

}
"""

# ============================================================
# SERVER
# ============================================================

SERVER = r"""
import http.server
import socketserver
import webbrowser

PORT = 9494

Handler =
http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ("", PORT),
    Handler
) as httpd:

    print()
    print("===================================")
    print(" ACROPOLE OMEGA ONLINE")
    print("===================================")

    print()
    print(
        f"SERVER -> http://localhost:{PORT}"
    )

    webbrowser.open(
        f"http://localhost:{PORT}"
    )

    httpd.serve_forever()
"""

# ============================================================
# EXPORT
# ============================================================

with open(
    BASE / "frontend/index.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(INDEX)

with open(
    BASE / "frontend/style.css",
    "w",
    encoding="utf-8"
) as f:

    f.write(STYLE)

with open(
    BASE / "frontend/script.js",
    "w",
    encoding="utf-8"
) as f:

    f.write(SCRIPT)

with open(
    BASE / "frontend/server.py",
    "w",
    encoding="utf-8"
) as f:

    f.write(SERVER)

# ============================================================
# POWERSHELL
# ============================================================

PS1 = f'''
cd "{BASE / "frontend"}"

python server.py
'''

with open(
    BASE / "INICIAR_ACROPOLE.ps1",
    "w",
    encoding="utf-8"
) as f:

    f.write(PS1)

# ============================================================
# FINAL
# ============================================================

print()
print("===================================================")
print(" ACROPOLE OMEGA")
print(" GLOBAL EDUCATIONAL OPERATING SYSTEM")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("ARQUIVOS:")

print(" [+] index.html")
print(" [+] style.css")
print(" [+] script.js")
print(" [+] server.py")
print(" [+] database.json")
print(" [+] INICIAR_ACROPOLE.ps1")

print()
print("===================================================")
print(" EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O")
print("===================================================")

print()
print("1. ABRIR POWERSHELL")

print()
print("2. EXECUTAR")

print()
print("./INICIAR_ACROPOLE.ps1")

print()
print("3. ACESSAR")

print()
print("http://localhost:9494")

print()
print("===================================================")
print(" NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO FINALIZADO")
print("===================================================")



