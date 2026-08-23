"""
===================================================================================
                       IOTEC NUCLEUS - GATEWAY & WEBHOOK WHATSAPP
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Canal Corporativo Oficial: (88) 99930-6416
 CNPJ: 61.549.037/0001-68
===================================================================================
"""

from flask import Flask, request, jsonify
import manifest
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def status_gateway():
    return jsonify({
        "modulo": "IOTEC WhatsApp Gateway Server",
        "titular": manifest.EMPRESA_TITULAR,
        "cnpj": manifest.CNPJ_TITULAR,
        "canal_oficial": manifest.WHATSAPP_CORPORATIVO,
        "status": "ONLINE_EM_LOCALHOST"
    }), 200

@app.route("/webhook/whatsapp", methods=["POST"])
def receber_mensagem_whatsapp():
    """
    Endpoint pronto para receber payloads de webhook do WhatsApp Business API.
    """
    payload = request.get_json(silent=True) or {}
    print("\n[+] MENSAGEM / EVENTO RECEBIDO NO WHATSAPP BUSINESS (88) 99930-6416:")
    print(f"    Data/Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"    Dados Payload: {payload}\n")

    # Resposta de confirmação de recebimento sem erros (HTTP 200)
    return jsonify({
        "status": "PROCESSADO",
        "recebido_por": manifest.EMPRESA_TITULAR
    }), 200

if __name__ == "__main__":
    manifest.exibir_banner_identidade()
    print("[+] Servidor Gateway de WhatsApp IOTEC rodando em http://localhost:5000")
    print("[+] Endpoint Webhook ativo em http://localhost:5000/webhook/whatsapp\n")
    app.run(host="0.0.0.0", port=5000, debug=False)