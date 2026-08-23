import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC GLOBAL REALTY

# ENTERPRISE FULLSCREEN REALTY PLATFORM

# VERSAO: 1.0

# ============================================================



import os

from pathlib import Path



# ============================================================

# ESTRUTURA

# ============================================================



BASE = Path("C:/IOTEC_REALTY_ENTERPRISE")



PASTAS = [



    "frontend",

    "backend",

    "database",

    "assets",

    "assets/imoveis",

    "assets/banners",

    "logs",

    "config",

    "licenses",

    "exports"



]



# ============================================================

# CRIAR PASTAS

# ============================================================



for pasta in PASTAS:
    pass



    caminho = BASE / pasta

    caminho.mkdir(parents=True, exist_ok=True)



# ============================================================

# PACKAGE.JSON

# ============================================================



PACKAGE_JSON = r'''

{

  "name": "iotec-global-realty",

  "private": true,

  "version": "1.0.0",

  "type": "module",



  "scripts": {

    "dev": "vite",

    "build": "vite build",

    "preview": "vite preview"

  },



  "dependencies": {



    "react": "^18.2.0",

    "react-dom": "^18.2.0",

    "react-router-dom": "^6.22.0",

    "framer-motion": "^11.0.0",

    "lucide-react": "^0.344.0",

    "recharts": "^2.12.0"



  },



  "devDependencies": {



    "@vitejs/plugin-react": "^4.2.0",

    "typescript": "^5.2.2",

    "vite": "^5.1.0"



  }

}

'''



# ============================================================

# INDEX.HTML

# ============================================================



INDEX_HTML = r'''

<!DOCTYPE html>



<html lang="en">



<head>



<meta charset="UTF-8" />

<meta name="viewport" content="width=device-width, initial-scale=1.0" />



<title>IOTEC GLOBAL REALTY</title>



</head>



<body>



<div id="root"></div>



<script type="module" src="/src/main.jsx"></script>



</body>



</html>

'''



# ============================================================

# MAIN.JSX

# ============================================================



MAIN_JSX = r'''

import React from "react";

import ReactDOM from "react-dom/client";



import "./style.css";



function App() {



    return (



        <div className="app">



            <header className="topbar">



                <div className="logo">



                    IOTEC GLOBAL REALTY



                </div>



                <div className="menu">



                    <button>Comprar</button>

                    <button>Alugar</button>

                    <button>Luxury</button>

                    <button>Commercial</button>

                    <button>Investments</button>



                </div>



            </header>



            <section className="hero">



                <div className="overlay">



                    <h1>



                        InteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia ImobiliÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ria Internacional



                    </h1>



                    <p>



                        Plataforma premium para gestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o,

                        intermediaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e exposiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de ativos.



                    </p>



                    <div className="search">



                        <input

                            placeholder="Buscar imÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³veis, regiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes, ativos..."

                        />



                        <button>



                            EXPLORAR



                        </button>



                    </div>



                </div>



            </section>



            <section className="dashboard">



                <div className="card">



                    <h2>Ativos</h2>

                    <span>2.840</span>



                </div>



                <div className="card">



                    <h2>Leads</h2>

                    <span>421</span>



                </div>



                <div className="card">



                    <h2>ComissÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</h2>

                    <span>US$ 182.000</span>



                </div>



                <div className="card">



                    <h2>Luxury</h2>

                    <span>92 imÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³veis</span>



                </div>



            </section>



            <section className="imoveis">



                <div className="imovel">



                    <img

                        src="https://images.unsplash.com/photo-1568605114967-8130f3a36994"

                    />



                    <div className="info">



                        <h3>Miami Ocean Residence</h3>



                        <p>



                            Luxury Residence ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Miami



                        </p>



                        <span>



                            US$ 2.800.000



                        </span>



                    </div>



                </div>



                <div className="imovel">



                    <img

                        src="https://images.unsplash.com/photo-1600585154526-990dced4db0d"

                    />



                    <div className="info">



                        <h3>Texas Commercial Center</h3>



                        <p>



                            Commercial Property ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Texas



                        </p>



                        <span>



                            US$ 4.200.000



                        </span>



                    </div>



                </div>



                <div className="imovel">



                    <img

                        src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c"

                    />



                    <div className="info">



                        <h3>Luxury Hills Mansion</h3>



                        <p>



                            Beverly Hills ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ California



                        </p>



                        <span>



                            US$ 8.900.000



                        </span>



                    </div>



                </div>



            </section>



        </div>



    );



}



ReactDOM.createRoot(

    document.getElementById("root")

).render(<App />);

'''



# ============================================================

# STYLE.CSS

# ============================================================



STYLE_CSS = r'''

* {



    margin: 0;

    padding: 0;

    box-sizing: border-box;



}



body {



    background: #050505;

    color: white;

    font-family: Arial, sans-serif;

    overflow-x: hidden;



}



.app {



    width: 100%;

    min-height: 100vh;



}



.topbar {



    width: 100%;

    height: 90px;



    display: flex;

    justify-content: space-between;

    align-items: center;



    padding: 0 40px;



    position: fixed;

    top: 0;



    background: rgba(0,0,0,0.65);



    backdrop-filter: blur(12px);



    z-index: 999;



}



.logo {



    font-size: 26px;

    font-weight: bold;

    letter-spacing: 2px;



}



.menu {



    display: flex;

    gap: 12px;



}



.menu button {



    background: transparent;

    border: 1px solid #444;



    color: white;



    padding: 12px 20px;



    border-radius: 12px;



    cursor: pointer;



}



.hero {



    width: 100%;

    height: 100vh;



    background-image:

    url("https://images.unsplash.com/photo-1505693416388-ac5ce068fe85");



    background-size: cover;

    background-position: center;



    display: flex;

    align-items: center;

    justify-content: center;



}



.overlay {



    width: 100%;

    height: 100%;



    background: rgba(0,0,0,0.55);



    display: flex;

    flex-direction: column;



    justify-content: center;

    align-items: center;



    text-align: center;



    padding: 40px;



}



.overlay h1 {



    font-size: 70px;

    max-width: 1200px;



}



.overlay p {



    margin-top: 20px;



    font-size: 22px;

    color: #cfcfcf;



}



.search {



    margin-top: 40px;



    display: flex;

    gap: 12px;



}



.search input {



    width: 500px;



    padding: 18px;



    border-radius: 14px;

    border: none;



    font-size: 18px;



}



.search button {



    background: #0a84ff;



    color: white;



    border: none;



    padding: 18px 28px;



    border-radius: 14px;



    cursor: pointer;



    font-weight: bold;



}



.dashboard {



    width: 100%;



    display: grid;



    grid-template-columns: repeat(4, 1fr);



    gap: 20px;



    padding: 60px;



}



.card {



    background: #111;



    border: 1px solid #222;



    border-radius: 20px;



    padding: 30px;



}



.card h2 {



    color: #999;



}



.card span {



    display: block;



    margin-top: 20px;



    font-size: 34px;

    font-weight: bold;



}



.imoveis {



    width: 100%;



    display: grid;



    grid-template-columns: repeat(3, 1fr);



    gap: 30px;



    padding: 60px;



}



.imovel {



    background: #111;



    border-radius: 20px;



    overflow: hidden;



    border: 1px solid #222;



}



.imovel img {



    width: 100%;

    height: 300px;



    object-fit: cover;



}



.info {



    padding: 20px;



}



.info h3 {



    font-size: 28px;



}



.info p {



    margin-top: 10px;



    color: #999;



}



.info span {



    display: block;



    margin-top: 20px;



    font-size: 24px;

    font-weight: bold;



}

'''



# ============================================================

# ESCREVER ARQUIVOS

# ============================================================



FRONTEND = BASE / "frontend"



(FRONTEND / "src").mkdir(parents=True, exist_ok=True)



with open(FRONTEND / "package.json", "w", encoding="utf-8") as f:
    pass

    f.write(PACKAGE_JSON)



with open(FRONTEND / "index.html", "w", encoding="utf-8") as f:
    pass

    f.write(INDEX_HTML)



with open(FRONTEND / "src/main.jsx", "w", encoding="utf-8") as f:
    pass

    f.write(MAIN_JSX)



with open(FRONTEND / "src/style.css", "w", encoding="utf-8") as f:
    pass

    f.write(STYLE_CSS)



# ============================================================

# POWERSHELL

# ============================================================



POWERSHELL = rf'''

cd "{FRONTEND}"



npm install



npm run dev

'''



with open(BASE / "INICIAR_FRONTEND.ps1", "w", encoding="utf-8") as f:
    pass

    f.write(POWERSHELL)



# ============================================================

# FINALIZAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



print("\n===================================================")

print(" IOTEC GLOBAL REALTY")

print(" ENTERPRISE PLATFORM GERADA")

print("===================================================")



print(f"\nBASE -> {BASE}")



print("\nESTRUTURA:")

for pasta in PASTAS:
    pass

    print(f" [+] {pasta}")



print("\nARQUIVOS:")

print(" [+] package.json")

print(" [+] index.html")

print(" [+] src/main.jsx")

print(" [+] src/style.css")

print(" [+] INICIAR_FRONTEND.ps1")



print("\n===================================================")

print(" EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

print("===================================================")



print("\n1. ABRIR POWERSHELL")

print("2. EXECUTAR:")

print(f'\ncd "{BASE}"')

print("\n3. RODAR:")

print("\npython NOME_DO_ARQUIVO.py")



print("\n4. DEPOIS:")

print("\n./INICIAR_FRONTEND.ps1")



print("\n===================================================")

print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO FINALIZADO")

print("===================================================")





