# ==========================================================
# 098_DATA_STANDARDIZATION_CENTER.py
# IOTEC DATA STANDARDIZATION CENTER
# ==========================================================

import json
import os
from datetime import datetime

print("=" * 90)
print("IOTEC DATA STANDARDIZATION CENTER")
print("CENTRO DE PADRONIZAÃƒâ€¡ÃƒÆ'O DE DADOS")
print("=" * 90)
print()

ARQUIVOS = {

    "warehouse": "IOTEC_EXPERIENCE_WAREHOUSE.json",

    "visual": "IOTEC_VISUAL_GENOME.json",

    "assets": "IOTEC_OFFICIAL_ASSETS.json",

    "code": "IOTEC_CODE_LIBRARY.json"

}

PADRAO = {

    "generated_at": datetime.now().isoformat(),

    "statistics": {

        "python_modules": 0,

        "html_interfaces": 0,

        "javascript_files": 0,

        "css_files": 0,

        "official_assets": 0,

        "external_assets": 0,

        "products": 0,

        "apis": 0,

        "campaigns": 0,

        "customers": 0

    },

    "sources": {},

    "warnings": []

}

# ----------------------------------------------------------

def procurar_numero(obj, palavras):

    if isinstance(obj, dict):

        for k, v in obj.items():

            chave = str(k).lower()

            if any(p in chave for p in palavras):

                if isinstance(v, int):

                    return v

            r = procurar_numero(v, palavras)

            if r is not None:

                return r

    elif isinstance(obj, list):

        for item in obj:

            r = procurar_numero(item, palavras)

            if r is not None:

                return r

    return None

# ----------------------------------------------------------

print("Analisando arquivos...\n")

for nome, arquivo in ARQUIVOS.items():

    if not os.path.exists(arquivo):

        PADRAO["warnings"].append(f"{arquivo} nÃƒÂ£o encontrado")

        print("Ã°Å¸â€Â´", arquivo)

        continue

    try:

        with open(arquivo, "r", encoding="utf-8") as f:

            dados = json.load(f)

        PADRAO["sources"][nome] = arquivo

        print("Ã°Å¸Å¸Â¢", arquivo)

        # ------------------------

        if nome == "warehouse":

            html = procurar_numero(

                dados,

                [

                    "html",

                    "interface",

                    "arquivo"

                ]

            )

            js = procurar_numero(

                dados,

                [

                    "javascript",

                    "js"

                ]

            )

            css = procurar_numero(

                dados,

                [

                    "css"

                ]

            )

            if html:

                PADRAO["statistics"]["html_interfaces"] = html

            if js:

                PADRAO["statistics"]["javascript_files"] = js

            if css:

                PADRAO["statistics"]["css_files"] = css

        # ------------------------

        elif nome == "assets":

            oficial = procurar_numero(

                dados,

                [

                    "oficial",

                    "official",

                    "patrimonio"

                ]

            )

            externo = procurar_numero(

                dados,

                [

                    "extern",

                    "depend"

                ]

            )

            if oficial:

                PADRAO["statistics"]["official_assets"] = oficial

            if externo:

                PADRAO["statistics"]["external_assets"] = externo

        # ------------------------

        elif nome == "code":

            mods = procurar_numero(

                dados,

                [

                    "python",

                    "module",

                    "arquivo",

                    "estudado"

                ]

            )

            if mods:

                PADRAO["statistics"]["python_modules"] = mods

        # ------------------------

        elif nome == "visual":

            produtos = procurar_numero(

                dados,

                [

                    "product",

                    "produto"

                ]

            )

            if produtos:

                PADRAO["statistics"]["products"] = produtos

    except Exception as erro:

        PADRAO["warnings"].append(str(erro))

        print("Ã°Å¸Å¸Â¡", arquivo)

print()

print("=" * 90)
print("ESTRUTURA PADRONIZADA")
print("=" * 90)
print()

for k, v in PADRAO["statistics"].items():

    print(k.ljust(25), v)

print()

print("=" * 90)
print("VALIDAÃƒâ€¡ÃƒÆ'O")
print("=" * 90)
print()

if PADRAO["warnings"]:

    print()

    print("Avisos encontrados:\n")

    for w in PADRAO["warnings"]:

        print("Ã¢Å¡Â ", w)

else:

    print("Nenhuma inconsistÃƒÂªncia encontrada.")

print()

print("=" * 90)
print("GERANDO ARQUIVO")
print("=" * 90)
print()

with open(

    "IOTEC_STANDARD_DATA.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        PADRAO,

        f,

        indent=4,

        ensure_ascii=False

    )

print("IOTEC_STANDARD_DATA.json criado com sucesso.")
print()

print("=" * 90)
print("MISSÃƒÆ'O")
print("=" * 90)
print()

print("Todos os departamentos")
print("passam a compartilhar")
print("a mesma estrutura")
print("de dados.")
print()

print("O Kernel deixa")
print("de depender")
print("de formatos")
print("diferentes.")
print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("PADRONIZAÃƒâ€¡ÃƒÆ'O CONCLUÃƒÂDA.")


