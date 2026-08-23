from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Banco de dados em memória (pode ser expandido para SQLite/PostgreSQL)
LEADS_DB = {}
VENDAS_DB = {}

@app.route('/')
def home():
    return jsonify({"status": "ONLINE", "sistema": "IOTEC Core Engine B2B"}), 200

# 1. RECEBE LEAD DO ROBÔ LOCAL E GERA CHECKOUT
@app.route('/api/leads/registrar', methods=['POST'])
def registrar_lead():
    data = request.json or {}
    cnpj = data.get("cnpj")
    empresa = data.get("empresa")
    telefone = data.get("telefone")
    
    if not cnpj or not telefone:
        return jsonify({"error": "CNPJ e Telefone são obrigatórios"}), 400
        
    lead_id = str(uuid.uuid4())[:8]
    checkout_url = f"https://iotec.netlify.app/?ref={lead_id}" # URL do seu Netlify
    
    LEADS_DB[lead_id] = {
        "cnpj": cnpj,
        "empresa": empresa,
        "telefone": telefone,
        "status": "Aguardando_Pagamento",
        "checkout_url": checkout_url
    }
    
    return jsonify({
        "status": "sucesso",
        "lead_id": lead_id,
        "checkout_url": checkout_url
    }), 201

# 2. NETLIFY CONSULTA O LEAD PARA EXIBIR A CERTIDÃO/PAGAMENTO
@app.route('/api/checkout/<lead_id>', methods=['GET'])
def obter_checkout(lead_id):
    lead = LEADS_DB.get(lead_id)
    if not lead:
        return jsonify({"error": "Oportunidade não encontrada"}), 404
    return jsonify(lead), 200

# 3. WEBHOOK RECEBE PAGAMENTO E LIBERA A CERTIDÃO
@app.route('/webhook/pagamento', methods=['POST'])
def webhook_pagamento():
    data = request.json or {}
    lead_id = data.get("ref") or data.get("custom_id")
    
    if lead_id in LEADS_DB:
        LEADS_DB[lead_id]["status"] = "PAGO"
        VENDAS_DB[lead_id] = LEADS_DB[lead_id]
        return jsonify({"status": "PAGAMENTO_CONFIRMADO", "lead": lead_id}), 200
        
    return jsonify({"status": "PROCESSADO_SEM_VINCULO"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
