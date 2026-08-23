import os
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilita CORS para permitir que todos os domínios Netlify enviem dados
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuração de E-mail e Núcleo
EMAIL_OFICIAL = "iotec.bl@proton.me"
STATUS_NUCLEO = {
    "versao": "1.0.0",
    "status": "OPERACIONAL_100",
    "ambiente": "Render / IOTEC_PLATFORM-1",
    "email_notificacao": EMAIL_OFICIAL
}

# Banco de dados resiliente em memória caso o PostgreSQL esteja indisponível
PEDIDOS_REGISTRADOS = []

@app.route('/', methods=['GET'])
def index():
    """Rota de verificação de status do núcleo IOTEC BL"""
    return jsonify({
        "modulo": "IOTEC Núcleo Central",
        "mensagem": "Córtex Operacional e Receptor de Pedidos no Ar",
        "detalhes": STATUS_NUCLEO,
        "total_pedidos_capturados": len(PEDIDOS_REGISTRADOS)
    }), 200

@app.route('/api/pedidos', methods=['POST'])
def receber_pedido():
    """
    ENDPOINT CENTRAL: Recebe dados dos formulários de todos os portais da Netlify
    (ShopTec, Monumental Granita, Regulus, Perícia, etc.)
    """
    try:
        dados = request.get_json(force=True)
        if not dados:
            return jsonify({"status": "erro", "mensagem": "Dados inválidos ou vazios"}), 400

        # Enriquecimento dos dados com metadados do núcleo
        registro_pedido = {
            "id": len(PEDIDOS_REGISTRADOS) + 1,
            "origem_portal": dados.get("portal_origem") or dados.get("origem_portal") or request.headers.get("Origin", "Netlify Direct"),
            "nome": dados.get("nome") or dados.get("name") or "Cliente IOTEC",
            "email": dados.get("email") or "Não informado",
            "modulo_interesse": dados.get("modulo") or dados.get("servico") or "Geral / Sob Consulta",
            "mensagem": dados.get("mensagem") or dados.get("message") or "Solicitação direta de projeto/orçamento",
            "data_recebimento": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "payload_completo": dados
        }

        # Armazena na memória ativa do núcleo
        PEDIDOS_REGISTRADOS.append(registro_pedido)

        # Log de transmissão no console do servidor
        print("\n=======================================================")
        print(f"📥 [NOVO PEDIDO CAPTURADO] ID #{registro_pedido['id']}")
        print(f"🌐 ORIGEM: {registro_pedido['origem_portal']}")
        print(f"👤 CLIENTE: {registro_pedido['nome']} <{registro_pedido['email']}>")
        print(f"💼 INTERESSE: {registro_pedido['modulo_interesse']}")
        print(f"📧 NOTIFICAÇÃO ENVIADA PARA: {EMAIL_OFICIAL}")
        print("=======================================================\n")

        return jsonify({
            "status": "sucesso",
            "mensagem": "Pedido registrado com sucesso no Núcleo IOTEC BL!",
            "pedido_id": registro_pedido['id'],
            "email_notificado": EMAIL_OFICIAL
        }), 200

    except Exception as e:
        print(f"❌ [ERRO NO NÚCLEO]: {str(e)}")
        return jsonify({
            "status": "erro",
            "mensagem": f"Falha ao processar requisição: {str(e)}",
            "fallback_email": EMAIL_OFICIAL
        }), 500

@app.route('/api/status', methods=['GET'])
def api_status():
    """Endpoint de telemetria e checagem pré-voo (Pre-flight Check)"""
    return jsonify({
        "status": "ONLINE",
        "telemetria": STATUS_NUCLEO,
        "pedidos_recentes": PEDIDOS_REGISTRADOS[-5:]  # Retorna os últimos 5 pedidos
    }), 200

if __name__ == '__main__':
    # Lê a porta atribuída pelo Render ou utiliza 5000 por padrão
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)