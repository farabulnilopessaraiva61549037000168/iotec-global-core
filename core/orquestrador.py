import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
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



def salvar_eventos(lista):
    pass

    caminho = os.path.join(BASE, "eventos.json")



    with open(caminho, "w", encoding="utf-8") as f:
        pass

        json.dump(lista, f, indent=2)



def processar():
    pass



    print("?? ORQUESTRADOR EXECUTANDO")



    eventos = ler_eventos()



    for e in eventos:
        pass



        if e.get("status") == "novo":
            pass



            assunto = e.get("assunto", "").lower()



            if "payment" in assunto or "pagamento" in assunto:
                pass

                e["tipo"] = "pagamento_confirmado"

                print("?? PAGAMENTO DETECTADO")



            elif "orÃƒÆ'Ã†â€™amento" in assunto:
                pass

                e["tipo"] = "lead"

                print("?? NOVO LEAD")



            else:
                pass

                e["tipo"] = "outro"



            e["status"] = "processado"



    salvar_eventos(eventos)



if __name__ == "__main__":
    pass

    processar()




