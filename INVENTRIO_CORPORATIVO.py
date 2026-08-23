import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC INVENTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO CORPORATIVO IMPERIAL

# ENTERPRISE INVENTORY ENGINE

# =========================================================



import os

import json

import hashlib

from datetime import datetime



# =========================================================

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# =========================================================



BASE_DIR = r"C:\IOTEC"



DOWNLOADS_DIR = os.path.join(

    os.path.expanduser("~"),

    "Downloads"

)



DIVERSOS_DIR = os.path.join(

    os.path.expanduser("~"),

    "Desktop",

    "DIVERSOS"

)



OUTPUT_DIR = os.path.join(

    BASE_DIR,

    "INVENTARIO_IMPERIAL"

)



JSON_OUTPUT = os.path.join(

    OUTPUT_DIR,

    "inventario_corporativo.json"

)



TXT_OUTPUT = os.path.join(

    OUTPUT_DIR,

    "inventario_executivo.txt"

)



# =========================================================

# DISTRITOS

# =========================================================



DISTRITOS = {



    "lexus_juris": [

        "juris",

        "adv",

        "legal",

        "tribunal",

        "juridico"

    ],



    "casa_turca": [

        "finance",

        "market",

        "consorcio",

        "treasury",

        "import"

    ],



    "regulus": [

        "media",

        "turismo",

        "luxo",

        "lifestyle",

        "premium"

    ],



    "omega": [

        "data",

        "analytics",

        "ai",

        "dashboard"

    ],



    "educacao": [

        "escola",

        "aluno",

        "professor",

        "educacao"

    ]

}



# =========================================================

# EXTENSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# =========================================================



EXTENSOES_VALIDAS = (

    ".html",

    ".htm",

    ".css",

    ".js",

    ".py",

    ".json"

)



# =========================================================

# ESTRUTURA

# =========================================================



def criar_estrutura():
    pass



    os.makedirs(

        OUTPUT_DIR,

        exist_ok=True

    )



# =========================================================

# HASH

# =========================================================



def gerar_hash(arquivo):
    pass



    sha = hashlib.sha256()



    try:
        pass



        with open(arquivo, "rb") as f:
            pass



            while True:
                pass



                bloco = f.read(4096)



                if not bloco:
                    pass

                    break



                sha.update(bloco)



        return sha.hexdigest()



    except:
        pass

        return "erro_hash"



# =========================================================

# TAMANHO

# =========================================================



def tamanho_mb(arquivo):
    pass



    try:
        pass



        tamanho = os.path.getsize(arquivo)



        return round(

            tamanho / (1024 * 1024),

            2

        )



    except:
        pass

        return 0



# =========================================================

# DISTRITO

# =========================================================



def identificar_distrito(nome):
    pass



    nome = nome.lower()



    for distrito, palavras in DISTRITOS.items():
        pass



        for palavra in palavras:
            pass



            if palavra in nome:
                pass

                return distrito



    return "indefinido"



# =========================================================

# CATEGORIA

# =========================================================



def categoria_arquivo(ext):
    pass



    mapa = {



        ".html": "frontend",

        ".htm": "frontend",

        ".css": "estilo_visual",

        ".js": "javascript",

        ".py": "backend_python",

        ".json": "dados"

    }



    return mapa.get(

        ext,

        "desconhecido"

    )



# =========================================================

# VALORAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================================================



def nivel_valor(nome):
    pass



    nome = nome.lower()



    premium = [

        "regulus",

        "lexus",

        "omega",

        "turca",

        "treasury",

        "governance"

    ]



    for termo in premium:
        pass



        if termo in nome:
            pass

            return "estrategico"



    return "operacional"



# =========================================================

# INVENTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO

# =========================================================



def inventariar_pasta(origem):
    pass



    inventario = []



    for raiz, dirs, arquivos in os.walk(origem):
        pass



        for arquivo in arquivos:
            pass



            if arquivo.endswith(

                EXTENSOES_VALIDAS

            ):



                caminho = os.path.join(

                    raiz,

                    arquivo

                )



                nome, ext = os.path.splitext(

                    arquivo

                )



                registro = {



                    "arquivo": arquivo,



                    "caminho": caminho,



                    "extensao": ext,



                    "categoria": categoria_arquivo(

                        ext

                    ),



                    "distrito": identificar_distrito(

                        arquivo

                    ),



                    "valor": nivel_valor(

                        arquivo

                    ),



                    "hash": gerar_hash(

                        caminho

                    ),



                    "tamanho_mb": tamanho_mb(

                        caminho

                    ),



                    "ultima_modificacao": str(

                        datetime.fromtimestamp(

                            os.path.getmtime(caminho)

                        )

                    )

                }



                inventario.append(

                    registro

                )



    return inventario



# =========================================================

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO TXT

# =========================================================



def gerar_relatorio_txt(dados):
    pass



    total = len(dados)



    estrategicos = len([

        x for x in dados

        if x["valor"] == "estrategico"

    ])



    operacionais = len([

        x for x in dados

        if x["valor"] == "operacional"

    ])



    with open(

        TXT_OUTPUT,

        "w",

        encoding="utf-8"

    ) as f:



        f.write("=" * 70 + "\n")

        f.write(" IOTEC INVENTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO CORPORATIVO IMPERIAL\n")

        f.write("=" * 70 + "\n\n")



        f.write(f"TOTAL DE ATIVOS: {total}\n")

        f.write(f"ATIVOS ESTRATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°GICOS: {estrategicos}\n")

        f.write(f"ATIVOS OPERACIONAIS: {operacionais}\n\n")



        f.write("=" * 70 + "\n")

        f.write(" DISTRITOS IDENTIFICADOS\n")

        f.write("=" * 70 + "\n\n")



        distritos = {}



        for item in dados:
            pass



            d = item["distrito"]



            if d not in distritos:
                pass

                distritos[d] = 0



            distritos[d] += 1



        for distrito, qtd in distritos.items():
            pass



            f.write(

                f"{distrito.upper()} -> {qtd} ativos\n"

            )



        f.write("\n")

        f.write("=" * 70 + "\n")

        f.write(" FIM DO RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO\n")

        f.write("=" * 70 + "\n")



# =========================================================

# JSON

# =========================================================



def salvar_json(dados):
    pass



    with open(

        JSON_OUTPUT,

        "w",

        encoding="utf-8"

    ) as f:



        json.dump(

            dados,

            f,

            indent=4,

            ensure_ascii=False

        )



# =========================================================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================================================



def executar_inventario():
    pass



    print("=" * 70)

    print(" IOTEC INVENTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO CORPORATIVO IMPERIAL")

    print("=" * 70)

    print()



    criar_estrutura()



    inventario_total = []



    if os.path.exists(DOWNLOADS_DIR):
        pass



        print("[+] ANALISANDO DOWNLOADS")



        inventario_total.extend(

            inventariar_pasta(

                DOWNLOADS_DIR

            )

        )



    if os.path.exists(DIVERSOS_DIR):
        pass



        print("[+] ANALISANDO DIVERSOS")



        inventario_total.extend(

            inventariar_pasta(

                DIVERSOS_DIR

            )

        )



    print()

    print("[+] GERANDO RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIOS")



    salvar_json(

        inventario_total

    )



    gerar_relatorio_txt(

        inventario_total

    )



    print()

    print("=" * 70)

    print(" INVENTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO FINALIZADO")

    print("=" * 70)



    print()



    print(f"ATIVOS ENCONTRADOS: {len(inventario_total)}")



    print()

    print(f"JSON -> {JSON_OUTPUT}")

    print(f"TXT  -> {TXT_OUTPUT}")



# =========================================================

# START

# =========================================================



if __name__ == "__main__":
    pass



    executar_inventario()






