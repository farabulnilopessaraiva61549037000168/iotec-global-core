import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_API_INTEGRACAO.py
# ============================================================

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ============================================================
# ROTA PRINCIPAL DO NÃƒÆ'Ã…Â¡CLEO
# ============================================================

@app.route("/api/iotec", methods=["POST"])
def iotec_core():
    pass

    data = request.json

    acao = data.get("acao")
    payload = data.get("payload")
    origem = data.get("origem")

    log = {
        "acao": acao,
        "payload": payload,
        "origem": origem,
        "timestamp": datetime.now().isoformat()
    }

    print("\n[IOTEC RECEBIDO]")
    print(log)

    # ========================================================
    # LÃƒÆ'Ã¢â‚¬Å"GICA DO NÃƒÆ'Ã…Â¡CLEO (EXPANSÃƒÆ'Ã‚ÂVEL)
    # ========================================================

    if acao == "interacao":
        return jsonify({
            "status": "ok",
            "mensagem": "InteraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o registrada no nÃƒÆ'Ã‚Âºcleo"
        })

    elif acao == "compra":
        return jsonify({
            "status": "ok",
            "mensagem": "Processando pagamento",
            "redirect": payload.get("link_pagamento")
        })

    elif acao == "lead":
        return jsonify({
            "status": "ok",
            "mensagem": "Lead capturado com sucesso"
        })

    else:
        return jsonify({
            "status": "erro",
            "mensagem": "AÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o nÃƒÆ'Ã‚Â£o reconhecida"
        })

# ============================================================
# ROTA DE TESTE
# ============================================================

@app.route("/")
def home():
    return "IOTEC API ONLINE"

# ============================================================
# EXECUÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O
# ============================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


