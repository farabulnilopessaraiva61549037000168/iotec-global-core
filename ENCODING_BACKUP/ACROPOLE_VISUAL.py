import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ACROPOLE VISUAL ENGINE
# CINEMATIC EDUCATIONAL CIVILIZATION
# VERSION 3.0
# ============================================================

from pathlib import Path
import json

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ACROPOLE_VISUAL")

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    BASE,
    BASE / "frontend",
    BASE / "database",
    BASE / "assets",
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

        "nome": "IOTEC ACROPOLE GLOBAL",
        "cnpj": "61.549.037/0001-68",
        "status": "ONLINE"

    },

    "acropoles": [

        {

            "nome": "ACROPOLE ATHENA",
            "pais": "Brasil",
            "cidade": "Fortaleza",

            "residentes": 182,

            "status": "OPERACIONAL",

            "estilo":
            "Neo-Minimalismo Grego"

        },

        {

            "nome": "ACROPOLE HELIOS",
            "pais": "Estados Unidos",
            "cidade": "Miami",

            "residentes": 96,

            "status": "EXPANSAO",

            "estilo":
            "Futurismo Mediterraneo"

        },

        {

            "nome": "ACROPOLE ORION",
            "pais": "JapÃƒÆ'Ã†â€™o",
            "cidade": "Tokyo",

            "residentes": 61,

            "status": "PROJECAO",

            "estilo":
            "Minimalismo Tecnologico"

        }

    ]

}

# ============================================================
# EXPORT DATABASE
# ============================================================

with open(

    BASE / "database/acropole_data.json",
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

INDEX = """
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>
IOTEC ACROPOLE GLOBAL
</title>

<link rel="stylesheet"
href="style.css">

</head>

<body>

<div class="background"></div>

<header class="hero">

    <div class="overlay"></div>

    <div class="hero-content">

        <h1>
            IOTEC ACROPOLE GLOBAL
        </h1>

        <p>

            Futuristic Educational Civilization

        </p>

        <button>

            EXPLORAR ACRÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPOLES

        </button>

    </div>

</header>

<section class="stats">

    <div class="card">

        <h2>3</h2>

        <p>
            AcrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³poles Globais
        </p>

    </div>

    <div class="card">

        <h2>339</h2>

        <p>
            Residentes AcadÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªmicos
        </p>

    </div>

    <div class="card">

        <h2>27</h2>

        <p>
            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âgoras Ativas
        </p>

    </div>

    <div class="card">

        <h2>18</h2>

        <p>
            Bibliotecas Inteligentes
        </p>

    </div>

</section>

<section class="acropoles">

    <h1>
        ACRÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPOLES INTERNACIONAIS
    </h1>

    <div class="grid">

        <div class="acropole-card">

            <div class="image athena"></div>

            <div class="content">

                <h2>
                    ACROPOLE ATHENA
                </h2>

                <p>
                    Fortaleza ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ Brasil
                </p>

                <span>
                    Neo-Minimalismo Grego
                </span>

            </div>

        </div>

        <div class="acropole-card">

            <div class="image helios"></div>

            <div class="content">

                <h2>
                    ACROPOLE HELIOS
                </h2>

                <p>
                    Miami ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ EUA
                </p>

                <span>
                    Futurismo MediterrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢neo
                </span>

            </div>

        </div>

        <div class="acropole-card">

            <div class="image orion"></div>

            <div class="content">

                <h2>
                    ACROPOLE ORION
                </h2>

                <p>
                    Tokyo ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ JapÃƒÆ'Ã†â€™o
                </p>

                <span>
                    Minimalismo TecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gico
                </span>

            </div>

        </div>

    </div>

</section>

<section class="vision">

    <div class="vision-box">

        <h1>

            EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Como CivilizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o

        </h1>

        <p>

            Ambientes concebidos para formar
            mentes disciplinadas, criativas,
            culturais e tecnologicamente avanÃƒÆ'Ã†â€™adas.

            NÃƒÆ'Ã†â€™o apenas escolas.

            AcrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³poles vivas.

        </p>

    </div>

</section>

</body>

</html>
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

}

.background {

    position: fixed;

    width: 100%;
    height: 100%;

    background:

    radial-gradient(
        circle at top left,
        rgba(0,120,255,0.16),
        transparent 30%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(0,255,200,0.08),
        transparent 30%
    );

    z-index: -1;

}

.hero {

    height: 100vh;

    position: relative;

    display: flex;

    justify-content: center;
    align-items: center;

    text-align: center;

}

.overlay {

    position: absolute;

    width: 100%;
    height: 100%;

    background:

    linear-gradient(

        to bottom,
        rgba(0,0,0,0.2),
        rgba(0,0,0,0.8)

    );

}

.hero-content {

    position: relative;
    z-index: 2;

}

.hero h1 {

    font-size: 78px;
    margin-bottom: 20px;

}

.hero p {

    font-size: 24px;
    opacity: 0.8;

    margin-bottom: 40px;

}

.hero button {

    padding: 18px 42px;

    border: none;

    border-radius: 18px;

    background:

    linear-gradient(

        135deg,
        rgba(0,140,255,0.8),
        rgba(0,255,200,0.5)

    );

    color: white;

    font-size: 18px;

    cursor: pointer;

}

.stats {

    display: grid;

    grid-template-columns:
    repeat(4,1fr);

    gap: 20px;

    padding: 80px;

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

    font-size: 52px;
    margin-bottom: 14px;

}

.acropoles {

    padding: 80px;

}

.acropoles h1 {

    font-size: 52px;
    margin-bottom: 40px;

}

.grid {

    display: grid;

    grid-template-columns:
    repeat(3,1fr);

    gap: 30px;

}

.acropole-card {

    overflow: hidden;

    border-radius: 28px;

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(20px);

    transition: 0.4s;

}

.acropole-card:hover {

    transform:
    translateY(-10px);

}

.image {

    height: 320px;

    background-size: cover;
    background-position: center;

}

.athena {

    background-image:

    linear-gradient(
        rgba(0,0,0,0.3),
        rgba(0,0,0,0.5)
    ),

    url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1');

}

.helios {

    background-image:

    linear-gradient(
        rgba(0,0,0,0.3),
        rgba(0,0,0,0.5)
    ),

    url('https://images.unsplash.com/photo-1494526585095-c41746248156');

}

.orion {

    background-image:

    linear-gradient(
        rgba(0,0,0,0.3),
        rgba(0,0,0,0.5)
    ),

    url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');

}

.content {

    padding: 30px;

}

.content h2 {

    font-size: 30px;
    margin-bottom: 12px;

}

.content p {

    opacity: 0.7;
    margin-bottom: 14px;

}

.content span {

    opacity: 0.8;

}

.vision {

    padding: 120px 80px;

}

.vision-box {

    padding: 80px;

    border-radius: 34px;

    background:

    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

}

.vision-box h1 {

    font-size: 54px;
    margin-bottom: 30px;

}

.vision-box p {

    font-size: 22px;
    line-height: 1.8;

    opacity: 0.82;

}
"""

# ============================================================
# SERVER
# ============================================================

SERVER = """
import http.server
import socketserver
import webbrowser

PORT = 8888

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(
    ('', PORT),
    Handler
) as httpd:

    print()
    print('===================================================')
    print(' IOTEC ACROPOLE VISUAL')
    print('===================================================')

    print()
    print(f'SERVER -> http://localhost:{PORT}')

    webbrowser.open(
        f'http://localhost:{PORT}'
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

) as arquivo:

    arquivo.write(INDEX)

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

) as arquivo:

    arquivo.write(PS1)

# ============================================================
# FINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC ACROPOLE VISUAL ENGINE")
print("===================================================")

print()
print(f"BASE -> {BASE}")

print()
print("ARQUIVOS:")

print(" [+] index.html")
print(" [+] style.css")
print(" [+] server.py")
print(" [+] acropole_data.json")
print(" [+] INICIAR_ACROPOLE.ps1")

print()
print("===================================================")
print(" EXECUCAO")
print("===================================================")

print()
print("1. ABRIR POWERSHELL")

print()
print("2. EXECUTAR")

print()
print("./INICIAR_ACROPOLE.ps1")

print()
print("3. ABRIR")

print()
print("http://localhost:8888")

print()
print("===================================================")
print(" NUCLEO FINALIZADO")
print("===================================================")



