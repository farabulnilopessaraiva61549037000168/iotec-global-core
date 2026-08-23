import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC ACROPOLE PRIME

# OFFICIAL WEBSITE ENGINE

# LUXURY EDUCATIONAL PLATFORM

# ============================================================



from pathlib import Path



# ============================================================

# BASE

# ============================================================



BASE = Path("C:/IOTEC_ACROPOLE_PRIME")



# ============================================================

# PASTAS

# ============================================================



PASTAS = [



    BASE,

    BASE / "frontend",

    BASE / "frontend/assets",

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

ACROPOLE PRIME

</title>



<link rel="stylesheet"

href="style.css">



</head>



<body>



<div class="background"></div>



<!-- HEADER -->



<header class="header">



    <div class="logo">



        <h1>

            ACROPOLE PRIME

        </h1>



        <span>

            GLOBAL EDUCATION

        </span>



    </div>



    <nav>



        <button onclick="abrir('familias')">

            FamÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­lias

        </button>



        <button onclick="abrir('metodo')">

            MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©todo

        </button>



        <button onclick="abrir('planos')">

            Planos

        </button>



        <button onclick="abrir('global')">

            Global

        </button>



        <button onclick="abrir('premium')">

            Premium

        </button>



    </nav>



</header>



<!-- HERO -->



<section class="hero">



    <div class="overlay"></div>



    <div class="hero-content">



        <h1>



            EducaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o para

            Grandes Destinos



        </h1>



        <p>



            Uma plataforma internacional

            preparada para desenvolver

            futuros cientistas,

            engenheiros,

            empresÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios,

            pesquisadores e lÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­deres.



        </p>



        <div class="hero-buttons">



            <button onclick="abrir('matricula')">



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

            PaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ses

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

            SatisfaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o

        </p>



    </div>



</section>



<!-- SECTION -->



<section

id="camada"

class="camada">



    <h1>



        A Nova CivilizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Educacional



    </h1>



    <p>



        Ambientes sofisticados,

        IA pedagÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³gica,

        materiais premium

        e acompanhamento global.



    </p>



</section>



<!-- FOOTER -->



<footer class="footer">



    <h2>

        IOTEC ACROPOLE PRIME

    </h2>



    <p>



        Plataforma internacional

        de educaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o premium.



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

        rgba(0,120,255,0.16),

        transparent 30%

    ),



    radial-gradient(

        circle at bottom right,

        rgba(255,215,0,0.05),

        transparent 30%

    );



    z-index: -1;



}



.header {



    position: fixed;



    width: 100%;



    display: flex;



    justify-content:

    space-between;



    align-items: center;



    padding: 24px 60px;



    background:



    rgba(0,0,0,0.25);



    backdrop-filter: blur(18px);



    z-index: 100;



}



.logo h1 {



    color: gold;



    font-size: 28px;



}



.logo span {



    opacity: 0.7;



    font-size: 14px;



}



nav {



    display: flex;



    gap: 14px;



}



nav button {



    padding: 14px 22px;



    border: none;



    border-radius: 14px;



    background:



    rgba(255,255,255,0.05);



    color: white;



    cursor: pointer;



    transition: 0.3s;



}



nav button:hover {



    background:



    rgba(0,120,255,0.16);



}



.hero {



    position: relative;



    height: 100vh;



    background:



    url('https://images.unsplash.com/photo-1519389950473-47ba0277781c');



    background-size: cover;

    background-position: center;



    display: flex;



    align-items: center;



    padding: 80px;



}



.overlay {



    position: absolute;



    width: 100%;

    height: 100%;



    background:



    linear-gradient(

        rgba(0,0,0,0.5),

        rgba(0,0,0,0.82)

    );



}



.hero-content {



    position: relative;



    z-index: 2;



    max-width: 900px;



}



.hero h1 {



    font-size: 84px;



    margin-bottom: 30px;



    line-height: 1.1;



}



.hero p {



    font-size: 24px;



    opacity: 0.82;



    margin-bottom: 40px;



}



.hero-buttons {



    display: flex;



    gap: 18px;



}



.hero-buttons button {



    padding: 20px 34px;



    border: none;



    border-radius: 18px;



    background:



    linear-gradient(

        135deg,

        #0077ff,

        #00d4ff

    );



    color: white;



    font-size: 16px;



    font-weight: bold;



    cursor: pointer;



}



.stats {



    display: grid;



    grid-template-columns:

    repeat(4,1fr);



    gap: 20px;



    padding: 60px;



}



.card {



    background:



    rgba(255,255,255,0.04);



    border:



    1px solid rgba(255,255,255,0.08);



    border-radius: 28px;



    padding: 50px;



    text-align: center;



    backdrop-filter: blur(18px);



}



.card h2 {



    font-size: 52px;



    margin-bottom: 14px;



}



.camada {



    margin: 40px 60px;



    padding: 60px;



    border-radius: 32px;



    background:



    rgba(255,255,255,0.03);



    border:



    1px solid rgba(255,255,255,0.08);



    min-height: 340px;



}



.camada h1 {



    font-size: 52px;



    margin-bottom: 20px;



}



.camada p {



    font-size: 22px;



    opacity: 0.82;



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



    padding: 24px;



}



.item h2 {



    margin-bottom: 12px;



}



.footer {



    padding: 80px;



    text-align: center;



    opacity: 0.8;



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

        EducaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Familiar Premium

        </h1>



        <div class="grid">



            <div class="item">



                <img src="

                https://images.unsplash.com/photo-1516627145497-ae6968895b74

                ">



                <div class="content">



                    <h2>

                        SupervisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Familiar

                    </h2>



                    <p>



                        Pais acompanham

                        o desenvolvimento

                        acadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªmico.



                    </p>



                </div>



            </div>



            <div class="item">



                <img src="

                https://images.unsplash.com/photo-1503676260728-1c00da094a0b

                ">



                <div class="content">



                    <h2>

                        Material Premium

                    </h2>



                    <p>



                        PortfÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³lios fÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­sicos,

                        aulas e simulados.



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

        CivilizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Intelectual

        </h1>



        <p style="

        margin-bottom:30px;

        opacity:0.8;

        ">



        Uma plataforma criada

        para desenvolver

        excelÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia intelectual.



        </p>



        <div class="grid">



            <div class="card">



                <h2>

                    Engenharia

                </h2>



            </div>



            <div class="card">



                <h2>

                    CiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia

                </h2>



            </div>



            <div class="card">



                <h2>

                    LideranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a

                </h2>



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



        A plataforma cria:

        aulas,

        simulados,

        revisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes,

        PDFs

        e trilhas inteligentes.



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



PORT = 9595



Handler =

http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(

    ("", PORT),

    Handler

) as httpd:



    print()

    print("===================================")

    print(" ACROPOLE PRIME ONLINE")

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

print(" ACROPOLE PRIME")

print(" OFFICIAL WEBSITE ENGINE")

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

print(" EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

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

print("http://localhost:9595")



print()

print("===================================================")

print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO FINALIZADO")

print("===================================================")







