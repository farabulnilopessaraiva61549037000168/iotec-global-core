import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =====================================================
# IOTEC NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO CENTRAL
# =====================================================

from flask import Flask, request, jsonify

app = Flask(__name__)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ BLOQUEIO DE ALTERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE INTERFACE
PROTECAO_INTERFACE = True

# =====================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  MOTOR DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# =====================================================

def processar_diagnostico(texto):
    if not texto:
        return "Descreva sua necessidade para anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise."

    return f"""
    ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â½ DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico Inteligente IOTEC:

    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise inicial concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da
    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â PossÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel necessidade de auditoria tecnolÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica
    ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â RecomendaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: avaliaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o detalhada com nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo

    Entrada recebida:
    "{texto[:100]}"
    """

# =====================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â API
# =====================================================

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.get_json()
    texto = data.get("texto", "")

    resposta = processar_diagnostico(texto)

    return jsonify({
        "resposta": resposta
    })

# =====================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =====================================================

if __name__ == "__main__":
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO IOTEC ATIVO")
    app.run(host="0.0.0.0", port=5000)


