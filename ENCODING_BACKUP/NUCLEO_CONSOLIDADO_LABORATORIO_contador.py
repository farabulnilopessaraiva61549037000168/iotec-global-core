import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Contador de 1 a 5
for i in range(1, 6):
    print(f"NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºmero: {i}")



