import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC ARQUEOLOGIA DIGITAL CORPORATIVA

# ESCAVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O PROFUNDA DO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

# =========================================================



import os

import json

import hashlib

from datetime import datetime



# =========================================================

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================================================



BASE_OUTPUT = r"C:\IOTEC\ARQUEOLOGIA_DIGITAL"



OUTPUT_JSON = os.path.join(

    BASE_OUTPUT,

    "arqueologia_digital.json"

)



OUTPUT_TXT = os.path.join(

    BASE_OUTPUT,

    "relatorio_arqueologico.txt"

)



# =========================================================

# DIRETÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIOS A ESCAVAR

# ADICIONE MAIS CAMINHOS SE NECESSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIO

# =========================================================



RESERVATORIOS = [



    r"C:\IOTEC",



    os.path.join(

        os.path.expanduser("~"),

        "Downloads"

    ),



    os.path.join(

        os.path.expanduser("~"),

        "Desktop",

        "DIVERSOS"

    ),



    r"D:\IOTEC",



    r"D:\BACKUPS",



    r"D:\PROJETOS",



]



# =========================================================

# IGNORAR

# =========================================================



IGNORAR_PASTAS = [



    "node_modules",

    "__pycache__",

    ".git",

    "venv",

    "env",

    "dist",

    "build",

    "cache",

    "temp"



]



# =========================================================

# EXTENSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES IMPORTANTES

# =========================================================



EXTENSOES = (



    ".html",

    ".htm",

    ".css",

    ".js",

    ".py",

    ".json",

    ".sql",

    ".md",

    ".txt"



)



# =========================================================

# ESTRUTURA

# =========================================================



def criar_estrutura():
    pass



    os.makedirs(

        BASE_OUTPUT,

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



        return round(

            os.path.getsize(arquivo) / (1024 * 1024),

            2

        )



    except:
        pass

        return 0



# =========================================================

# IDENTIFICA ERA

# =========================================================



def identificar_era(caminho):
    pass



    caminho = caminho.lower()



    if "backup" in caminho:
        pass

        return "era_backup"



    if "clone" in caminho:
        pass

        return "era_clones"



    if "restore" in caminho:
        pass

        return "era_restauracao"



    if "old" in caminho:
        pass

        return "era_legado"



    if "v1" in caminho:
        pass

        return "era_v1"



    if "v2" in caminho:
        pass

        return "era_v2"



    return "era_atual"



# =========================================================

# IDENTIFICA VALOR

# =========================================================



def identificar_valor(nome):
    pass



    nome = nome.lower()



    termos = [



        "regulus",

        "lexus",

        "omega",

        "governance",

        "turca",

        "treasury",

        "premium",

        "core",

        "engine",

        "orchestrator",

        "dashboard"



    ]



    score = 0



    for termo in termos:
        pass



        if termo in nome:
            pass

            score += 20



    return min(score, 100)



# =========================================================

# DETECTA MATRIZ

# =========================================================



def detectar_matriz(nome):
    pass



    nome = nome.lower()



    if "clone" in nome:
        pass

        return False



    if "copy" in nome:
        pass

        return False



    if "backup" in nome:
        pass

        return False



    return True



# =========================================================

# ESCAVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================================================



def escavar_reservatorio(origem):
    pass



    encontrados = []



    for raiz, dirs, arquivos in os.walk(origem):
        pass



        dirs[:] = [



            d for d in dirs

            if d not in IGNORAR_PASTAS



        ]



        for arquivo in arquivos:
            pass



            if arquivo.endswith(EXTENSOES):
                pass



                caminho = os.path.join(

                    raiz,

                    arquivo

                )



                try:
                    pass



                    modificado = datetime.fromtimestamp(

                        os.path.getmtime(caminho)

                    )



                except:
                    pass



                    modificado = "desconhecido"



                registro = {



                    "arquivo": arquivo,



                    "caminho": caminho,



                    "extensao": os.path.splitext(

                        arquivo

                    )[1],



                    "hash": gerar_hash(

                        caminho

                    ),



                    "tamanho_mb": tamanho_mb(

                        caminho

                    ),



                    "era": identificar_era(

                        caminho

                    ),



                    "valor": identificar_valor(

                        arquivo

                    ),



                    "matriz": detectar_matriz(

                        arquivo

                    ),



                    "ultima_modificacao": str(

                        modificado

                    )

                }



                encontrados.append(

                    registro

                )



    return encontrados



# =========================================================

# DUPLICADOS

# =========================================================



def detectar_duplicados(dados):
    pass



    hashes = {}



    duplicados = []



    for item in dados:
        pass



        h = item["hash"]



        if h in hashes:
            pass



            duplicados.append(

                item

            )



        else:
            pass



            hashes[h] = item



    return duplicados



# =========================================================

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO

# =========================================================



def gerar_relatorio(dados, duplicados):
    pass



    total = len(dados)



    matrizes = len([

        x for x in dados

        if x["matriz"]

    ])



    premium = len([

        x for x in dados

        if x["valor"] >= 40

    ])



    with open(

        OUTPUT_TXT,

        "w",

        encoding="utf-8"

    ) as f:



        f.write("=" * 70 + "\n")

        f.write(" IOTEC ARQUEOLOGIA DIGITAL\n")

        f.write("=" * 70 + "\n\n")



        f.write(f"TOTAL DE ATIVOS: {total}\n")

        f.write(f"MATRIZES: {matrizes}\n")

        f.write(f"ATIVOS PREMIUM: {premium}\n")

        f.write(f"DUPLICADOS: {len(duplicados)}\n\n")



        f.write("=" * 70 + "\n")

        f.write(" TOP 100 MAIS VALIOSOS\n")

        f.write("=" * 70 + "\n\n")



        top = sorted(

            dados,

            key=lambda x: x["valor"],

            reverse=True

        )[:100]



        for item in top:
            pass



            linha = (

                f"[{item['valor']}] "

                f"{item['arquivo']} "

                f"-> {item['era']} "

                f"-> MATRIZ={item['matriz']}\n"

            )



            f.write(linha)



# =========================================================

# JSON

# =========================================================



def salvar_json(dados):
    pass



    with open(

        OUTPUT_JSON,

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



def executar():
    pass



    print("=" * 70)

    print(" IOTEC ARQUEOLOGIA DIGITAL")

    print("=" * 70)

    print()



    criar_estrutura()



    ativos = []



    for reservatorio in RESERVATORIOS:
        pass



        if os.path.exists(reservatorio):
            pass



            print(

                f"[+] ESCAVANDO -> {reservatorio}"

            )



            encontrados = escavar_reservatorio(

                reservatorio

            )



            ativos.extend(

                encontrados

            )



    print()

    print("[+] ANALISANDO DUPLICADOS")



    duplicados = detectar_duplicados(

        ativos

    )



    print()

    print("[+] GERANDO RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIOS")



    salvar_json(

        ativos

    )



    gerar_relatorio(

        ativos,

        duplicados

    )



    print()

    print("=" * 70)

    print(" ESCAVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O FINALIZADA")

    print("=" * 70)



    print()



    print(

        f"ATIVOS ENCONTRADOS: {len(ativos)}"

    )



    print(

        f"DUPLICADOS: {len(duplicados)}"

    )



    print()



    print(

        f"JSON -> {OUTPUT_JSON}"

    )



    print(

        f"TXT  -> {OUTPUT_TXT}"

    )



# =========================================================

# START

# =========================================================



if __name__ == "__main__":
    pass



    executar()




