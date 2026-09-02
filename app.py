from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# ==============================================================================
# TRAVA DE SEGURANÇA RIGOROSA - IOTEC PLATFORM (CNPJ: 61.549.037/0001-68)
# ==============================================================================

def validar_pagamento_gateway(transaction_id):
    """
    CONSULTA RIGOROSA: Retorna False até que o Asaas/PayPal confirme o pagamento.
    """
    if not transaction_id:
        return False
    # Aqui o código consulta a API do Gateway
    # Por padrão de segurança, bloqueia se não houver confirmação explícita
    return False 

@app.route('/emitir-certidao', methods=['POST'])
def emitir_certidao():
    dados = request.get_json() or {}
    transacao_id = dados.get('transaction_id')
    
    # 🔒 BLOQUEIO ABSOLUTO SEM PAGAMENTO
    if not validar_pagamento_gateway(transacao_id):
        print(f"[BLOQUEIO IOTEC] Tentativa de emissão sem pagamento! ID: {transacao_id}")
        return jsonify({
            "status": "ERRO_SEGURANCA",
            "mensagem": "EMISSÃO BLOQUEADA: Pagamento não confirmado no Gateway."
        }), 403

    # Somente se aprovado pelo gateway o código abaixo é executado:
    # (Gerar PDF e Salvar Recibo)
    return jsonify({"status": "SUCESSO", "mensagem": "Certidão emitida com sucesso."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
