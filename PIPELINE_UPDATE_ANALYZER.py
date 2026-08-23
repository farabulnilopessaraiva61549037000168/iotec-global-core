from pathlib import Path
import re

ROOT = Path(r"C:\IOTEC")

print("="*70)
print("PIPELINE UPDATE ANALYZER")
print("="*70)

padrao = re.compile(
    r"UPDATE\s+pipeline.*?SET.*?status\s*=\s*['"]([^'"]+)['"]",
    re.IGNORECASE | re.DOTALL
)

encontrou = False

for arquivo in ROOT.rglob("*.py"):

    try:
        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except:
        continue

    for m in padrao.finditer(texto):

        encontrou = True

        print()
        print("-"*70)
        print(arquivo.name)
        print("-"*70)
        print("Novo status:", m.group(1))

if not encontrou:

    print()
    print("Nenhum UPDATE pipeline SET status localizado.")


