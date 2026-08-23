import os
import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
# Permite chamadas de qualquer portal Netlify
CORS(app, resources={r"/api/*": {"origins": "*"}})

EMAIL_OFICIAL = "iotec.bl@proton.me"
PEDIDOS_REGISTRADOS = []

# --- ROTAS DA API DE PEDIDOS ---
@app.route('/api/pedidos', methods=['POST'])
def receber_pedido():
    try:
        dados = request.get_json(force=True)
        registro = {
            "id": len(PEDIDOS_REGISTRADOS) + 1,
            "origem": dados.get("portal_origem", "Netlify Direct"),
            "nome": dados.get("nome", "Cliente IOTEC"),
            "email": dados.get("email", "Não informado"),
            "mensagem": dados.get("mensagem", ""),
            "data": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        PEDIDOS_REGISTRADOS.append(registro)
        print(f"📥 [PEDIDO CAPTURADO] ID #{registro['id']} via {registro['origem']}")
        return jsonify({"status": "sucesso", "pedido_id": registro['id']}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.route('/api/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify({
        "total": len(PEDIDOS_REGISTRADOS),
        "pedidos": PEDIDOS_REGISTRADOS
    }), 200

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()}), 200

# --- PORTAL WEBFLASK V1 (VISÃO PRINCIPAL) ---
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "modulo": "IOTEC Portal WebFlask V1",
        "status": "OPERACIONAL",
        "mensagem": "Córtex Operacional e Receptor de Pedidos /api/pedidos Ativo",
        "ambiente": "Render / IOTEC_PLATFORM-1",
        "pedidos_capturados": len(PEDIDOS_REGISTRADOS),
        "endpoints": ["/api/health", "/api/pedidos"]
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
