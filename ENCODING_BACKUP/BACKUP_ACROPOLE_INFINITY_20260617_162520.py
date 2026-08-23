import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ACROPOLE INFINITY
# CINEMATIC WEB EXPERIENCE
# ============================================================

from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ACROPOLE_INFINITY")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
    BASE / "frontend/assets",
    BASE / "logs"

]

for pasta in PASTAS:
    pass

    pasta.mkdir(
        parents=True,
        exist_ok=True
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
ACROPOLE INFINITY
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<!-- BACKGROUND -->

<div class="background"></div>

<!-- HEADER -->

<header class="header">

    <div class="logo">

        <h1>
            ACROPOLE
        </h1>

        <span>
            INFINITY
        </span>

    </div>

    <nav>

        <button onclick="abrir('familias')">
            FamÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias
        </button>

        <button onclick="abrir('ia')">
            IA
        </button>

        <button onclick="abrir('global')">
            Global
        </button>

        <button onclick="abrir('premium')">
            Premium
        </button>

        <button onclick="abrir('future')">
            Futuro
        </button>

    </nav>

</header>

<!-- HERO -->

<section class="hero">

    <div class="overlay"></div>

    <video autoplay muted loop playsinline>

        <source
        src="
https://cdn.coverr.co/videos/coverr-working-on-a-computer-5176/1080p.mp4
        "
        type="video/mp4">

    </video>

    <div class="hero-content">

        <span>
            GLOBAL EDUCATIONAL CIVILIZATION
        </span>

        <h1>

            O Futuro da EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
            ComeÃƒÆ'Ã†â€™a Aqui

        </h1>

        <p>

            Uma plataforma internacional
            gerida por inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia artificial,
            preparada para desenvolver
            cientistas,
            empresÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios,
            engenheiros,
            lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deres
            e grandes intelectuais.

        </p>

        <div class="hero-buttons">

            <button onclick="abrir('explorar')">

                EXPLORAR ACROPOLE

            </button>

            <button onclick="abrir('ia')">

                IA EDUCACIONAL

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

        <h2>120+</h2>

        <p>
            PaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ses
        </p>

    </div>

    <div class="card">

        <h2>5K+</h2>

        <p>
            Mentores
        </p>

    </div>

    <div class="card">

        <h2>98%</h2>

        <p>
            AprovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
        </p>

    </div>

</section>

<!-- EXPERIENCE -->

<section
id="camada"
class="camada">

    <h1>

        Uma Nova CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Educacional

    </h1>

    <p>

        Ambientes premium,
        IA pedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica,
        portfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lios fÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­sicos,
        bibliotecas globais,
        engenharia educacional
        e acompanhamento familiar.

    </p>

</section>

<!-- FOOTER -->

<footer class="footer">

    <h2>
        IOTEC ACROPOLE INFINITY
    </h2>

    <p>

        Plataforma internacional
        de educaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o premium.

    </p>

    <span>

        CNPJ:
        61.549.037/0001-68

    </span>

</footer>

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

    background: #030712;
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
        rgba(0,140,255,0.16),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(255,215,0,0.05),
        transparent 30%
    );

    z-index: -5;

}

.header {

    position: fixed;

    width: 100%;

    display: flex;

    justify-content:
    space-between;

    align-items: center;

    padding: 26px 70px;

    z-index: 100;

    background:

    rgba(0,0,0,0.18);

    backdrop-filter: blur(16px);

}

.logo h1 {

    font-size: 30px;

    color: gold;

}

.logo span {

    opacity: 0.7;

    letter-spacing: 4px;

}

nav {

    display: flex;

    gap: 14px;

}

nav button {

    padding: 14px 22px;

    border: none;

    border-radius: 16px;

    background:

    rgba(255,255,255,0.05);

    color: white;

    cursor: pointer;

    transition: 0.3s;

}

nav button:hover {

    background:

    rgba(0,140,255,0.18);

    transform:
    translateY(-2px);

}

.hero {

    position: relative;

    height: 100vh;

    overflow: hidden;

    display: flex;

    align-items: center;

    padding: 80px;

}

.hero video {

    position: absolute;

    width: 100%;
    height: 100%;

    object-fit: cover;

}

.overlay {

    position: absolute;

    width: 100%;
    height: 100%;

    background:

    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.88)
    );

    z-index: 1;

}

.hero-content {

    position: relative;

    z-index: 2;

    max-width: 900px;

}

.hero-content span {

    color: gold;

    letter-spacing: 4px;

}

.hero h1 {

    font-size: 92px;

    line-height: 1.05;

    margin-top: 20px;
    margin-bottom: 30px;

}

.hero p {

    font-size: 24px;

    opacity: 0.82;

    line-height: 1.6;

    margin-bottom: 40px;

}

.hero-buttons {

    display: flex;

    gap: 18px;

}

.hero-buttons button {

    padding: 22px 34px;

    border: none;

    border-radius: 18px;

    background:

    linear-gradient(
        135deg,
        #0066ff,
        #00c6ff
    );

    color: white;

    font-weight: bold;

    cursor: pointer;

    transition: 0.3s;

}

.hero-buttons button:hover {

    transform:
    scale(1.04);

}

.stats {

    display: grid;

    grid-template-columns:
    repeat(4,1fr);

    gap: 24px;

    padding: 80px;

}

.card {

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(16px);

    border-radius: 30px;

    padding: 50px;

    text-align: center;

}

.card h2 {

    font-size: 56px;

    margin-bottom: 14px;

}

.camada {

    margin: 40px 80px;

    min-height: 420px;

    padding: 70px;

    border-radius: 36px;

    background:

    rgba(255,255,255,0.03);

    border:

    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

}

.camada h1 {

    font-size: 64px;

    margin-bottom: 24px;

}

.camada p {

    font-size: 24px;

    opacity: 0.82;

    line-height: 1.7;

}

.grid {

    display: grid;

    grid-template-columns:
    repeat(3,1fr);

    gap: 24px;

}

.item {

    background:

    rgba(255,255,255,0.04);

    border:

    1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    overflow: hidden;

}

.item img {

    width: 100%;
    height: 240px;

    object-fit: cover;

}

.item .content {

    padding: 26px;

}

.item h2 {

    margin-bottom: 12px;

}

.footer {

    padding: 100px;

    text-align: center;

    opacity: 0.75;

}
"""

# ============================================================
# JS
# ============================================================

SCRIPT = r"""
function abrir(tipo) {

    const camada =
    document.getElementById(
        "camada"
    );

    if(tipo === "familias") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Familiar Premium
        </h1>

        <div class="grid">

            <div class="item">

                <img src="
https://images.unsplash.com/photo-1516627145497-ae6968895b74
                ">

                <div class="content">

                    <h2>
                        SupervisÃƒÆ'Ã†â€™o Familiar
                    </h2>

                    <p>

                        Pais acompanham
                        o desenvolvimento
                        intelectual dos filhos.

                    </p>

                </div>

            </div>

            <div class="item">

                <img src="
https://images.unsplash.com/photo-1503676260728-1c00da094a0b
                ">

                <div class="content">

                    <h2>
                        PortfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lios Premium
                    </h2>

                    <p>

                        Materiais fÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­sicos
                        sofisticados
                        e semestrais.

                    </p>

                </div>

            </div>

            <div class="item">

                <img src="
https://images.unsplash.com/photo-1522202176988-66273c2fd55f
                ">

                <div class="content">

                    <h2>
                        IA Educacional
                    </h2>

                    <p>

                        Trilhas inteligentes
                        personalizadas.

                    </p>

                </div>

            </div>

        </div>

        `;

    }

    if(tipo === "premium") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Intelectual
        </h1>

        <div class="grid">

            <div class="card">

                <h2>
                    Engenharia
                </h2>

            </div>

            <div class="card">

                <h2>
                    CiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
                </h2>

            </div>

            <div class="card">

                <h2>
                    LideranÃƒÆ'Ã†â€™a
                </h2>

            </div>

        </div>

        `;

    }

    if(tipo === "ia") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:24px;
        ">
        IA EDUCACIONAL
        </h1>

        <p style="
        margin-bottom:30px;
        opacity:0.82;
        ">

        O nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo cria:
        aulas,
        revisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes,
        simulados,
        cronogramas,
        trilhas
        e experiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias de aprendizagem.

        </p>

        <div class="card">

            <h2>
                Aprendizagem Adaptativa
            </h2>

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

PORT = 9696

Handler =
http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ("", PORT),
    Handler
) as httpd:

    print()
    print("===================================")
    print(" ACROPOLE INFINITY ONLINE")
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
print(" ACROPOLE INFINITY")
print(" CINEMATIC WEB EXPERIENCE")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("ARQUIVOS:")

print(" [+] index.html")
print(" [+] style.css")
print(" [+] script.js")
print(" [+] server.py")
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
print("http://localhost:9696")

print()
print("===================================================")
print(" NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO FINALIZADO")
print("===================================================")



