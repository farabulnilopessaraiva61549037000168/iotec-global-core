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
    pass

    return """

    <h1>ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ IoTec Online</h1>

    <p>Sistema funcionando com sucesso.</p>

    """



# Rota de teste de API

@app.route("/api/status")

def status():
    pass

    return jsonify({

        "status": "online",

        "sistema": "IoTec",

        "mensagem": "API funcionando corretamente"

    })



# Porta dinÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢mica para Render

if __name__ == "__main__":
    pass

    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)




