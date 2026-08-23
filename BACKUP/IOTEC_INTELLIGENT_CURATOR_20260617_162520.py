import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, jsonify

from flask_cors import CORS

from datetime import datetime

import os

import uuid



app = Flask(__name__)

CORS(app)



ROOT = r"C:\IOTEC"



ATIVOS = []



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



@app.route('/')



def home():
    pass



    return jsonify({



        "empresa": "IOTEC",



        "modo": "organizacao_inteligente",



        "curator": "online",



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



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



            if arquivo in nomes:
                pass



                MAPAS["duplicados"].append(ativo)



            nomes.append(arquivo)



            if ext in [

                ".html",

                ".css",

                ".js",

                ".jsx"

            ]:



                MAPAS["interfaces"].append(ativo)



            if ext == ".py":
                pass



                MAPAS["backends"].append(ativo)



            for categoria in ativo["categorias"]:
                pass



                MAPAS[categoria].append(ativo)



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



        "interfaces":

        len(MAPAS["interfaces"]),



        "top_ativos":

        premium[:20],



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



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




