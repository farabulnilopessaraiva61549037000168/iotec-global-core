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
    setores = ["PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblico", "PME", "Agro", "Tech", "MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dia"]
    return {
        "setor": random.choice(setores),
        "score": random.randint(5, 40)
    }

def decidir(entrada):
    pass

    if entrada["score"] >= 30:
        return "saida"
    elif entrada["score"] >= 20:
        return "monitorar"
    elif entrada["score"] >= 10:
        return "esperar"
    else:
        return "bloqueio"

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=2)

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return {
            "entradas": [],
            "saidas": [],
            "bloqueios": []
        }

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo rodando 24h...")

while True:
    pass

    dados = carregar()

    entrada = gerar_entrada()
    decisao = decidir(entrada)

    dados["entradas"].append(entrada)

    if decisao == "saida":
        dados["saidas"].append(entrada)

    elif decisao == "bloqueio":
        dados["bloqueios"].append(entrada)

    salvar(dados)

    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ciclo executado")

    time.sleep(10)  # intervalo


