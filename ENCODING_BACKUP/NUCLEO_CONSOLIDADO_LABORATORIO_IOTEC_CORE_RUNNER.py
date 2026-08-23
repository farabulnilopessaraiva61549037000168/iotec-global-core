import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
from mail_reader import ler_emails  # seu mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo iniciado...")

while True:
    try:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ Verificando e-mails...")
        ler_emails()

    except Exception as e:
        print("Erro:", e)

    time.sleep(30)  # verifica a cada 30 segundos


