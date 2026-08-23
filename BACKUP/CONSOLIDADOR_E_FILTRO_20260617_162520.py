import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC - CONSOLIDADOR E FILTRO PROFISSIONAL

# REGULUS CORE ORGANIZER v2.0

# EMPRESA: IOTEC

# OBJETIVO:

# FILTRAR DEPENDÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIAS EXTERNAS

# IDENTIFICAR MATRIZES REAIS

# ORGANIZAR O NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO PROFISSIONALMENTE

# ============================================================



import os

import json

import shutil

import hashlib

from datetime import datetime

from collections import defaultdict



# ============================================================

# PASTAS ANALISADAS

# ============================================================



PASTAS_ANALISE = [

    r"C:\IOTEC",

    r"C:\Users\Bruno Lopes\Downloads",

    r"C:\Users\Bruno Lopes\Desktop\DIVERSOS",

    r"D:\IOTEC"

]



# ============================================================

# EXTENSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES IMPORTANTES

# ============================================================



EXTENSOES_VALIDAS = [

    ".py",

    ".html",

    ".css",

    ".js",

    ".json",

    ".tsx",

    ".jsx",

    ".sql"

]



# ============================================================

# PASTAS DE RISCO / DEPENDÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIAS

# ============================================================



IGNORAR_PASTAS = [



    "site-packages",

    "node_modules",

    "venv",

    "anaconda",

    "Lib",

    "vendor",

    "conda-meta",

    "__pycache__",

    ".git",

    ".idea",

    ".vscode"



]



# ============================================================

# PALAVRAS-CHAVE IOTEC

# ============================================================



PALAVRAS_IOTEC = [



    "iotec",

    "regulus",

    "dashboard",

    "enterprise",

    "govtech",

    "analytics",

    "juris",

    "core",

    "engine",

    "omega",

    "interface",

    "frontend",

    "backend"



]



# ============================================================

# ESTRUTURA CENTRAL

# ============================================================



NUCLEO = {

    "empresa": "IOTEC",

    "cidade": "REGULUS_CITY",

    "modo": "consolidacao_profissional",

    "status": "online",

    "timestamp": str(datetime.now())

}



# ============================================================

# SAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDA PROFISSIONAL

# ============================================================



BASE_SAIDA = r"C:\IOTEC\NUCLEO_CONSOLIDADO"



PASTAS_SAIDA = {



    "matrizes": os.path.join(BASE_SAIDA, "MATRIZES"),

    "laboratorio": os.path.join(BASE_SAIDA, "LABORATORIO"),

    "frontend": os.path.join(BASE_SAIDA, "FRONTEND"),

    "backend": os.path.join(BASE_SAIDA, "BACKEND"),

    "analytics": os.path.join(BASE_SAIDA, "ANALYTICS"),

    "financeiro": os.path.join(BASE_SAIDA, "FINANCEIRO"),

    "govtech": os.path.join(BASE_SAIDA, "GOVTECH"),

    "juridico": os.path.join(BASE_SAIDA, "JURIDICO"),

    "duplicados": os.path.join(BASE_SAIDA, "DUPLICADOS"),

    "quarentena": os.path.join(BASE_SAIDA, "QUARENTENA"),

    "logs": os.path.join(BASE_SAIDA, "LOGS")



}



# ============================================================

# CRIAR PASTAS

# ============================================================



for pasta in PASTAS_SAIDA.values():
    pass

    os.makedirs(pasta, exist_ok=True)



# ============================================================

# BANCO CENTRAL

# ============================================================



ATIVOS = []

HASHES = {}

DUPLICADOS = []

LOGS = []



# ============================================================

# LOG

# ============================================================



def registrar_log(evento):
    pass



    LOGS.append({

        "timestamp": str(datetime.now()),

        "evento": evento

    })



# ============================================================

# HASH

# ============================================================



def gerar_hash(caminho):
    pass



    try:
        pass



        with open(caminho, "rb") as f:
            pass

            return hashlib.md5(f.read()).hexdigest()



    except:
        pass

        return None



# ============================================================

# DETECTAR RISCO

# ============================================================



def eh_dependencia_externa(caminho):
    pass



    caminho_lower = caminho.lower()



    for pasta in IGNORAR_PASTAS:
        pass



        if pasta.lower() in caminho_lower:
            pass

            return True



    return False



# ============================================================

# DETECTAR IDENTIDADE IOTEC

# ============================================================



def eh_ativo_iotec(nome):
    pass



    nome = nome.lower()



    for palavra in PALAVRAS_IOTEC:
        pass



        if palavra in nome:
            pass

            return True



    return False



# ============================================================

# CLASSIFICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



def classificar(nome):
    pass



    nome = nome.lower()



    if "html" in nome or "css" in nome:
        pass

        return "frontend"



    if "api" in nome or "server" in nome:
        pass

        return "backend"



    if "analytics" in nome or "dashboard" in nome:
        pass

        return "analytics"



    if "finance" in nome or "paypal" in nome:
        pass

        return "financeiro"



    if "gov" in nome:
        pass

        return "govtech"



    if "juris" in nome or "legal" in nome:
        pass

        return "juridico"



    return "laboratorio"



# ============================================================

# ESCAVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O PROFISSIONAL

# ============================================================



def escavar():
    pass



    print("\n======================================================")

    print(" IOTEC CONSOLIDADOR PROFISSIONAL")

    print("======================================================")



    total = 0



    for pasta in PASTAS_ANALISE:
        pass



        print(f"\n[+] ANALISANDO -> {pasta}")



        if not os.path.exists(pasta):
            pass

            continue



        for raiz, dirs, arquivos in os.walk(pasta):
            pass



            dirs[:] = [

                d for d in dirs

                if d not in IGNORAR_PASTAS

            ]



            for arquivo in arquivos:
                pass



                ext = os.path.splitext(arquivo)[1].lower()



                if ext not in EXTENSOES_VALIDAS:
                    pass

                    continue



                caminho = os.path.join(raiz, arquivo)



                if eh_dependencia_externa(caminho):
                    pass



                    registrar_log(

                        f"DEPENDENCIA IGNORADA -> {caminho}"

                    )



                    continue



                hash_arquivo = gerar_hash(caminho)



                if hash_arquivo in HASHES:
                    pass



                    DUPLICADOS.append(caminho)



                    registrar_log(

                        f"DUPLICADO -> {caminho}"

                    )



                    try:
                        pass

                        shutil.copy2(

                            caminho,

                            PASTAS_SAIDA["duplicados"]

                        )

                    except:
                        pass

                        pass



                    continue



                HASHES[hash_arquivo] = caminho



                tipo = classificar(arquivo)



                ativo = {

                    "nome": arquivo,

                    "caminho": caminho,

                    "tipo": tipo,

                    "hash": hash_arquivo,

                    "iotec": eh_ativo_iotec(arquivo)

                }



                ATIVOS.append(ativo)



                destino = PASTAS_SAIDA[tipo]



                try:
                    pass



                    shutil.copy2(caminho, destino)



                except:
                    pass



                    registrar_log(

                        f"ERRO COPIA -> {caminho}"

                    )



                total += 1



    print("\n======================================================")

    print(" ESCAVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O FINALIZADA")

    print("======================================================")



    print(f"\nATIVOS PROFISSIONAIS: {total}")

    print(f"DUPLICADOS: {len(DUPLICADOS)}")



# ============================================================

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO ESTRATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°GICO

# ============================================================



def relatorio():
    pass



    print("\n======================================================")

    print(" MAPA ESTRATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°GICO")

    print("======================================================")



    setores = defaultdict(int)



    for ativo in ATIVOS:
        pass

        setores[ativo["tipo"]] += 1



    for setor, quantidade in setores.items():
        pass



        print(f"\n{setor.upper()} -> {quantidade}")



# ============================================================

# MATRIZES IMPORTANTES

# ============================================================



def matrizes():
    pass



    print("\n======================================================")

    print(" MATRIZES IOTEC")

    print("======================================================")



    encontrados = 0



    for ativo in ATIVOS:
        pass



        if ativo["iotec"]:
            pass



            encontrados += 1



            print(f"\nNOME: {ativo['nome']}")

            print(f"TIPO: {ativo['tipo']}")

            print(f"CAMINHO: {ativo['caminho']}")



            try:
                pass



                shutil.copy2(

                    ativo["caminho"],

                    PASTAS_SAIDA["matrizes"]

                )



            except:
                pass

                pass



            if encontrados >= 30:
                pass

                break



# ============================================================

# EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O JSON

# ============================================================



def exportar():
    pass



    relatorio = {



        "nucleo": NUCLEO,

        "ativos": len(ATIVOS),

        "duplicados": len(DUPLICADOS),

        "logs": LOGS,

        "timestamp": str(datetime.now())



    }



    arquivo = os.path.join(

        BASE_SAIDA,

        "RELATORIO_CONSOLIDADO.json"

    )



    with open(arquivo, "w", encoding="utf-8") as f:
        pass



        json.dump(

            relatorio,

            f,

            indent=4,

            ensure_ascii=False

        )



    print("\n======================================================")

    print(" EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

    print("======================================================")



    print(f"\nJSON -> {arquivo}")



# ============================================================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



def iniciar():
    pass



    escavar()



    relatorio()



    matrizes()



    exportar()



    print("\n======================================================")

    print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO CONSOLIDADO COM SUCESSO")

    print("======================================================\n")



# ============================================================

# START

# ============================================================



if __name__ == "__main__":
    pass

    iniciar()




