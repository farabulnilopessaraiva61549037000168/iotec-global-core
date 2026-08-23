import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import glob

ROOT = r"C:\IOTEC"

print("=" * 70)
print("IOTEC EXECUTION DISCOVERY")
print("=" * 70)
print()

arquivos = sorted(glob.glob(os.path.join(ROOT, "*.py")))

executaveis = []
bibliotecas = []

for arq in arquivos:

    try:

        with open(arq, "r", encoding="utf-8", errors="ignore") as f:
            codigo = f.read()

        if 'if __name__ == "__main__":' in codigo:
            executaveis.append(os.path.basename(arq))
        else:
            bibliotecas.append(os.path.basename(arq))

    except Exception:
        pass

print(f"Arquivos analisados : {len(arquivos)}")
print(f"ExecutÃ¡veis         : {len(executaveis)}")
print(f"Bibliotecas         : {len(bibliotecas)}")

print()
print("=" * 70)
print("EXECUTÃVEIS")
print("=" * 70)

for nome in executaveis[:100]:
    print(nome)

if len(executaveis) > 100:
    print(f"... +{len(executaveis)-100} executÃ¡veis")

print()
print("=" * 70)
print("ANÃLISE FINALIZADA")
print("=" * 70)




