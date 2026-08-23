import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# -*- coding: utf-8 -*-



import os

import json

import time

from datetime import datetime



BASE = r"C:\IOTEC_OMEGA_X"



ORDERS_FILE = os.path.join(BASE, "orders.json")



HTML_FILE = os.path.join(

BASE,

"CONTROL_TOWER",

"live_monitor.html"

)



os.makedirs(

os.path.dirname(HTML_FILE),

exist_ok=True

)



def load_orders():
    pass



```

if not os.path.exists(ORDERS_FILE):
    pass

    return []



try:
    pass



    with open(

        ORDERS_FILE,

        "r",

        encoding="utf-8"

    ) as f:



        return json.load(f)



except:
    pass

    return []

```



def generate_html(orders):
    pass



```

cards = ""



orders = list(reversed(orders))



for item in orders[:50]:
    pass



    try:
        pass



        cards += f"""



        <div class="card">



            <h2>{item[0]}</h2>



            <p><b>Cliente:</b> {item[1]}</p>



            <p><b>PaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­s:</b> {item[2]}</p>



            <p><b>Setor:</b> {item[3]}</p>



            <p><b>Produto:</b> {item[4]}</p>



            <p><b>Valor:</b> R$ {item[5]}</p>



            <p><b>Status:</b> {item[6]}</p>



            <p><b>HorÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio:</b> {item[7]}</p>



        </div>



        """



    except:
        pass

        pass



html = f"""



<!DOCTYPE html>



<html lang="pt-br">



<head>



<meta charset="UTF-8">



<meta http-equiv="refresh" content="3">



<title>IOTEC TOWER</title>



<style>



body{{

    background:#050816;

    color:white;

    font-family:Arial;

    padding:30px;

}}



.card{{

    background:#111827;

    border-radius:20px;

    padding:20px;

    margin-bottom:20px;

}}



h1{{

    color:#38bdf8;

}}



</style>



</head>



<body>



<h1>IOTEC CENTRAL OPERATION TOWER</h1>



{cards}



</body>



</html>



"""



return html

```



while True:
    pass



```

orders = load_orders()



html = generate_html(orders)



with open(

    HTML_FILE,

    "w",

    encoding="utf-8"

) as f:



    f.write(html)



print(

    "[" + datetime.now().strftime("%H:%M:%S") + "]",

    "TORRE ATUALIZADA"

)



time.sleep(3)

```






