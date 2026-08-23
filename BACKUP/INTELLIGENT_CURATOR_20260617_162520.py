import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC INTELLIGENT CURATOR

# CURADORIA OPERACIONAL INTELIGENTE

# =========================================================



from flask import Flask, jsonify



from flask_cors import CORS



from datetime import datetime



import os



import json



import uuid



# =========================================================

# APP

# =========================================================



app = Flask(__name__)



CORS(app)



# =========================================================

# CONFIG

# =========================================================



ROOT = r"C:\IOTEC"



# =========================================================

# BIBLIOTECA

# =========================================================



ATIVOS = []



# =========================================================

# MAPAS

# =========================================================



MAPAS = {



    "interfaces": [],



    "backends": [],



    "engines": [],



    "governanca": [],



    "seguranca": [],



    "autonomia": [],



    "marketing": [],



    "producao": [],



    "analise": [],



    "duplicados": [],



    "premium": []

}



# =========================================================

# CLASSIFICADOR

# =========================================================



PALAVRAS_CHAVE = {



    "engines": [



        "engine",

        "core",

        "gateway",

        "kernel",

        "master"

    ],



    "governanca": [



        "govern",

        "control",

        "tower",

        "manager",

        "supervisor"

    ],



    "seguranca": [



        "security",

        "protect",

        "audit",

        "shield"

    ],



    "autonomia": [



        "auto",

        "adaptive",

        "autonomous"

    ],



    "marketing": [



        "cliente",

        "marketing",

        "publicidade",

        "branding",

        "atendente"

    ],



    "producao": [



        "dashboard",

        "interface",

        "visual",

        "frontend",

        "html"

    ],



    "analise": [



        "analise",

        "analytics",

        "diagnostico",

        "detectar"

    ]

}



# =========================================================

# CLASSIFICAR

# =========================================================



def classificar(nome):
    pass



    nome_lower = nome.lower()



    categorias = []



    for categoria, palavras in PALAVRAS_CHAVE.items():
        pass



        for palavra in palavras:
            pass



            if palavra in nome_lower:
                pass



                categorias.append(categoria)



                break



    return categorias



# =========================================================

# PREMIUM SCORE

# =========================================================



def premium_score(nome):
    pass



    score = 0



    nome = nome.lower()



    if "iotec" in nome:
        pass



        score += 3



    if "core" in nome:
        pass



        score += 4



    if "engine" in nome:
        pass



        score += 4



    if "gateway" in nome:
        pass



        score += 5



    if "adaptive" in nome:
        pass



        score += 5



    if "autonomous" in nome:
        pass



        score += 5



    if "global" in nome:
        pass



        score += 4



    if "intelligence" in nome:
        pass



        score += 5



    return score



# =========================================================

# EXPLORAR

# =========================================================



@app.route('/curator/explorar')



def explorar():
    pass



    global ATIVOS



    ATIVOS.clear()



    for chave in MAPAS:
        pass



        MAPAS[chave].clear()



    nomes = []



    for pasta, subpastas, arquivos in os.walk(ROOT):
        pass



        for arquivo in arquivos:
            pass



            path = os.path.join(



                pasta,

                arquivo

            )



            ext = os.path.splitext(



                arquivo

            )[1].lower()



            if ext not in [



                ".py",

                ".html",

                ".js",

                ".jsx",

                ".json",

                ".css"

            ]:



                continue



            ativo = {



                "id":

                str(uuid.uuid4()),



                "arquivo":

                arquivo,



                "path":

                path,



                "extensao":

                ext,



                "categorias":

                classificar(arquivo),



                "score":

                premium_score(arquivo),



                "timestamp":

                datetime.now().strftime(

                    "%d/%m/%Y %H:%M:%S"

                )

            }



            # =================================================

            # DUPLICADOS

            # =================================================



            if arquivo in nomes:
                pass



                MAPAS["duplicados"].append(ativo)



            nomes.append(arquivo)



            # =================================================

            # INTERFACES

            # =================================================



            if ext in [



                ".html",

                ".css",

                ".js",

                ".jsx"

            ]:



                MAPAS["interfaces"].append(ativo)



            # =================================================

            # BACKENDS

            # =================================================



            if ext == ".py":
                pass



                MAPAS["backends"].append(ativo)



            # =================================================

            # CATEGORIAS

            # =================================================



            for categoria in ativo["categorias"]:
                pass



                MAPAS[categoria].append(ativo)



            # =================================================

            # PREMIUM

            # =================================================



            if ativo["score"] >= 8:
                pass



                MAPAS["premium"].append(ativo)



            ATIVOS.append(ativo)



    return jsonify({



        "status":

        "curadoria_finalizada",



        "ativos":

        len(ATIVOS),



        "premium":

        len(MAPAS["premium"]),



        "interfaces":

        len(MAPAS["interfaces"]),



        "backends":

        len(MAPAS["backends"]),



        "duplicados":

        len(MAPAS["duplicados"])

    })



# =========================================================

# MAPA

# =========================================================



@app.route('/curator/mapa')



def mapa():
    pass



    resumo = {}



    for categoria, itens in MAPAS.items():
        pass



        resumo[categoria] = len(itens)



    return jsonify({



        "modo":

        "organizacao_inteligente",



        "resumo":

        resumo

    })



# =========================================================

# PREMIUM

# =========================================================



@app.route('/curator/premium')



def premium():
    pass



    premium = sorted(



        MAPAS["premium"],



        key=lambda x: x["score"],



        reverse=True

    )



    return jsonify({



        "premium":

        len(premium),



        "ativos":

        premium[:100]

    })



# =========================================================

# GOVERNANCA

# =========================================================



@app.route('/curator/governanca')



def governanca():
    pass



    return jsonify({



        "governanca":

        MAPAS["governanca"][:100]

    })



# =========================================================

# ENGINES

# =========================================================



@app.route('/curator/engines')



def engines():
    pass



    return jsonify({



        "engines":

        MAPAS["engines"][:100]

    })



# =========================================================

# PRODUCAO

# =========================================================



@app.route('/curator/producao')



def producao():
    pass



    return jsonify({



        "producao":

        MAPAS["producao"][:100]

    })



# =========================================================

# DUPLICADOS

# =========================================================



@app.route('/curator/duplicados')



def duplicados():
    pass



    return jsonify({



        "duplicados":

        MAPAS["duplicados"][:100]

    })



# =========================================================

# RELATORIO EXECUTIVO

# =========================================================



@app.route('/curator/executivo')



def executivo():
    pass



    premium = sorted(



        MAPAS["premium"],



        key=lambda x: x["score"],



        reverse=True

    )



    return jsonify({



        "empresa":

        "IOTEC",



        "modo":

        "curadoria_executiva",



        "ativos":

        len(ATIVOS),



        "premium":

        len(MAPAS["premium"]),



        "engines":

        len(MAPAS["engines"]),



        "governanca":

        len(MAPAS["governanca"]),



        "seguranca":

        len(MAPAS["seguranca"]),



        "autonomia":

        len(MAPAS["autonomia"]),



        "interfaces":

        len(MAPAS["interfaces"]),



        "top_ativos":

        premium[:20],



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# START

# =========================================================



if __name__ == '__main__':
    pass



    print("")

    print("=" * 70)

    print(" IOTEC INTELLIGENT CURATOR ")

    print("=" * 70)

    print("")



    app.run(



        host='0.0.0.0',



        port=7400

    )




