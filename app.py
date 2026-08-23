from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

LEADS_DB = {}
VENDAS_DB = {}
FEED_NOTICIAS = []

def log_noticia(categoria, mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    evento = {
        "timestamp": timestamp,
        "categoria": categoria, # CAIXA, MINERACAO, SISTEMA, VENDAS
        "mensagem": mensagem
    }
    FEED_NOTICIAS.insert(0, evento)
    if len(FEED_NOTICIAS) > 100:
        FEED_NOTICIAS.pop()

log_noticia("SISTEMA", "Central de Operações IOTEC inicializada no Render.")

@app.route('/')
def home():
    receita_total = sum(v.get("valor", 0) for v in VENDAS_DB.values())
    return jsonify({
        "sistema": "IOTEC Core Engine B2B",
        "status": "ONLINE",
        "total_leads": len(LEADS_DB),
        "total_vendas": len(VENDAS_DB),
        "receita_acumulada_brl": receita_total,
        "feed_noticias_recente": FEED_NOTICIAS[:10]
    }), 200

# 1. ROBÔ REGISTRA LEAD E GERA CHECKOUT
@app.route('/api/leads/registrar', methods=['POST'])
def registrar_lead():
    data = request.json or {}
    cnpj = data.get("cnpj")
    empresa = data.get("empresa")
    telefone = data.get("telefone")
    
    if not cnpj or not telefone:
        return jsonify({"error": "CNPJ e Telefone obrigatórios"}), 400
        
    lead_id = str(uuid.uuid4())[:8]
    checkout_url = f"https://iotec.netlify.app/?ref={lead_id}"
    
    LEADS_DB[lead_id] = {
        "cnpj": cnpj,
        "empresa": empresa,
        "telefone": telefone,
        "status": "Aguardando_Pagamento",
        "checkout_url": checkout_url
    }
    
    log_noticia("MINERACAO", f"Novo lead registrado: {empresa} (CNPJ: {cnpj})")
    
    return jsonify({
        "status": "sucesso",
        "lead_id": lead_id,
        "checkout_url": checkout_url
    }), 201

# 2. CONSULTA DO CHECKOUT NO NETLIFY
@app.route('/api/checkout/<lead_id>', methods=['GET'])
def obter_checkout(lead_id):
    lead = LEADS_DB.get(lead_id)
    if not lead:
        return jsonify({"error": "Oportunidade não encontrada"}), 404
    return jsonify(lead), 200

# 3. WEBHOOK RECEBE PAGAMENTO (ENTRADA DE CAIXA)
@app.route('/webhook/pagamento', methods=['POST'])
def webhook_pagamento():
    data = request.json or {}
    lead_id = data.get("ref") or data.get("custom_id")
    valor = float(data.get("valor", 150.00))
    
    if lead_id in LEADS_DB:
        LEADS_DB[lead_id]["status"] = "PAGO"
        LEADS_DB[lead_id]["valor"] = valor
        VENDAS_DB[lead_id] = LEADS_DB[lead_id]
        
        empresa = LEADS_DB[lead_id]["empresa"]
        log_noticia("CAIXA", f"💰 ENTRADA DE CAIXA CONFIRMADA! R$ {valor:.2f} recebidos de {empresa} (Ref: {lead_id})")
        
        return jsonify({"status": "PAGAMENTO_CONFIRMADO", "lead": lead_id}), 200
        
    log_noticia("CAIXA", f"⚠️ Recebido pagamento avulso/desconhecido no valor de R$ {valor:.2f}")
    return jsonify({"status": "PROCESSADO_SEM_VINCULO"}), 200

# 4. PAINEL CENTRAL / NOTÍCIAS COMPLETO
@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    receita_total = sum(v.get("valor", 0) for v in VENDAS_DB.values())
    return jsonify({
        "resumo_caixa": {
            "receita_total": receita_total,
            "vendas_confirmadas": len(VENDAS_DB),
            "leads_em_aberto": len(LEADS_DB) - len(VENDAS_DB)
        },
        "central_noticias": FEED_NOTICIAS,
        "vendas_recentes": list(VENDAS_DB.values())
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
