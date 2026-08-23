import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

from EXPANSAO_COMPLETA import processar_interface

arquivo = r"C:\IoTec\interfaces_origem\IOTEC BL ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Construtora de InovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes e Tecnologia.htm"

saida = processar_interface(arquivo)

print("Arquivo gerado:", saida)



