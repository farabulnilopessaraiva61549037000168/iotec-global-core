import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

relatorio = {
    "data": str(datetime.now()),
    "motores": [],
    "bancos": [],
    "jsons": [],
    "reservatorios": [],
    "duplicados": [],
    "vazios": [],
    "erros": []
}

# ----------------------------------
# PYTHON ENGINES
# ----------------------------------

for arquivo in ROOT.glob("*.py"):
    pass

    tamanho = arquivo.stat().st_size

    relatorio["motores"].append({
        "arquivo": arquivo.name,
        "bytes": tamanho
    })

    if tamanho == 0:
        relatorio["vazios"].append(arquivo.name)

# ----------------------------------
# SQLITE
# ----------------------------------

for banco in ROOT.glob("*.db"):
    pass

    try:
        pass

        conn = sqlite3.connect(banco)

        cursor = conn.cursor()

        cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """)

        tabelas = cursor.fetchall()

        relatorio["bancos"].append({
            "arquivo": banco.name,
            "tabelas": len(tabelas)
        })

        conn.close()

    except Exception as e:
        pass

        relatorio["erros"].append({
            "arquivo": banco.name,
            "erro": str(e)
        })

# ----------------------------------
# JSON
# ----------------------------------

for js in ROOT.glob("*.json"):
    pass

    try:
        pass

        with open(js, "r", encoding="utf-8") as f:
            pass

            dados = json.load(f)

        relatorio["jsons"].append({
            "arquivo": js.name,
            "tipo": str(type(dados))
        })

    except Exception as e:
        pass

        relatorio["erros"].append({
            "arquivo": js.name,
            "erro": str(e)
        })

# ----------------------------------
# DETECTAR ENGINES
# ----------------------------------

engines = []

for py in ROOT.glob("*.py"):
    pass

    nome = py.stem.upper()

    if "ENGINE" in nome:
        pass

        engines.append(nome)

contador = {}

for item in engines:
    pass

    contador[item] = contador.get(item, 0) + 1

for k, v in contador.items():
    pass

    if v > 1:
        pass

        relatorio["duplicados"].append({
            "motor": k,
            "quantidade": v
        })

# ----------------------------------
# RESERVATORIOS
# ----------------------------------

for nome in os.listdir(ROOT):
    pass

    caminho = ROOT / nome

    if caminho.is_dir():
        pass

        try:
            pass

            quantidade = len(list(caminho.iterdir()))

            relatorio["reservatorios"].append({
                "nome": nome,
                "itens": quantidade
            })

            if quantidade == 0:
                pass

                relatorio["vazios"].append(nome)

        except:
            pass

# ----------------------------------
# RESUMO
# ----------------------------------

relatorio["resumo"] = {

    "motores_total":
        len(relatorio["motores"]),

    "bancos_total":
        len(relatorio["bancos"]),

    "json_total":
        len(relatorio["jsons"]),

    "reservatorios_total":
        len(relatorio["reservatorios"]),

    "erros_total":
        len(relatorio["erros"]),

    "vazios_total":
        len(relatorio["vazios"])
}

saida = ROOT / "IOTEC_SYSTEM_AUDIT_REPORT.json"

with open(saida, "w", encoding="utf-8") as f:
    pass

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nAUDITORIA CONCLUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDA\n")
print(json.dumps(relatorio["resumo"], indent=4))
print(f"\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO: {saida}")




