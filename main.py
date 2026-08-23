import os
import random
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

class CoordenadoriaGeral:
    def auditar(self):
        mesas = [
            {"id": "MESA-01", "cliente": "Transportadora Ceará Cargas (Privada)", "status": "PROPOSTA_ENVIADA", "valor": 199.00},
            {"id": "MESA-02", "cliente": "Distribuidora Nordeste", "status": "AGUARDANDO_PIX", "valor": 49.90},
            {"id": "MESA-03", "cliente": "Prefeitura / Gestão Pública (CIGM)", "status": "ALINHAMENTO_COORDENADORIA", "valor": 1200.00}
        ]
        return {
            "total_mesas": len(mesas),
            "projecao_caixa": "R$ 1448.90",
            "mesas": mesas,
            "diretriz": "Coordenadoria monitorando 100% das negociações ativas."
        }

coordenadoria = CoordenadoriaGeral()

@app.route("/", methods=["GET"])
@app.route("/api/readiness", methods=["GET", "POST"])
@app.route("/api/v1/coordenadoria", methods=["GET"])
def readiness():
    dados_coordenadoria = coordenadoria.auditar()
    return jsonify({
        "readiness_score": 100,
        "status": "SISTEMA_MONETIZAVEL_E_MONITORADO",
        "coordenadoria_geral": dados_coordenadoria,
        "checkout_pix_rapido": {
            "servico": "Auditoria Autônoma de Dados",
            "valor": 49.90,
            "link_checkout": "https://iotec-platform-1.onrender.com/api/readiness"
        }
    }), 200

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "OK", "app": "IOTEC PORTAL"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)