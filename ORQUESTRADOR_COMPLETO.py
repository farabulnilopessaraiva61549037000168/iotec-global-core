import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC - ORQUESTRADOR COMPLETO

# ============================================================



import os



BASE = "C:\\IoTec"



estrutura = {

    "backend": {

        "app.py": """from flask import Flask, request, jsonify

import random



app = Flask(__name__)



@app.route("/processar", methods=["POST"])

def processar():
    pass

    data = request.json

    pedido = data.get("pedido")

    valor = random.uniform(1,5)



    return jsonify({"resposta": f"Processado: {pedido}", "valor": valor})



if __name__ == "__main__":
    pass

    app.run(port=5000)

""",

        "requirements.txt": "flask"

    },



    "frontend": {

        "index.html": """<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>IoTec</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<div class="container">

<h1>IoTec</h1>

<input id="input" placeholder="Digite..." />

<button onclick="enviar()">Enviar</button>

<p id="resposta"></p>

</div>

<script src="app.js"></script>

</body>

</html>

""",



        "style.css": """body {

background:#0D0D0D;

color:#FFF;

display:flex;

justify-content:center;

align-items:center;

height:100vh;

}

.container {

background:#1A1A1A;

padding:30px;

border-radius:10px;

}

""",



        "app.js": """function enviar(){

let entrada = document.getElementById("input").value;



fetch("http://localhost:5000/processar", {

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({pedido:entrada})

})

.then(res=>res.json())

.then(data=>{

document.getElementById("resposta").innerText=data.resposta;

});

}

"""

    },



    "config": {

        ".env": "NETLIFY_AUTH_TOKEN=\nNETLIFY_SITE_ID=\nBACKEND_URL="

    },



    "deploy.py": """print("Deploy preparado. Configure tokens e execute manualmente.")"""

}



# ============================================================

# CRIAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O AUTOMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂTICA

# ============================================================



for pasta, arquivos in estrutura.items():
    pass

    caminho_pasta = os.path.join(BASE, pasta)

    os.makedirs(caminho_pasta, exist_ok=True)



    if isinstance(arquivos, dict):
        pass

        for nome, conteudo in arquivos.items():
            pass

            with open(os.path.join(caminho_pasta, nome), "w", encoding="utf-8") as f:
                pass

                f.write(conteudo)

    else:
        pass

        with open(os.path.join(BASE, pasta), "w", encoding="utf-8") as f:
            pass

            f.write(arquivos)



print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ IoTec estruturado automaticamente em C:\\IoTec")






