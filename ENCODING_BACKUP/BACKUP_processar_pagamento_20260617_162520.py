import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from nucleo import processar_pagamento

if "pagamento recebido" in corpo.lower():
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° PAGAMENTO DETECTADO")
    processar_pagamento(29.90, "Pagamento PayPal automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico")


