import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import glob
import hashlib
from datetime import datetime

ROOT = r"C:\IOTEC"

print("="*70)
print("IOTEC MODULE REGISTRY")
print("="*70)
print()

arquivos = sorted(glob.glob(ROOT+"\\*.py"))

registro=[]

for arq in arquivos:

    try:

        nome=os.path.basename(arq)

        tamanho=os.path.getsize(arq)

        data=datetime.fromtimestamp(
            os.path.getmtime(arq)
        ).strftime("%d/%m/%Y %H:%M")

        with open(arq,"rb") as f:

            md5=hashlib.md5(f.read()).hexdigest()[:12]

        registro.append({

            "nome":nome,

            "size":tamanho,

            "data":data,

            "hash":md5

        })

    except Exception:

        pass

print(f"MÃ"DULOS REGISTRADOS : {len(registro)}")
print()

for r in registro:

    print(f"{r['nome']:40} {r['size']:8} bytes   {r['hash']}")

print()
print("="*70)
print("REGISTRY FINALIZADO")
print("="*70)





