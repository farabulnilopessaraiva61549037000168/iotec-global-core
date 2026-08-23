import os
import re
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

ESTADOS = [
    "PROPOSTA_ENVIADA",
    "PAGAMENTO_PENDENTE",
    "AGUARDANDO_PAGAMENTO",
    "PAGAMENTO_RECEBIDO",
    "CLIENTE_ATIVO",
    "EM_ANALISE",
    "NEGOCIACAO"
]

print("="*70)
print("STATE TRANSITION ANALYZER")
print("="*70)

resultado = {}

for estado in ESTADOS:
    resultado[estado] = {
        "read": [],
        "write": []
    }

for arquivo in ROOT.rglob("*.py"):

    try:
        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except:
        continue

    linhas = texto.splitlines()

    for numero, linha in enumerate(linhas,1):

        for estado in ESTADOS:

            if estado not in linha:
                continue

            linha_upper = linha.upper()

            if (
                "UPDATE" in linha_upper
                or "SET" in linha_upper
                or "=" in linha
            ):
                resultado[estado]["write"].append(
                    (arquivo.name,numero)
                )
            else:
                resultado[estado]["read"].append(
                    (arquivo.name,numero)
                )

print()

for estado in ESTADOS:

    print("="*70)
    print(estado)
    print("="*70)

    print()

    print("ESCREVEM")

    if resultado[estado]["write"]:

        for arq,linha in resultado[estado]["write"]:
            print(f"  {arq}  (linha {linha})")

    else:

        print("  Nenhum")

    print()

    print("LEEM")

    if resultado[estado]["read"]:

        for arq,linha in resultado[estado]["read"]:
            print(f"  {arq}  (linha {linha})")

    else:

        print("  Nenhum")

    print()

print("="*70)
print("ANÃLISE")
print("="*70)

if len(resultado["PAGAMENTO_PENDENTE"]["write"]) == 0:

    print()
    print("GARGALO CONFIRMADO")
    print()
    print("Nenhum arquivo grava")
    print("PAGAMENTO_PENDENTE.")
    print()
    print("Existe uma transiÃ§Ã£o")
    print("faltando no fluxo.")
else:
    print("TransiÃ§Ã£o localizada.")


