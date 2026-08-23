import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC BL - GLOBAL SHOPPING PLATFORM V1
# ============================================================
# Portal institucional + shopping tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gico internacional
# ============================================================

from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>IOTEC BL | Construtora de Tecnologia e InovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:#050b18;
    color:#fff;
}

/* HEADER */
header{
    background:linear-gradient(90deg,#0a1a35,#07101f);
    padding:20px;
    text-align:center;
    border-bottom:1px solid rgba(255,255,255,0.1);
}

header h1{
    margin:0;
    font-size:28px;
    letter-spacing:2px;
}

/* HERO */
.hero{
    padding:80px;
    text-align:center;
}

.hero h2{
    font-size:40px;
}

.hero p{
    color:#aaa;
}

/* GRID */
.grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
    padding:40px;
}

/* CARD */
.card{
    background:rgba(255,255,255,0.05);
    padding:25px;
    border-radius:15px;
    transition:0.3s;
}

.card:hover{
    transform:scale(1.05);
    background:rgba(255,255,255,0.1);
}

/* BUTTON */
.btn{
    background:#00c3ff;
    color:#000;
    padding:10px 20px;
    border:none;
    margin-top:10px;
    cursor:pointer;
}

/* SECTION */
.section{
    padding:50px;
}

.title{
    font-size:28px;
    margin-bottom:20px;
}

/* FOOTER */
footer{
    text-align:center;
    padding:20px;
    color:#777;
}
</style>

</head>

<body>

<header>
    <h1>IOTEC BL - CONSTRUTORA DE TECNOLOGIA E INOVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES</h1>
</header>

<div class="hero">
    <h2>Shopping Global de Tecnologia e SoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes Inteligentes</h2>
    <p>Produtos, sistemas e soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes para todos os setores da economia mundial</p>
</div>

<div class="section">
    <div class="title">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Portas Globais</div>
    <div class="grid">
        <div class="card">Brasil</div>
        <div class="card">AmÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rica do Norte</div>
        <div class="card">Europa</div>
        <div class="card">ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âsia</div>
        <div class="card">Oriente MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dio</div>
        <div class="card">Global</div>
    </div>
</div>

<div class="section">
    <div class="title">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Campanhas EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicas</div>
    <div class="grid">
        <div class="card">
            <h3>Portal de Pagamentos</h3>
            <p>SoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o completa de monetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o</p>
            <button class="btn">Comprar</button>
        </div>

        <div class="card">
            <h3>GestÃƒÆ'Ã†â€™o PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblica</h3>
            <p>Ecossistema completo para prefeituras</p>
            <button class="btn">Comprar</button>
        </div>

        <div class="card">
            <h3>SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde Inteligente</h3>
            <p>GestÃƒÆ'Ã†â€™o e anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de epidemias</p>
            <button class="btn">Comprar</button>
        </div>
    </div>
</div>

<div class="section">
    <div class="title">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Vitrine de Produtos</div>
    <div class="grid">
        <div class="card">
            <h3>Produto 01</h3>
            <p>DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica</p>
            <button class="btn">Ver QR / Comprar</button>
        </div>

        <div class="card">
            <h3>Produto 02</h3>
            <p>DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica</p>
            <button class="btn">Ver QR / Comprar</button>
        </div>

        <div class="card">
            <h3>Produto 03</h3>
            <p>DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica</p>
            <button class="btn">Ver QR / Comprar</button>
        </div>
    </div>
</div>

<div class="section">
    <div class="title">ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Sistemas Sob Demanda</div>
    <div class="card">
        <h3>Descreva sua necessidade</h3>
        <p>VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª participa da criaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do sistema ideal em atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© 72h</p>
        <button class="btn">Criar Meu Sistema</button>
    </div>
</div>

<footer>
    IOTEC BL ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© Plataforma Global de Tecnologia
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ IOTEC SHOPPING GLOBAL RODANDO...")
    app.run(host="0.0.0.0", port=5000)


