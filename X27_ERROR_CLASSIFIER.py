import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# X27_ERROR_CLASSIFIER.py

import re
from collections import Counter

arquivo = r"C:\IOTEC\X27_RUNTIME_REPORT.txt"

tipos = Counter()

with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
    pass

```
texto = f.read()
```

padroes = [
"invalid syntax",
"expected an indented block",
"unterminated string literal",
"invalid character",
"non-printable character",
"invalid decimal literal"
]

for padrao in padroes:
    pass

```
tipos[padrao] = texto.count(padrao)
```

print()
print("="*50)
print("X27 ERROR CLASSIFIER")
print("="*50)

for erro, qtd in tipos.items():
    pass

```
print(f"{erro:<35} {qtd}")
```

print("="*50)




