import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

catalogo = {

    "gerado_em": str(datetime.now()),

    "versao": "1.0",

    "categorias": {

        "EMPRESAS": {
            "status": "VAZIO",
            "fontes": []
        },

        "ESCOLAS": {
            "status": "VAZIO",
            "fontes": []
        },

        "UNIVERSIDADES": {
            "status": "VAZIO",
            "fontes": []
        },

        "FORNECEDORES": {
            "status": "VAZIO",
            "fontes": []
        },

        "TERCEIRIZADAS": {
            "status": "VAZIO",
            "fontes": []
        },

        "PARCEIROS": {
            "status": "VAZIO",
            "fontes": []
        }

    },

    "estatisticas": {

        "categorias": 6,

        "fontes_total": 0,

        "fontes_ativas": 0
    }
}

saida = ROOT / "IOTEC_SOURCE_CATALOG.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        catalogo,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nSOURCE CATALOG CRIADO\n")

print("CATEGORIAS:", 6)

print("FONTES:", 0)

print("\nARQUIVO:")

print(saida)




