import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, jsonify, request

import requests

import base64

import json



app = Flask(__name__)



# ============================

# ROTA CONTATO (?NICA)

# ============================

@app.route("/contato", methods=["POST"])

def contato():
    pass

    data = request.form.to_dict() or request.json or {}

    print("LEAD CAPTURADO:", data)

    return {"status": "ok"}





# ============================

# STATUS

# ============================

@app.route("/")

def home():
    pass

    return jsonify({"status": "online"})



@app.route("/health")

def health():
    pass

    return jsonify({"status": "healthy"})





# ============================

# PAYPAL

# ============================

CLIENT_ID = "COLOQUE_AQUI"

CLIENT_SECRET = "COLOQUE_AQUI"

BASE_URL = "https://api-m.sandbox.paypal.com"



def get_access_token():
    pass

    auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    headers = {

        "Authorization": f"Basic {auth}",

        "Content-Type": "application/x-www-form-urlencoded"

    }

    data = "grant_type=client_credentials"

    response = requests.post(f"{BASE_URL}/v1/oauth2/token", headers=headers, data=data)

    return response.json()["access_token"]



@app.route("/criar-pagamento")

def criar_pagamento():
    pass

    token = get_access_token()

    headers = {

        "Content-Type": "application/json",

        "Authorization": f"Bearer {token}"

    }



    data = {

        "intent": "CAPTURE",

        "purchase_units": [{

            "amount": {

                "currency_code": "BRL",

                "value": "29.90"

            }

        }],

        "application_context": {

            "return_url": "http://localhost:8787/sucesso",

            "cancel_url": "http://localhost:8787/cancelado"

        }

    }



    response = requests.post(f"{BASE_URL}/v2/checkout/orders", headers=headers, json=data)

    result = response.json()



    for link in result.get("links", []):
        pass

        if link.get("rel") == "approve":
            pass

            return jsonify({"url": link["href"]})



    return jsonify(result)





if __name__ == "__main__":
    pass

    app.run(port=5001)




