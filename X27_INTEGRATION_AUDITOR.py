import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

print("=" * 70)
print("X27 INTEGRATION AUDITOR")
print("=" * 70)

print()

if not os.path.exists(ENV_FILE):

    print("ARQUIVO NAO ENCONTRADO")
    print()
    print(ENV_FILE)

else:

    print("ARQUIVO LOCALIZADO")
    print()
    print(ENV_FILE)
    print()

    with open(
        ENV_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        linhas = f.readlines()

    if len(linhas) == 0:

        print("ARQUIVO VAZIO")

    else:

        for linha in linhas:

            linha = linha.strip()

            if "=" in linha:

                chave, valor = linha.split("=", 1)

                status = (
                    "ONLINE"
                    if valor.strip()
                    else "OFFLINE"
                )

                print(
                    f"{chave:30} {status}"
                )

print()
print("=" * 70)



