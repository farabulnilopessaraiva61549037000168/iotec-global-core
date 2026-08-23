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

CLIENT_ID = "AUFsIcepzxZyce0ii28lKKcFdflhRQioxI8mzBJvKSKGikX8B53NNy0rWP3ga04_itSAvQzvCgWF-YEY"

CLIENT_SECRET = "EOcWsBThytL1r9SIafn_3wwulYBJXNeHHvuJHHumANzuww-FF5no2wxtX44_14FWfif4X1ww3TUxuaix"

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

    result = response.json(); print(result)



    for link in result.get("links", []):
        pass

        if link.get("rel") == "approve":
            pass

            return jsonify({
                "order_id": result["id"],
                "url": link["href"]
            })



    return jsonify(result)







@app.route("/order-status/<order_id>")
def order_status(order_id):

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/v2/checkout/orders/{order_id}",
        headers=headers
    )

    if response.status_code != 200:
        return jsonify({
            "success": False,
            "http": response.status_code,
            "response": response.text
        }), response.status_code

    dados = response.json()

    return jsonify({
        "success": True,
        "order_id": dados.get("id"),
        "status": dados.get("status"),
        "intent": dados.get("intent")
    })


if __name__ == "__main__":
    pass

    app.run(port=5001)







