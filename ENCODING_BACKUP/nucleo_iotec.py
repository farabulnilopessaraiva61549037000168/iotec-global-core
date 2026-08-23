import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =====================================================
# ROTAS VISUAIS (SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DAS PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂGINAS)
# =====================================================

@app.route("/")
def home():
    return "NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo ativo"

@app.route("/servicos")
def servicos():
    return "PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gina de serviÃƒÆ'Ã†â€™os ativa (placeholder)"

@app.route("/diagnostico")
def diagnostico_page():
    return "PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gina de diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico ativa (placeholder)"

@app.route("/portais")
def portais():
    return "PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gina de portais ativa (placeholder)"



