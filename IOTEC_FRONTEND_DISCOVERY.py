import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

print("\nIOTEC FRONTEND DISCOVERY\n")

extensoes = [
    "*.html",
    "*.htm",
    "*.js",
    "*.jsx",
    "*.ts",
    "*.tsx"
]

achados = []

for ext in extensoes:
    pass

    for arq in ROOT.rglob(ext):
        pass

        achados.append(arq)

print("ARQUIVOS ENCONTRADOS:", len(achados))
print("")

for item in sorted(achados):
    pass

    nome = item.name.lower()

    if any(
        chave in nome
        for chave in [
            "contact",
            "lead",
            "form",
            "orcamento",
            "pagamento",
            "checkout",
            "cliente",
            "portal"
        ]
    ):

        print(item)

print("")
print("FIM")




