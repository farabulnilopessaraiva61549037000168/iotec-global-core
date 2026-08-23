import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ACROPOLE COSMOS
# CINEMATIC EDUCATIONAL EXPERIENCE
# ============================================================

from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ACROPOLE_COSMOS")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
    BASE / "frontend/assets"

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
ACROPOLE COSMOS
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<!-- HERO -->

<section class="hero">

    <div class="overlay"></div>

    <img
    class="hero-image"
    src="
https://images.unsplash.com/photo-1523050854058-8df90110c9f1
    ">

    <header class="header">

        <div class="logo">

            <h1>
                ACROPOLE
            </h1>

            <span>
                COSMOS
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

            <button onclick="abrir('future')">
                Futuro
            </button>

        </nav>

    </header>

    <div class="hero-content">

        <span>
            GLOBAL EDUCATIONAL CIVILIZATION
        </span>

        <h1>

            EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Para
            Grandes Destinos

        </h1>

        <p>

            Uma plataforma internacional
            criada para desenvolver
            cientistas,
            engenheiros,
            lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­deres,
            pesquisadores
            e grandes intelectuais.

        </p>

        <div class="buttons">

            <button onclick="abrir('premium')">

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

        IA pedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica,
        materiais premium,
        experiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias sofisticadas,
        bibliotecas globais
        e acompanhamento familiar.

    </p>

</section>

<!-- GALLERY -->

<section class="gallery">

    <div class="item">

        <img src="
https://images.unsplash.com/photo-1509062522246-3755977927d7
        ">

    </div>

    <div class="item">

        <img src="
https://images.unsplash.com/photo-1451187580459-43490279c0fa
        ">

    </div>

    <div class="item">

        <img src="
https://images.unsplash.com/photo-1498050108023-c5249f4df085
        ">

    </div>

</section>

<!-- FOOTER -->

<footer class="footer">

    <h2>
        IOTEC ACROPOLE COSMOS
    </h2>

    <p>

        Plataforma internacional
        de educaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o premium.

    </p>

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

    background: #020617;
    color: white;

    font-family: Arial;

    overflow-x: hidden;

}

.hero {

    position: relative;

    height: 100vh;

    overflow: hidden;

}

.hero-image {

    position: absolute;

    width: 100%;
    height: 100%;

    object-fit: cover;

    animation:
    zoom 20s infinite alternate;

}

@keyframes zoom {

    from {

        transform: scale(1);

    }

    to {

        transform: scale(1.08);

    }

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

.header {

    position: relative;

    z-index: 10;

    display: flex;

    justify-content:
    space-between;

    align-items: center;

    padding: 30px 70px;

}

.logo h1 {

    color: gold;

    font-size: 34px;

}

.logo span {

    letter-spacing: 4px;

    opacity: 0.7;

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

    rgba(255,255,255,0.06);

    backdrop-filter: blur(16px);

    color: white;

    cursor: pointer;

    transition: 0.3s;

}

nav button:hover {

    background:

    rgba(0,120,255,0.18);

}

.hero-content {

    position: relative;

    z-index: 5;

    max-width: 900px;

    padding: 140px 80px;

}

.hero-content span {

    color: gold;

    letter-spacing: 5px;

}

.hero-content h1 {

    font-size: 92px;

    line-height: 1.05;

    margin-top: 20px;
    margin-bottom: 30px;

}

.hero-content p {

    font-size: 24px;

    opacity: 0.82;

    line-height: 1.6;

    margin-bottom: 40px;

}

.buttons {

    display: flex;

    gap: 18px;

}

.buttons button {

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

.buttons button:hover {

    transform: scale(1.04);

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

    border-radius: 30px;

    padding: 50px;

    text-align: center;

    backdrop-filter: blur(18px);

}

.card h2 {

    font-size: 56px;

    margin-bottom: 14px;

}

.camada {

    margin: 40px 80px;

    min-height: 320px;

    padding: 70px;

    border-radius: 36px;

    background:

    rgba(255,255,255,0.03);

    border:

    1px solid rgba(255,255,255,0.08);

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

.gallery {

    display: grid;

    grid-template-columns:
    repeat(3,1fr);

    gap: 24px;

    padding: 80px;

}

.item {

    overflow: hidden;

    border-radius: 28px;

}

.item img {

    width: 100%;
    height: 320px;

    object-fit: cover;

    transition: 0.5s;

}

.item img:hover {

    transform: scale(1.06);

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

        <p>

        SupervisÃƒÆ'Ã†â€™o familiar,
        portfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³lios fÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­sicos,
        IA pedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica
        e desenvolvimento intelectual.

        </p>

        `;

    }

    if(tipo === "ia") {

        camada.innerHTML = `

        <h1 style="
        margin-bottom:30px;
        ">
        IA EDUCACIONAL
        </h1>

        <p>

        O nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo cria:
        aulas,
        revisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes,
        simulados,
        cronogramas,
        trilhas
        e experiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias inteligentes.

        </p>

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

PORT = 9797

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ("", PORT),
    Handler
) as httpd:

    print()
    print("===================================")
    print(" ACROPOLE COSMOS ONLINE")
    print("===================================")

    print()
    print(
        "SERVER -> http://localhost:9797"
    )

    webbrowser.open(
        "http://localhost:9797"
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
print(" ACROPOLE COSMOS")
print(" CINEMATIC EDUCATIONAL EXPERIENCE")
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
print("http://localhost:9797")

print()
print("===================================================")
print(" NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO FINALIZADO")
print("===================================================")



