import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC COMMAND TOWER V1.0
#
# Interface humana de controle operacional IoTec
#
# Objetivo:
# Visualizar o estado da plataforma
#
# ===============================================================


from flask import Flask, render_template_string
from datetime import datetime
import os


app = Flask(__name__)



HTML = """

<!DOCTYPE html>

<html>

<head>

<title>
IOTEC COMMAND TOWER
</title>


<meta http-equiv="refresh" content="10">


<style>

body {

font-family: Arial;
background:#0b1220;
color:white;
padding:30px;

}


.card {

background:#172033;
padding:20px;
margin:15px;
border-radius:10px;

}


.green {

color:#00ff88;

}


.yellow {

color:#ffd700;

}


.red {

color:#ff4444;

}


h1 {

font-size:35px;

}


</style>


</head>


<body>


<h1>
Ã°Å¸Å¡â‚¬ IOTEC DIGITAL COMMAND TOWER
</h1>


<div class="card">

<h2>
CENTRAL DE CONTROLE
</h2>

<p>
Data:
{{data}}
</p>

<p>
Sistema:
ONLINE
</p>

</div>




<div class="card">

<h2>
STATUS DOS SETORES
</h2>


<p class="green">
Ã°Å¸Å¸Â¢ Motores Python encontrados
</p>


<p class="yellow">
Ã°Å¸Å¸Â¡ IntegraÃƒÂ§ÃƒÂµes precisam validaÃƒÂ§ÃƒÂ£o
</p>


<p class="red">
Ã°Å¸â€Â´ Fluxo comercial necessita teste real
</p>


</div>





<div class="card">


<h2>
FLUXO COMERCIAL
</h2>


<p>

Cliente

Ã¢â€ â€œ

Portal

Ã¢â€ â€œ

FormulÃƒÂ¡rio

Ã¢â€ â€œ

NÃƒÂºcleo

Ã¢â€ â€œ

Pagamento

Ã¢â€ â€œ

Entrega


</p>


</div>





<div class="card">


<h2>
PRÃƒâ€œXIMAS MISSÃƒâ€¢ES
</h2>


<ul>

<li>
Validar formulÃƒÂ¡rio principal
</li>

<li>
Confirmar checkout real
</li>

<li>
Testar pedido completo
</li>

<li>
Conectar agentes
</li>


</ul>


</div>



</body>

</html>


"""





@app.route("/")


def torre():

    return render_template_string(
        HTML,
        data=datetime.now()
    )





if __name__ == "__main__":

    print("="*60)

    print(
        "IOTEC DIGITAL COMMAND TOWER"
    )

    print(
        "Abrindo painel operacional..."
    )

    print(
        "http://127.0.0.1:5000"
    )

    print("="*60)


    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )



