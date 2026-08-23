import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC GLOBAL REALTY CONNECTED PLATFORM
# VERSAO EXECUTAVEL
# ============================================================

import os
from pathlib import Path

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_GLOBAL_REALTY_CONNECTED")

FRONTEND = BASE / "frontend"
BACKEND = BASE / "backend"

# ============================================================
# PASTAS
# ============================================================

PASTAS = [

    FRONTEND,
    FRONTEND / "src",
    FRONTEND / "src/pages",

    BACKEND

]

for pasta in PASTAS:
    pass

    pasta.mkdir(parents=True, exist_ok=True)

# ============================================================
# PACKAGE JSON
# ============================================================

PACKAGE_JSON = """
{
  "name": "iotec-global-realty",
  "private": true,
  "version": "1.0.0",
  "type": "module",

  "scripts": {

    "dev": "vite",
    "build": "vite build"

  },

  "dependencies": {

    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.0"

  },

  "devDependencies": {

    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.1.0"

  }
}
"""

# ============================================================
# INDEX HTML
# ============================================================

INDEX_HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8" />

<meta name="viewport"
content="width=device-width, initial-scale=1.0" />

<title>IOTEC GLOBAL REALTY</title>

</head>

<body>

<div id="root"></div>

<script type="module" src="/src/main.jsx"></script>

</body>

</html>
"""

# ============================================================
# MAIN JSX
# ============================================================

MAIN_JSX = """
import React from "react";
import ReactDOM from "react-dom/client";

import {

BrowserRouter,
Routes,
Route,
Link

} from "react-router-dom";

import "./style.css";

function Home() {

    async function explorar() {

        const busca =
        document.getElementById("busca").value;

        const resposta =
        await fetch(
            `http://localhost:8000/search?q=${busca}`
        );

        const dados =
        await resposta.json();

        alert(JSON.stringify(dados));

    }

    return (

        <div>

            <section className="hero">

                <div className="overlay">

                    <h1>

                        IOTEC GLOBAL REALTY

                    </h1>

                    <p>

                        InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia ImobiliÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria Internacional

                    </p>

                    <div className="search">

                        <input
                            id="busca"
                            placeholder="Buscar imÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³veis..."
                        />

                        <button
                            onClick={explorar}
                        >

                            EXPLORAR

                        </button>

                    </div>

                </div>

            </section>

            <section className="menu-grid">

                <Link to="/buy">
                    Comprar
                </Link>

                <Link to="/rent">
                    Alugar
                </Link>

                <Link to="/luxury">
                    Luxury
                </Link>

                <Link to="/commercial">
                    Commercial
                </Link>

                <Link to="/investments">
                    Investments
                </Link>

            </section>

        </div>

    );

}

function Buy() {

    return (
        <h1 className="page">
            Comprar ImÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³veis
        </h1>
    );

}

function Rent() {

    return (
        <h1 className="page">
            Alugar ImÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³veis
        </h1>
    );

}

function Luxury() {

    return (
        <h1 className="page">
            Luxury Properties
        </h1>
    );

}

function Commercial() {

    return (
        <h1 className="page">
            Commercial Assets
        </h1>
    );

}

function Investments() {

    return (
        <h1 className="page">
            Investment Center
        </h1>
    );

}

function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Home />}
                />

                <Route
                    path="/buy"
                    element={<Buy />}
                />

                <Route
                    path="/rent"
                    element={<Rent />}
                />

                <Route
                    path="/luxury"
                    element={<Luxury />}
                />

                <Route
                    path="/commercial"
                    element={<Commercial />}
                />

                <Route
                    path="/investments"
                    element={<Investments />}
                />

            </Routes>

        </BrowserRouter>

    );

}

ReactDOM.createRoot(
    document.getElementById("root")
).render(<App />);
"""

# ============================================================
# STYLE CSS
# ============================================================

STYLE_CSS = """
* {

    margin: 0;
    padding: 0;
    box-sizing: border-box;

}

body {

    background: #050505;
    color: white;
    font-family: Arial;
    overflow-x: hidden;

}

.hero {

    width: 100%;
    height: 100vh;

    background-image:
    url('https://images.unsplash.com/photo-1505693416388-ac5ce068fe85');

    background-size: cover;
    background-position: center;

}

.overlay {

    width: 100%;
    height: 100%;

    background: rgba(0,0,0,0.65);

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

}

.overlay h1 {

    font-size: 72px;

}

.overlay p {

    margin-top: 20px;
    font-size: 22px;

}

.search {

    margin-top: 40px;

    display: flex;
    gap: 10px;

}

.search input {

    width: 420px;

    padding: 18px;

    border: none;
    border-radius: 14px;

}

.search button {

    padding: 18px 28px;

    border: none;

    border-radius: 14px;

    background: #0a84ff;

    color: white;

    cursor: pointer;

}

.menu-grid {

    width: 100%;

    display: flex;

    justify-content: center;

    gap: 20px;

    padding: 40px;

    background: #111;

}

.menu-grid a {

    color: white;

    text-decoration: none;

    border: 1px solid #333;

    padding: 16px 24px;

    border-radius: 12px;

}

.page {

    padding: 100px;

    font-size: 50px;

}
"""

# ============================================================
# BACKEND
# ============================================================

BACKEND_MAIN = """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

IMOVEIS = [

    {

        "id": 1,
        "titulo": "Miami Ocean Residence",
        "cidade": "Miami",
        "valor": "US$ 2.800.000"

    },

    {

        "id": 2,
        "titulo": "Luxury Hills Mansion",
        "cidade": "California",
        "valor": "US$ 8.900.000"

    }

]

@app.get("/")

def home():
    pass

    return {

        "status": "ONLINE",
        "empresa": "IOTEC GLOBAL REALTY"

    }

@app.get("/search")

def search(q: str = ""):
    pass

    resultados = []

    for item in IMOVEIS:
        pass

        if q.lower() in item["cidade"].lower():
            pass

            resultados.append(item)

    return {

        "query": q,
        "resultados": resultados

    }
"""

# ============================================================
# POWERSHELL
# ============================================================

POWERSHELL = f"""
cd "{FRONTEND}"

npm install

npm run dev
"""

BACKEND_PS = f"""
cd "{BACKEND}"

pip install fastapi uvicorn

uvicorn main:app --reload
"""

# ============================================================
# ESCREVER
# ============================================================

with open(FRONTEND / "package.json", "w", encoding="utf-8") as f:
    f.write(PACKAGE_JSON)

with open(FRONTEND / "index.html", "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)

with open(FRONTEND / "src/main.jsx", "w", encoding="utf-8") as f:
    f.write(MAIN_JSX)

with open(FRONTEND / "src/style.css", "w", encoding="utf-8") as f:
    f.write(STYLE_CSS)

with open(BACKEND / "main.py", "w", encoding="utf-8") as f:
    f.write(BACKEND_MAIN)

with open(BASE / "INICIAR_FRONTEND.ps1", "w", encoding="utf-8") as f:
    f.write(POWERSHELL)

with open(BASE / "INICIAR_BACKEND.ps1", "w", encoding="utf-8") as f:
    f.write(BACKEND_PS)

# ============================================================
# FINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC GLOBAL REALTY CONNECTED")
print("===================================================")

print()
print("BASE:")
print(BASE)

print()
print("FRONTEND:")
print(FRONTEND)

print()
print("BACKEND:")
print(BACKEND)

print()
print("ARQUIVOS GERADOS:")
print(" [+] package.json")
print(" [+] index.html")
print(" [+] main.jsx")
print(" [+] style.css")
print(" [+] backend/main.py")
print(" [+] INICIAR_FRONTEND.ps1")
print(" [+] INICIAR_BACKEND.ps1")

print()
print("===================================================")
print(" EXECUCAO")
print("===================================================")

print()
print("1. EXECUTE:")
print("   ./INICIAR_BACKEND.ps1")

print()
print("2. EM OUTRO TERMINAL:")
print("   ./INICIAR_FRONTEND.ps1")

print()
print("3. ACESSE:")
print("   http://localhost:5173")

print()
print("===================================================")
print(" NUCLEO FINALIZADO")
print("===================================================")


