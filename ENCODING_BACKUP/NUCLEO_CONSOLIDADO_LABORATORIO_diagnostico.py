import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

BASE = os.path.join(os.path.expanduser("~"), "Desktop", "OFICINA_IOTEC")

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Verificando:", BASE)
print("="*50)

if not os.path.exists(BASE):
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ PASTA NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EXISTE")
else:
    for raiz, dirs, arquivos in os.walk(BASE):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â", raiz)
        for a in arquivos:
            print("   -", a)


