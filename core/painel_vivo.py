import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time

import json

import os



BASE = "C:\\IOTEC\\CORE"



def ler_eventos():
    pass

    caminho = os.path.join(BASE, "eventos.json")



    if not os.path.exists(caminho):
        pass

        return []



    try:
        pass

        with open(caminho, "r", encoding="utf-8") as f:
            pass

            return json.load(f)

    except:
        pass

        return []



def limpar():
    pass

    os.system("cls")



def painel():
    pass



    print("?? IOTEC NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO VIVO")

    print("="*40)



    while True:
        pass



        eventos = ler_eventos()



        limpar()



        print("?? IOTEC NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO VIVO")

        print("="*40)



        for e in eventos[-10:]:
            pass



            tipo = e.get("tipo")

            assunto = e.get("assunto")

            hora = e.get("hora")



            print(f"[{hora}] {tipo.upper()} -> {assunto}")



        time.sleep(3)



if __name__ == "__main__":
    pass

    painel()




