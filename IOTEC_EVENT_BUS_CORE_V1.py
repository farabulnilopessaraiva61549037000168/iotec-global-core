import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC EVENT BUS CORE V1.0
#
# Sistema nervoso central da plataforma
#
# FunÃƒÂ§ÃƒÂ£o:
# Receber, registrar e distribuir eventos reais
# dos mÃƒÂ³dulos IoTec.
#
# Fluxo:
#
# AGENTE
#   |
#   v
# EVENT BUS
#   |
#   v
# COMMAND TOWER
#
# ===============================================================


from flask import Flask, request, jsonify
from datetime import datetime
import json
from pathlib import Path


app = Flask(__name__)


ARQUIVO_MEMORIA = Path(
    "IOTEC_OPERATION_MEMORY.json"
)



# ---------------------------------------------------------------
# Inicializa memÃƒÂ³ria
# ---------------------------------------------------------------

def carregar_memoria():

    if ARQUIVO_MEMORIA.exists():

        with open(
            ARQUIVO_MEMORIA,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)


    return {
        "eventos": []
    }





def salvar_memoria(memoria):

    with open(
        ARQUIVO_MEMORIA,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            memoria,
            arquivo,
            indent=4,
            ensure_ascii=False
        )





# ---------------------------------------------------------------
# Receber evento dos agentes
# ---------------------------------------------------------------

@app.route(
    "/evento",
    methods=["POST"]
)
def receber_evento():


    dados = request.json


    evento = {


        "timestamp":
        str(datetime.now()),


        "origem":
        dados.get(
            "origem",
            "desconhecida"
        ),


        "tipo":
        dados.get(
            "tipo",
            "evento"
        ),


        "descricao":
        dados.get(
            "descricao",
            ""
        ),


        "status":
        dados.get(
            "status",
            "NORMAL"
        ),


        "prioridade":
        dados.get(
            "prioridade",
            "BAIXA"
        )

    }



    memoria = carregar_memoria()


    memoria["eventos"].append(
        evento
    )


    salvar_memoria(
        memoria
    )



    return jsonify({

        "recebido": True,

        "evento": evento

    })






# ---------------------------------------------------------------
# Consultar eventos
# ---------------------------------------------------------------

@app.route(
    "/eventos",
    methods=["GET"]
)
def consultar_eventos():


    memoria = carregar_memoria()


    return jsonify(
        memoria
    )






# ---------------------------------------------------------------
# Status do nÃƒÂºcleo
# ---------------------------------------------------------------

@app.route(
    "/status",
    methods=["GET"]
)
def status():


    memoria = carregar_memoria()


    return jsonify({

        "sistema":
        "IOTEC EVENT BUS CORE V1.0",


        "estado":
        "ONLINE",


        "eventos_registrados":
        len(
            memoria["eventos"]
        ),


        "hora":
        str(datetime.now())

    })







# ---------------------------------------------------------------
# ExecuÃƒÂ§ÃƒÂ£o
# ---------------------------------------------------------------

if __name__ == "__main__":


    print("="*70)

    print(
        " IOTEC EVENT BUS CORE V1.0 "
    )

    print(
        " SISTEMA NERVOSO OPERACIONAL "
    )

    print("="*70)


    print()

    print(
        "Servidor:"
    )

    print(
        "http://192.168.0.102:6000"
    )


    print()


    app.run(

        host="0.0.0.0",

        port=5001,

        debug=False

    )




