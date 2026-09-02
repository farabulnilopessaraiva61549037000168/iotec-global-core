from flask import Flask, request, jsonify
import json
import datetime
import os

app = Flask(__name__)
CAIXA_PATH = "C:\\IOTEC\\caixa_real.json"
NETLIFY_ORIGIN = "https://deft-choux-097d84.netlify.app"

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

if not os.path.exists(CAIXA_PATH):
    with open(CAIXA_PATH, "w") as f:
        json.dump({"CNPJ": "61.549.037/0001-68", "domain": NETLIFY_ORIGIN, "saldo_real": 0.0, "transacoes": []}, f)

@app.route('/', methods=['GET'])
def home():
    return f"<h1>🚀 Núcleo IOTEC — Servidor de Produção</h1><p>Conectado ao Domínio: {NETLIFY_ORIGIN}</p><p>CNPJ Matriz: 61.549.037/0001-68</p>"

@app.route('/caixa', methods=['GET'])
def ver_caixa():
    with open(CAIXA_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/webhook/<gateway>', methods=['POST', 'OPTIONS'])
def receber_pagamento_real(gateway):
    if request.method == 'OPTIONS':
        return jsonify({'status': 'OK'}), 200

    dados = request.get_json()
    if dados and dados.get("status") in ["PAID", "APPROVED", "CONFIRMED", "succeeded"]:
        valor = float(dados.get("amount", 0.0))
        doc_nome = dados.get("documento_nome", "Certidão Oficial IOTEC")
        
        with open(CAIXA_PATH, "r") as f:
            caixa = json.load(f)
            
        caixa["saldo_real"] += valor
        caixa["transacoes"].append({
            "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "gateway": gateway,
            "produto": doc_nome,
            "valor": valor,
            "origem": NETLIFY_ORIGIN
        })
        
        with open(CAIXA_PATH, "w") as f:
            json.dump(caixa, f, indent=4)
            
        print(f"💰 [TRANSAÇÃO REAL RECEBIDA VIA NETLIFY] R$ {valor:.2f} via {gateway}")
        return jsonify({"status": "SUCCESS", "message": "Caixa real atualizado com sucesso"}), 200
    
    return jsonify({"status": "IGNORED", "message": "Pagamento pendente ou inválido"}), 400

if __name__ == '__main__':
    print(f"🚀 NÚCLEO IOTEC APONTADO PARA: {NETLIFY_ORIGIN}")
    app.run(host='0.0.0.0', port=5000)