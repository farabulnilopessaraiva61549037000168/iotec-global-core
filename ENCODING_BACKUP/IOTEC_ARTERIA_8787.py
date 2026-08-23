import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "IOTEC ARTERIA 8787 OK"

@app.route("/webhook/paypal", methods=["GET", "POST"])
def webhook_paypal():
    return jsonify({
        "ok": True,
        "metodo": request.method,
        "mensagem": "Webhook local ativa"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)


