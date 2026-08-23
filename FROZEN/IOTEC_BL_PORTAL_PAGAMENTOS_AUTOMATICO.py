import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC BL - CONSTRUTORA DE TECNOLOGIA

# IOTEC_BL_PORTAL_PAGAMENTOS_AUTOMATICO.py

# ============================================================

# OBJETIVO:

# Construir um portal institucional robusto, sem remendos,

# com leitura automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica de links de pagamento (PicPay e outros)

# dentro do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo central, geraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de QR Codes vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lidos e

# exposiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o visual premium dos produtos.

#

# RECURSOS:

# - Portal institucional novo

# - Leitura automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica de links em .txt, .json, .md, .csv, .py

# - DetecÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de links PicPay

# - AssociaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de links aos produtos

# - GeraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de QR Code real com base no link encontrado

# - CatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo JSON persistente

# - Logs

# - Fallback seguro

#

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O:

#   python IOTEC_BL_PORTAL_PAGAMENTOS_AUTOMATICO.py

#

# ACESSO:

#   http://127.0.0.1:8080

#

# OBSERVAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O:

# - Ajuste NUCLEO_DIR se quiser apontar para outro diretÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio.

# - O QR Code sÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ serÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ gerado se houver link real encontrado.

# ============================================================



import os

import re

import sys

import json

import html

import time

import shutil

import socket

import logging

import datetime

import subprocess

import importlib

from pathlib import Path

from typing import List, Dict, Optional, Tuple



# ------------------------------------------------------------

# AUTO-INSTALAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O DE DEPENDÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦ NCIAS

# ------------------------------------------------------------

def garantir_dependencia(pacote: str, import_name: Optional[str] = None) -> None:
    pass

    nome_import = import_name or pacote

    try:
        pass

        importlib.import_module(nome_import)

    except ImportError:
        pass

        print(f"[INFO] Instalando dependÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia: {pacote}")

        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])



garantir_dependencia("flask", "flask")

garantir_dependencia("qrcode", "qrcode")

garantir_dependencia("Pillow", "PIL")



from flask import Flask, jsonify, send_from_directory, render_template_string

import qrcode



# ------------------------------------------------------------

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O GERAL

# ------------------------------------------------------------

APP_NAME = "IOTEC BL - Construtora de Tecnologia"

MODULE_NAME = "IOTEC_BL_PORTAL_PAGAMENTOS_AUTOMATICO"

HOST = "127.0.0.1"

PORT = 8080



BASE_DIR = Path.cwd()

ROOT_DIR = BASE_DIR / "IOTEC_BL_PORTAL_AUTO"

ASSETS_DIR = ROOT_DIR / "assets"

IMAGES_DIR = ASSETS_DIR / "images"

VIDEOS_DIR = ASSETS_DIR / "videos"

QRCODES_DIR = ASSETS_DIR / "qrcodes"

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

EXPORT_DIR = ROOT_DIR / "export"

BACKUP_DIR = ROOT_DIR / "backup"



# AJUSTE AQUI SE QUISER APONTAR DIRETAMENTE PARA O NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

NUCLEO_DIR = BASE_DIR / "nucleo"



CATALOGO_FILE = DATA_DIR / "catalogo_produtos.json"

MAPEAMENTO_FILE = DATA_DIR / "mapeamento_pagamentos.json"

PAGAMENTOS_ENCONTRADOS_FILE = DATA_DIR / "pagamentos_encontrados.json"



TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")



for pasta in [

    ROOT_DIR, ASSETS_DIR, IMAGES_DIR, VIDEOS_DIR, QRCODES_DIR,

    DATA_DIR, LOG_DIR, EXPORT_DIR, BACKUP_DIR

]:

    pasta.mkdir(parents=True, exist_ok=True)



LOG_FILE = LOG_DIR / f"{MODULE_NAME}_{TIMESTAMP}.log"



logging.basicConfig(

    filename=str(LOG_FILE),

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    encoding="utf-8"

)



# ------------------------------------------------------------

# UTILITÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂRIOS

# ------------------------------------------------------------

def agora() -> datetime.datetime:
    pass

    return datetime.datetime.now()



def agora_iso() -> str:
    pass

    return agora().isoformat()



def formatar_brl(valor: float) -> str:
    pass

    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")



def slugify(texto: str) -> str:
    pass

    texto = texto.lower().strip()

    mapa = {

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡": "a", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ ": "a", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡": "a", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢": "a",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©": "e", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª": "e",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­": "i",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³": "o", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµ": "o", "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´": "o",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº": "u",

        "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡": "c"

    }

    for a, b in mapa.items():
        pass

        texto = texto.replace(a, b)



    saida = []

    for ch in texto:
        pass

        if ch.isalnum():
            pass

            saida.append(ch)

        elif ch in (" ", "-", "_"):
            pass

            saida.append("-")



    texto = "".join(saida)

    while "--" in texto:
        pass

        texto = texto.replace("--", "-")

    return texto.strip("-")



def salvar_json(caminho: Path, dados) -> None:
    pass

    with open(caminho, "w", encoding="utf-8") as f:
        pass

        json.dump(dados, f, ensure_ascii=False, indent=4)



def carregar_json(caminho: Path, padrao):
    pass

    if caminho.exists():
        pass

        with open(caminho, "r", encoding="utf-8") as f:
            pass

            return json.load(f)

    return padrao



def copiar_para_area_trabalho(arquivo: Path) -> Optional[Path]:
    pass

    try:
        pass

        desktop = Path.home() / "Desktop"

        if desktop.exists():
            pass

            destino = desktop / arquivo.name

            shutil.copy2(arquivo, destino)

            return destino

    except Exception as e:
        pass

        logging.warning(f"Falha ao copiar arquivo para ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rea de trabalho: {e}")

    return None



def obter_ip_local() -> str:
    pass

    try:
        pass

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(("8.8.8.8", 80))

        ip = s.getsockname()[0]

        s.close()

        return ip

    except Exception:
        pass

        return "127.0.0.1"



def gerar_qrcode(texto: str, destino: Path) -> bool:
    pass

    try:
        pass

        qr = qrcode.QRCode(version=1, box_size=10, border=3)

        qr.add_data(texto)

        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(destino)

        return True

    except Exception as e:
        pass

        logging.error(f"Falha ao gerar QR Code para {destino.name}: {e}")

        return False



def ler_texto_seguro(caminho: Path) -> str:
    pass

    tentativas = ["utf-8", "utf-8-sig", "latin-1", "cp1252"]

    for enc in tentativas:
        pass

        try:
            pass

            return caminho.read_text(encoding=enc, errors="ignore")

        except Exception:
            pass

            continue

    return ""



def resumo_caminho(caminho: Path) -> str:
    pass

    try:
        pass

        return str(caminho.resolve())

    except Exception:
        pass

        return str(caminho)



# ------------------------------------------------------------

# REGEX DE URL

# ------------------------------------------------------------

URL_PATTERN = re.compile(

    r"https?://[^\s"'<>\]\)]+",

    re.IGNORECASE

)



# ------------------------------------------------------------

# CATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLOGO BASE

# ------------------------------------------------------------

def criar_catalogo_base() -> Dict:
    pass

    produtos = [

        {

            "id": "P001",

            "nome": "SNIA Score Global 9.85",

            "slug": "snia-score-global-985",

            "categoria": "AvaliaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Empresarial",

            "descricao": "AvaliaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gica com score institucional, leitura de maturidade analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica e parecer executivo para posicionamento competitivo.",

            "preco": 997.00,

            "publico_alvo": "Empresas, consultorias, instituiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes e gestores",

            "entrega": "RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio + score + parecer executivo",

            "ativo": True,

            "destaque": True,

            "payment_key": "snia-score-global-985",

            "link_pagamento": "",

            "origem_pagamento": "",

            "tipo_pagamento": "",

            "qrcode": "",

            "preco_formatado": formatar_brl(997.00)

        },

        {

            "id": "P002",

            "nome": "GestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de Crises com InteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia Artificial",

            "slug": "gestao-de-crises-com-inteligencia-artificial",

            "categoria": "GestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de Crises",

            "descricao": "AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise situacional, classificaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de risco, apoio ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡  decisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia aplicada para cenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios crÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ticos.",

            "preco": 2497.00,

            "publico_alvo": "ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"rgÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡os, prefeituras, defesa civil, consultorias e operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes sensÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­veis",

            "entrega": "DiagnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³stico + painel + orientaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnica",

            "ativo": True,

            "destaque": True,

            "payment_key": "gestao-de-crises-com-inteligencia-artificial",

            "link_pagamento": "",

            "origem_pagamento": "",

            "tipo_pagamento": "",

            "qrcode": "",

            "preco_formatado": formatar_brl(2497.00)

        },

        {

            "id": "P003",

            "nome": "SeguranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a ViÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ria Inteligente",

            "slug": "seguranca-viaria-inteligente",

            "categoria": "SeguranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a ViÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ria",

            "descricao": "AnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise de mobilidade, risco e criticidade operacional para apoio tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnico em polÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ticas de seguranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a viÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ria.",

            "preco": 1897.00,

            "publico_alvo": "MunicÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­pios, secretarias, gestores de trÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢nsito e empresas",

            "entrega": "RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio + indicadores + plano de aÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

            "ativo": True,

            "destaque": False,

            "payment_key": "seguranca-viaria-inteligente",

            "link_pagamento": "",

            "origem_pagamento": "",

            "tipo_pagamento": "",

            "qrcode": "",

            "preco_formatado": formatar_brl(1897.00)

        },

        {

            "id": "P004",

            "nome": "AssistÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia AnalÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tica Institucional",

            "slug": "assistencia-analitica-institucional",

            "categoria": "Assessoria",

            "descricao": "ServiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o digital de apoio analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tico para tomada de decisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o, leitura de cenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios e inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia aplicada.",

            "preco": 3500.00,

            "publico_alvo": "Empresas, ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rgÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡os, lideranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡as e operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes institucionais",

            "entrega": "AssistÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnica + relatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rios + suporte analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tico",

            "ativo": True,

            "destaque": False,

            "payment_key": "assistencia-analitica-institucional",

            "link_pagamento": "",

            "origem_pagamento": "",

            "tipo_pagamento": "",

            "qrcode": "",

            "preco_formatado": formatar_brl(3500.00)

        },

        {

            "id": "P005",

            "nome": "Pacote Executivo SNIA Internacional",

            "slug": "pacote-executivo-snia-internacional",

            "categoria": "Plano Premium",

            "descricao": "Pacote executivo com avaliaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o institucional, posicionamento global e estrutura premium de apresentaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o.",

            "preco": 8900.00,

            "publico_alvo": "Diretores, investidores, empresas e projetos em expansÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

            "entrega": "DossiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª premium + parecer + plano executivo",

            "ativo": True,

            "destaque": True,

            "payment_key": "pacote-executivo-snia-internacional",

            "link_pagamento": "",

            "origem_pagamento": "",

            "tipo_pagamento": "",

            "qrcode": "",

            "preco_formatado": formatar_brl(8900.00)

        }

    ]

    return {

        "app": APP_NAME,

        "modulo": MODULE_NAME,

        "gerado_em": agora_iso(),

        "produtos": produtos

    }



def inicializar_catalogo() -> Dict:
    pass

    if not CATALOGO_FILE.exists():
        pass

        dados = criar_catalogo_base()

        salvar_json(CATALOGO_FILE, dados)

        logging.info("CatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo base criado.")

        return dados

    return carregar_json(CATALOGO_FILE, criar_catalogo_base())



# ------------------------------------------------------------

# MAPEAMENTO OPCIONAL DE PAGAMENTOS

# ------------------------------------------------------------

def criar_mapeamento_base() -> Dict[str, List[str]]:
    pass

    """

    VocÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª pode editar este arquivo depois para amarrar explicitamente

    nomes/termos dos arquivos do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo a cada produto.

    """

    mapeamento = {

        "snia-score-global-985": [

            "snia score",

            "score global",

            "score 9.85",

            "avaliacao empresarial"

        ],

        "gestao-de-crises-com-inteligencia-artificial": [

            "gestao de crises",

            "crises",

            "inteligencia artificial crise"

        ],

        "seguranca-viaria-inteligente": [

            "seguranca viaria",

            "transito",

            "mobilidade"

        ],

        "assistencia-analitica-institucional": [

            "assistencia analitica",

            "analitica institucional",

            "assessoria"

        ],

        "pacote-executivo-snia-internacional": [

            "pacote executivo",

            "internacional",

            "premium"

        ]

    }

    return mapeamento



def inicializar_mapeamento() -> Dict[str, List[str]]:
    pass

    if not MAPEAMENTO_FILE.exists():
        pass

        salvar_json(MAPEAMENTO_FILE, criar_mapeamento_base())

    return carregar_json(MAPEAMENTO_FILE, criar_mapeamento_base())



# ------------------------------------------------------------

# VARREDURA DE LINKS DE PAGAMENTO NO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO

# ------------------------------------------------------------

EXTENSOES_PERMITIDAS = {".txt", ".json", ".md", ".csv", ".py", ".html", ".htm", ".ini", ".yaml", ".yml"}



def classificar_link(url: str) -> str:
    pass

    u = url.lower()

    if "picpay" in u:
        pass

        return "PicPay"

    if "mercadopago" in u or "mercado pago" in u:
        pass

        return "Mercado Pago"

    if "pagseguro" in u:
        pass

        return "PagSeguro"

    if "stripe" in u:
        pass

        return "Stripe"

    return "Outro"



def pontuar_link(url: str) -> int:
    pass

    score = 0

    u = url.lower()



    if u.startswith("https://"):
        pass

        score += 3

    elif u.startswith("http://"):
        pass

        score += 1



    if "picpay" in u:
        pass

        score += 10

    if "checkout" in u:
        pass

        score += 3

    if "pagar" in u or "payment" in u or "pay" in u:
        pass

        score += 2

    if "app.picpay.com" in u or "picpay.me" in u:
        pass

        score += 4



    return score



def extrair_links_de_texto(texto: str) -> List[str]:
    pass

    encontrados = URL_PATTERN.findall(texto or "")

    limpos = []

    for item in encontrados:
        pass

        item = item.rstrip(".,;)]}>")

        if item not in limpos:
            pass

            limpos.append(item)

    return limpos



def varrer_pagamentos_no_nucleo(nucleo_dir: Path) -> List[Dict]:
    pass

    resultados = []



    if not nucleo_dir.exists():
        pass

        logging.warning(f"NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o encontrado: {nucleo_dir}")

        return resultados



    for caminho in nucleo_dir.rglob("*"):
        pass

        try:
            pass

            if not caminho.is_file():
                pass

                continue

            if caminho.suffix.lower() not in EXTENSOES_PERMITIDAS:
                pass

                continue

            if caminho.stat().st_size > 5 * 1024 * 1024:
                pass

                continue



            texto = ler_texto_seguro(caminho)

            if not texto.strip():
                pass

                continue



            urls = extrair_links_de_texto(texto)

            if not urls:
                pass

                continue



            for url in urls:
                pass

                tipo = classificar_link(url)

                score = pontuar_link(url)

                resultados.append({

                    "arquivo": resumo_caminho(caminho),

                    "nome_arquivo": caminho.name,

                    "url": url,

                    "tipo": tipo,

                    "score": score

                })



        except Exception as e:
            pass

            logging.warning(f"Falha ao analisar arquivo {caminho}: {e}")



    resultados.sort(key=lambda x: x["score"], reverse=True)

    salvar_json(PAGAMENTOS_ENCONTRADOS_FILE, resultados)

    logging.info(f"Varredura de pagamentos concluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­da. Links encontrados: {len(resultados)}")

    return resultados



# ------------------------------------------------------------

# ASSOCIAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O LINK -> PRODUTO

# ------------------------------------------------------------

def associar_pagamentos_ao_catalogo(

    catalogo: Dict,

    pagamentos: List[Dict],

    mapeamento: Dict[str, List[str]]

) -> Dict:

    produtos = catalogo.get("produtos", [])



    for produto in produtos:
        pass

        produto["link_pagamento"] = ""

        produto["origem_pagamento"] = ""

        produto["tipo_pagamento"] = ""

        produto["qrcode"] = ""

        produto["preco_formatado"] = formatar_brl(float(produto.get("preco", 0)))



        slug = produto.get("slug", "")

        nome = produto.get("nome", "").lower()

        categoria = produto.get("categoria", "").lower()

        payment_key = produto.get("payment_key", slug)

        palavras = [slug, payment_key, nome, categoria]

        palavras.extend(mapeamento.get(payment_key, []))



        melhor = None

        melhor_score = -1



        for pagamento in pagamentos:
            pass

            origem = (pagamento.get("arquivo", "") + " " + pagamento.get("nome_arquivo", "")).lower()

            url = pagamento.get("url", "").lower()

            score = pagamento.get("score", 0)



            bonus = 0

            for palavra in palavras:
                pass

                p = palavra.lower().strip()

                if p and (p in origem or p in url):
                    pass

                    bonus += 8



            score_total = score + bonus



            if score_total > melhor_score:
                pass

                melhor = pagamento

                melhor_score = score_total



        if melhor and melhor_score >= 8:
            pass

            produto["link_pagamento"] = melhor["url"]

            produto["origem_pagamento"] = melhor["arquivo"]

            produto["tipo_pagamento"] = melhor["tipo"]



            qr_nome = f"{produto['slug']}.png"

            qr_path = QRCODES_DIR / qr_nome

            ok = gerar_qrcode(melhor["url"], qr_path)

            if ok:
                pass

                produto["qrcode"] = f"/qrcodes/{qr_nome}"



    catalogo["gerado_em"] = agora_iso()

    salvar_json(CATALOGO_FILE, catalogo)

    return catalogo



# ------------------------------------------------------------

# RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIOS

# ------------------------------------------------------------

def gerar_relatorio_execucao(catalogo: Dict, pagamentos: List[Dict]) -> Path:
    pass

    linhas = []

    linhas.append("=" * 70)

    linhas.append("RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO EXECUTIVO - PORTAL E PAGAMENTOS")

    linhas.append("=" * 70)

    linhas.append(f"Empresa          : {APP_NAME}")

    linhas.append(f"MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³dulo           : {MODULE_NAME}")

    linhas.append(f"Gerado em        : {agora().strftime('%d/%m/%Y %H:%M:%S')}")

    linhas.append(f"NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo analisado : {resumo_caminho(NUCLEO_DIR)}")

    linhas.append(f"Links encontrados: {len(pagamentos)}")

    linhas.append("")



    produtos = catalogo.get("produtos", [])

    soma = 0.0

    ativos = 0

    com_pagamento = 0



    for produto in produtos:
        pass

        if produto.get("ativo", True):
            pass

            ativos += 1

            soma += float(produto.get("preco", 0))

        if produto.get("link_pagamento"):
            pass

            com_pagamento += 1



        linhas.append(f"Produto          : {produto.get('nome', '')}")

        linhas.append(f"Categoria        : {produto.get('categoria', '')}")

        linhas.append(f"PreÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o            : {produto.get('preco_formatado', '')}")

        linhas.append(f"Pagamento        : {produto.get('tipo_pagamento', 'NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o associado') or 'NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o associado'}")

        linhas.append(f"Link             : {produto.get('link_pagamento', '') or 'NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O ENCONTRADO'}")

        linhas.append(f"Origem           : {produto.get('origem_pagamento', '') or 'NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O LOCALIZADA'}")

        linhas.append("-" * 70)



    linhas.append("")

    linhas.append(f"Produtos ativos           : {ativos}")

    linhas.append(f"Produtos com pagamento    : {com_pagamento}")

    linhas.append(f"Valor nominal do catÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo : {formatar_brl(soma)}")

    linhas.append(f"SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o 1 venda/produto : {formatar_brl(soma)}")

    linhas.append(f"SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o mensal (22 dias): {formatar_brl(soma * 22)}")

    linhas.append(f"SimulaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o anual           : {formatar_brl(soma * 22 * 12)}")



    relatorio = EXPORT_DIR / "RELATORIO_EXECUTIVO_PORTAL.txt"

    relatorio.write_text("\n".join(linhas), encoding="utf-8")

    copiar_para_area_trabalho(relatorio)

    return relatorio



def gerar_backup(catalogo: Dict) -> Path:
    pass

    destino = BACKUP_DIR / f"catalogo_backup_{TIMESTAMP}.json"

    salvar_json(destino, catalogo)

    copiar_para_area_trabalho(destino)

    return destino



# ------------------------------------------------------------

# MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDIAS

# ------------------------------------------------------------

def criar_arquivo_leia_me_midias() -> None:
    pass

    texto = f"""IOTEC BL - CONSTRUTORA DE TECNOLOGIA



PASTAS DE MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂDIA:

- {IMAGES_DIR}

- {VIDEOS_DIR}



ARQUIVOS RECOMENDADOS:

- hero.mp4

- institucional.mp4

- lateral_01.jpg

- lateral_02.jpg

- lateral_03.jpg



Se nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o houver mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­dia, o portal usa fundo premium padrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o.

"""

    destino = DATA_DIR / "LEIA_ME_MIDIAS.txt"

    destino.write_text(texto, encoding="utf-8")

    copiar_para_area_trabalho(destino)



def listar_midias() -> Tuple[List[str], List[str]]:
    pass

    imagens = []

    videos = []



    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
        pass

        imagens.extend([p.name for p in sorted(IMAGES_DIR.glob(ext))])



    for ext in ("*.mp4", "*.webm", "*.ogg"):
        pass

        videos.extend([p.name for p in sorted(VIDEOS_DIR.glob(ext))])



    return imagens, videos



def escolher_midias() -> Tuple[Optional[str], Optional[str], List[str]]:
    pass

    imagens, videos = listar_midias()



    hero = None

    lateral_video = None



    for v in videos:
        pass

        low = v.lower()

        if low == "hero.mp4":
            pass

            hero = v

        elif "institucional" in low:
            pass

            lateral_video = v



    if hero is None and videos:
        pass

        hero = videos[0]



    if lateral_video is None:
        pass

        for v in videos:
            pass

            if v != hero:
                pass

                lateral_video = v

                break



    laterais = imagens[:6]

    return hero, lateral_video, laterais



# ------------------------------------------------------------

# FLASK

# ------------------------------------------------------------

app = Flask(__name__)



HTML_TEMPLATE = r"""

<!DOCTYPE html>

<html lang="pt-BR">

<head>

    <meta charset="UTF-8">

    <title>IOTEC BL ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" Construtora de Tecnologia</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>

        :root{

            --bg:#06111d;

            --bg2:#0a182a;

            --bg3:#10233c;

            --line:rgba(255,255,255,.08);

            --text:#eef5ff;

            --muted:#9db2ce;

            --blue:#5ea2ff;

            --blue2:#8cc0ff;

            --green:#42d3a2;

            --gold:#eac06b;

            --panel:rgba(9,20,36,.72);

            --shadow:0 20px 60px rgba(0,0,0,.35);

        }

        *{box-sizing:border-box}

        html,body{

            margin:0;padding:0;width:100%;min-height:100%;

            font-family:"Segoe UI",Arial,Helvetica,sans-serif;

            color:var(--text);

            background:

                radial-gradient(circle at 10% 10%, rgba(94,162,255,.12), transparent 22%),

                radial-gradient(circle at 90% 20%, rgba(66,211,162,.10), transparent 20%),

                linear-gradient(135deg, var(--bg), var(--bg2), var(--bg3));

            overflow-x:hidden;

            scroll-behavior:smooth;

        }

        .shell{position:relative;min-height:100vh}

        .topbar{

            position:sticky;top:0;z-index:100;

            backdrop-filter:blur(16px);

            background:rgba(5,12,22,.64);

            border-bottom:1px solid var(--line);

        }

        .topbar-inner{

            max-width:1900px;margin:0 auto;padding:16px 24px;

            display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;

        }

        .brand{display:flex;align-items:center;gap:16px}

        .orb{

            width:56px;height:56px;border-radius:50%;

            background:radial-gradient(circle at 35% 30%, #9ed0ff 0%, #5ea2ff 28%, #1f568f 64%, #0b1f35 100%);

            box-shadow:inset 0 0 18px rgba(255,255,255,.15),0 0 28px rgba(94,162,255,.24);

            position:relative;flex-shrink:0;

        }

        .orb:before{

            content:"";position:absolute;inset:11px;border-radius:50%;

            border:1px solid rgba(255,255,255,.14);

        }

        .brand-text h1{margin:0;font-size:clamp(22px,2.5vw,34px);font-weight:900}

        .brand-text p{margin:4px 0 0 0;color:var(--muted);font-size:13px}

        .menu{display:flex;gap:10px;flex-wrap:wrap}

        .menu a,.menu button{

            text-decoration:none;color:var(--text);

            background:rgba(255,255,255,.04);

            border:1px solid var(--line);

            padding:11px 16px;border-radius:12px;font-weight:700;cursor:pointer;

        }

        .hero{

            max-width:1900px;margin:0 auto;

            padding:24px 24px 10px 24px;

            display:grid;grid-template-columns:1.4fr .6fr;gap:20px;

            min-height:calc(100vh - 90px);

        }

        .hero-main{

            position:relative;border-radius:30px;overflow:hidden;border:1px solid var(--line);

            background:#08121f;min-height:760px;box-shadow:var(--shadow);

        }

        .hero-media{position:absolute;inset:0;overflow:hidden}

        .hero-media video,.hero-media img{

            width:100%;height:100%;object-fit:cover;display:block;

            filter:brightness(.56) saturate(1.08);transform:scale(1.02);

        }

        .hero-overlay{

            position:absolute;inset:0;

            background:

                linear-gradient(90deg, rgba(4,12,21,.92) 0%, rgba(4,12,21,.70) 44%, rgba(4,12,21,.34) 74%, rgba(4,12,21,.18) 100%),

                linear-gradient(180deg, rgba(0,0,0,.18), rgba(0,0,0,.34));

        }

        .hero-content{

            position:relative;z-index:2;height:100%;

            display:flex;flex-direction:column;justify-content:center;

            padding:54px;max-width:920px;

        }

        .kicker{

            display:inline-flex;align-items:center;gap:8px;width:max-content;

            padding:9px 14px;border-radius:999px;

            background:rgba(94,162,255,.12);

            border:1px solid rgba(94,162,255,.22);

            color:#cfe2ff;font-size:12px;font-weight:900;

            letter-spacing:.9px;text-transform:uppercase;

        }

        .hero-content h2{

            margin:20px 0 14px 0;

            font-size:clamp(36px,5vw,78px);

            line-height:1.02;letter-spacing:-1.4px;font-weight:950;max-width:860px;

        }

        .hero-content p{

            margin:0;font-size:17px;line-height:1.8;color:#d8e5f7;max-width:820px;

        }

        .hero-actions{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap}

        .btn{

            display:inline-flex;align-items:center;justify-content:center;gap:8px;

            text-decoration:none;border:none;cursor:pointer;

            padding:15px 20px;border-radius:14px;font-weight:900;font-size:14px;

            transition:transform .18s ease;

        }

        .btn:hover{transform:translateY(-2px)}

        .btn-primary{

            background:linear-gradient(135deg,var(--blue),var(--blue2));

            color:#06111d;box-shadow:0 12px 24px rgba(94,162,255,.26);

        }

        .btn-secondary{

            background:rgba(255,255,255,.05);border:1px solid var(--line);color:var(--text);

        }

        .hero-stats{

            margin-top:28px;display:grid;

            grid-template-columns:repeat(3,minmax(160px,1fr));gap:14px;max-width:760px;

        }

        .hero-stat{

            background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);

            border-radius:18px;padding:16px 18px;backdrop-filter:blur(8px);

        }

        .hero-stat .label{

            font-size:11px;color:#aac0dd;text-transform:uppercase;letter-spacing:.9px;margin-bottom:8px;

        }

        .hero-stat .value{font-size:clamp(18px,2vw,26px);font-weight:900}

        .hero-side{display:grid;grid-template-rows:1fr auto;gap:18px;min-height:760px}

        .side-media-stack{display:grid;grid-template-rows:repeat(3,1fr);gap:18px}

        .media-card{

            position:relative;border-radius:24px;overflow:hidden;border:1px solid var(--line);

            background:#0a1627;box-shadow:var(--shadow);min-height:190px;

        }

        .media-card img,.media-card video{

            width:100%;height:100%;object-fit:cover;display:block;filter:brightness(.72);

        }

        .media-card .overlay{

            position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,.05), rgba(0,0,0,.55));

        }

        .media-card .label{

            position:absolute;left:16px;bottom:14px;z-index:2;padding:8px 12px;border-radius:999px;

            background:rgba(6,17,29,.62);border:1px solid rgba(255,255,255,.08);

            font-size:12px;font-weight:800;letter-spacing:.7px;

        }

        .side-panel,.section-panel{

            border-radius:24px;border:1px solid var(--line);

            background:linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));

            padding:22px;box-shadow:var(--shadow);

        }

        .side-panel h3,.section-head h3{margin:0 0 12px 0;font-size:22px}

        .side-panel p,.section-head p,.meta-text{

            margin:0;color:var(--muted);line-height:1.7;font-size:14px;

        }

        .pill-list{display:grid;gap:10px;margin-top:16px}

        .pill{

            padding:12px 14px;border-radius:14px;background:rgba(255,255,255,.03);

            border:1px solid var(--line);font-weight:700;color:#dce9fa;

        }

        .section{

            max-width:1900px;margin:0 auto;padding:16px 24px 30px 24px;

        }

        .section-head{

            display:flex;justify-content:space-between;align-items:end;gap:18px;flex-wrap:wrap;margin-bottom:18px;

        }

        .section-head h3{

            font-size:clamp(28px,3vw,44px);font-weight:900;letter-spacing:-.7px;

        }

        .solutions-grid{

            display:grid;grid-template-columns:repeat(auto-fit, minmax(350px, 1fr));gap:18px;

        }

        .product-card{

            border-radius:24px;border:1px solid var(--line);

            background:linear-gradient(180deg, rgba(255,255,255,.045), rgba(255,255,255,.02));

            box-shadow:var(--shadow);overflow:hidden;display:flex;flex-direction:column;

        }

        .product-head{padding:22px 22px 12px 22px;border-bottom:1px solid rgba(255,255,255,.06)}

        .badge-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}

        .badge{

            display:inline-flex;align-items:center;justify-content:center;

            border-radius:999px;padding:7px 12px;font-size:11px;font-weight:800;

            text-transform:uppercase;letter-spacing:.8px;border:1px solid rgba(255,255,255,.08);

        }

        .badge-blue{background:rgba(94,162,255,.14);color:#cfe3ff}

        .badge-green{background:rgba(66,211,162,.12);color:#cfffee}

        .badge-gold{background:rgba(234,192,107,.12);color:#ffe4a1}

        .product-title{margin:0;font-size:24px;font-weight:900;line-height:1.2}

        .product-body{padding:18px 22px 20px 22px;display:grid;grid-template-columns:1fr 155px;gap:18px}

        .product-desc{color:var(--muted);font-size:14px;line-height:1.8;min-height:112px}

        .meta-box{

            margin-top:12px;border:1px solid var(--line);border-radius:14px;padding:12px;background:rgba(255,255,255,.03);

        }

        .meta-label{

            font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);margin-bottom:6px;

        }

        .meta-value{font-size:13px;line-height:1.55;color:#eef5ff}

        .qr-panel{

            border:1px solid rgba(255,255,255,.08);border-radius:18px;background:#fff;padding:12px;color:#0c1520;

            display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:245px;

        }

        .qr-panel img{width:100%;max-width:126px;height:auto}

        .qr-title{

            margin-top:10px;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.8px;color:#1b2838;text-align:center;

        }

        .qr-fallback{

            font-size:12px;text-align:center;line-height:1.5;color:#334155;font-weight:700;

        }

        .product-footer{padding:0 22px 22px 22px}

        .price-row{display:flex;align-items:end;justify-content:space-between;gap:12px;margin-bottom:14px}

        .price-label{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.9px}

        .price-value{font-size:36px;font-weight:900;letter-spacing:-1px;color:var(--green);line-height:1;margin-top:6px}

        .footer-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px}

        .footer{

            margin-top:18px;border-top:1px solid var(--line);background:rgba(5,12,22,.55);backdrop-filter:blur(18px);

        }

        .footer-inner{

            max-width:1900px;margin:0 auto;padding:18px 24px;

            display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;color:var(--muted);font-size:13px;

        }

        @media (max-width: 1200px){

            .hero{grid-template-columns:1fr;min-height:auto}

            .hero-main,.hero-side{min-height:auto}

            .side-media-stack{grid-template-columns:repeat(3,1fr);grid-template-rows:none}

        }

        @media (max-width: 900px){

            .product-body{grid-template-columns:1fr}

        }

        @media (max-width: 860px){

            .hero-content{padding:34px 24px}

            .hero-stats{grid-template-columns:1fr}

            .side-media-stack{grid-template-columns:1fr}

        }

        @media (max-width: 640px){

            .topbar-inner,.section,.hero{padding-left:16px;padding-right:16px}

            .hero-content h2{font-size:36px}

            .footer-actions{grid-template-columns:1fr}

        }

    </style>

</head>

<body>

<div class="shell">



<header class="topbar">

    <div class="topbar-inner">

        <div class="brand">

            <div class="orb"></div>

            <div class="brand-text">

                <h1>IOTEC BL ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" Construtora de Tecnologia</h1>

                <p>Arquitetura digital, inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia aplicada e soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes tecnolÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³gicas para mercado, gestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o e expansÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o institucional</p>

            </div>

        </div>

        <nav class="menu">

            <a href="#solucoes">SoluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes</a>

            <a href="#pagamentos">Pagamentos</a>

            <button onclick="ativarFullscreen()">Tela cheia</button>

        </nav>

    </div>

</header>



<section class="hero">

    <div class="hero-main">

        <div class="hero-media">

            {% if hero_video %}

                <video autoplay muted loop playsinline>

                    <source src="/videos/{{ hero_video }}" type="video/mp4">

                </video>

            {% elif laterais and laterais|length > 0 %}

                <img src="/images/{{ laterais[0] }}" alt="Imagem institucional">

            {% else %}

                <div style="width:100%;height:100%;background:linear-gradient(135deg,#0b1a2c,#10233c,#18385c);"></div>

            {% endif %}

        </div>

        <div class="hero-overlay"></div>

        <div class="hero-content">

            <div class="kicker">CONSTRUTORA DE TECNOLOGIA ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· PORTAL EXECUTIVO</div>

            <h2>PresenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a institucional, soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes digitais e arquitetura comercial em um ambiente visual premium.</h2>

            <p>

                A IOTEC BL estrutura soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes tecnolÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³gicas com foco em inteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia aplicada, organizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o operacional,

                apresentaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o institucional e capacidade de expansÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o para mercados pÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºblicos e privados.

            </p>

            <div class="hero-actions">

                <a href="#solucoes" class="btn btn-primary">Explorar soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes</a>

                <a href="#pagamentos" class="btn btn-secondary">Ver pagamentos</a>

            </div>

            <div class="hero-stats">

                <div class="hero-stat">

                    <div class="label">Produtos ativos</div>

                    <div class="value">{{ total_produtos }}</div>

                </div>

                <div class="hero-stat">

                    <div class="label">Produtos com pagamento</div>

                    <div class="value">{{ produtos_com_pagamento }}</div>

                </div>

                <div class="hero-stat">

                    <div class="label">Valor do catÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo</div>

                    <div class="value">{{ soma_catalogo }}</div>

                </div>

            </div>

        </div>

    </div>



    <aside class="hero-side">

        <div class="side-media-stack">

            {% for item in side_cards %}

            <div class="media-card">

                {% if item.tipo == "video" %}

                    <video autoplay muted loop playsinline>

                        <source src="/videos/{{ item.arquivo }}" type="video/mp4">

                    </video>

                {% else %}

                    <img src="/images/{{ item.arquivo }}" alt="MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­dia institucional">

                {% endif %}

                <div class="overlay"></div>

                <div class="label">{{ item.rotulo }}</div>

            </div>

            {% endfor %}

        </div>



        <div class="side-panel">

            <h3>Estrutura operacional do portal</h3>

            <p>

                Este ambiente lÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª a base interna, localiza links de pagamento, associa QR Codes vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lidos e organiza

                a apresentaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o institucional em uma vitrine digital mais robusta e coerente com a marca.

            </p>

            <div class="pill-list">

                <div class="pill">Leitura automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica de pagamentos do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo</div>

                <div class="pill">QR Codes reais a partir de links encontrados</div>

                <div class="pill">Base pronta para crescimento comercial</div>

            </div>

        </div>

    </aside>

</section>



<section class="section" id="solucoes">

    <div class="section-head">

        <div>

            <h3>CatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo executivo de soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes</h3>

            <p>Produtos e serviÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡os organizados para exposiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o comercial, apresentaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o institucional e operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o digital.</p>

        </div>

    </div>



    <div class="solutions-grid">

        {% for p in produtos %}

        <article class="product-card" id="pagamentos">

            <div class="product-head">

                <div class="badge-row">

                    <span class="badge badge-blue">{{ p.categoria }}</span>

                    {% if p.destaque %}

                        <span class="badge badge-gold">Destaque</span>

                    {% endif %}

                    {% if p.link_pagamento %}

                        <span class="badge badge-green">{{ p.tipo_pagamento or 'Pagamento' }}</span>

                    {% endif %}

                </div>

                <h4 class="product-title">{{ p.nome }}</h4>

            </div>



            <div class="product-body">

                <div>

                    <div class="product-desc">{{ p.descricao }}</div>



                    <div class="meta-box">

                        <div class="meta-label">PÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºblico-alvo</div>

                        <div class="meta-value">{{ p.publico_alvo }}</div>

                    </div>



                    <div class="meta-box">

                        <div class="meta-label">Entrega</div>

                        <div class="meta-value">{{ p.entrega }}</div>

                    </div>



                    <div class="meta-box">

                        <div class="meta-label">Origem do pagamento</div>

                        <div class="meta-value">

                            {{ p.origem_pagamento if p.origem_pagamento else 'Nenhum link vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lido associado atÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© o momento.' }}

                        </div>

                    </div>

                </div>



                <div class="qr-panel">

                    {% if p.qrcode %}

                        <img src="{{ p.qrcode }}" alt="QR Code {{ p.nome }}">

                        <div class="qr-title">QR Code de pagamento</div>

                    {% else %}

                        <div class="qr-fallback">

                            Pagamento nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o associado.<br>

                            O QR Code sÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© exibido quando um link vÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lido ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© encontrado no nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo.

                        </div>

                    {% endif %}

                </div>

            </div>



            <div class="product-footer">

                <div class="price-row">

                    <div>

                        <div class="price-label">PreÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o</div>

                        <div class="price-value">{{ p.preco_formatado }}</div>

                    </div>

                </div>



                <div class="footer-actions">

                    {% if p.link_pagamento %}

                        <a class="btn btn-primary" href="{{ p.link_pagamento }}" target="_blank">Abrir pagamento</a>

                        <button class="btn btn-secondary" onclick="copiarTexto('{{ p.link_pagamento|e }}')">Copiar link</button>

                    {% else %}

                        <button class="btn btn-secondary" disabled>Pagamento indisponÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel</button>

                        <button class="btn btn-secondary" disabled>Sem link encontrado</button>

                    {% endif %}

                </div>

            </div>

        </article>

        {% endfor %}

    </div>

</section>



<footer class="footer">

    <div class="footer-inner">

        <div>IOTEC BL ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" Construtora de Tecnologia</div>

        <div>{{ gerado_em }}</div>

        <div>Portal executivo com pagamentos automatizados</div>

    </div>

</footer>



</div>



<script>

async function ativarFullscreen(){

    try{

        if(!document.fullscreenElement){

            await document.documentElement.requestFullscreen();

        }else{

            await document.exitFullscreen();

        }

    }catch(e){

        console.log("Fullscreen indisponÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel.", e);

    }

}

async function copiarTexto(texto){

    if(!texto){

        return;

    }

    try{

        await navigator.clipboard.writeText(texto);

        alert("Link copiado com sucesso.");

    }catch(e){

        alert("NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o foi possÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel copiar o link.");

    }

}

</script>

</body>

</html>

"""



@app.route("/")

def home():
    pass

    catalogo = carregar_json(CATALOGO_FILE, criar_catalogo_base())

    produtos = [p for p in catalogo.get("produtos", []) if p.get("ativo", True)]



    total_produtos = len(produtos)

    produtos_com_pagamento = sum(1 for p in produtos if p.get("link_pagamento"))

    soma = sum(float(p.get("preco", 0)) for p in produtos)



    hero_video, lateral_video, laterais = escolher_midias()

    side_cards = []



    if len(laterais) > 0:
        pass

        side_cards.append({"tipo": "imagem", "arquivo": laterais[0], "rotulo": "Imagem institucional"})

    elif lateral_video:
        pass

        side_cards.append({"tipo": "video", "arquivo": lateral_video, "rotulo": "VÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­deo institucional"})



    if len(laterais) > 1:
        pass

        side_cards.append({"tipo": "imagem", "arquivo": laterais[1], "rotulo": "PresenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a corporativa"})

    elif lateral_video:
        pass

        side_cards.append({"tipo": "video", "arquivo": lateral_video, "rotulo": "Estrutura visual"})



    if lateral_video:
        pass

        side_cards.append({"tipo": "video", "arquivo": lateral_video, "rotulo": "MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­dia institucional"})

    elif len(laterais) > 2:
        pass

        side_cards.append({"tipo": "imagem", "arquivo": laterais[2], "rotulo": "Ambiente executivo"})



    while len(side_cards) < 3 and laterais:
        pass

        idx = min(len(side_cards), len(laterais) - 1)

        side_cards.append({"tipo": "imagem", "arquivo": laterais[idx], "rotulo": "Imagem institucional"})



    return render_template_string(

        HTML_TEMPLATE,

        produtos=produtos,

        total_produtos=total_produtos,

        produtos_com_pagamento=produtos_com_pagamento,

        soma_catalogo=formatar_brl(soma),

        hero_video=hero_video,

        laterais=laterais,

        side_cards=side_cards,

        gerado_em=agora().strftime("%d/%m/%Y %H:%M:%S")

    )



@app.route("/api/catalogo")

def api_catalogo():
    pass

    return jsonify(carregar_json(CATALOGO_FILE, criar_catalogo_base()))



@app.route("/api/pagamentos")

def api_pagamentos():
    pass

    return jsonify(carregar_json(PAGAMENTOS_ENCONTRADOS_FILE, []))



@app.route("/images/<path:nome>")

def servir_imagem(nome):
    pass

    return send_from_directory(IMAGES_DIR, nome)



@app.route("/videos/<path:nome>")

def servir_video(nome):
    pass

    return send_from_directory(VIDEOS_DIR, nome)



@app.route("/qrcodes/<path:nome>")

def servir_qrcode(nome):
    pass

    return send_from_directory(QRCODES_DIR, nome)



# ------------------------------------------------------------

# ROTINA PRINCIPAL

# ------------------------------------------------------------

def preparar_portal() -> Dict:
    pass

    criar_arquivo_leia_me_midias()



    catalogo = inicializar_catalogo()

    mapeamento = inicializar_mapeamento()

    pagamentos = varrer_pagamentos_no_nucleo(NUCLEO_DIR)

    catalogo = associar_pagamentos_ao_catalogo(catalogo, pagamentos, mapeamento)



    relatorio = gerar_relatorio_execucao(catalogo, pagamentos)

    backup = gerar_backup(catalogo)



    logging.info(f"RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio gerado em {relatorio}")

    logging.info(f"Backup gerado em {backup}")



    return {

        "catalogo": catalogo,

        "pagamentos": pagamentos,

        "relatorio": relatorio,

        "backup": backup

    }



def main():
    pass

    print("=" * 76)

    print(APP_NAME)

    print(MODULE_NAME)

    print("=" * 76)



    resultado = preparar_portal()

    ip_local = obter_ip_local()



    print(f"Base do portal       : {ROOT_DIR}")

    print(f"NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo analisado     : {NUCLEO_DIR}")

    print(f"CatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡logo             : {CATALOGO_FILE}")

    print(f"Pagamentos encontrados: {len(resultado['pagamentos'])}")

    print(f"RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio            : {resultado['relatorio']}")

    print(f"Backup               : {resultado['backup']}")

    print("-" * 76)

    print(f"ACESSO LOCAL         : http://127.0.0.1:{PORT}")

    print(f"ACESSO NA REDE       : http://{ip_local}:{PORT}")

    print("-" * 76)

    print("ObservaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o: o QR Code sÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© gerado quando um link real ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© localizado no nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo.")

    print("=" * 76)



    app.run(host=HOST, port=PORT, debug=False, use_reloader=False, threaded=True)



if __name__ == "__main__":
    pass

    main()




