import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC_API_INTEGRACAO.py

# ============================================================



from flask import Flask, request, jsonify

from datetime import datetime



app = Flask(__name__)



# ============================================================

# ROTA PRINCIPAL DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO

# ============================================================



@app.route("/api/iotec", methods=["POST"])

def iotec_core():
    pass



    data = request.json



    acao = data.get("acao")

    payload = data.get("payload")

    origem = data.get("origem")



    log = {

        "acao": acao,

        "payload": payload,

        "origem": origem,

        "timestamp": datetime.now().isoformat()

    }



    print("\n[IOTEC RECEBIDO]")

    print(log)



    # ========================================================

    # LÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œGICA DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO (EXPANSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEL)

    # ========================================================



    if acao == "interacao":
        pass

        return jsonify({

            "status": "ok",

            "mensagem": "InteraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o registrada no nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo"

        })



    elif acao == "compra":
        pass

        return jsonify({

            "status": "ok",

            "mensagem": "Processando pagamento",

            "redirect": payload.get("link_pagamento")

        })



    elif acao == "lead":
        pass

        return jsonify({

            "status": "ok",

            "mensagem": "Lead capturado com sucesso"

        })



    else:
        pass

        return jsonify({

            "status": "erro",

            "mensagem": "AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o nÃƒÆ'Ã†â€™o reconhecida"

        })



# ============================================================

# ROTA DE TESTE

# ============================================================



@app.route("/")

def home():
    pass

    return "IOTEC API ONLINE"



# ============================================================

# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O

# ============================================================



if __name__ == "__main__":
    pass

    app.run(host="0.0.0.0", port=5000)






