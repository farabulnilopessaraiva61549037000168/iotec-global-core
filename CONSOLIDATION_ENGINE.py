import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC CONSOLIDATION ENGINE

# CONSOLIDACAO ORGANIZACIONAL DO ECOSSISTEMA

# =========================================================



from flask import Flask, jsonify



from flask_cors import CORS



from datetime import datetime



import os



import hashlib



import uuid



# =========================================================

# APP

# =========================================================



app = Flask(__name__)



CORS(app)



# =========================================================

# ROOT

# =========================================================



ROOT = r"C:\IOTEC"



# =========================================================

# BASES

# =========================================================



ARQUIVOS = []



DUPLICADOS = []



ORFAOS = []



PREMIUM = []



LABORATORIO = []



PRODUCAO = []



MAPA_HASH = {}



# =========================================================

# EXTENSOES

# =========================================================



VALIDOS = [



    ".py",

    ".html",

    ".css",

    ".js",

    ".jsx",

    ".json",

    ".md"

]



# =========================================================

# PALAVRAS PREMIUM

# =========================================================



PALAVRAS_PREMIUM = [



    "gateway",

    "kernel",

    "core",

    "engine",

    "tower",

    "autonomous",

    "adaptive",

    "security",

    "manager"

]



# =========================================================

# PALAVRAS LAB

# =========================================================



PALAVRAS_LAB = [



    "teste",

    "test",

    "backup",

    "old",

    "beta",

    "temp",

    "experimental",

    "rascunho",

    "prototype"

]



# =========================================================

# HASH

# =========================================================



def gerar_hash(path):
    pass



    try:
        pass



        with open(path, "rb") as f:
            pass



            return hashlib.md5(



                f.read()



            ).hexdigest()



    except:
        pass



        return None



# =========================================================

# PREMIUM

# =========================================================



def eh_premium(nome):
    pass



    nome = nome.lower()



    for palavra in PALAVRAS_PREMIUM:
        pass



        if palavra in nome:
            pass



            return True



    return False



# =========================================================

# LAB

# =========================================================



def eh_laboratorio(nome):
    pass



    nome = nome.lower()



    for palavra in PALAVRAS_LAB:
        pass



        if palavra in nome:
            pass



            return True



    return False



# =========================================================

# ORFAO

# =========================================================



def eh_orfao(path):
    pass



    try:
        pass



        tamanho = os.path.getsize(path)



        if tamanho < 200:
            pass



            return True



        return False



    except:
        pass



        return False



# =========================================================

# HOME

# =========================================================



@app.route('/')



def home():
    pass



    return jsonify({



        "engine":

        "online",



        "tipo":

        "consolidacao_organizacional",



        "empresa":

        "IOTEC",



        "timestamp":

        datetime.now().strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    })



# =========================================================

# CONSOLIDAR

# =========================================================



@app.route('/consolidation/executar')



def executar():
    pass



    global MAPA_HASH



    ARQUIVOS.clear()



    DUPLICADOS.clear()



    ORFAOS.clear()



    PREMIUM.clear()



    LABORATORIO.clear()



    PRODUCAO.clear()



    MAPA_HASH.clear()



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



            if ext not in VALIDOS:
                pass



                continue



            hash_arquivo = gerar_hash(path)



            item = {



                "id":

                str(uuid.uuid4()),



                "arquivo":

                arquivo,



                "path":

                path,



                "extensao":

                ext,



                "hash":

                hash_arquivo,



                "timestamp":

                datetime.now().strftime(

                    "%d/%m/%Y %H:%M:%S"

                )

            }



            # =================================================

            # DUPLICADOS

            # =================================================



            if hash_arquivo in MAPA_HASH:
                pass



                DUPLICADOS.append(item)



            else:
                pass



                MAPA_HASH[hash_arquivo] = path



            # =================================================

            # PREMIUM

            # =================================================



            if eh_premium(arquivo):
                pass



                PREMIUM.append(item)



            # =================================================

            # LAB

            # =================================================



            if eh_laboratorio(arquivo):
                pass



                LABORATORIO.append(item)



            else:
                pass



                PRODUCAO.append(item)



            # =================================================

            # ORFAOS

            # =================================================



            if eh_orfao(path):
                pass



                ORFAOS.append(item)



            ARQUIVOS.append(item)



    return jsonify({



        "status":

        "consolidacao_finalizada",



        "ativos":

        len(ARQUIVOS),



        "duplicados":

        len(DUPLICADOS),



        "orfÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡os":

        len(ORFAOS),



        "premium":

        len(PREMIUM),



        "laboratorio":

        len(LABORATORIO),



        "producao":

        len(PRODUCAO)

    })



# =========================================================

# DUPLICADOS

# =========================================================



@app.route('/consolidation/duplicados')



def duplicados():
    pass



    return jsonify({



        "duplicados":

        DUPLICADOS[:300]

    })



# =========================================================

# PREMIUM

# =========================================================



@app.route('/consolidation/premium')



def premium():
    pass



    return jsonify({



        "premium":

        PREMIUM[:300]

    })



# =========================================================

# ORFAOS

# =========================================================



@app.route('/consolidation/orfaos')



def orfaos():
    pass



    return jsonify({



        "orfaos":

        ORFAOS[:300]

    })



# =========================================================

# LAB

# =========================================================



@app.route('/consolidation/laboratorio')



def laboratorio():
    pass



    return jsonify({



        "laboratorio":

        LABORATORIO[:300]

    })



# =========================================================

# PRODUCAO

# =========================================================



@app.route('/consolidation/producao')



def producao():
    pass



    return jsonify({



        "producao":

        PRODUCAO[:300]

    })



# =========================================================

# EXECUTIVO

# =========================================================



@app.route('/consolidation/executivo')



def executivo():
    pass



    return jsonify({



        "empresa":

        "IOTEC",



        "modo":

        "governanca_consolidada",



        "ativos":

        len(ARQUIVOS),



        "duplicados":

        len(DUPLICADOS),



        "orfÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡os":

        len(ORFAOS),



        "premium":

        len(PREMIUM),



        "laboratorio":

        len(LABORATORIO),



        "producao":

        len(PRODUCAO),



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

    print(" IOTEC CONSOLIDATION ENGINE ")

    print("=" * 70)

    print("")



    app.run(



        host='0.0.0.0',



        port=7500

    )






