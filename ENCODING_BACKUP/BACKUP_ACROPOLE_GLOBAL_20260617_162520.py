import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ACROPOLE GLOBAL
# LOGIN + MATRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCULA + DASHBOARD ENGINE
# VERSION 2.0
# ============================================================

from pathlib import Path
import json

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ACROPOLE_ENTERPRISE")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
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

    "usuarios": [

        {

            "nome": "Bruno Lopes",
            "tipo": "Administrador",
            "email": "iotec.bl@proton.me"

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
# INDEX
# ============================================================

INDEX = r"""
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>
ACROPOLE GLOBAL
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<div class="background"></div>

<!-- LOGIN -->

<section id="loginScreen"
class="login-screen">

    <div class="login-box">

        <h1>
            ACROPOLE GLOBAL
        </h1>

        <p>

            Plataforma Internacional
            de EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o AvanÃƒÆ'Ã†â€™ada

        </p>

        <input
        id="email"
        placeholder="E-mail">

        <input
        id="senha"
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

        <h1>
            ACRÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPOLE
        </h1>

        <button onclick="abrir('inicio')">
            InÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cio
        </button>

        <button onclick="abrir('planos')">
            Planos
        </button>

        <button onclick="abrir('ia')">
            IA Educacional
        </button>

        <button onclick="abrir('familias')">
            FamÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias
        </button>

        <button onclick="abrir('matricula')">
            MatrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cula
        </button>

        <button onclick="abrir('biblioteca')">
            Biblioteca
        </button>

    </aside>

    <!-- MAIN -->

    <main class="main">

        <!-- HERO -->

        <section class="hero">

            <div>

                <h1>

                    EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do Futuro

                </h1>

                <p>

                    Ambientes premium
                    para famÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias,
                    estudantes e mentores.

                </p>

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
                Bem-vindo ÃƒÆ'Ã†â€™  AcrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pole
            </h1>

            <p>

                EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o internacional,
                IA pedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica e
                civilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o intelectual.

            </p>

        </section>

    </main>

</section>

<script src="script.js"></script>

</body>

</html>
"""

# ============================================================
# STYLE
# ============================================================

STYLE = r"""
* {

    margin: 0;
    padding: 0;
    box-sizing: border-box;

}

body {

    background: #040816;
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
        rgba(255,215,0,0.06),
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

    margin-bottom: 20px;

    color: gold;

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

    width: 260px;

    padding: 40px 20px;

    background:

    rgba(255,255,255,0.03);

    border-right:

    1px solid rgba(255,255,255,0.08);

}

.sidebar h1 {

    margin-bottom: 40px;

    color: gold;

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

}

.main {

    flex: 1;

    padding: 40px;

}

.hero {

    height: 300px;

    border-radius: 28px;

    overflow: hidden;

    background:

    linear-gradient(
        rgba(0,0,0,0.5),
        rgba(0,0,0,0.7)
    ),

    url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1');

    background-size: cover;
    background-position: center;

    display: flex;
    align-items: center;

    padding: 50px;

    margin-bottom: 30px;

}

.hero h1 {

    font-size: 54px;

    margin-bottom: 20px;

}

.hero p {

    font-size: 20px;

    opacity: 0.8;

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

}

.card h2 {

    font-size: 42px;

    margin-bottom: 10px;

}

.camada {

    min-height: 320px;

    background:

    rgba(255,255,255,0.03);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 40px;

}

.plan-grid {

    display: grid;

    grid-template-columns:
    repeat(3,1fr);

    gap: 20px;

}

.plan {

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 30px;

}

.plan h2 {

    margin-bottom: 20px;

}

.plan button {

    width: 100%;

    margin-top: 20px;

    padding: 16px;

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

}
"""

# ============================================================
# SCRIPT
# ============================================================

SCRIPT = r"""
function entrar() {

    document.getElementById(
        "loginScreen"
    ).classList.add("hidden");

    document.getElementById(
        "dashboard"
    ).classList.remove("hidden");

}

function abrir(tipo) {

    const camada =
    document.getElementById(
        "camada"
    );

    if(tipo === "planos") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        Planos Internacionais
        </h1>

        <div class="plan-grid">

            <div class="plan">

                <h2>
                    BASIC
                </h2>

                <p>
                    US$ 900/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

                <br>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Biblioteca
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Disciplinas
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ IA BÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡sica
                </p>

                <button>

                    MATRICULAR

                </button>

            </div>

            <div class="plan">

                <h2>
                    PRO
                </h2>

                <p>
                    US$ 3.200/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

                <br>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ IA AvanÃƒÆ'Ã†â€™ada
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Mentoria
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Trilhas Inteligentes
                </p>

                <button>

                    MATRICULAR

                </button>

            </div>

            <div class="plan">

                <h2>
                    PREMIUM
                </h2>

                <p>
                    US$ 12.000/mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs
                </p>

                <br>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ResidÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Mentores Globais
                </p>

                <p>
                    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Ambiente Exclusivo
                </p>

                <button>

                    MATRICULAR

                </button>

            </div>

        </div>

        `;

    }

    if(tipo === "ia") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:20px;
        ">
        IA EDUCACIONAL
        </h1>

        <p style="
        margin-bottom:20px;
        opacity:0.8;
        ">

        O nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo cria automaticamente:
        aulas, exercÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cios,
        simulados e revisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.

        </p>

        <input
        id="pedido"
        placeholder="
        Ex: aprender cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lculo
        "
        style="
        width:100%;
        padding:18px;
        border:none;
        border-radius:14px;
        background:rgba(255,255,255,0.08);
        color:white;
        margin-bottom:20px;
        ">

        <button onclick="gerar()"
        style="
        padding:18px 30px;
        border:none;
        border-radius:14px;
        background:linear-gradient(
        135deg,
        #0077ff,
        #00d4ff
        );
        color:white;
        cursor:pointer;
        ">

        GERAR MATERIAL

        </button>

        <div
        id="resultado"
        style="
        margin-top:30px;
        "></div>

        `;

    }

}

function gerar() {

    const valor =
    document.getElementById(
        "pedido"
    ).value;

    document.getElementById(
        "resultado"
    ).innerHTML = `

    <div class="card">

        <h2>
            Material Gerado
        </h2>

        <p>

            A AcrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pole preparou
            uma trilha inteligente para:

            <strong>
            ${valor}
            </strong>

        </p>

        <br>

        <p>
            ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Aula Especial
        </p>

        <p>
            ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ExercÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cios
        </p>

        <p>
            ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Simulado
        </p>

        <p>
            ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ RevisÃƒÆ'Ã†â€™o Guiada
        </p>

    </div>

    `;

}
"""

# ============================================================
# SERVER
# ============================================================

SERVER = r"""
import http.server
import socketserver
import webbrowser

PORT = 9191

Handler =
http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ("", PORT),
    Handler
) as httpd:

    print()
    print("===================================")
    print(" ACROPOLE ENTERPRISE ONLINE")
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
print(" ACROPOLE ENTERPRISE")
print(" LOGIN + MATRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCULA + DASHBOARD")
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
print("http://localhost:9191")

print()
print("===================================================")
print(" NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO FINALIZADO")
print("===================================================")



