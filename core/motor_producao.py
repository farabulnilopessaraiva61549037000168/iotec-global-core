import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

import os

from datetime import datetime



BASE = "C:\\IOTEC\\CORE"



def ler_eventos():
    pass

    caminho = os.path.join(BASE, "eventos.json")



    if not os.path.exists(caminho):
        pass

        return []



    with open(caminho, "r", encoding="utf-8") as f:
        pass

        return json.load(f)



def salvar_ordem(ordem):
    pass

    caminho = os.path.join(BASE, "ordens.json")



    if not os.path.exists(caminho):
        pass

        lista = []

    else:
        pass

        with open(caminho, "r", encoding="utf-8") as f:
            pass

            lista = json.load(f)



    lista.append(ordem)



    with open(caminho, "w", encoding="utf-8") as f:
        pass

        json.dump(lista, f, indent=2)



def executar():
    pass



    eventos = ler_eventos()



    for e in eventos:
        pass



        if e.get("tipo") == "pagamento_confirmado" and not e.get("ordem_gerada"):
            pass



            ordem = {

                "cliente": e.get("assunto"),

                "status": "produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

                "inicio": datetime.now().strftime("%H:%M:%S")

            }



            salvar_ordem(ordem)



            e["ordem_gerada"] = True



            print("?? ORDEM DE PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O GERADA")



    with open(os.path.join(BASE, "eventos.json"), "w", encoding="utf-8") as f:
        pass

        json.dump(eventos, f, indent=2)



if __name__ == "__main__":
    pass

    executar()




