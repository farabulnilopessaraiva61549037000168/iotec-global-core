import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# X27_ERROR_STATISTICS.py

from collections import Counter

arquivo = r"C:\IOTEC\X27_RUNTIME_REPORT.txt"

contador = Counter()

with open(
    arquivo,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    texto = f.read()

padroes = [
    "invalid syntax",
    "invalid character",
    "unterminated string literal",
    "expected",
    "invalid decimal literal"
]

for p in padroes:
    contador[p] = texto.count(p)

print()
print("="*50)
print("X27 ERROR STATISTICS")
print("="*50)

for erro, qtd in contador.items():
    print(f"{erro:<30} {qtd}")



