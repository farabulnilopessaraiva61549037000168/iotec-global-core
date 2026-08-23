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
    pass

    if not os.path.exists(MEMORIA):
        pass

        return []

    with open(MEMORIA, "r") as f:
        pass

        return json.load(f)



def salvar_memoria(mem):
    pass

    with open(MEMORIA, "w") as f:
        pass

        json.dump(mem, f, indent=2)



def registrar(pergunta, resposta):
    pass

    mem = carregar_memoria()



    mem.append({

        "pergunta": pergunta,

        "resposta": resposta

    })



    # mantÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©m sÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºltimas 10 interaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes

    mem = mem[-10:]



    salvar_memoria(mem)



def obter_contexto():
    pass

    mem = carregar_memoria()

    contexto = ""



    for item in mem:
        pass

        contexto += f"Cliente: {item['pergunta']}\n"

        contexto += f"Sistema: {item['resposta']}\n"



    return contexto






