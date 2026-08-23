import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import os

MEMORIA = "C:\\IOTEC\\memoria_dialogo.json"

def carregar_memoria():
    if not os.path.exists(MEMORIA):
        return []
    with open(MEMORIA, "r") as f:
        return json.load(f)

def salvar_memoria(mem):
    with open(MEMORIA, "w") as f:
        json.dump(mem, f, indent=2)

def registrar(pergunta, resposta):
    mem = carregar_memoria()

    mem.append({
        "pergunta": pergunta,
        "resposta": resposta
    })

    # mantÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©m sÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltimas 10 interaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
    mem = mem[-10:]

    salvar_memoria(mem)

def obter_contexto():
    mem = carregar_memoria()
    contexto = ""

    for item in mem:
        contexto += f"Cliente: {item['pergunta']}\n"
        contexto += f"Sistema: {item['resposta']}\n"

    return contexto


