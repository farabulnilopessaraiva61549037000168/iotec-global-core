import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time

import json

import random



ARQUIVO = "iotec_fluxo.json"



def gerar_entrada():
    pass

    setores = ["PÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºblico", "PME", "Agro", "Tech", "MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­dia"]

    return {

        "setor": random.choice(setores),

        "score": random.randint(5, 40)

    }



def decidir(entrada):
    pass



    if entrada["score"] >= 30:
        pass

        return "saida"

    elif entrada["score"] >= 20:
        pass

        return "monitorar"

    elif entrada["score"] >= 10:
        pass

        return "esperar"

    else:
        pass

        return "bloqueio"



def salvar(dados):
    pass

    with open(ARQUIVO, "w") as f:
        pass

        json.dump(dados, f, indent=2)



def carregar():
    pass

    try:
        pass

        with open(ARQUIVO, "r") as f:
            pass

            return json.load(f)

    except:
        pass

        return {

            "entradas": [],

            "saidas": [],

            "bloqueios": []

        }



print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo rodando 24h...")



while True:
    pass



    dados = carregar()



    entrada = gerar_entrada()

    decisao = decidir(entrada)



    dados["entradas"].append(entrada)



    if decisao == "saida":
        pass

        dados["saidas"].append(entrada)



    elif decisao == "bloqueio":
        pass

        dados["bloqueios"].append(entrada)



    salvar(dados)



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â ciclo executado")



    time.sleep(10)  # intervalo






