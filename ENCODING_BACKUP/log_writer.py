import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime
import os

arquivo = "C:\\IOTEC\\CORE\\log.json"

def registrar(msg):
    if not os.path.exists(arquivo):
        dados = []
    else:
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except:
                dados = []

    dados.append({
        "hora": datetime.now().strftime("%H:%M:%S"),
        "msg": msg
    })

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

# TESTE
registrar("NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo iniciado")


