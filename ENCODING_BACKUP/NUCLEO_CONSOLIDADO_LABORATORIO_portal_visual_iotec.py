import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "IOTEC ARTERIA 8787 OK"

@app.route("/webhook/paypal", methods=["GET", "POST"])
def webhook_paypal():
    return jsonify({
        "ok": True,
        "metodo": request.method,
        "mensagem": "Webhook local ativa"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)# CARREGAR RANKING
ranking_file = STATE / "ranking.json"

top = []
if ranking_file.exists():
    with open(ranking_file, "r", encoding="utf-8") as f:
        top = json.load(f)

# SEÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O TOP
html += """
<h2 style="padding:20px;"> TOP INTERFACES</h2>
<div class="grid">
"""

for item in top[:20]:
    img = item["arquivo"]
    html += f"""
    <div class="card">
        <img src="file:///{img}">
        <div class="nome">{item['nome']}  {item['score']}</div>
    </div>
    """

html += "</div>"


