import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

ARQ = "memoria_clientes.json"

def carregar():
    try:
        with open(ARQ, "r") as f:
            return json.load(f)
    except:
        return {}

def salvar(memoria):
    with open(ARQ, "w") as f:
        json.dump(memoria, f, indent=2)

def registrar_cliente(telefone, nome, servico):
    memoria = carregar()

    if telefone not in memoria:
        memoria[telefone] = {
            "nome": nome,
            "servico": servico,
            "historico": [],
            "status": "ATIVO"
        }

    salvar(memoria)

def adicionar_interacao(telefone, tipo, mensagem):
    memoria = carregar()

    memoria[telefone]["historico"].append({
        tipo: mensagem
    })

    salvar(memoria)


