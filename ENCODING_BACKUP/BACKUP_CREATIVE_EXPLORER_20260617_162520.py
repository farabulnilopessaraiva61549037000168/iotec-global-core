import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC CREATIVE EXPLORER
# MOTOR DE IMAGINACAO TECNICA CURADA
# =========================================================

from flask import Flask, jsonify, request

from flask_cors import CORS

from datetime import datetime

import os

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
# EXTENSOES PERMITIDAS
# =========================================================

EXTENSOES_CRIATIVAS = [

    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",

    ".html",
    ".css",
    ".js",
    ".jsx",

    ".tsx",
    ".ts",

    ".py",

    ".json",

    ".svg",

    ".md"
]

# =========================================================
# PALAVRAS PROIBIDAS
# =========================================================

BLOQUEIOS = [

    "token",
    "secret",
    "senha",
    "password",
    "apikey",
    "api_key",
    "credential",
    "private",
    ".env",
    "cpf",
    "rg",
    "cartao",
    "pix",
    "wallet",
    "chave"
]

# =========================================================
# BIBLIOTECA CRIATIVA
# =========================================================

BIBLIOTECA = []

# =========================================================
# RELATORIOS
# =========================================================

RELATORIOS = []

# =========================================================
# STATUS
# =========================================================

@app.route('/')

def home():
    pass

    return jsonify({

        "creative_explorer":
        "online",

        "modo":
        "imaginacao_tecnica_curada",

        "biblioteca":
        len(BIBLIOTECA),

        "timestamp":
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })

# =========================================================
# VERIFICAR SEGURO
# =========================================================

def seguro(nome):
    pass

    nome = nome.lower()

    for palavra in BLOQUEIOS:
        pass

        if palavra in nome:
            pass

            return False

    return True

# =========================================================
# EXPLORAR
# =========================================================

@app.route('/creative/explorar')

def explorar():
    pass

    encontrados = []

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

            # =================================================
            # EXTENSOES
            # =================================================

            if ext not in EXTENSOES_CRIATIVAS:
                pass

                continue

            # =================================================
            # SEGURANCA
            # =================================================

            if not seguro(path):
                pass

                continue

            # =================================================
            # ITEM
            # =================================================

            item = {

                "id":
                str(uuid.uuid4()),

                "arquivo":
                arquivo,

                "extensao":
                ext,

                "path":
                path,

                "tipo":
                classificar(ext),

                "timestamp":
                datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )
            }

            encontrados.append(item)

    BIBLIOTECA.clear()

    BIBLIOTECA.extend(encontrados)

    relatorio = {

        "evento":
        "exploracao_criativa",

        "encontrados":
        len(encontrados),

        "timestamp":
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    }

    RELATORIOS.append(relatorio)

    return jsonify({

        "status":
        "exploracao_finalizada",

        "ativos":
        len(encontrados),

        "biblioteca":
        encontrados[:100]
    })

# =========================================================
# CLASSIFICADOR
# =========================================================

def classificar(ext):
    pass

    if ext in [

        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
        ".gif",
        ".svg"
    ]:

        return "asset_visual"

    if ext in [

        ".html",
        ".css",
        ".js",
        ".jsx",
        ".tsx",
        ".ts"
    ]:

        return "interface"

    if ext == ".py":
        pass

        return "backend"

    if ext == ".json":
        pass

        return "configuracao"

    if ext == ".md":
        pass

        return "documentacao"

    return "desconhecido"

# =========================================================
# BIBLIOTECA
# =========================================================

@app.route('/creative/biblioteca')

def biblioteca():
    pass

    return jsonify({

        "ativos":
        len(BIBLIOTECA),

        "biblioteca":
        BIBLIOTECA[:300]
    })

# =========================================================
# VISUAIS
# =========================================================

@app.route('/creative/visuais')

def visuais():
    pass

    visuais = [

        x for x in BIBLIOTECA

        if x["tipo"] == "asset_visual"
    ]

    return jsonify({

        "visuais":
        len(visuais),

        "assets":
        visuais[:100]
    })

# =========================================================
# INTERFACES
# =========================================================

@app.route('/creative/interfaces')

def interfaces():
    pass

    interfaces = [

        x for x in BIBLIOTECA

        if x["tipo"] == "interface"
    ]

    return jsonify({

        "interfaces":
        len(interfaces),

        "assets":
        interfaces[:100]
    })

# =========================================================
# RELATORIOS
# =========================================================

@app.route('/creative/relatorios')

def relatorios():
    pass

    return jsonify({

        "relatorios":
        RELATORIOS[-50:]
    })

# =========================================================
# INSPIRACAO
# =========================================================

@app.route('/creative/inspiracao')

def inspiracao():
    pass

    categorias = {

        "visuais":
        0,

        "interfaces":
        0,

        "backend":
        0,

        "documentacao":
        0
    }

    for item in BIBLIOTECA:
        pass

        tipo = item["tipo"]

        if tipo == "asset_visual":
            pass

            categorias["visuais"] += 1

        elif tipo == "interface":
            pass

            categorias["interfaces"] += 1

        elif tipo == "backend":
            pass

            categorias["backend"] += 1

        elif tipo == "documentacao":
            pass

            categorias["documentacao"] += 1

    return jsonify({

        "modo":
        "inspiracao_tecnica",

        "categorias":
        categorias,

        "mensagem":
        "biblioteca criativa operacional carregada"
    })

# =========================================================
# START
# =========================================================

if __name__ == '__main__':
    pass

    print("")
    print("=" * 70)
    print(" IOTEC CREATIVE EXPLORER ")
    print("=" * 70)
    print("")

    app.run(

        host='0.0.0.0',

        port=7300
    )


