import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

from datetime import datetime



def gerar_ordem(produto_nome):
    pass



    with open("C:\\IOTEC\\CORE\\produtos.json", "r", encoding="utf-8") as f:
        pass

        produtos = json.load(f)



    produto = next((p for p in produtos if p["nome"] == produto_nome), None)



    if not produto:
        pass

        print("Produto nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o encontrado")

        return



    ordem = {

        "produto": produto_nome,

        "hora": datetime.now().strftime("%H:%M:%S"),

        "itens": produto["itens"],

        "status": "em produÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o"

    }



    with open("C:\\IOTEC\\CORE\\ordens.json", "a", encoding="utf-8") as f:
        pass

        f.write(json.dumps(ordem) + "\n")



    print("Ordem gerada:", ordem)



# TESTE

gerar_ordem("SNIA Score Global 9.85")




