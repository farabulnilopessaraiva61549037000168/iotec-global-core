import logging
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='[WEBHOOK-IOTEC] %(message)s')

MERCADO_PAGO_TOKEN = "APP_USR-6181905353270296-072908-78bbbbe69e0e9d7df828a6037067be76-1263677665"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "mensagem": "Servidor Webhook IOTEC ativo"}), 200

@app.route("/webhook/mercadopago", methods=["GET", "POST"], strict_slashes=False)
def receber_notificacao():
    if request.method == "GET":
        return jsonify({
            "status": "online",
            "mensagem": "Servidor Webhook IOTEC rodando e pronto para receber notificacoes."
        }), 200

    dados = request.get_json() or {}
    tipo_evento = request.args.get("type") or dados.get("type")
    
    if tipo_evento == "payment":
        payment_id = request.args.get("data.id") or dados.get("data", {}).get("id")
        if payment_id:
            logging.info(f"Notificação de pagamento recebida! ID: {payment_id}")
            verificar_e_processar_pagamento(payment_id)
            return jsonify({"status": "recebido"}), 200

    return jsonify({"status": "ignorado"}), 200

def verificar_e_processar_pagamento(payment_id):
    url = f"https://api.mercadopago.com/v1/payments/{payment_id}"
    headers = {"Authorization": f"Bearer {MERCADO_PAGO_TOKEN}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            dados_pagamento = response.json()
            status = dados_pagamento.get("status")
            valor = dados_pagamento.get("transaction_amount")
            email = dados_pagamento.get("payer", {}).get("email")
            if status == "approved":
                logging.info(f"? PAGAMENTO CONFIRMADO! Valor: R$ {valor} | Cliente: {email}")
            else:
                logging.info(f"Pagamento {payment_id} com status: {status}")
        else:
            logging.error(f"Erro na API do Gateway: {response.status_code}")
    except Exception as e:
        logging.error(f"Falha ao conectar com a API: {e}")

if __name__ == "__main__":
    logging.info("Servidor Webhook IOTEC iniciado na porta 5000...")
    app.run(host="0.0.0.0", port=5000)
