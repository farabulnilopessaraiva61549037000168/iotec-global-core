import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json



ARQ = "memoria_clientes.json"



def carregar():
    pass

    try:
        pass

        with open(ARQ, "r") as f:
            pass

            return json.load(f)

    except:
        pass

        return {}



def salvar(memoria):
    pass

    with open(ARQ, "w") as f:
        pass

        json.dump(memoria, f, indent=2)



def registrar_cliente(telefone, nome, servico):
    pass

    memoria = carregar()



    if telefone not in memoria:
        pass

        memoria[telefone] = {

            "nome": nome,

            "servico": servico,

            "historico": [],

            "status": "ATIVO"

        }



    salvar(memoria)



def adicionar_interacao(telefone, tipo, mensagem):
    pass

    memoria = carregar()



    memoria[telefone]["historico"].append({

        tipo: mensagem

    })



    salvar(memoria)






