# ==========================================================
# 099_JSON_ARCHAEOLOGIST.py
# IOTEC JSON ARCHAEOLOGIST
# ==========================================================

import os
import json
from datetime import datetime

print("=" * 90)
print("IOTEC JSON ARCHAEOLOGIST")
print("ARQUEÃƒâ€œLOGO DOS JSONS DA IOTEC")
print("=" * 90)
print()

ROOT = r"C:\IOTEC"

mapa = {
    "generated_at": datetime.now().isoformat(),
    "json_files": []
}


def explorar(obj):

    estrutura = {}

    if isinstance(obj, dict):

        estrutura["type"] = "object"
        estrutura["keys"] = {}

        for k, v in obj.items():

            estrutura["keys"][k] = explorar(v)

    elif isinstance(obj, list):

        estrutura["type"] = "list"

        estrutura["items"] = len(obj)

        if obj:

            estrutura["sample"] = explorar(obj[0])

    else:

        estrutura["type"] = type(obj).__name__

    return estrutura


total = 0

print("Escavando arquivos JSON...\n")

for pasta, _, arquivos in os.walk(ROOT):

    for arquivo in arquivos:

        if not arquivo.lower().endswith(".json"):
            continue

        caminho = os.path.join(pasta, arquivo)

        try:

            with open(caminho, "r", encoding="utf-8") as f:

                dados = json.load(f)

            estrutura = explorar(dados)

            mapa["json_files"].append({

                "arquivo": arquivo,

                "caminho": caminho,

                "estrutura": estrutura

            })

            total += 1

            print("Ã°Å¸Å¸Â¢", arquivo)

        except Exception as erro:

            mapa["json_files"].append({

                "arquivo": arquivo,

                "erro": str(erro)

            })

            print("Ã°Å¸â€Â´", arquivo)

print()

print("=" * 90)
print("RESUMO")
print("=" * 90)
print()

print("JSON encontrados........", total)
print()

print("=" * 90)
print("TOP 20")
print("=" * 90)
print()

for item in mapa["json_files"][:20]:

    print()

    print(item["arquivo"])

    if "estrutura" in item:

        estrutura = item["estrutura"]

        if estrutura["type"] == "object":

            print("Campos:")

            for campo in estrutura["keys"]:

                print("   Ã¢â‚¬Â¢", campo)

    else:

        print("Erro:", item["erro"])

print()

with open(

    "IOTEC_JSON_MAP.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        mapa,

        f,

        indent=4,

        ensure_ascii=False

    )

print("=" * 90)
print("ARQUIVO GERADO")
print("=" * 90)
print()

print("IOTEC_JSON_MAP.json")
print()

print("=" * 90)
print("MISSÃƒÆ'O")
print("=" * 90)
print()

print("O Kernel passa")
print("a conhecer")
print("a estrutura")
print("de todos")
print("os JSON")
print("da empresa.")
print()

print("Nenhum arquivo")
print("permanece")
print("desconhecido.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("JSON ARCHAEOLOGIST OPERACIONAL.")


