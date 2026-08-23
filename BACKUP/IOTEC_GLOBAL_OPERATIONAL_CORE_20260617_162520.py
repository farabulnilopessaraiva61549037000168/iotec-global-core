import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC_GLOBAL_OPERATIONAL_CORE.py

# =========================================================

# IOTEC BL ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â GLOBAL OPERATIONAL CORE

# Construtora e Distribuidora de InovaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e Tecnologia

# =========================================================



import os

import sys

import json

import uuid

import sqlite3

import subprocess

from datetime import datetime



# =========================================================

# AUTO INSTALLER

# =========================================================



REQUIRED_PACKAGES = [

    "flask",

    "requests"

]



def ensure_package(package):
    pass



    try:
        pass

        __import__(package)



    except ImportError:
        pass



        print(f"[AUTO-INSTALL] Installing {package}...")



        subprocess.check_call(

            [sys.executable, "-m", "pip", "install", package]

        )



for package in REQUIRED_PACKAGES:
    pass

    ensure_package(package)



# =========================================================

# IMPORTS

# =========================================================



from flask import Flask

from flask import request

from flask import jsonify

from flask import render_template_string



# =========================================================

# CONFIG

# =========================================================



CORE_NAME = "IOTEC"

CORE_VERSION = "2.0"

CORE_MODE = "GLOBAL_OPERATIONAL"



EMAIL_COMMERCIAL = "iotec.bl@proton.me"



CNPJ = "61.549.037/0001-68"



BASE_DIR = os.path.dirname(os.path.abspath(__file__))



DATABASE_PATH = os.path.join(BASE_DIR, "iotec_global.db")



# =========================================================

# DATABASE

# =========================================================



def initialize_database():
    pass



    connection = sqlite3.connect(DATABASE_PATH)



    cursor = connection.cursor()



    cursor.execute("""

    CREATE TABLE IF NOT EXISTS leads (



        id TEXT PRIMARY KEY,

        company TEXT,

        client TEXT,

        email TEXT,

        phone TEXT,

        service TEXT,

        budget REAL,

        priority TEXT,

        description TEXT,

        created_at TEXT



    )

    """)



    connection.commit()

    connection.close()



    print("[CORE] DATABASE ONLINE")



initialize_database()



# =========================================================

# FLASK

# =========================================================



app = Flask(__name__)



# =========================================================

# PRIORITY ENGINE

# =========================================================



def classify_priority(budget):
    pass



    try:
        pass



        budget = float(budget)



    except:
        pass



        budget = 0



    if budget >= 100000:
        pass

        return "CRITICAL"



    elif budget >= 10000:
        pass

        return "HIGH"



    elif budget >= 3000:
        pass

        return "MEDIUM"



    return "NORMAL"



# =========================================================

# HTML INTERFACE

# =========================================================



HOME_HTML = """

<!DOCTYPE html>

<html lang="pt-br">



<head>



<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">



<title>IOTEC BL</title>



<style>



body{

    background:#07080D;

    color:white;

    font-family:Arial;

    margin:0;

    padding:0;

}



header{

    padding:40px;

    text-align:center;

    background:#111827;

}



h1{

    color:#D4AF37;

}



.container{

    width:90%;

    max-width:900px;

    margin:auto;

    padding:40px 0;

}



.card{

    background:#111827;

    border:1px solid #222;

    border-radius:12px;

    padding:25px;

    margin-bottom:25px;

}



input, textarea, select{



    width:100%;

    padding:14px;

    margin-top:10px;

    margin-bottom:20px;

    border-radius:8px;

    border:none;

    background:#1F2937;

    color:white;

}



button{



    background:#D4AF37;

    color:black;

    padding:14px 20px;

    border:none;

    border-radius:8px;

    font-weight:bold;

    cursor:pointer;

}



.status{



    color:#4ADE80;

    font-weight:bold;

}



</style>



</head>



<body>



<header>



<h1>IOTEC BL</h1>



<p>

Construtora e Distribuidora de InovaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e Tecnologia

</p>



<p class="status">

ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO OPERACIONAL ONLINE

</p>



<p>

CNPJ: 61.549.037/0001-68

</p>



<p>

iotec.bl@proton.me

</p>



</header>



<div class="container">



<div class="card">



<h2>Solicitar Sistema</h2>



<form method="POST" action="/encomendar">



<input

name="company"

placeholder="Nome da empresa"

required

>



<input

name="client"

placeholder="Nome do cliente"

required

>



<input

name="email"

placeholder="E-mail"

required

>



<input

name="phone"

placeholder="Telefone"

required

>



<select name="service">



<option>Site Institucional</option>

<option>Dashboard BI</option>

<option>ERP / CRM</option>

<option>IA Empresarial</option>

<option>AutomaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</option>



</select>



<input

name="budget"

placeholder="OrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡amento estimado"

required

>



<textarea

name="description"

placeholder="Descreva seu projeto"

rows="6"

required

></textarea>



<button type="submit">

ENVIAR AO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

</button>



</form>



</div>



<div class="card">



<h2>Status Operacional</h2>



<ul>



<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Flask Online</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Banco de Dados Online</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Pipeline de Leads</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â ClassificaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Inteligente</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Captura Global</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo Operacional</li>

<li>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â Render Ready</li>



</ul>



</div>



</div>



</body>

</html>

"""



# =========================================================

# ROUTES

# =========================================================



@app.route("/")

def home():
    pass



    return render_template_string(HOME_HTML)



# =========================================================



@app.route("/status")

def status():
    pass



    return jsonify({



        "core": CORE_NAME,

        "version": CORE_VERSION,

        "mode": CORE_MODE,

        "status": "ONLINE",

        "render_ready": True,

        "database": "ONLINE"



    })



# =========================================================



@app.route("/encomendar", methods=["POST"])

def encomendar():
    pass



    data = request.form



    lead_id = str(uuid.uuid4())



    company = data.get("company")

    client = data.get("client")

    email = data.get("email")

    phone = data.get("phone")

    service = data.get("service")

    budget = data.get("budget")

    description = data.get("description")



    priority = classify_priority(budget)



    connection = sqlite3.connect(DATABASE_PATH)



    cursor = connection.cursor()



    cursor.execute("""



    INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)



    """, (



        lead_id,

        company,

        client,

        email,

        phone,

        service,

        budget,

        priority,

        description,

        str(datetime.now())



    ))



    connection.commit()

    connection.close()



    print("=" * 60)

    print("[NEW GLOBAL LEAD]")

    print("=" * 60)



    print(f"ID         : {lead_id}")

    print(f"COMPANY    : {company}")

    print(f"CLIENT     : {client}")

    print(f"SERVICE    : {service}")

    print(f"BUDGET     : {budget}")

    print(f"PRIORITY   : {priority}")



    return f"""



    <html>



    <body style='background:#07080D;color:white;

    font-family:Arial;text-align:center;padding:80px;'>



    <h1 style='color:#D4AF37;'>

    REQUEST RECEIVED

    </h1>



    <p>

    Your request has been successfully received.

    </p>



    <p>

    ID: {lead_id}

    </p>



    <p>

    The IOTEC operational core will analyze your request.

    </p>



    </body>



    </html>



    """



# =========================================================



@app.route("/admin")

def admin():
    pass



    connection = sqlite3.connect(DATABASE_PATH)



    cursor = connection.cursor()



    cursor.execute("""

    SELECT * FROM leads

    ORDER BY created_at DESC

    """)



    leads = cursor.fetchall()



    connection.close()



    return jsonify({



        "total_leads": len(leads),

        "leads": leads



    })



# =========================================================

# STARTUP

# =========================================================



if __name__ == "__main__":
    pass



    print("=" * 60)

    print("IOTEC GLOBAL OPERATIONAL CORE")

    print("=" * 60)



    print("[CORE] GLOBAL OPERATIONAL MODE")

    print("[CORE] DATABASE ONLINE")

    print("[CORE] WEB PIPELINE ONLINE")

    print("[CORE] LEAD ENGINE ONLINE")

    print("[CORE] AUTO INSTALLER ONLINE")

    print("[CORE] RENDER READY")

    print("[CORE] GLOBAL ACCESS READY")



    PORT = int(os.environ.get("PORT", 5000))



    app.run(



        host="0.0.0.0",

        port=PORT,

        debug=False



    )




