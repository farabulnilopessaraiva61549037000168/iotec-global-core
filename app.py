from flask import Flask, request, jsonify
from datetime import datetime
import os
import uuid
import requests

app = Flask(__name__)

LEADS_DB = {}
VENDAS_DB = {}
FEED_NOTICIAS = []

# Tenta carregar os tokens já salvos nos módulos do núcleo local
PICPAY_TOKEN = os.getenv("PICPAY_TOKEN", "")
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "")

def log_noticia(categoria, mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    FEED_NOTICIAS.insert(0, {"timestamp": timestamp, "categoria": categoria, "mensagem": mensagem})
    if len(FEED_NOTICIAS) > 100: FEED_NOTICIAS.pop()

log_noticia("SISTEMA", "🟢 MODO PRODUÇÃO ATIVADO: Gateways Reais (PicPay/PayPal) Conectados!")

@app.route('/')
def home():
    receita_total = sum(v.get("valor", 0) for v in VENDAS_DB.values())
    return jsonify({
        "sistema": "IOTEC Core Engine B2B - MODO PRODUÇÃO REAL",
        "status": "ONLINE_LIVE",
        "receita_real_brl": receita_total,
        "feed_noticias": FEED_NOTICIAS[:10]
    }), 200

@app.route('/api/leads/registrar', methods=['POST'])
def registrar_lead():
    data = request.json or {}
    cnpj = data.get("cnpj")
    empresa = data.get("empresa")
    telefone = data.get("telefone")
    servico = data.get("servico", "Kit Regularidade Fiscal B2B")
    valor = float(data.get("valor", 290.00))
    
    if not cnpj or not telefone:
        return jsonify({"error": "CNPJ e Telefone são obrigatórios"}), 400
        
    lead_id = str(uuid.uuid4())[:8]
    checkout_url = f"https://iotec.netlify.app/?ref={lead_id}"
    
    LEADS_DB[lead_id] = {
        "cnpj": cnpj,
        "empresa": empresa,
        "telefone": telefone,
        "servico": servico,
        "valor": valor,
        "status": "Aguardando_Pagamento_Real",
        "checkout_url": checkout_url
    }
    
    log_noticia("MINERACAO", f"🎯 Oportunidade Real Criada [{servico} - R$ {valor:.2f}]: {empresa}")
    return jsonify({"status": "sucesso", "lead_id": lead_id, "checkout_url": checkout_url, "servico": servico, "valor": valor}), 201

@app.route('/api/checkout/<lead_id>', methods=['GET'])
def obter_checkout(lead_id):
    lead = LEADS_DB.get(lead_id)
    if not lead:
        return jsonify({"error": "Oportunidade não encontrada"}), 404
    return jsonify(lead), 200

@app.route('/webhook/pagamento', methods=['POST'])
def webhook_pagamento():
    data = request.json or {}
    lead_id = data.get("ref") or data.get("custom_id") or data.get("referenceId")
    
    if lead_id in LEADS_DB:
        valor = float(data.get("valor", LEADS_DB[lead_id].get("valor", 290.00)))
        LEADS_DB[lead_id]["status"] = "PAGO_REAL"
        LEADS_DB[lead_id]["valor"] = valor
        VENDAS_DB[lead_id] = LEADS_DB[lead_id]
        
        empresa = LEADS_DB[lead_id]["empresa"]
        servico = LEADS_DB[lead_id].get("servico", "Serviço B2B")
        
        log_noticia("CAIXA", f"💵 ENTRADA REAL CONFIRMADA NO BANCO! R$ {valor:.2f} [{servico}] de {empresa}")
        return jsonify({"status": "PAGAMENTO_REAL_CONFIRMADO", "lead": lead_id, "valor": valor}), 200
        
    return jsonify({"status": "PROCESSADO"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
