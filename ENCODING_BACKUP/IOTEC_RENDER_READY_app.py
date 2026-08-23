import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, jsonify

app = Flask(__name__)

# Rota principal (ESSENCIAL)
@app.route("/")
def home():
    return """
    <h1>ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ IoTec Online</h1>
    <p>Sistema funcionando com sucesso.</p>
    """

# Rota de teste de API
@app.route("/api/status")
def status():
    return jsonify({
        "status": "online",
        "sistema": "IoTec",
        "mensagem": "API funcionando corretamente"
    })

# Porta dinÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢mica para Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


