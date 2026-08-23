import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Conecta na API do Stripe ou do PayPal
def gerar_cobranca(cliente, valor):
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â³ CobranÃƒÆ'Ã†â€™a gerada para {cliente} no valor de R${valor}")
    # IntegraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o real: stripe.Charge.create(...)

gerar_cobranca('Empresa XYZ', 199.90)



